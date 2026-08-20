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
- Required semantics: preserve EPCIS `eventTime` as the capturing application's assertion of
  when an event occurred; use repository `recordTime` only for its bookkeeping meaning; retain
  corrections/error declarations, source observation time, derivation, and current assertion
  state separately.
- Missingness: absence of an observation is not an event and is never proof of non-occurrence.
  Return supported events, inferred events, unresolved omissions, and censored intervals as
  different output types.
- Leakage control: source-reliability values are generator-declared scenario inputs or learned
  only on development data. Hidden truth and holdout outcomes may never set them.
- Limitation: cannot recover facts that no available source supports. A reconstructed order is
  an inference with coverage and uncertainty, not a cleaned-up authoritative timeline.
- Source: [[source-gs1-epcis-cbv-2-0]].
- Linked datasets: [[dataset-openepcis-generated-event-logs]], [[dataset-permissioned-terminal-facility-event-feed]].
- Linked experiment: [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]].
