---
type: dataset
status: candidate
phase: phase-i
schema_version: 1.0.0
verification: confirmed
access: open synthetic generation — OpenEPCIS Test Data Generator, local, at no cost; the corpus itself is not yet generated
licence: generator is Apache 2.0; corpus licence and redistribution terms must be declared when the corpus is generated
updated: 2026-08-18
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
- Verification boundary: the generator and its Apache-2.0 licence are confirmed; the
  project corpus does not yet exist. Pin an image digest or commit before generation.
- Standard profile: EPCIS 2.0.1 with CBV 2.0.0. Validate generated JSON/JSON-LD against
  GS1's normative schema and, where applicable, SHACL artifacts.
- Events: CBV supplies standard steps such as arriving, loading, unloading, receiving, and
  departing. Tender, appointment, gate-status, dock-status, release, project confidence,
  permitted-use, and assertion-provenance fields are freight-profile extensions, not CBV
  terms.
- Use: derive delayed, duplicated, contradictory, and threat-model-specific altered observations,
  plus trace-level omissions under a separate observability model.
- Limitation: generated traces are synthetic feasibility fixtures, not facility ground truth.
  An event-hash identifier identifies content; it does not authenticate the source or prove
  the event occurred. Generated-output licensing does not automatically inherit a calibration
  dataset's licence; record each input and transformation separately.
- Sources: [[source-gs1-epcis-cbv-2-0]], [[source-openepcis-test-data-generator]].
- Linked experiment: [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]]
- Also supports: [[experiment-e5-orchestration-value]].
- Linked methods: [[method-event-log-generation-and-anomaly-injection]], [[method-provenance-aware-event-reconstruction]], [[method-expert-adjudication]].
