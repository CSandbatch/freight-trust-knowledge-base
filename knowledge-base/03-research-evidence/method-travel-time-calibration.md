---
type: method
status: candidate
schema_version: 1.0.0
tags:
- type/method
- lifecycle/candidate
- domain/freight
- domain/orchestration
---
# Travel-Time Calibration

Fits synthetic route and delay distributions to public truck travel-time observations so event simulations have realistic timing.

- Use: calibrate E2 and later E5 simulations.
- Strength: improves realism without claiming public travel-time data is facility ground truth.
- Limitation: aggregate travel times do not capture partner-specific appointment, dock, or chassis constraints.
- Linked dataset: [[dataset-bts-truck-travel-time-data]].
- Linked experiments: [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]], [[experiment-e5-orchestration-value]].
