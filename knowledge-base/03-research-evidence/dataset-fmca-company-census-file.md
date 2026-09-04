---
type: dataset
status: candidate
phase: phase-i
schema_version: 1.0.0
verification: confirmed
access: bulk download, CSV/JSON/XML via Socrata; no login, no API key, no agreement
licence: metadata licence field reads "unknown"; public access is confirmed but reuse and derived-benchmark redistribution rights are unresolved
updated: 2026-08-20
tags:
- type/dataset
- domain/identity
- domain/freight
- confidence/dataset
- audience/internal
- lifecycle/candidate
---
# FMCSA Company Census File

Real identity and registration seed records for carrier entity resolution.

- **Live source check (2026-08-20):** dataset `az4n-8mr2` is a tabular public asset. A live
  count query returned 4,487,571 rows; the columns endpoint returned 147 columns; `DOT_NUMBER`
  is the declared row identifier. The data timestamp was 2026-08-18T14:01:28Z and the separate
  metadata timestamp was 2026-08-20T10:16:01Z. Counts and timestamps are retrieval-time facts,
  not permanent dataset properties.
- **Access:** unauthenticated Socrata SODA and bulk CSV export. The successful E1 snapshot used
  `https://data.transportation.gov/api/v3/views/az4n-8mr2/export.csv?accessType=DOWNLOAD`.
- **Fields:** carrier identifiers, legal/DBA names, physical/mailing addresses, contacts,
  operations, equipment/drivers, status and review attributes. The official
  `MCMIS Company Census Data Dictionary (Rev08), 2026-01-23` was retrieved with the snapshot;
  blank portal column descriptions are not treated as field definitions.
- **Cadence/history:** metadata declares `R/P1D`; FMCSA says the file is built from a
  24-hour-old database and updated daily. The portal exposed no archived versions during this
  retrieval, so historical state must be captured prospectively through immutable snapshots.
- Use: normalize entities and create time-aware identity cases.
- Limitation: it carries no labeled fraud or chameleon-carrier outcomes; expert adjudication is required.
- Rights boundary: do not infer a public-domain or redistribution licence from government hosting;
  the exact published licence field is `https://project-open-data.cio.gov/unknown-license/`.
  Obtain a rights decision before distributing source rows or derived record data.
- **Frozen local snapshot:** the 2026-08-20 acquisition contains 2,111,561,467 CSV bytes with
  SHA-256 `e7160e46cca201a68e6d7db759b2a2ccc969c6955a7e35bb28d4c06fabe67f04`.
  Raw and row-level derived files are ignored and local-only. The public, row-free manifest is
  [[e1-company-census-snapshot-manifest-2026-08-20.json]].
- Linked experiment: [[experiment-e1-entity-resolution-and-identity-assurance]]
- Linked methods: [[method-deterministic-entity-matching]], [[method-probabilistic-entity-resolution]], [[method-graph-assisted-entity-resolution]].
