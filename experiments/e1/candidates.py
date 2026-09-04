from __future__ import annotations

import csv
import json
import os
import sqlite3
from collections import Counter
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path
from typing import Any

from .io import sha256_file
from .normalize import normalize_name, normalize_phone, normalize_postal, normalize_street


CANDIDATE_VERSION = "0.1.0"


def _keys(row: dict[str, str]) -> list[tuple[str, str]]:
    name, _ = normalize_name(row.get("legal_name"))
    dba, _ = normalize_name(row.get("dba_name"))
    phone, _ = normalize_phone(row.get("phone"))
    street, _ = normalize_street(row.get("phy_street"))
    city = (row.get("phy_city") or "").strip().upper()
    state = (row.get("phy_state") or "").strip().upper()
    postal, _ = normalize_postal(row.get("phy_zip"))
    result: list[tuple[str, str]] = []
    if phone:
        result.append(("same_normalized_phone", phone))
    if street and city and state:
        result.append(("same_normalized_physical_address", f"{street}|{city}|{state}|{postal or ''}"))
    if postal and name and len(name.replace(" ", "")) >= 5:
        result.append(("same_zip_name_prefix", f"{postal}|{name.replace(' ', '')[:8]}"))
    tokens = [token for token in set((name or "").split() + (dba or "").split()) if len(token) >= 8 and not token.isdigit()]
    for token in sorted(tokens)[:3]:
        result.append(("same_unusual_name_token", token))
    return result


