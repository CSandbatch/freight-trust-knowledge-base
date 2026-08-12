---
type: dataset
status: candidate
phase: phase-i
schema_version: 1.0.0
verification: not-attempted
access: open synthetic generation — OpenEPCIS Test Data Generator, local, at no cost; the corpus itself is not yet generated
licence: generator is Apache 2.0; the generated corpus's licence inherits its calibration input, and the BTS-ATRI upstream terms used for calibration are unread, so redistributability is unresolved
updated: 2026-08-03
tags:
- type/dataset
- domain/provenance
- domain/freight
- confidence/synthetic
- audience/internal
- lifecycle/candidate
- domain/standards
---
# OpenEPCIS-Generated Event Logs

Synthetic facility and goods-movement event traces.

- Access: open synthetic generation.
- Events: tender, appointment, arrival, dock, loading, departure, and delivery.
- Use: inject missing, delayed, duplicated, contradictory, and tampered events.
- Limitation: synthetic timing is not real-facility ground truth without calibration or partner validation.
- Linked experiment: [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]]
- Also supports: [[experiment-e5-orchestration-value]].
- Linked methods: [[method-event-log-generation-and-anomaly-injection]], [[method-provenance-aware-event-reconstruction]], [[method-expert-adjudication]].
