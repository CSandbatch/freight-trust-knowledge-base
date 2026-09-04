from __future__ import annotations

import csv
import gzip
import io
import json
import os
import re
import unicodedata
from pathlib import Path
from typing import Any, Iterable


NORMALIZATION_VERSION = "0.1.0"
LEGAL_SUFFIXES = {"LLC", "L L C", "LTD", "LIMITED", "INC", "INCORPORATED", "CORP", "CORPORATION", "CO", "COMPANY", "LP", "LLP", "PLLC"}
STREET_WORDS = {
    "STREET": "ST", "ROAD": "RD", "AVENUE": "AVE", "BOULEVARD": "BLVD", "HIGHWAY": "HWY",
    "LANE": "LN", "DRIVE": "DR", "COURT": "CT", "PARKWAY": "PKWY", "PLACE": "PL",
    "NORTH": "N", "SOUTH": "S", "EAST": "E", "WEST": "W", "SUITE": "STE",
}


def _ascii_upper(value: str | None) -> tuple[str | None, list[str]]:
    if value is None or not value.strip():
        return None, []
    operations: list[str] = []
    current = value.strip()
    if current != value:
        operations.append("trim")
    folded = unicodedata.normalize("NFKD", current).encode("ascii", "ignore").decode("ascii")
    if folded != current:
        operations.append("unicode_ascii_fold")
    upper = folded.upper()
    if upper != folded:
        operations.append("uppercase")
    return upper, operations


def normalize_identifier(value: str | None) -> tuple[str | None, list[str]]:
    upper, operations = _ascii_upper(value)
    if upper is None:
        return None, operations
    digits = re.sub(r"\D", "", upper).lstrip("0") or "0"
    if digits != upper:
        operations.append("digits_only_and_strip_leading_zeroes")
    return digits, operations


def normalize_name(value: str | None) -> tuple[str | None, list[str]]:
    upper, operations = _ascii_upper(value)
    if upper is None:
        return None, operations
    punct = re.sub(r"[^A-Z0-9]+", " ", upper)
    if punct != upper:
        operations.append("punctuation_to_space")
    punct = re.sub(r"\bL\s+L\s+C\b", "LLC", punct)
    punct = re.sub(r"\bL\s+L\s+P\b", "LLP", punct)
    tokens = punct.split()
    while tokens and tokens[-1] in LEGAL_SUFFIXES:
        tokens.pop()
        operations.append("remove_terminal_legal_suffix")
    normalized = " ".join(tokens)
    if normalized != punct.strip() and not any(op == "remove_terminal_legal_suffix" for op in operations):
        operations.append("collapse_whitespace")
    return normalized or None, operations


def normalize_phone(value: str | None) -> tuple[str | None, list[str]]:
    upper, operations = _ascii_upper(value)
    if upper is None:
        return None, operations
    digits = re.sub(r"\D", "", upper)
    if digits != upper:
        operations.append("digits_only")
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
        operations.append("remove_nanp_country_code")
    if len(digits) != 10:
        operations.append("invalid_nanp_length")
        return None, operations
    return digits, operations


def normalize_postal(value: str | None) -> tuple[str | None, list[str]]:
    upper, operations = _ascii_upper(value)
    if upper is None:
        return None, operations
    compact = re.sub(r"[^A-Z0-9]", "", upper)
    if compact != upper:
        operations.append("remove_postal_punctuation")
    if compact.isdigit() and len(compact) >= 5:
        compact = compact[:5]
        operations.append("zip5")
    return compact or None, operations


def normalize_street(value: str | None) -> tuple[str | None, list[str]]:
    upper, operations = _ascii_upper(value)
    if upper is None:
        return None, operations
    punct = re.sub(r"[^A-Z0-9]+", " ", upper)
    if punct != upper:
        operations.append("punctuation_to_space")
    tokens = [STREET_WORDS.get(token, token) for token in punct.split()]
    if tokens != punct.split():
        operations.append("street_abbreviations")
    return " ".join(tokens) or None, operations


def _integer(value: str | None) -> int | None:
    try:
        return int(value) if value not in (None, "") else None
    except ValueError:
        return None


def _value(raw: str | None, normalizer) -> dict[str, Any]:
    normalized, operations = normalizer(raw)
    return {"raw": raw or None, "normalized": normalized, "operations": operations}


