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

`C*` is selected among eligible C2/C3 variants and a gate-qualified C6 using development data
only. Selection criteria, C6 promotion gates and tie-break rules are frozen before test access.
The test set is not used to select the “best” model. Exactly one C2/C3/C6 system reaches the
confirmatory holdout as `C*`; every nonselected configuration remains descriptive.

## 3. Primary estimand and hierarchical success gate

The primary operational unit is a post-cutoff **observation-resolution decision** with one of three actions:

- `LINK_EXISTING` — attach to one existing legal-person cluster;
- `CREATE_NEW` — initiate a new legal-person cluster;
- `ABSTAIN` — defer to human review.

For automatic decisions, define design-weighted:

- **assignment precision (PPV):** proportion of non-abstained automatic assignments/creations that are correct;
- **assignment recall / auto-resolution yield:** proportion of gold-resolvable test observations correctly resolved automatically;
- **coverage:** proportion of eligible observations receiving a non-abstained automatic decision.

The joint assignment estimand is primary, but `LINK_EXISTING` and `CREATE_NEW` are also reported
separately with action-specific precision, recall, coverage, confusion counts, and error severity.
A false attachment to an existing legal person and an erroneous new-cluster creation are distinct
harms; neither may be hidden by pooling the two actions.

The confirmatory gate is hierarchical:

1. **Safety gate:** the lower bound of the preregistered 95% confidence interval for `C*` assignment precision is at least `P*` in the primary F6 time-forward cohort.
2. **Utility gate:** only if Gate 1 passes, compare `C*` with C1 on assignment recall/auto-resolution yield at the same `P*` policy and the same review-budget constraint. Success requires the lower 95% CI for the paired improvement to exceed the preregistered minimum meaningful improvement `Delta*` (or zero if the PI explicitly chooses a pure-superiority criterion before test opening).

`P*` and `Delta*` are set from harm analysis, development baseline performance, review capacity and pilot-based precision calculations, never from final-test results.

This structure prevents an apparent recall gain from being purchased through unsafe false merges.

### 3.1 Frozen operating-point and C* selection algorithm

The pilot fixes `P*`, `Delta*`, the common maximum human-review fraction `B`, the development
confidence procedure, and a finite ordered grid of permitted thresholds/policies. For each frozen
system configuration, evaluate every grid point on development data and retain only points with:

1. nonzero automatic coverage;
2. review fraction at or below `B`; and
3. lower development confidence bound for joint assignment precision at or above `P*`.

Select that configuration's point with greatest design-weighted assignment yield. Break exact
ties, in order, by the larger precision lower bound, lower false-attachment rate, higher candidate
recall, lower median per-decision cost, and finally the preregistered stable configuration ID. A
configuration with no retained point is ineligible; an all-abstain policy is reported as zero
coverage/yield and cannot create a nominal precision pass from an empty denominator.

C6 must first pass all separately frozen promotion gates. Among eligible C2/C3 variants and any
gate-qualified C6 configuration, select `C*` by the same development operating-point algorithm and
the same ordered tie-break above. C1 is tuned by the same operating-point rule but remains the
fixed comparator rather than a C* candidate. If C1 has no eligible nonzero-coverage point, report
that failure and its zero-yield all-review policy explicitly; do not silently relax `P*` or `B`.
Every grid, gate, confidence procedure, cost definition, and configuration ID is hashed before
test access.

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

Entity-level cluster estimands use the preregistered multiplicity-adjusted Horvitz-Thompson or
Hájek estimator based on the probability that at least one in-frame anchor for the adjudicated
legal person was sampled. Observation-decision estimands use the inclusion probability induced by
the same entity-selection and frozen cluster-expansion rule. Duplicated anchors never create
duplicate entity contributions merely because more than one anchor was selected.

Primary CIs and paired method contrasts use a survey/design-aware **entity-level resampling procedure**: resample primary sampled entities/registration anchors within design strata (or use equivalent replicate weights), carry their full cluster/error contribution together, recompute weighted metrics, and preserve method pairing within each replicate.

Do not bootstrap record pairs independently.

The preregistration fixes:

- bootstrap/replicate-weight algorithm;
- number of replicates (default target 2,000 unless simulation demonstrates a different requirement);
- confidence level (95%);
- method for percentile/BCa or design-based intervals;
- behavior in sparse strata.

If sample-size or sparse-cell conditions invalidate the planned interval, the analysis reports the failure rather than switching post hoc to a more favorable method.

Before lock, simulation must include zero-error and rare-error regimes near `P*`, unequal weights,
duplicate anchors, small strata, and varying cluster sizes. It compares the candidate design-based
interval procedures for lower-tail coverage and decision error, then freezes one procedure and its
boundary behavior. If none achieves the preregistered coverage tolerance at the feasible sample
size, the automatic-use claim is narrowed or abandoned rather than relying on an unstable lower
bound. The default 2,000 replicates is not binding if simulation shows that more are required.

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

The complete-case primary analysis targets the closure-eligible population defined in
[[e1-benchmark-sampling-and-split-plan]]. Report design-weighted closure failure and reasons by
stratum, plus frozen best/worst plausible outcome bounds for excluded incomplete clusters. Any
response-propensity adjustment is secondary and must be development-fitted and preregistered. If
closure exclusions or bounds change the primary decision, do not generalize to the unrestricted
frame population.

