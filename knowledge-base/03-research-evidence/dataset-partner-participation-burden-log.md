---
type: dataset
status: to-build
phase: phase-i-or-pilot
schema_version: 1.0.0
verification: not-attempted
access: to-build — consent-based collection from participating carriers, brokers, facilities, and reviewers during a pilot
licence: not yet drafted — consent instrument and terms do not exist yet
updated: 2026-08-20
tags:
- type/dataset
- domain/adoption
- domain/equity
- confidence/mixed
- audience/internal
- lifecycle/to-build
- domain/freight
---
# Partner Participation and Burden Log

Specification for consent-based adoption and equity outcome records. This public note is not
the storage location for participant records.

- Access: collected from participating carriers, brokers, facilities, and reviewers.
- Fields: invitation, activation, repeat use, requested fields, staff minutes, rejection reasons, appeals, fleet-size band.
- Use: measure reciprocal value, retention, and small-carrier burden.
- Limitation: sample size and representativeness depend on partner recruitment.
- Institutional gate: no recruitment or identifiable/private collection before the documented
  determination or approval required by the responsible institution/sponsor process and approval
  of the data-management boundary.
- Private storage: raw or pseudonymized rows, refusal reasons, costs, harms, and linkage keys
  remain outside Git in encrypted access-controlled storage; the re-identification key is separate.
- Public-vault boundary: only the schema, blank instruments, synthetic examples,
  disclosure-control method, and reviewed aggregates may be committed. The `audience/internal`
  tag does not make a Git-tracked knowledge-base file private.
- Export gate: predeclare aggregation and suppression review; do not publish row-level records or
  small cells that could expose a participant or commercially sensitive operation.
- Linked experiment: [[experiment-e4-participation-and-small-carrier-equity]]
- Linked method: [[method-staged-participation-and-equity-evaluation]].
- Human-subjects source: [[source-nsf-common-rule-human-subjects-consent]].
