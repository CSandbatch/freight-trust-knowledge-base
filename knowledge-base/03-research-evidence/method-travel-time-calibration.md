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
- Method boundary: preserve annual county pair and the published 25th/50th/75th percentiles;
  document any interpolation or fitted distribution and validate it against held-out published
  quantiles. Do not subtract the aggregate movement time to infer facility service time.
- Limitation: aggregate elapsed movement times can include stops and do not capture
  partner-specific appointment, dock, labor, queue, chassis, or facility constraints.
- Source: [[source-bts-atri-freight-mobility-initiative]].
- Linked dataset: [[dataset-bts-truck-travel-time-data]].
- Linked experiments: [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]], [[experiment-e5-orchestration-value]].
