import csv
import gzip
import json
import tempfile
import unittest
from pathlib import Path

from experiments.e1.candidates import generate_candidates
from experiments.e1.cli import FIXTURE, dry_run, validate
from experiments.e1.io import sha256_file
from experiments.e1.normalize import canonicalize, normalize_file, normalize_name, normalize_phone, normalize_street
from experiments.e1.profile import profile_csv


class E1NormalizationTests(unittest.TestCase):
    def test_name_normalization_preserves_deterministic_equivalence(self):
        self.assertEqual(normalize_name("Acme Transportation, L.L.C.")[0], "ACME TRANSPORTATION")
        self.assertEqual(normalize_name("ACME TRANSPORTATION LLC")[0], "ACME TRANSPORTATION")

    def test_address_and_phone_normalization(self):
        self.assertEqual(normalize_street("123 HIGHWAY 71 NORTH")[0], "123 HWY 71 N")
        self.assertEqual(normalize_phone("+1 (512) 555-0100")[0], "5125550100")
        self.assertIsNone(normalize_phone("555-0100")[0])

    def test_canonical_record_preserves_raw_and_operations(self):
        with FIXTURE.open("r", encoding="utf-8-sig", newline="") as handle:
            row = next(csv.DictReader(handle))
        record = canonicalize(row, 2, "2026-08-18T14:01:28Z")
        self.assertEqual(record["names"]["legal"]["raw"], "Acme Transportation, L.L.C.")
        self.assertEqual(record["names"]["legal"]["normalized"], "ACME TRANSPORTATION")
        self.assertIn("remove_terminal_legal_suffix", record["names"]["legal"]["operations"])
        self.assertEqual(record["identifier"]["namespace"], "USDOT")


class E1PipelineTests(unittest.TestCase):
    def test_protocol_and_fixture_validate(self):
        result = validate(FIXTURE)
        self.assertTrue(result["valid"])
        self.assertEqual(result["semantic_human_freeze"], "pending")

    def test_uppercase_bulk_export_header_is_accepted(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "upper.csv"
            lines = FIXTURE.read_text(encoding="utf-8").splitlines()
            source.write_text(lines[0].upper() + "\n" + lines[1] + "\n", encoding="utf-8")
            self.assertTrue(validate(source)["valid"])
            output = Path(directory) / "normalized.jsonl.gz"
            self.assertEqual(normalize_file(source, output, "2026-08-18T14:01:28Z")["records_written"], 1)

    def test_profile_counts_all_fixture_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "profile.json"
            result = profile_csv(FIXTURE, output)
            self.assertEqual(result["rows_profiled"], 8)
            self.assertEqual(result["column_count"], 19)
            self.assertEqual(result["columns"]["phone"]["missing"], 3)

    def test_normalization_is_byte_deterministic(self):
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.jsonl.gz"
            second = Path(directory) / "second.jsonl.gz"
            normalize_file(FIXTURE, first, "2026-08-18T14:01:28Z")
            normalize_file(FIXTURE, second, "2026-08-18T14:01:28Z")
            self.assertEqual(sha256_file(first), sha256_file(second))
            with gzip.open(first, "rt", encoding="utf-8") as handle:
                records = [json.loads(line) for line in handle]
            self.assertEqual(len(records), 8)

    def test_candidates_are_canonical_deduplicated_and_warn_against_identity_inference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = root / "candidates.csv"
            report_path = root / "report.json"
            report = generate_candidates(FIXTURE, output, report_path, max_block_size=10, max_pairs=1000)
            with output.open("r", encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertGreater(len(rows), 0)
            self.assertEqual(len(rows), len({(row["record_a"], row["record_b"]) for row in rows}))
            self.assertTrue(all(row["record_a"] < row["record_b"] for row in rows))
            self.assertTrue(all(json.loads(row["field_similarities_json"])["legal_name_sequence_ratio"] >= 0 for row in rows))
            self.assertTrue(all(row["temporal_distance_days"] == "0" for row in rows))
            self.assertEqual(report["candidate_recall_status"], "not_measurable_without_adjudicated_gold_or_continuity_fixture")
            acme = next(row for row in rows if row["record_a"].endswith(":1001") and row["record_b"].endswith(":1002"))
            self.assertIn("same_normalized_phone", acme["blocking_rules_triggered"])
            self.assertIn("same_zip_name_prefix", acme["blocking_rules_triggered"])

    def test_dry_run_is_replay_stable(self):
        first = dry_run()["hashes"]
        second = dry_run()["hashes"]
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
