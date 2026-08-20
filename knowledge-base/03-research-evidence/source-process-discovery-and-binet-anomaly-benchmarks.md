---
type: source
status: active
schema_version: 1.0.0
source_class: peer_reviewed
verification: confirmed
accessed: 2026-08-18
updated: 2026-08-18
review_by: 2028-08-18
tags: [type/source, domain/data-science, domain/provenance, confidence/primary, audience/internal, programme/e2, lifecycle/active]
---
# PDC hidden truth and BINet artificial anomaly benchmarks

## Citation and verification

Process Discovery Contest 2020 dataset, 4TU.ResearchData,
<https://data.4tu.nl/articles/dataset/Process_Discovery_Contest_2020/14626020>, with contest
purpose at <https://www.tf-pm.org/competitions-awards/discovery-contest>. Nolle et al.,
*BINet: Multivariate Business Process Anomaly Detection Using Deep Learning*, 2019,
<https://arxiv.org/abs/1902.03155>. Inspected 2026-08-18.

## Exact support

PDC supports synthetic logs with hidden reference processes for discovery/conformance
evaluation. BINet supplies artificial Skip, Insert, Rework, Early, Late, and Attribute
anomaly operators and labeled evaluation construction.

## Limits and E2 relevance

PDC is not an anomaly-injection/tamper benchmark. BINet's operators and 30% altered-case
design are not freight threat evidence or transferable prevalence. Freight fabrication,
backdating, replay, clock, multi-source contradiction, and omission are project-authored
operators whose threat model and rates must be preregistered.

Consumers: [[method-event-log-generation-and-anomaly-injection]] · [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]]
