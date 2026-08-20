---
type: method
status: candidate
schema_version: 1.0.0
tags:
- type/method
- lifecycle/candidate
- domain/freight
- domain/provenance
---
# Event-Log Generation and Anomaly Injection

Creates valid base traces, then injects labeled missing, delayed, duplicated, contradictory, and tampered events at controlled rates.

- Use: construct the E2 facility-event benchmark.
- Strength: produces known ground truth and repeatable difficulty levels.
- Task separation: classify altered observed events at event level; detect omissions at trace
  level against an expected-process and observability model; treat dwell intervals with missing
  endpoints as censored rather than inventing an event row whose status is `missing`.
- Precedent boundary: the Process Discovery Contest supports hidden-truth synthetic process
  and conformance evaluation. Nolle et al.'s BINet work supports artificial Skip, Insert,
  Rework, Early, Late, and Attribute anomaly operators. Neither source supplies freight
  fabrication, replay, backdating, clock, or multi-source contradiction operators; those are
  project-authored synthetic design choices with an explicit threat model.
- Reproducibility: freeze the base trace before alteration and retain generator version,
  configuration, random seed, operator, changed fields, severity, and hidden label.
- Limitation: synthetic anomalies may not represent real operational failure modes. Logical
  anomaly detection is not cryptographic tamper evidence and does not prove source truth.
- Sources: [[source-process-discovery-and-binet-anomaly-benchmarks]].
- Linked datasets: [[dataset-openepcis-generated-event-logs]], [[dataset-bts-truck-travel-time-data]].
- Linked experiment: [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]].
