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
# Dasylva & Goussanou — false negatives introduced by blocking

## Citation

Abel Dasylva and Arthur Goussanou. “Estimating the false negatives due to blocking in record linkage.” *Survey Methodology* 47(2), 2021, 299–311; Statistics Canada release 2022-01-06.

<https://www150.statcan.gc.ca/n1/pub/12-001-x/2021002/article/00002-eng.htm>

## Methodological contribution

Blocking reduces the quadratic comparison space but can permanently discard true matches before the resolver sees them. The paper treats blocking loss as part of total linkage error rather than as a computational detail.

## E1 consequence

- candidate generation is included in end-to-end evaluation;
- candidate recall/pair completeness and reduction ratio are reported separately;
- a resolver cannot claim high recall conditional on candidates if the blocking stage systematically drops true matches;
- common-candidate-set analyses are secondary mechanism ablations, not substitutes for end-to-end performance.

## Consumers

[[e1-benchmark-sampling-and-split-plan]] · [[experiment-e1-entity-resolution-and-identity-assurance]] · [[method-probabilistic-entity-resolution]] · [[method-graph-assisted-entity-resolution]]
