---
type: source
status: active
schema_version: 1.0.0
source_class: peer-reviewed
verification: confirmed
accessed: 2026-08-08
updated: 2026-08-08
review_by: 2028-08-08
tags:
- type/source
- domain/identity
- domain/data-science
- confidence/peer-reviewed
- audience/internal
- programme/e1
- lifecycle/active
---
# Lam et al. 2026 — ambiguity-aware clerical-review sampling

## Citation

Joseph Lam et al. “Designing Ambiguity-Aware Clerical Review: A Stratified Sampling Framework for Record Linkage and Deduplication.” *International Journal of Population Data Science* 11(5), 2026. DOI: 10.23889/ijpds.v11i5.3595. Preprint: arXiv:2608.01401.

<https://ijpds.org/article/view/3595>

## Methodological contribution

Clerical review is expensive and is often sampled informally. The paper treats review as finite-population sampling over strata that can incorporate match score, comparison pattern, ambiguity, and demographic/group characteristics. It makes the tradeoff among workload, precision, representativeness, and coverage explicit.

## E1 consequence

- any model-dependent clerical monitoring sample must have a declared sampling frame and inclusion probabilities;
- oversampling ambiguous or high-score cases is acceptable only with design-aware estimation or when the cohort is explicitly labeled a challenge set;
- sampling strata and budgets are frozen before final performance estimation;
- the final benchmark must not silently equate “interesting cases” with a representative population.

## Consumers

[[e1-benchmark-sampling-and-split-plan]] · [[e1-adjudicator-governance-and-training]] · [[e1-academic-design-review]]
