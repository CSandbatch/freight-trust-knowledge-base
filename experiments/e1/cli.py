from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path

import yaml

from .acquire import acquire_snapshot, inspect_snapshot
from .candidates import generate_candidates
from .io import sha256_file
from .normalize import normalize_file
from .profile import profile_csv


ROOT = Path(__file__).resolve().parents[2]
PROTOCOL = Path(__file__).resolve().parent / "config" / "e1_protocol.yaml"
ONTOLOGY = ROOT / "knowledge-base" / "03-research-evidence" / "e1-identity-ontology.yaml"
FIXTURE = ROOT / "experiments" / "fixtures" / "e1" / "company-census-sample.csv"
REQUIRED_SOURCE_FIELDS = {"dot_number", "legal_name", "dba_name", "phy_street", "phy_city", "phy_state", "phy_zip", "phy_country", "phone", "status_code", "business_org_desc", "power_units", "total_drivers"}


def validate(input_csv: Path | None = None) -> dict[str, object]:
    protocol = yaml.safe_load(PROTOCOL.read_text(encoding="utf-8"))
    ontology = yaml.safe_load(ONTOLOGY.read_text(encoding="utf-8"))
    failures: list[str] = []
    if protocol.get("status") != "build-slice-frozen":
        failures.append("protocol is not build-slice-frozen")
    if ontology.get("status") != "freeze-candidate":
        failures.append("controlling ontology status changed")
    if "train_entity_resolution_model" not in protocol.get("scope", {}).get("prohibited_actions", []):
        failures.append("model-training prohibition missing")
    if input_csv:
        import csv
        with input_csv.open("r", encoding="utf-8-sig", newline="") as handle:
            fields = {name.lower() for name in (csv.DictReader(handle).fieldnames or [])}
        missing = sorted(REQUIRED_SOURCE_FIELDS - fields)
        if missing:
            failures.append(f"source header missing fields: {missing}")
    if failures:
        raise ValueError("; ".join(failures))
    return {"valid": True, "protocol_id": protocol["protocol_id"], "protocol_version": protocol["version"], "semantic_standard_version": ontology["version"], "semantic_human_freeze": protocol["semantic_gate"]["human_freeze"]}


def dry_run() -> dict[str, object]:
    validate(FIXTURE)
    observed_at = "2026-08-18T14:01:28Z"
    with tempfile.TemporaryDirectory(prefix="freight-trust-e1-") as temporary:
        root = Path(temporary)
        profile_path = root / "profile.json"
        normalized_path = root / "normalized.jsonl.gz"
        candidates_path = root / "candidates.csv"
        report_path = root / "candidate-report.json"
        profile_csv(FIXTURE, profile_path)
        normalize_file(FIXTURE, normalized_path, observed_at)
        generate_candidates(FIXTURE, candidates_path, report_path, max_block_size=10, max_pairs=1000)
        return {
            "valid": True,
            "fixture": str(FIXTURE),
            "hashes": {path.name: sha256_file(path) for path in (profile_path, normalized_path, candidates_path, report_path)},
            "profile": json.loads(profile_path.read_text(encoding="utf-8")),
            "candidate_report": json.loads(report_path.read_text(encoding="utf-8")),
        }


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description="E1 Stage 0-4 data preparation")
    sub = command.add_subparsers(dest="command", required=True)
    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("--input", type=Path)
    acquire_parser = sub.add_parser("acquire")
    acquire_parser.add_argument("--output-root", type=Path, default=Path("data/raw"))
    acquire_parser.add_argument("--snapshot-date", required=True)
    acquire_parser.add_argument("--limit", type=int)
    inspect_parser = sub.add_parser("inspect")
    inspect_parser.add_argument("snapshot_dir", type=Path)
    profile_parser = sub.add_parser("profile")
    profile_parser.add_argument("input_csv", type=Path)
    profile_parser.add_argument("output_json", type=Path)
    profile_parser.add_argument("--limit", type=int)
    normalize_parser = sub.add_parser("normalize")
    normalize_parser.add_argument("input_csv", type=Path)
    normalize_parser.add_argument("output_jsonl_gz", type=Path)
    normalize_parser.add_argument("--observed-at", required=True)
    normalize_parser.add_argument("--limit", type=int)
    candidate_parser = sub.add_parser("candidates")
    candidate_parser.add_argument("input_csv", type=Path)
    candidate_parser.add_argument("output_csv", type=Path)
    candidate_parser.add_argument("report_json", type=Path)
    candidate_parser.add_argument("--max-block-size", type=int, default=50)
    candidate_parser.add_argument("--max-pairs", type=int, default=250_000)
    candidate_parser.add_argument("--limit", type=int)
    sub.add_parser("dry-run")
    return command


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.command == "validate":
        result = validate(args.input)
    elif args.command == "acquire":
        result = {"snapshot_dir": str(acquire_snapshot(args.output_root, args.snapshot_date, args.limit))}
    elif args.command == "inspect":
        result = inspect_snapshot(args.snapshot_dir)
    elif args.command == "profile":
        result = profile_csv(args.input_csv, args.output_json, limit=args.limit)
    elif args.command == "normalize":
        result = normalize_file(args.input_csv, args.output_jsonl_gz, args.observed_at, args.limit)
    elif args.command == "candidates":
        result = generate_candidates(args.input_csv, args.output_csv, args.report_json, args.max_block_size, args.max_pairs, args.limit)
    else:
        result = dry_run()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
