from __future__ import annotations

import csv
import json
import os
from collections import Counter
from pathlib import Path
from typing import Any

from .io import sha256_file


PROFILE_VERSION = "0.1.0"


def profile_csv(input_csv: Path, output_json: Path, top_k: int = 10, limit: int | None = None) -> dict[str, Any]:
    if output_json.exists():
        raise FileExistsError(f"refusing to overwrite: {output_json}")
    part = output_json.with_name(output_json.name + ".part")
    if part.exists():
        raise FileExistsError(f"refusing to overwrite incomplete output: {part}")
    with input_csv.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("CSV has no header")
        names = [name.lower() for name in reader.fieldnames]
        reader.fieldnames = names
        stats = {name: {"missing": 0, "nonempty": 0, "max_length": 0, "numeric": 0, "examples": [], "top_values": Counter()} for name in names}
        rows = 0
        for row in reader:
            if limit is not None and rows >= limit:
                break
            rows += 1
            for name in names:
                value = row.get(name, "")
                column = stats[name]
                if value is None or not value.strip():
                    column["missing"] += 1
                    continue
                value = value.strip()
                column["nonempty"] += 1
                column["max_length"] = max(column["max_length"], len(value))
                try:
                    float(value)
                    column["numeric"] += 1
                except ValueError:
                    pass
                if len(column["examples"]) < 3 and value not in column["examples"]:
                    column["examples"].append(value)
                # Exact top values are retained only while cardinality stays bounded.
                counter: Counter[str] = column["top_values"]
                counter[value] += 1
                if len(counter) > 2048:
                    for key, _ in counter.most_common()[1024:]:
                        del counter[key]
        columns: dict[str, Any] = {}
        for name, column in stats.items():
            counter = column.pop("top_values")
            columns[name] = {
                **column,
                "missing_rate": column["missing"] / rows if rows else None,
                "numeric_rate_among_nonempty": column["numeric"] / column["nonempty"] if column["nonempty"] else None,
                "top_values_approximate": [{"value": key, "count": count} for key, count in counter.most_common(top_k)],
            }
    profile = {
        "profile_version": PROFILE_VERSION,
        "input": str(input_csv),
        "input_sha256": sha256_file(input_csv),
        "rows_profiled": rows,
        "column_count": len(names),
        "columns": columns,
        "limits": ["top value counts use bounded-memory heavy-hitter approximation", "blank strings count as missing", "numeric parsing is lexical and does not certify semantic type"],
    }
    output_json.parent.mkdir(parents=True, exist_ok=True)
    try:
        part.write_text(json.dumps(profile, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        os.replace(part, output_json)
    except BaseException:
        if part.exists():
            part.unlink()
        raise
    return profile
