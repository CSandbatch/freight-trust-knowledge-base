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
- domain/data-science
- domain/standards
- confidence/mixed
- audience/internal
- programme/e1
---
# E1 Reporting and Reproducibility Checklist

This is an E1-specific reporting contract. [[source-tripod-ai-2024-reporting-analogue]] is used only as a mature transparency analogue; E1 is not a clinical prediction study.

## A. Research question and scope

- [ ] Target population and use context stated.
- [ ] Legal-person Task A target separated from Task B/C/dispositions.
- [ ] Primary confirmatory question identified.
- [ ] Secondary/exploratory questions labeled.
- [ ] Intended use and prohibited consequential uses stated.

## B. Data and benchmark construction

- [ ] Frame snapshot ID/date/hash reported.
- [ ] Inclusion/exclusion rules reported.
- [ ] Sampling strata, selection probabilities and weights reported.
- [ ] Cohort R representative sample separated from Cohort H challenge set.
- [ ] Cohort J jurisdiction/external holdout identified if present.
- [ ] Cluster-closure procedure reported.
- [ ] Source access/coverage gaps reported.
- [ ] Gold-reference uncertainty and disagreement reported.
- [ ] Redistribution rights and sensitive-field handling reported.

## C. Temporal validity and leakage

- [ ] `T_train_end`, `T_dev_end`, feature cutoff, test window and adjudication cutoff reported.
- [ ] Gold-label/test entities excluded from parameter/model tuning.
- [ ] Pre-cutoff reference history distinguished from training labels.
- [ ] F6a continuing and F6b novel entities reported separately.
- [ ] All learned preprocessing fit only on train/dev.
- [ ] Graph edge/embedding leakage audit passed.
- [ ] Test-set access log retained.

## D. Methods

- [ ] Deterministic baseline fully specified.
- [ ] Fellegi-Sunter/probabilistic baseline fully specified.
- [ ] Graph method fully specified.
- [ ] Candidate-generation/blocking rules reported for every method.
- [ ] Hyperparameter search space/budget and selection criterion reported.
- [ ] Final `C*` selected before test opening.
- [ ] Random seeds, library versions and runtime environment locked.

## E. Primary evaluation

- [ ] `P*`, `Delta*` and review budget preregistered.
- [ ] Assignment precision, recall/auto-resolution yield and coverage reported.
- [ ] Hierarchical safety→utility gate followed.
- [ ] Design weights applied.
- [ ] 95% CIs based on entity/design-aware resampling.
- [ ] Paired method difference reported.
- [ ] No post-hoc threshold changes.

## F. Clustering and candidate evaluation

- [ ] Pairwise precision/recall reported.
- [ ] B-cubed precision/recall/F1 reported.
- [ ] Cluster precision/recall and exact-cluster recovery reported where meaningful.
- [ ] Over-merge and under-merge distributions reported.
- [ ] Candidate recall/pair completeness and reduction ratio reported.
- [ ] End-to-end recall includes blocking misses.

## G. Calibration and abstention

- [ ] Calibration intercept/in-the-large reported.
- [ ] Calibration slope reported.
- [ ] Reliability curve reported.
- [ ] Brier score reported.
- [ ] ECE, if used, labeled secondary.
- [ ] Risk-coverage curve reported.
- [ ] Operating-point coverage and accepted-case error reported.
- [ ] Abstention by subgroup reported.

## H. Human review

- [ ] Gold adjudicators separated from operational reviewers.
- [ ] Reviewer training and qualification documented.
- [ ] Observed and label-specific agreement reported.
- [ ] Chance-corrected agreement reported with caveats.
- [ ] Disagreement/adjudication/UNRESOLVED rates reported.
- [ ] Workflow experiment randomization and reviewer/case blocking reported.
- [ ] Review time distribution and accuracy reported together.

## I. Subgroups, robustness and failure modes

- [ ] Prespecified subgroup denominators/effective sample sizes reported.
- [ ] No binary subgroup conclusion where precision is inadequate.
- [ ] Challenge cohort clearly marked nonrepresentative.
- [ ] Corruption mechanism and severity reported.
- [ ] Reference-standard sensitivity analyses reported.
- [ ] Error taxonomy and representative false merges/splits documented.

## J. Reproducibility

- [ ] Protocol hash and Git commit recorded.
- [ ] Data manifest hashes recorded.
- [ ] Train/dev/test manifests access-controlled and versioned.
- [ ] Code/dependency lockfile archived.
- [ ] Full model configuration archived.
- [ ] Sampling/replicate-weight file archived.
- [ ] Test run performed through one frozen command/workflow.
- [ ] Raw predictions retained before metric computation.
- [ ] Deviations from protocol logged with timestamps and approver.
- [ ] Negative/null results retained.

## K. Claim discipline

- [ ] “Effective in benchmark” not upgraded to “operationally useful” without operational evidence.
- [ ] Challenge-set success not generalized to population accuracy.
- [ ] Anchor-visible F0 control not presented as headline performance.
- [ ] Task A identity result not presented as fraud/chameleon determination.
- [ ] Scope limits by jurisdiction/source availability stated.

## Sources

[[source-tripod-ai-2024-reporting-analogue]] · [[source-binette-2024-entity-centric-er-evaluation]] · [[source-harron-2017-linkage-quality-guide]]
