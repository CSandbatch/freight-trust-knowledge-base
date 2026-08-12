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
- domain/data-science
- domain/identity
- confidence/secondary
- audience/internal
- programme/e1
- lifecycle/active
---
# Traub et al. 2024 — evaluation of selective classification / abstention

## Citation

Jeremias Traub et al. “Overcoming Common Flaws in the Evaluation of Selective Classification Systems.” arXiv:2407.01032, 2024.

<https://arxiv.org/abs/2407.01032>

## Methodological contribution

Selective classifiers trade coverage against error by abstaining. Evaluating only one rejection threshold can hide poor behavior elsewhere on the coverage-risk curve. The paper proposes generalized risk-coverage evaluation and highlights common methodological flaws in abstention benchmarking.

## E1 consequence

- C4 is evaluated across a full risk/coverage curve plus a preregistered operating point;
- accepted-case precision and coverage are always reported together;
- area-under-generalized-risk-coverage is exploratory/supporting, not the sole endpoint;
- abstention is separately audited by subgroup so safety is not purchased through disproportionate deferral.

## Consumers

[[e1-statistical-analysis-and-preregistration-plan]] · [[experiment-e1-entity-resolution-and-identity-assurance]]