def _address(row: dict[str, str], prefix: str) -> dict[str, Any]:
    if prefix == "physical":
        raw_fields = {"street": row.get("phy_street"), "city": row.get("phy_city"), "state": row.get("phy_state"), "postal_code": row.get("phy_zip"), "country": row.get("phy_country")}
    else:
        raw_fields = {"street": row.get("carrier_mailing_street"), "city": row.get("carrier_mailing_city"), "state": row.get("carrier_mailing_state"), "postal_code": row.get("carrier_mailing_zip"), "country": row.get("carrier_mailing_country")}
    street, street_ops = normalize_street(raw_fields["street"])
    city, city_ops = _ascii_upper(raw_fields["city"])
    state, state_ops = _ascii_upper(raw_fields["state"])
    postal, postal_ops = normalize_postal(raw_fields["postal_code"])
    country, country_ops = _ascii_upper(raw_fields["country"])
    components = {"street": street, "city": city, "state": state, "postal_code": postal, "country": country}
    normalized = "|".join(value or "" for value in components.values()) or None
    raw = "|".join(raw_fields[key] or "" for key in ("street", "city", "state", "postal_code", "country")) or None
    return {"raw": raw, "normalized": normalized, "operations": street_ops + city_ops + state_ops + postal_ops + country_ops, "components": components}


def canonicalize(row: dict[str, str], source_row: int, observed_at: str) -> dict[str, Any]:
    identifier, identifier_ops = normalize_identifier(row.get("dot_number"))
    if not identifier:
        raise ValueError(f"source row {source_row} has no usable DOT_NUMBER")
    legal = _value(row.get("legal_name"), normalize_name)
    dba = _value(row.get("dba_name"), normalize_name)
    phone = _value(row.get("phone"), normalize_phone)
    physical = _address(row, "physical")
    mailing = _address(row, "mailing")
    missingness = [name for name, value in {"legal_name": legal["normalized"], "physical_address": physical["normalized"], "phone": phone["normalized"]}.items() if not value]
    conflicts: list[str] = []
    if physical["normalized"] and mailing["normalized"] and physical["normalized"] != mailing["normalized"]:
        conflicts.append("physical_mailing_address_differ")
    operations = {"identifier": identifier_ops, "legal_name": legal["operations"], "dba_name": dba["operations"], "phone": phone["operations"], "physical_address": physical["operations"], "mailing_address": mailing["operations"]}
    return {
        "record_id": f"fmcsa-census:{identifier}", "source_id": "az4n-8mr2", "observed_at": observed_at,
        "valid_from": None, "valid_to": None,
        "identifier": {"namespace": "USDOT", "raw": row.get("dot_number") or "", "normalized": identifier},
        "names": {"legal": legal, "dba": dba}, "addresses": {"physical": physical, "mailing": mailing}, "phone": phone,
        "attributes": {"status": row.get("status_code") or None, "entity_type": row.get("business_org_desc") or None, "fleet_size": row.get("fleetsize") or None, "power_units": _integer(row.get("power_units")), "drivers": _integer(row.get("total_drivers"))},
        "claims": {"insurance": [], "safety": []}, "relationship_edges": [],
        "quality": {"source_freshness": observed_at, "source_quality": "public_dataset_unknown_redistribution_licence", "missingness_flags": missingness, "conflict_flags": conflicts},
        "provenance": {"dataset_id": "az4n-8mr2", "source_row": source_row, "normalization_version": NORMALIZATION_VERSION, "operations": operations},
    }


def iter_canonical(input_csv: Path, observed_at: str, limit: int | None = None) -> Iterable[dict[str, Any]]:
    with input_csv.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        reader.fieldnames = [name.lower() for name in (reader.fieldnames or [])]
        for index, row in enumerate(reader, start=2):
            if limit is not None and index - 2 >= limit:
                break
            yield canonicalize(row, index, observed_at)


def normalize_file(input_csv: Path, output_jsonl_gz: Path, observed_at: str, limit: int | None = None) -> dict[str, Any]:
    if output_jsonl_gz.exists():
        raise FileExistsError(f"refusing to overwrite: {output_jsonl_gz}")
    part = output_jsonl_gz.with_name(output_jsonl_gz.name + ".part")
    if part.exists():
        raise FileExistsError(f"refusing to overwrite incomplete output: {part}")
    output_jsonl_gz.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    try:
        with part.open("xb") as raw_output:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw_output, compresslevel=6, mtime=0) as compressed:
                with io.TextIOWrapper(compressed, encoding="utf-8", newline="\n") as output:
                    for record in iter_canonical(input_csv, observed_at, limit):
                        output.write(json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")
                        count += 1
        os.replace(part, output_jsonl_gz)
    except BaseException:
        if part.exists():
            part.unlink()
        raise
    return {"records_written": count, "output": str(output_jsonl_gz), "normalization_version": NORMALIZATION_VERSION}
