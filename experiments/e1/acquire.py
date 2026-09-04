from __future__ import annotations

import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .io import canonical_json, request_json, stream_download, utc_now, write_new


DATASET_ID = "az4n-8mr2"
PORTAL_URL = f"https://data.transportation.gov/Trucking-and-Motorcoaches/Company-Census-File/{DATASET_ID}/about_data"
METADATA_URL = f"https://data.transportation.gov/api/views/{DATASET_ID}.json"
NORMALIZED_METADATA_URL = f"https://data.transportation.gov/api/views/metadata/v1/{DATASET_ID}"
COLUMNS_URL = f"https://data.transportation.gov/api/views/{DATASET_ID}/columns.json"
COUNT_URL = f"https://data.transportation.gov/resource/{DATASET_ID}.json?$select=count(*)"
BULK_URL = f"https://data.transportation.gov/api/v3/views/{DATASET_ID}/export.csv?accessType=DOWNLOAD"
DICTIONARY_URL = "https://data.transportation.gov/api/views/az4n-8mr2/files/05274d1b-8109-4409-a4ef-237e12f870c9?download=true&filename=MCMIS%20Company%20Census%20Data%20Dictionary%28Rev08%292026-01-23.pdf"


def _timestamp(seconds: Any) -> str | None:
    if seconds in (None, ""):
        return None
    return datetime.fromtimestamp(int(seconds), timezone.utc).isoformat().replace("+00:00", "Z")


def _custom(metadata: dict[str, Any], group: str, key: str) -> Any:
    fields = metadata.get("metadata", {}).get("custom_fields", {}).get(group, {})
    return next((value for name, value in fields.items() if name.strip() == key), None)


def acquire_snapshot(output_root: Path, snapshot_date: str, limit: int | None = None) -> Path:
    destination = output_root / "fmcsa" / "company_census" / snapshot_date
    staging = destination.with_name(destination.name + ".part")
    if destination.exists() or staging.exists():
        raise FileExistsError(f"snapshot or staging directory already exists: {destination}")
    staging.mkdir(parents=True)

    try:
        retrieval_started = utc_now()
        metadata = request_json(METADATA_URL)
        normalized_metadata = request_json(NORMALIZED_METADATA_URL)
        columns = request_json(COLUMNS_URL)
        count_payload = request_json(COUNT_URL)
        source_rows = int(count_payload[0]["count"])
        export_url = BULK_URL if limit is None else f"https://data.transportation.gov/resource/{DATASET_ID}.csv?$limit={limit}"

        csv_path = staging / "company_census.csv"
        digest, size = stream_download(export_url, csv_path)
        dictionary_path = staging / "mcmis-company-census-data-dictionary-rev08-2026-01-23.pdf"
        dictionary_digest, dictionary_size = stream_download(DICTIONARY_URL, dictionary_path)
        post_metadata = request_json(METADATA_URL)
        post_normalized_metadata = request_json(NORMALIZED_METADATA_URL)
        post_count_payload = request_json(COUNT_URL)
        post_rows = int(post_count_payload[0]["count"])
        retrieval_completed = utc_now()

        manifest = {
        "manifest_version": "0.1.0",
        "experiment": "E1",
        "stage": 2,
        "snapshot_date": snapshot_date,
        "immutable": True,
        "retrieval": {
            "started_at": retrieval_started,
            "completed_at": retrieval_completed,
            "mechanism": "Socrata bulk CSV export" if limit is None else "Socrata SODA bounded CSV query",
            "export_url": export_url,
            "requested_limit": limit,
        },
        "source": {
            "publisher": "Federal Motor Carrier Safety Administration",
            "dataset_name": metadata.get("name"),
            "dataset_id": DATASET_ID,
            "portal_url": PORTAL_URL,
            "metadata_url": METADATA_URL,
            "normalized_metadata_url": NORMALIZED_METADATA_URL,
            "columns_url": COLUMNS_URL,
            "field_dictionary_url": DICTIONARY_URL,
            "count_url": COUNT_URL,
            "rows_updated_at": _timestamp(metadata.get("rowsUpdatedAt")),
            "metadata_updated_at": normalized_metadata.get("metadataUpdatedAt"),
            "source_row_count_at_retrieval": source_rows,
            "source_row_count_postflight": post_rows,
            "source_column_count": len(columns),
            "row_identifier": next((column.get("fieldName") for column in columns if column.get("id") == metadata.get("metadata", {}).get("rowIdentifier")), None),
            "public_access_level": _custom(metadata, "Common Core", "Public Access Level"),
            "update_frequency": _custom(metadata, "Common Core", "Update Frequency"),
            "licence_published": _custom(metadata, "Common Core", "License") or metadata.get("license") or "unknown",
            "rights_note": "Public access does not establish redistribution rights; rights review remains open.",
            "postflight": {
                "rows_updated_at": _timestamp(post_metadata.get("rowsUpdatedAt")),
                "metadata_updated_at": post_normalized_metadata.get("metadataUpdatedAt"),
                "source_changed_during_retrieval": (
                    metadata.get("rowsUpdatedAt") != post_metadata.get("rowsUpdatedAt")
                    or source_rows != post_rows
                ),
            },
        },
        "artifact": {
            "path": "company_census.csv",
            "bytes": size,
            "sha256": digest,
            "content_type": "text/csv",
        },
        "field_dictionary": {
            "path": dictionary_path.name,
            "bytes": dictionary_size,
            "sha256": dictionary_digest,
            "content_type": "application/pdf",
        },
        }

        write_new(staging / "source_metadata.json", canonical_json(metadata))
        write_new(staging / "source_normalized_metadata.json", canonical_json(normalized_metadata))
        write_new(staging / "source_postflight_metadata.json", canonical_json(post_metadata))
        write_new(staging / "source_postflight_normalized_metadata.json", canonical_json(post_normalized_metadata))
        write_new(staging / "source_columns.json", canonical_json(columns))
        write_new(staging / "sha256.txt", f"{digest}  company_census.csv\n{dictionary_digest}  {dictionary_path.name}\n".encode("ascii"))
        write_new(staging / "manifest.json", canonical_json(manifest))
        os.replace(staging, destination)
    except BaseException:
        if staging.exists():
            shutil.rmtree(staging)
        raise
    return destination


def inspect_snapshot(snapshot_dir: Path) -> dict[str, Any]:
    manifest_path = snapshot_dir / "manifest.json"
    with manifest_path.open("r", encoding="utf-8") as handle:
        manifest = json.load(handle)
    csv_path = snapshot_dir / manifest["artifact"]["path"]
    dictionary_path = snapshot_dir / manifest["field_dictionary"]["path"]
    required_names = ["source_metadata.json", "source_normalized_metadata.json", "source_columns.json", "sha256.txt"]
    if "postflight" in manifest.get("source", {}):
        required_names.extend(["source_postflight_metadata.json", "source_postflight_normalized_metadata.json"])
    required = [csv_path, dictionary_path, *(snapshot_dir / name for name in required_names)]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"incomplete snapshot: {missing}")
    from .io import sha256_file

    actual = sha256_file(csv_path)
    expected = manifest["artifact"]["sha256"]
    dictionary_actual = sha256_file(dictionary_path)
    return {
        "snapshot_dir": str(snapshot_dir),
        "complete": actual == expected,
        "expected_sha256": expected,
        "actual_sha256": actual,
        "bytes": csv_path.stat().st_size,
        "source_rows": manifest["source"]["source_row_count_at_retrieval"],
        "source_columns": manifest["source"]["source_column_count"],
        "field_dictionary_complete": dictionary_actual == manifest["field_dictionary"]["sha256"],
    }
