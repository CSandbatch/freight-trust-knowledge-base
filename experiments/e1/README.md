# E1 Stages 0-4

This package implements the pre-model E1 data path: source validation, immutable Company Census
acquisition, corpus profiling, canonical normalization and bounded candidate generation. It does
not train or evaluate an entity-resolution model.

Use the repository virtual environment from the repository root:

```powershell
.\.venv\Scripts\python.exe -m experiments.e1 validate --input <company-census.csv>
.\.venv\Scripts\python.exe -m experiments.e1 acquire --output-root data\raw --snapshot-date YYYY-MM-DD
.\.venv\Scripts\python.exe -m experiments.e1 inspect <snapshot-directory>
.\.venv\Scripts\python.exe -m experiments.e1 profile <input.csv> <profile.json>
.\.venv\Scripts\python.exe -m experiments.e1 normalize <input.csv> <records.jsonl.gz> --observed-at <UTC-timestamp>
.\.venv\Scripts\python.exe -m experiments.e1 candidates <input.csv> <pairs.csv> <report.json> --limit 250000
.\.venv\Scripts\python.exe -m experiments.e1 dry-run
```

All operational raw, derived and run paths are ignored. The source licence metadata remains
unknown, so do not add source rows or row-level derived records to Git. Candidate pairs are
retrieval aids only; shared fields do not establish identity, and blocking recall is not
measurable until a model-independent adjudicated continuity fixture exists.
