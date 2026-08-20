---
type: source
status: active
schema_version: 1.0.0
source_class: peer-reviewed
verification: confirmed
accessed: 2026-08-18
updated: 2026-08-18
review_by: 2027-08-18
tags:
- type/source
- domain/identity
- domain/data-science
- confidence/peer-reviewed
- audience/internal
- programme/e1
- lifecycle/active
---
# Guo, Klein, and Huang 2026 — cost-aware LLM entity matching

## Citation and verification

Chaohui Guo, Michel C. A. Klein, and Zhisheng Huang. “CaRL-EM: Cost-Aware Reinforcement
Learning for Entity Matching with LLMs.” *Proceedings of the 64th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers)*, July 2026, 27281–27293.
DOI: 10.18653/v1/2026.acl-long.1258.

- ACL Anthology record: <https://aclanthology.org/2026.acl-long.1258/>
- Paper: <https://aclanthology.org/2026.acl-long.1258.pdf>
- DOI: <https://doi.org/10.18653/v1/2026.acl-long.1258>

The official ACL Anthology metadata, abstract, and paper were retrieved 2026-08-18. Venue,
authors, date, pages, DOI, seven-benchmark scope, operator set, model-selection design, and stated
quality/cost objective were checked directly rather than taken from a search-result snippet.

## What the source supports

CaRL-EM formulates multi-candidate LLM entity matching as a sequential decision problem. A learned
controller selects among `Match`, `Compare`, `Select`, and `Decide` operations and among model
capacities while incorporating inference cost. The paper reports a better quality–cost tradeoff
than its evaluated LLM baselines and manually designed pipelines across seven established entity-
matching benchmarks.

This establishes peer-reviewed precedent for treating candidate topology, operator choice, model
choice, and inference cost as coupled experimental components rather than assuming that one
pairwise prompt is the only LLM design.

## Limits

- The seven benchmarks do not test U.S. freight legal-person identity, FMCSA registrant
  continuity, E1 typed relationships, or regulatory dispositions.
- The reported results do not validate E1's `CREATE_NEW`, global cluster-coherence, calibrated
  abstention, high-precision safety floor, time-forward contamination controls, or human-review
  workflow.
- A learned controller adds model-selection degrees of freedom, training dependencies, action-
  ordering effects, and a compound model/provider cost surface. Those components would require
  their own frozen development budget and manifest in E1.
- Published benchmark performance and costs cannot be imported as E1 targets or current hosted-
  model prices.
- The paper does not establish that public benchmark examples were absent from every underlying
  model's pretraining data.

## E1 relevance

CaRL-EM is evidence that cost-aware multi-candidate routing is a credible future C6 variant. It is
not part of the default C6 implementation. Any adoption must be prospectively versioned and freeze
the controller, action space, model pool, provider routes, training data, stopping rule, and total
budget before test access. It cannot justify dynamic provider routing or post-holdout selection.

## Consumers

[[method-llm-assisted-entity-resolution]] ·
[[e1-statistical-analysis-and-preregistration-plan]] ·
[[experiment-e1-entity-resolution-and-identity-assurance]]
