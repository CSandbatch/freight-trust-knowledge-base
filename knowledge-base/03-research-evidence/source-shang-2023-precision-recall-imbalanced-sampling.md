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
- domain/data-science
- domain/identity
- confidence/peer-reviewed
- audience/internal
- programme/e1
- lifecycle/active
---
# Shang et al. 2023 — precision/recall under imbalanced evaluation sampling

## Citation

Hongwei Shang, Jean-Marc Langlois, Kostas Tsioutsiouliklis, Changsung Kang. “Precision/Recall on Imbalanced Test Data.” *Proceedings of AISTATS 2023*, PMLR 206:9879–9891.

<https://proceedings.mlr.press/v206/shang23a.html>

## Methodological contribution

When labels are scarce and the positive class is rare, oversampling evaluation strata changes the observed class balance and requires adjusted estimators and confidence intervals. The paper derives interval procedures for adjusted precision/recall under such sampling.

## E1 consequence

Purposive or disproportionate sampling is never followed by naive precision/recall calculation. E1 either uses the entity-centric probability sample for population estimates or carries explicit sampling weights/design-aware intervals.

## Consumers

[[e1-benchmark-sampling-and-split-plan]] · [[e1-statistical-analysis-and-preregistration-plan]]
