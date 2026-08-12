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
- Limitation: synthetic anomalies may not represent all real operational failure modes.
- Linked datasets: [[dataset-openepcis-generated-event-logs]], [[dataset-bts-truck-travel-time-data]].
- Linked experiment: [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]].