## 12. Multiplicity

Only the hierarchical primary Gate 1/Gate 2 sequence is confirmatory. H2-H6, ablations, Task B/C, challenge-cohort results, calibration slices and subgroup contrasts are secondary/exploratory unless separately preregistered with a multiplicity procedure.

Do not select a favorable endpoint after test inspection. Where multiple formal secondary hypotheses are promoted to confirmatory status, use a declared family-wise or false-discovery procedure before test opening.

The bounded C6 L0-L2 method variants and L3-L7 diagnostics are not eight opportunities to choose
a favorable test result. The preregistration fixes the primary C6 configuration or a development-
only selection rule, compute/API-call budget, tie-break, and which contrasts are descriptive.
L3-L7 are evidence-view/safety/validity diagnostics and cannot be selected as a headline system.

## 13. Method-selection discipline

Before the final test:

- enumerate eligible C2/C3 algorithms and the conditionally eligible C6 configuration;
- freeze preprocessing;
- freeze hyperparameter search spaces and computational budgets;
- freeze development metric and tie-break rule;
- select exactly one `C*` for confirmatory comparison;
- retain all rejected configurations and development scores in the run log.

The final holdout is opened through one immutable batch manifest. C1 and `C*` are the only
confirmatory systems. Any preregistered nonselected configuration included in that same batch is
secondary/descriptive and consumes its holdout evaluation permanently; it cannot be rerun,
retuned, or used to revise selection. Configurations absent from the batch receive no later access
to that holdout and require a genuinely new external validation set for future claims.

The confirmatory test evaluates the frozen selected system, not “the best final-test run.” **Exactly one development-selected `C*` reaches the confirmatory test.**

### C6 promotion rule

Before the first confirmatory test opening, development data must show that numerically frozen
schema-validity, evidence-support, prompt-injection, repeated-inference stability,
privacy/data-egress, calibration/abstention, latency/cost, subgroup, candidate-recall, and
cluster-reconciliation gates are met. Its exact model/provider, prompt/schema, evidence view,
fallback/retry behavior, compute budget and selection rule must be locked. A gate-qualified C6
then competes under the same development criterion/tie-break as the eligible C2/C3 systems, and
exactly one system reaches the confirmatory holdout as `C*`. If a gate fails or another system is
selected, C6 remains secondary and all of its nonselected outputs are descriptive. No favorable
holdout result can be used to revise eligibility or promotion.

## 13A. C6-specific analyses

Report C6 in both the common-candidate resolver view and, where implemented, its frozen end-to-end
retrieval view. In addition to all applicable E1 outcomes, estimate:

- schema-valid response, unknown-evidence-ID and unsupported-assertion rates;
- evidence-citation coverage/precision under the frozen audit sample;
- abstention and system-failure rates by reason;
- cluster-reconciliation intervention, inconsistent-cycle and conflicting-assignment rates;
- L5 action, target-cluster and cited-evidence flip rates across identical repeats;
- paired L6 masked/randomized-versus-original performance change;
- L7 prompt-injection success rate;
- tokens, per-decision cost, latency, retries, timeouts and provider failures; and
- all safety/error outcomes by F6a/F6b, fleet size, source environment, feature regime,
  missingness and graph degree where precision permits.

The preregistered H6 method contrast pairs C6 with the designated non-LLM probabilistic
comparator on the same common candidate/evidence packets and reports the design-weighted
assignment-yield difference at the frozen precision/review point with its 95% interval. The
end-to-end comparison repeats that contrast with each method's own retrieval losses included.
The H6 contrast excludes L3 graph augmentation. L3 is instead analyzed as a preregistered
`resolver family × evidence view` factorial contrast in which C6 and the designated non-LLM
comparator receive the identical graph serialization; neither its main effect nor interaction may
be described as LLM-specific incremental value without that equal-evidence contrast.
H6 is secondary when C6 is not selected as `C*`. If C6 passes its gates and is selected, the
hierarchical H1a/H1b C1-versus-`C*` analysis—not H6—provides its confirmatory test. In neither
case can a favorable holdout result redefine selection or promotion.

Model self-reported confidence is not a probability. Calibration applies only to a reproducible,
predeclared score with a development-fitted calibrator. Accuracy, evidence faithfulness,
nondeterminism, contamination diagnostics, privacy, and operability remain separate outcomes.

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

C6 tables additionally name the exact model/provider/configuration, evidence view,
common-candidate versus end-to-end view, prompt/schema version, reconciliation version, request
failure denominator and whether the result is an L0-L2 method variant or L3-L7 diagnostic. Only
the single gate-qualified, development-selected C6 configuration may be confirmatory, and only if
it is `C*`; every other C6 result is secondary/descriptive.

Use [[e1-reporting-and-reproducibility-checklist]].

## Sources

[[source-binette-2024-entity-centric-er-evaluation]] · [[source-chipperfield-2018-linkage-precision-recall-estimation]] · [[source-shang-2023-precision-recall-imbalanced-sampling]] · [[source-harron-2017-linkage-quality-guide]] · [[source-traub-2024-selective-classification-evaluation]] · [[source-van-calster-2016-calibration-hierarchy]] · [[source-dasylva-2016-clerical-review-quality]]
