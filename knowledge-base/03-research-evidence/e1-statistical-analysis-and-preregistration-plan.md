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
- confidence/mixed
- audience/internal
- programme/e1
---
# E1 Statistical Analysis and Preregistration Plan

## 1. Inferential posture

E1 is primarily an **estimation and comparative validation study**, not a fishing expedition for a small p-value. The confirmatory analysis has one hierarchical primary question; all other comparisons are secondary or exploratory and are labeled accordingly.

The final test set is opened once after protocol, sampling, preprocessing, model selection, calibration, thresholds and code paths are frozen.

## 2. Primary scientific question

In the representative, time-forward Cohort R, does the single development-selected non-manual system `C*` resolve more legal-person observations than the deterministic baseline C1 **while maintaining the preregistered safety precision floor and the same human-review budget**?

`C*` is selected between eligible C2/C3 variants using development data only. Selection criteria and tie-break rules are frozen before test access. The test set is not used to select the “best” model.

## 3. Primary estimand and hierarchical success gate

The primary operational unit is a post-cutoff **observation-resolution decision** with one of three actions:

- `LINK_EXISTING` — attach to one existing legal-person cluster;
- `CREATE_NEW` — initiate a new legal-person cluster;
- `ABSTAIN` — defer to human review.

For automatic decisions, define design-weighted:

- **assignment precision (PPV):** proportion of non-abstained automatic assignments/creations that are correct;
- **assignment recall / auto-resolution yield:** proportion of gold-resolvable test observations correctly resolved automatically;
- **coverage:** proportion of eligible observations receiving a non-abstained automatic decision.

The confirmatory gate is hierarchical:

1. **Safety gate:** the lower bound of the preregistered 95% confidence interval for `C*` assignment precision is at least `P*` in the primary F6 time-forward cohort.
2. **Utility gate:** only if Gate 1 passes, compare `C*` with C1 on assignment recall/auto-resolution yield at the same `P*` policy and the same review-budget constraint. Success requires the lower 95% CI for the paired improvement to exceed the preregistered minimum meaningful improvement `Delta*` (or zero if the PI explicitly chooses a pure-superiority criterion before test opening).

`P*` and `Delta*` are set from harm analysis, development baseline performance, review capacity and pilot-based precision calculations, never from final-test results.

This structure prevents an apparent recall gain from being purchased through unsafe false merges.

## 4. Secondary clustering metrics

Because Task A truth is a partition, E1 also reports:

- pairwise precision and recall;
- B-cubed precision, recall and F1;
- cluster precision and cluster recall;
- number/rate of over-merged gold entities;
- number/rate of split gold entities;
- distribution of merge and split sizes;
- exact-cluster recovery where meaningful.

Naive benchmark F1 is not used as the sole system-ranking statistic. [[source-binette-2024-entity-centric-er-evaluation]] documents that benchmark precision/F1 can be biased and can reverse method rankings.

## 5. Candidate-generation metrics

Blocking is part of the end-to-end system. Report:

- pair completeness / candidate recall;
- recall@K where ranked candidates exist;
- reduction ratio;
- average, median and P95 candidate-set size;
- candidate-generation latency;
- classification/resolution recall conditional on the true candidate being generated;
- total end-to-end recall including blocking false negatives.

See [[source-dasylva-goussanou-2021-blocking-false-negatives]].

## 6. Calibration

For methods producing probabilities/confidences, report on the representative test cohort:

- calibration-in-the-large / intercept;
- calibration slope;
- smoothed reliability/calibration plot;
- Brier score;
- log loss where probabilities are strictly defined;
- ECE only as a secondary bin-dependent summary.

Calibration is evaluated separately by F6a/F6b and major preregistered subgroups when sample size permits. Calibration models are fit on development only. See [[source-van-calster-2016-calibration-hierarchy]].

## 7. Abstention / selective prediction

Report the complete risk-coverage curve, accepted-case error as coverage increases, and the preregistered operating point. The primary C4 workflow must state:

- confidence quantity used for abstention;
- threshold-selection rule;
- expected review capacity;
- action when a human also abstains;
- whether a case may ever be auto-merged after prior human uncertainty.

AUGRC or similar generalized risk-coverage summaries may be reported as exploratory measures, but interpretation remains anchored to the operational `P*`/coverage point. See [[source-traub-2024-selective-classification-evaluation]].

## 8. Sampling weights and uncertainty

Cohort R estimates respect the sampling design from [[e1-benchmark-sampling-and-split-plan]].

Primary CIs and paired method contrasts use a survey/design-aware **entity-level resampling procedure**: resample primary sampled entities/registration anchors within design strata (or use equivalent replicate weights), carry their full cluster/error contribution together, recompute weighted metrics, and preserve method pairing within each replicate.

Do not bootstrap record pairs independently.

The preregistration fixes:

- bootstrap/replicate-weight algorithm;
- number of replicates (default target 2,000 unless simulation demonstrates a different requirement);
- confidence level (95%);
- method for percentile/BCa or design-based intervals;
- behavior in sparse strata.

If sample-size or sparse-cell conditions invalidate the planned interval, the analysis reports the failure rather than switching post hoc to a more favorable method.

## 9. Reference-standard uncertainty

Final adjudication is the primary reference standard, but human review is not assumed infallible.

Report:

