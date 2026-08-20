---
type: dataset
status: candidate
phase: phase-i
schema_version: 1.0.0
verification: confirmed
access: free download, data.bts.gov Socrata, CSV/API
licence: US Public Domain, as stated in the BTS dataset metadata
updated: 2026-08-18
tags:
- type/dataset
- domain/freight
- confidence/dataset
- audience/internal
- lifecycle/candidate
- domain/orchestration
---
# BTS Truck Travel-Time Data

Public timing data for calibrating synthetic freight movement.

- Access: public/open annual files and Socrata API. The current product covers 2018–2024.
- Method: BTS derives annual county-pair 25th, 50th, and 75th percentile elapsed travel
  times from an ATRI-supplied sample of processed truck GPS pings. County pairs with fewer
  than 100 observed movements are excluded, and movement counts are binned.
- Use: constrain transit-time distributions in event simulations to empirically plausible
  county-pair ranges. Preserve year and county pair; do not convert published quantiles into
  unsupported facility-level distributions.
- Limitation: a movement is elapsed time from the last ping in an origin county to the first
  ping in a destination county and may include stops. The product contains no appointment,
  gate, dock, loading, release, or departure ground truth and no individual trajectories.
- Source: [[source-bts-atri-freight-mobility-initiative]].
- Linked experiment: [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]]
- Also supports: [[experiment-e5-orchestration-value]].
- Linked methods: [[method-travel-time-calibration]].
