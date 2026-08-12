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
# Provenance-Aware Event Reconstruction

Reconstructs an event timeline while retaining source, timestamp, confidence, missingness, and contradiction metadata instead of presenting inferred events as facts.

- Use: compare provenance-aware reconstruction with a simple timestamp baseline in E2.
- Strength: keeps dwell measurement explainable and open to dispute review.
- Limitation: cannot recover facts that no available source supports.
- Linked datasets: [[dataset-openepcis-generated-event-logs]], [[dataset-permissioned-terminal-facility-event-feed]].
- Linked experiment: [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]].
