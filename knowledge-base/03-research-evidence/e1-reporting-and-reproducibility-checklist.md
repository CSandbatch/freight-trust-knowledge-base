---
type: method
status: candidate
schema_version: 1.0.0
updated: 2026-08-18
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
- [ ] Duplicate-anchor multiplicity, entity/observation inclusion-probability derivation, and simulation recovery test reported.
- [ ] Cohort R representative sample separated from Cohort H challenge set.
- [ ] Cohort J jurisdiction/external holdout identified if present.
- [ ] Cluster-closure procedure reported.
- [ ] Design-weighted closure failures/reasons, closure-eligible estimand, and frozen exclusion bounds/sensitivity reported.
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
- [ ] Finite operating-policy grid, `P*`/review-budget feasibility rule, C* selection objective, and ordered tie-break frozen.
- [ ] Random seeds, library versions and runtime environment locked.
- [ ] C6 promotion gates frozen and evaluated on development only before any C* eligibility decision.
- [ ] Exactly one gate-qualified C2/C3/C6 system selected as `C*`; all nonselected outputs labeled descriptive.
- [ ] C6 exact model/provider, prompt/schema/evidence view, routing/fallback/retry rules and reconciliation layer locked.
- [ ] C6 common-candidate and end-to-end views reported separately.
- [ ] L0-L7 purposes, primary C6 configuration/selection rule and compute/API-call budget preregistered.

## E. Primary evaluation

- [ ] `P*`, `Delta*` and review budget preregistered.
- [ ] Assignment precision, recall/auto-resolution yield and coverage reported.
- [ ] `LINK_EXISTING` and `CREATE_NEW` precision, recall, confusion counts, coverage, and harm categories reported separately.
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
- [ ] C6 self-reported confidence not treated as calibrated probability.

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
- [ ] C6 schema failures, unsupported assertions, unknown evidence IDs and reconciliation interventions reported.
- [ ] C6 repeated-inference action/target/evidence flip rates reported.
- [ ] C6 candidate-order randomization/counterbalancing diagnostic and order-induced flip rate reported.
- [ ] C6 masked/randomized-name and chronology contamination diagnostics reported with residual risk.
- [ ] C6 prompt-injection challenge success rate reported.
- [ ] C6 latency, tokens, cost, retry/timeout and provider-failure distributions reported.

## J. Reproducibility

- [ ] Protocol hash and Git commit recorded.
- [ ] Preregistration registry/location, immutable version, timestamp, and any embargo/access policy recorded.
- [ ] Data manifest hashes recorded.
- [ ] Train/dev/test manifests access-controlled and versioned.
- [ ] Code/dependency lockfile archived.
- [ ] Full model configuration archived.
- [ ] C6 raw request/response records retained under the most restrictive input classification.
- [ ] C6 request IDs/timestamps, exact route, prompts, schemas, evidence manifests and response-validator version archived.
- [ ] Dynamic model routing and silent provider fallback prohibited.
- [ ] Hosted-model field-level privacy/data-egress approval archived; restricted records excluded or processed only in an approved environment.
- [ ] Sampling/replicate-weight file archived.
- [ ] Test run performed through one frozen command/workflow.
- [ ] Immutable one-shot batch manifest identifies confirmatory and secondary configurations; no later run reuses the holdout.
- [ ] Raw predictions retained before metric computation.
- [ ] Deviations from protocol logged with timestamps and approver.
- [ ] Negative/null results retained.

## K. Claim discipline

- [ ] “Effective in benchmark” not upgraded to “operationally useful” without operational evidence.
- [ ] Challenge-set success not generalized to population accuracy.
- [ ] Anchor-visible F0 control not presented as headline performance.
- [ ] Task A identity result not presented as fraud/chameleon determination.
- [ ] Scope limits by jurisdiction/source availability stated.
- [ ] C6 output not described as authoritative evidence, legal identity, reincarnation/fraud determination, deployment fitness, or future-model performance.
- [ ] C6 labeled confirmatory only when it passed frozen development gates and was selected prospectively as the single `C*`; all other C6 outputs labeled secondary/descriptive.
- [ ] Hosted C6 result described as performance of the exact dated black-box route; pretraining contamination and future-provider/model generalization remain unresolved.

## Sources

[[source-tripod-ai-2024-reporting-analogue]] · [[source-binette-2024-entity-centric-er-evaluation]] · [[source-harron-2017-linkage-quality-guide]]
