---
type: log
status: current
owner: research-and-knowledge-architecture-lead
schema_version: 1.0.0
updated: '2026-08-18'
tags:
- type/log
- domain/freight
- domain/identity
- domain/data-science
- lifecycle/current
- audience/internal
- programme/e1
---
# E1 Academic Design Conformance Report — RC2

> [!warning] Scope of this stored conformance result
> The 35/35 result predates the 2026-08-18 decision to add
> [[method-llm-assisted-entity-resolution]]. It remains evidence about the controlling E1
> sampling, inferential and reporting design, but it is not a passed review of the new LLM
> implementation. LLM eligibility for `C*` remains blocked by
> [[09-meta/gaps/gap-018-e1-llm-readiness]] and requires an executable adversarial/conformance
> rerun before final-test access.

Mechanical conformance check for the post-review E1 protocol. This report tests whether the protocol contains the methodological controls required by [[e1-academic-design-review]]. It does **not** certify empirical validity, legal correctness, reviewer competence, or peer-reviewed acceptance.

**Result: 35/35 checks passed.**

| # | Design requirement | Result |
|---:|---|---|
| 1 | Single confirmatory hierarchical question | **PASS** |
| 2 | Exactly one development-selected C* reaches test | **PASS** |
| 3 | Probability-based representative Cohort R | **PASS** |
| 4 | Purposive Cohort H barred from population accuracy claims | **PASS** |
| 5 | Optional Cohort J for external validity | **PASS** |
| 6 | Entity-centric cluster closure tracked | **PASS** |
| 7 | Continuing F6a and novel F6b separated | **PASS** |
| 8 | Training/development and confirmatory test legal persons label-disjoint | **PASS** |
| 9 | Pre-cutoff reference history distinguished from training labels | **PASS** |
| 10 | Learned preprocessing/embeddings/calibration train-dev only | **PASS** |
| 11 | Graph path leakage audit required | **PASS** |
| 12 | Candidate generation included end-to-end | **PASS** |
| 13 | Common-candidate ablation isolates resolver contribution | **PASS** |
| 14 | Assignment precision is safety estimand | **PASS** |
| 15 | Auto-resolution yield/recall is utility estimand | **PASS** |
| 16 | Coverage is reported | **PASS** |
| 17 | Clustering metrics go beyond pairwise F1 | **PASS** |
| 18 | Calibration hierarchy goes beyond ECE | **PASS** |
| 19 | Full risk-coverage analysis required | **PASS** |
| 20 | Design-weighted inference required | **PASS** |
| 21 | Pair-independent bootstrap prohibited | **PASS** |
| 22 | Paired method comparison preserved in resampling | **PASS** |
| 23 | Reference-standard uncertainty sensitivity required | **PASS** |
| 24 | Subgroup uncertainty includes insufficient-precision outcome | **PASS** |
| 25 | Multiplicity/model-selection discipline specified | **PASS** |
| 26 | Simulation-based sample-size planning and freeze | **PASS** |
| 27 | Gold adjudicators and operational reviewers separated | **PASS** |
| 28 | Operational human cases randomized within reviewer blocks | **PASS** |
| 29 | Same reviewer never sees same case in both conditions | **PASS** |
| 30 | Synthetic corruption restricted to observation noise | **PASS** |
| 31 | Test set opened once after protocol freeze | **PASS** |
| 32 | Frozen hashes/manifests and raw predictions required | **PASS** |
| 33 | Protocol deviations and negative/null results retained | **PASS** |
| 34 | No deployment recommendation from benchmark alone | **PASS** |
| 35 | Final hostile review has zero open Critical/Major | **PASS** |

## Interpretation

A clean result means the written design includes the preregistration, sampling, split, leakage, reference-standard, inference, calibration, abstention, human-review, robustness, and reproducibility controls selected during the academic review. Numeric thresholds and final sample size remain deliberately unfrozen until the development-only pilot and PI/domain harm analysis are complete.

Related: [[e1-academic-design-review]] · [[e1-benchmark-sampling-and-split-plan]] · [[e1-statistical-analysis-and-preregistration-plan]] · [[e1-reporting-and-reproducibility-checklist]] · [[experiment-e1-entity-resolution-and-identity-assurance]]
