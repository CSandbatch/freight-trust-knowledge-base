---
type: source
status: active
schema_version: 1.0.0
source_class: preprint
verification: confirmed
accessed: 2026-08-08
updated: 2026-08-08
review_by: 2028-08-08
tags:
- type/source
- domain/identity
- domain/data-science
- confidence/secondary
- audience/internal
- programme/e1
- lifecycle/active
---
# Binette et al. — entity-centric evaluation of entity-resolution systems

## Citation

Olivier Binette, Youngsoo Baek, Siddharth Engineer, Christina Jones, Abel Dasylva, Jerome P. Reiter. “How to Evaluate Entity Resolution Systems: An Entity-Centric Framework with Application to Inventor Name Disambiguation.” arXiv:2404.05622, first submitted 2024; current manuscript retrieved 2026-08-08.

<https://arxiv.org/abs/2404.05622>

## Methodological contribution

The paper treats entity resolution as a clustering problem and shows why pair-only benchmark evaluation can mislead. It proposes sampling fully resolved entities/clusters, then estimating global pairwise and B-cubed precision/recall through entity-centric, sampling-aware estimators. The authors explicitly warn that naive pairwise precision computed only on a benchmark can be optimistic and that biased precision combined with recall can reverse F1 rankings of competing systems.

The framework distinguishes cluster-wise error analysis, global metric estimation, sampling design, and monitoring statistics. This is directly aligned with E1 because Task A gold truth is a legal-person partition rather than a bag of unrelated pair labels.

## E1 consequence

- primary benchmark evaluation uses a probability-based **entity-centric representative cohort**;
- purposively selected hard cases are kept as a separate challenge cohort and are not used to make population-prevalence claims;
- global precision/recall estimates retain sampling/inclusion weights;
- pairwise metrics are supplemented with B-cubed and cluster/merge/split metrics;
- benchmark construction must aim at fully resolving sampled entities rather than validating only system-proposed pairs.

## Consumers

[[e1-benchmark-sampling-and-split-plan]] · [[e1-statistical-analysis-and-preregistration-plan]] · [[experiment-e1-entity-resolution-and-identity-assurance]] · [[e1-academic-design-review]]

## Related primary method and model evidence

[[source-fellegi-sunter-1969-record-linkage-theory]] ·
[[source-li-2021-ditto-deep-entity-matching]] ·
[[source-wang-2022-reality-ideality-entity-matching]] ·
[[source-peeters-2025-llm-entity-matching]] ·
[[source-wang-2025-comem-llm-entity-matching]] ·
[[source-de-meer-pardo-2025-gralmatch]] ·
[[source-wadhwa-2024-explanation-distillation-entity-matching]] ·
[[source-kamsteeg-2025-entity-matching-calibration]] ·
[[source-openrouter-routing-privacy-and-metadata]]