def generate_candidates(input_csv: Path, output_csv: Path, report_json: Path, max_block_size: int = 50, max_pairs: int = 250_000, limit: int | None = None) -> dict[str, Any]:
    if output_csv.exists() or report_json.exists():
        raise FileExistsError("refusing to overwrite candidate outputs")
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    output_part = output_csv.with_name(output_csv.name + ".part")
    report_part = report_json.with_name(report_json.name + ".part")
    database = output_csv.with_suffix(".sqlite.part")
    if database.exists() or output_part.exists() or report_part.exists():
        raise FileExistsError("refusing to overwrite incomplete candidate output")
    connection = sqlite3.connect(database)
    generation_complete = False
    try:
        connection.executescript("""
            PRAGMA journal_mode=OFF;
            PRAGMA synchronous=OFF;
            CREATE TABLE records(record_id TEXT PRIMARY KEY, legal_name TEXT, physical_address TEXT, phone TEXT, postal_code TEXT);
            CREATE TABLE blocks(rule TEXT NOT NULL, block_key TEXT NOT NULL, record_id TEXT NOT NULL);
            CREATE INDEX blocks_key ON blocks(rule, block_key, record_id);
            CREATE TABLE pairs(record_a TEXT NOT NULL, record_b TEXT NOT NULL, reasons TEXT NOT NULL, PRIMARY KEY(record_a, record_b));
        """)
        records = 0
        with input_csv.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            reader.fieldnames = [name.lower() for name in (reader.fieldnames or [])]
            for row in reader:
                if limit is not None and records >= limit:
                    break
                dot = (row.get("dot_number") or "").strip().lstrip("0") or "0"
                record_id = f"fmcsa-census:{dot}"
                legal_name, _ = normalize_name(row.get("legal_name"))
                phone, _ = normalize_phone(row.get("phone"))
                street, _ = normalize_street(row.get("phy_street"))
                postal, _ = normalize_postal(row.get("phy_zip"))
                physical_address = "|".join((street or "", (row.get("phy_city") or "").strip().upper(), (row.get("phy_state") or "").strip().upper(), postal or ""))
                connection.execute("INSERT OR REPLACE INTO records VALUES (?, ?, ?, ?, ?)", (record_id, legal_name, physical_address, phone, postal))
                connection.executemany("INSERT INTO blocks VALUES (?, ?, ?)", [(rule, key, record_id) for rule, key in _keys(row)])
                records += 1
                if records % 50_000 == 0:
                    connection.commit()
        connection.commit()

        rule_yields: Counter[str] = Counter()
        excluded: Counter[str] = Counter()
        pair_count = 0
        cursor = connection.execute("SELECT rule, block_key, COUNT(*) FROM blocks GROUP BY rule, block_key ORDER BY rule, block_key")
        for rule, block_key, count in cursor:
            if count < 2:
                continue
            if count > max_block_size:
                excluded[rule] += 1
                continue
            ids = [row[0] for row in connection.execute("SELECT DISTINCT record_id FROM blocks WHERE rule=? AND block_key=? ORDER BY record_id", (rule, block_key))]
            for left, right in combinations(ids, 2):
                existing = connection.execute("SELECT reasons FROM pairs WHERE record_a=? AND record_b=?", (left, right)).fetchone()
                if existing:
                    reasons = sorted(set(existing[0].split("|")) | {rule})
                    connection.execute("UPDATE pairs SET reasons=? WHERE record_a=? AND record_b=?", ("|".join(reasons), left, right))
                else:
                    connection.execute("INSERT INTO pairs VALUES (?, ?, ?)", (left, right, rule))
                    pair_count += 1
                rule_yields[rule] += 1
                if pair_count >= max_pairs:
                    break
            if pair_count >= max_pairs:
                break
        cursor.close()
        connection.commit()

        covered = connection.execute("SELECT COUNT(DISTINCT record_id) FROM (SELECT record_a AS record_id FROM pairs UNION SELECT record_b FROM pairs)").fetchone()[0]
        with output_part.open("x", encoding="utf-8", newline="") as output:
            writer = csv.writer(output, lineterminator="\n")
            writer.writerow(["record_a", "record_b", "blocking_rules_triggered", "field_similarities_json", "temporal_distance_days"])
            query = """
                SELECT p.record_a, p.record_b, p.reasons,
                       a.legal_name, b.legal_name, a.physical_address, b.physical_address,
                       a.phone, b.phone, a.postal_code, b.postal_code
                FROM pairs p JOIN records a ON a.record_id=p.record_a JOIN records b ON b.record_id=p.record_b
                ORDER BY p.record_a, p.record_b
            """
            rows_cursor = connection.execute(query)
            for left, right, reasons, name_a, name_b, address_a, address_b, phone_a, phone_b, postal_a, postal_b in rows_cursor:
                signals = {
                    "legal_name_sequence_ratio": round(SequenceMatcher(None, name_a or "", name_b or "").ratio(), 6),
                    "same_normalized_address": bool(address_a and address_a == address_b),
                    "same_normalized_phone": bool(phone_a and phone_a == phone_b),
                    "same_normalized_postal_code": bool(postal_a and postal_a == postal_b),
                }
                writer.writerow([left, right, reasons, json.dumps(signals, sort_keys=True, separators=(",", ":")), 0])
            rows_cursor.close()
        generation_complete = True
    finally:
        connection.close()
        if database.exists():
            database.unlink()
        if not generation_complete and output_part.exists():
            output_part.unlink()

    possible_pairs = records * (records - 1) // 2
    report = {
        "candidate_version": CANDIDATE_VERSION,
        "input": str(input_csv),
        "input_sha256": sha256_file(input_csv),
        "records_read": records,
        "records_with_candidates": covered,
        "candidate_pairs": pair_count,
        "possible_unordered_pairs": possible_pairs,
        "reduction_ratio": 1 - (pair_count / possible_pairs) if possible_pairs else None,
        "max_block_size": max_block_size,
        "max_pairs": max_pairs,
        "pair_cap_reached": pair_count >= max_pairs,
        "rule_pair_emissions_before_deduplication": dict(sorted(rule_yields.items())),
        "block_size_exclusions": dict(sorted(excluded.items())),
        "candidate_recall_status": "not_measurable_without_adjudicated_gold_or_continuity_fixture",
        "identity_warning": "A candidate reason is retrieval evidence only and never entails same legal person.",
    }
    try:
        report_part.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
        os.replace(output_part, output_csv)
        os.replace(report_part, report_json)
    except BaseException:
        for path in (output_part, report_part):
            if path.exists():
                path.unlink()
        raise
    return report