- observed agreement;
- label-specific agreement;
- Cohen's kappa and a prevalence-robust complement such as Gwet's AC1, interpreted descriptively rather than against arbitrary “good/bad” cutoffs;
- disagreement/adjudication rate;
- `UNRESOLVED` rate;
- reviewer-specific sensitivity analyses.

Primary model metrics are repeated under at least:

1. final adjudicated labels;
2. exclusion of contested/adjudicated cases;
3. reviewer-A and reviewer-B labels separately;
4. conservative lower/upper bounds for gold-`UNRESOLVED` cases when the metric is identifiable.

If disagreement remains materially high after training, a latent-class/reference-standard sensitivity analysis is considered, consistent with [[source-dasylva-2016-clerical-review-quality]].

## 10. Missingness and source absence

Missingness is never silently converted to disagreement. For each field, predeclare whether missingness is:

- structural/not applicable;
- source not available;
- source available but field absent;
- field redacted;
- extraction failure;
- temporally not yet observed.

Learned imputation or missingness encoders are trained on development only. Missingness itself may be predictive, so its use as a feature is separately declared and audited for source/jurisdiction leakage.

## 11. Subgroups and representativeness

Predeclared descriptive/validity subgroups include:

- fleet-size band;
- F6a continuing vs F6b novel entities;
- jurisdiction/source-access environment;
- record age;
- missing/claimed/corrupted anchor condition;
- graph degree/high-degree weak-field collision;
- source combination.

For each, report effective sample size, number of gold-positive opportunities, point estimate and interval. No binary “fair/unfair” or “passes/fails” claim is made from an underpowered subgroup. If effective sample size is inadequate, the result is `insufficient precision`.

A hierarchical/multilevel model may be used as a secondary shrinkage analysis, but raw design-weighted subgroup estimates remain visible. [[source-bailey-2019-record-linkage-bias]] and [[source-harron-2017-linkage-quality-guide]] motivate this analysis because linkage errors can be systematically concentrated.

## 12. Multiplicity

Only the hierarchical primary Gate 1/Gate 2 sequence is confirmatory. H2-H5, ablations, Task B/C, challenge-cohort results, calibration slices and subgroup contrasts are secondary/exploratory unless separately preregistered with a multiplicity procedure.

Do not select a favorable endpoint after test inspection. Where multiple formal secondary hypotheses are promoted to confirmatory status, use a declared family-wise or false-discovery procedure before test opening.

## 13. Method-selection discipline

Before the final test:

- enumerate eligible C2/C3 algorithms;
- freeze preprocessing;
- freeze hyperparameter search spaces and computational budgets;
- freeze development metric and tie-break rule;
- select exactly one `C*` for confirmatory comparison;
- retain all rejected configurations and development scores in the run log.

The confirmatory test evaluates the frozen selected system, not “the best final-test run.” **Exactly one development-selected `C*` reaches the confirmatory test.**

## 14. Human-review workflow experiment

Gold adjudicators and operational workflow reviewers are different people/roles.

For C0/manual versus C4/assisted review:

- each operational reviewer sees a case only once;
- no operational reviewer sees the same case in both manual and assisted conditions;
- cases are randomized to manual or assisted condition within reviewer blocks;
- reviewers cross over across **different cases**, preventing memory/carryover contamination;
- both conditions receive equivalent underlying evidence; the assisted arm additionally receives the permitted E1 explanation/ranking packet;
- accuracy is scored against independent frozen gold;
- capture elapsed time, active interaction time, abstention, confidence and evidence opened.

Analyze correctness and log-time using a mixed-effects or equivalently paired/block-aware model with reviewer and case effects. Report time distributions rather than means alone. If reviewers differ materially in experience, include prespecified reviewer-level covariates or stratification.

This arm is operational/secondary and does not redefine gold truth.

## 15. Stress/challenge analysis

Cohort H is analyzed separately. Report case-level pass/fail by failure mechanism and paired degradation under controlled corruptions. Do not compute an unweighted “challenge-set accuracy” and imply population meaning.

For synthetic corruption, report the uncorrupted counterpart and the within-case change so difficulty composition cannot drive apparent method differences.

## 16. Sample-size / precision planning

After a development-only adjudication pilot, run simulation under the actual entity-centric sampling and split design. Select test size to satisfy:

- desired half-width for the precision safety estimate near `P*`;
- desired half-width for recall/auto-resolution yield;
- desired precision/power for the paired `C* - C1` improvement `Delta*`;
- minimum effective sample sizes for the few subgroups designated as decision-critical;
- available adjudication budget.

The simulation assumptions, random seed, code and selected `n` are frozen. If the budget cannot meet the required precision, E1 narrows its claim instead of pretending the sample is adequate.

## 17. Reporting

Every final result table states:

- cohort (R/H/J);
- split/regime (F0-F6, including F6a/F6b);
- weighting method;
- eligible denominator;
- abstentions/unresolved counts;
- point estimate and 95% CI;
- whether the analysis was confirmatory, secondary, or exploratory.

Use [[e1-reporting-and-reproducibility-checklist]].

## Sources

[[source-binette-2024-entity-centric-er-evaluation]] · [[source-chipperfield-2018-linkage-precision-recall-estimation]] · [[source-shang-2023-precision-recall-imbalanced-sampling]] · [[source-harron-2017-linkage-quality-guide]] · [[source-traub-2024-selective-classification-evaluation]] · [[source-van-calster-2016-calibration-hierarchy]] · [[source-dasylva-2016-clerical-review-quality]]
