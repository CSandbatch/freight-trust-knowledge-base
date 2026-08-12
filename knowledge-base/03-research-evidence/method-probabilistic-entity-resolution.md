---
type: method
status: candidate
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/method
- lifecycle/candidate
- domain/freight
- domain/identity
- programme/e1
---
# Probabilistic Entity Resolution

Estimates evidence for record-to-legal-person assignment under uncertainty rather than forcing a
binary match from brittle field rules. Candidate implementations may include Fellegi–Sunter-
style linkage, supervised pair classification, or other calibrated models, but the target
semantics are fixed by [[e1-carrier-identity-and-relationship-standard]], not learned from the
model.

## E1 constraints

- Evaluate under the same F0–F6 feature regimes as every other condition.
- Task A predicts `SAME_LEGAL_PERSON`, `DISTINCT_LEGAL_PERSON`, or abstains/returns unresolved;
  it does not predict “chameleon” from motive/safety history.
- Safety, enforcement, bankruptcy, and other negative-history motive fields are masked from
  Task A to prevent circular identity labeling.
- Claimed identifiers and authoritative assignments are distinct features.
- Calibration is fit only on development data; thresholds are frozen before the final holdout.
- Pair probabilities must reconcile to coherent entity clusters or be explicitly treated as
  pairwise evidence rather than canonical identity truth.

## Evaluation

Report end-to-end assignment precision/recall/coverage at declared operating points; pairwise and B-cubed/cluster metrics; calibration intercept, slope, reliability curve and Brier score; risk-coverage/abstention curves; blocking recall; subgroup performance; and entity-cluster consistency. ECE, if reported, is secondary. Anchor-visible results are diagnostic controls only.

- Strength: handles partial disagreement, missingness, and uncertain evidence.
- Limitation: requires adjudicated labels, calibration, explicit false-positive controls, and a
  cluster-resolution policy; learned correlations can reproduce weak-field or subgroup bias.
- Linked dataset: [[dataset-fmca-company-census-file]], [[dataset-fmca-registration-insurance-safety-records]], [[dataset-e1-adjudicated-carrier-identity-cases]].
- Linked experiment: [[experiment-e1-entity-resolution-and-identity-assurance]].

## Model-selection and test discipline

Eligible probabilistic variants, preprocessing, hyperparameter search space, calibration method and selection/tie-break criterion are frozen on development data. Only a single development-selected candidate may enter the confirmatory final-test comparison.
