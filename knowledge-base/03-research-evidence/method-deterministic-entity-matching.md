---
type: method
status: candidate
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/method
- lifecycle/candidate
- domain/freight
- domain/identity
- programme/e1
---
# Deterministic Entity Matching

Transparent rule-based baseline for E1. It normalizes identifiers, names, addresses, and other
permitted fields, then applies a preregistered decision rule. It is a baseline, not the gold
standard and not a legal definition of identity.

## E1 constraints

- Run under the same F0–F6 feature regimes defined in [[e1-carrier-identity-and-relationship-standard]].
- An authoritative USDOT-visible run is an **anchor-visible control**, not the headline entity-
  resolution result; otherwise the benchmark can collapse into identifier lookup.
- A claimed USDOT is not treated as an authoritative assignment.
- MC/operating authority, DBA, owner, address, insurer, vehicle, or equipment matches do not
  imply legal-person identity by themselves.
- Safety/enforcement/motive attributes are excluded from Task A.
- Deterministic rules must be time-aware and may abstain when evidence is missing or conflicting.

## Outputs

Candidate set, rule fired, evidence fields, Task A prediction, abstention state, explanation,
and runtime. Blocking recall is reported separately from end-to-end recall.

- Strength: easy to audit and reproduce; establishes the transparent floor.
- Limitation: brittle to spelling changes, missing anchors, temporal drift, and deliberately
  misleading claims; rule interactions can encode hidden bias.
- Linked dataset: [[dataset-fmca-company-census-file]], [[dataset-fmca-registration-insurance-safety-records]], [[dataset-e1-adjudicated-carrier-identity-cases]].
- Linked experiment: [[experiment-e1-entity-resolution-and-identity-assurance]].
