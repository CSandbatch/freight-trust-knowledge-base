---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-20
updated: 2026-08-20
review_by: 2027-08-18
tags: [type/source, domain/provenance, domain/standards, confidence/primary, audience/internal, programme/e2, lifecycle/active]
---
# GS1 EPCIS 2.0.1 and CBV 2.0.0

## Citation and verification

GS1, *EPCIS and CBV Implementation Guideline / Standard artifacts*. EPCIS 2.0.1 is listed
as published 2025-07-01; CBV current artifact is 2.0.0. Directly inspected 2026-08-18:
<https://ref.gs1.org/standards/epcis/artefacts>,
<https://ref.gs1.org/standards/epcis/2.0.1/>, and
<https://ref.gs1.org/standards/cbv/>.

## Exact support

Normative authority for EPCIS event/document/repository semantics, including `eventTime`,
repository `recordTime` (EPCIS 2.0.1 section 7.2.2), event business context, locations,
`errorDeclaration`, and namespaced user/vendor extensions (section 9.1); CBV
defines standard business steps/dispositions such as arriving, receiving, loading,
unloading, and departing.

## Limits and E2 relevance

The published artifact set includes normative JSON Schema and SHACL. The standards do not supply
observations, a facility benchmark, observability truth, provenance confidence, anomaly labels,
or appointment/gate/dock status vocabulary. Those are explicit namespaced project profile or
wrapper fields. E2 must validate generated documents against pinned artifacts and preserve
time/correction meanings.

Consumers: [[dataset-openepcis-generated-event-logs]] · [[method-provenance-aware-event-reconstruction]] · [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]]
