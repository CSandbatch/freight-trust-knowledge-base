---
type: dataset
status: candidate
phase: phase-i
schema_version: 1.0.0
verification: confirmed
access: named FMCSA and DOT Data Portal files are publicly downloadable; field/source suitability remains predicate-specific
licence: unresolved — current DOT Data Portal metadata reports Unknown License; public access does not establish benchmark redistribution rights
updated: 2026-08-18
tags:
- type/dataset
- domain/identity
- domain/freight
- confidence/primary
- audience/internal
- action/needs-verification
- lifecycle/candidate
---
# FMCSA Registration, Insurance, and Safety Records

Candidate authoritative evidence attributes for carrier verification, subject to predicate,
effective-date, schema, and source-rights checks.

- **Verified current access:** FMCSA's Open Data Program successor page links current DOT Data
  Portal datasets. The Motus operating-authority family includes “All With History” baselines and
  daily-difference variants for carrier, authority history, insurance, insurance history, BOC-3,
  and revocation/suspension records. Selected live records expose documented fields and declare a
  daily cadence. See [[source-fmcsa-licensing-and-insurance-dataset]] and
  [[source-fmcsa-mcmis-catalog]].
- **Legacy status:** the former `jeyh-5nsj` Licensing & Insurance catalog record is an empty,
  link-only legacy stub. It is not the current data feed and must not be treated as an active
  table.
- **Use:** test time-bounded evidence linkage, freshness, conflicts, candidate generation, and
  predicate-specific source weighting. Safety/enforcement/motive fields remain excluded from E1
  Task A.
- **Limits:** catalog metadata reports `Unknown License`; legacy and Motus schemas are not assumed
  equivalent; several date fields are typed as text; declared cadence is not a delivery guarantee;
  and no one record establishes current legal-person identity by itself. Crash/inspection/safety
  families require their own field-level verification rather than inheriting the Motus
  operating-authority verification.
- **Release rule:** public downloadability is not treated as permission to redistribute source
  rows, enriched packets, prompts, or the derived benchmark. Rights are tracked per incorporated
  source and case.
- Linked experiment: [[experiment-e1-entity-resolution-and-identity-assurance]]
- Linked methods: [[method-deterministic-entity-matching]], [[method-probabilistic-entity-resolution]], [[method-graph-assisted-entity-resolution]].
