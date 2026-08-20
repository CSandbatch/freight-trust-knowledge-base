---
type: evidence
status: active
schema_version: 1.0.0
updated: 2026-08-18
confidence_default: mixed
tags:
- type/evidence
- lifecycle/active
- domain/freight
- domain/identity
- domain/data-science
- confidence/mixed
- audience/internal
- programme/e1
---
# E1 Academic Design Review — iterative methods review

> [!note] 2026-08-18 method-extension boundary
> This review hardened the pre-LLM C1/C2/C3 design. [[dec-013-llm-e1-challenger]] later added
> a prospective constrained LLM resolver. The earlier “zero open Critical/Major” verdict must
> not be read as empirical or conformance approval of a model, provider, prompt, data-egress
> path, calibration layer, or cluster reconciler that did not yet exist. The new extension is
> governed by [[method-llm-assisted-entity-resolution]] and
> [[09-meta/gaps/gap-018-e1-llm-readiness]].

## Scope and standard of review

This review asks whether E1 is designed so that a competent external methods reviewer could distinguish:

- the target population from a hand-picked challenge set;
- the gold/reference standard from the model being evaluated;
- candidate-generation error from resolver error;
- model development from independent evaluation;
- legal-person clustering from pair classification;
- automatic decisions from abstention/human workflow;
- point estimates from inferential uncertainty;
- benchmark validity from operational/generalization claims.

The review is grounded in modern entity-resolution/record-linkage evaluation, official-statistics record-linkage methodology, clerical-review design, calibration/selective-classification evaluation, and transparent prediction-model reporting analogues. It does not claim peer review or legal certification.

## Reviewer A — statistical/inferential design, pass 1

### A-C1 — representative inference was not identified by a valid design
**Severity: Critical.** The prior protocol called for stratified hard cases and “prevalence-weighted” estimates but did not define a probability sampling frame or inclusion probabilities. That is insufficient for population-level precision/recall. Modern ER evaluation explicitly warns that naive benchmark precision/F1 can be biased and even reverse method rankings.

**Disposition:** CLOSED. Added [[e1-benchmark-sampling-and-split-plan]] with a probability-based entity-centric Cohort R, explicit design weights, cluster-closure audit, and a separate purposive Cohort H challenge set. Source: [[source-binette-2024-entity-centric-er-evaluation]], [[source-lam-2026-ambiguity-aware-clerical-review]], [[source-shang-2023-precision-recall-imbalanced-sampling]].

### A-C2 — primary endpoint and success criterion were overloaded
**Severity: Critical.** Precision, recall, F1, FPR, coverage and review time were all “primary,” leaving large researcher degrees of freedom.

**Disposition:** CLOSED. Confirmatory analysis is now hierarchical: safety precision floor `P*` first, then improvement in design-weighted assignment recall/auto-resolution yield over C1 at the same safety/review budget. One development-selected `C*` reaches final test. Other outcomes are secondary.

### A-M1 — uncertainty method was underspecified
**Severity: Major.** “Entity-level clustered bootstrap or equivalent” did not identify the sampling design or paired comparison procedure.

**Disposition:** CLOSED. The SAP now requires design-aware entity/anchor-level resampling within strata, paired method differences within each replicate, fixed interval algorithm and replicate count before test opening.

### A-M2 — sample size lacked an inferential target
**Severity: Major.** “Sized by desired CI width” was conceptually right but not operational.

**Disposition:** CLOSED. Development-only pilot estimates nuisance quantities; simulation under the actual sampling design selects `n` to meet declared CI-width and method-difference precision/power/assurance targets. If budget is inadequate, claims are narrowed.

### A-M3 — subgroup guardrail was binary without an information criterion
**Severity: Major.** “Materially worse” could become subjective, especially in sparse groups.

**Disposition:** CLOSED. All subgroups report effective sample size and CIs; underpowered groups receive `insufficient precision`, not “pass.” Any formal subgroup tests require separate preregistration/multiplicity control.

## Reviewer B — entity-resolution / benchmark methodology, pass 1

### B-C1 — pairwise metrics did not match the clustering target
**Severity: Critical.** Task A truth is an equivalence partition, but the prior design still centered pairwise P/R/F1. Pair metrics can obscure over-merges and cluster-size effects.

**Disposition:** CLOSED. Primary operational evaluation is observation-to-entity/new-entity assignment; secondary clustering evaluation now includes pairwise, B-cubed, cluster precision/recall, exact-cluster recovery, and merge/split distributions. Source: [[source-binette-2024-entity-centric-er-evaluation]].

### B-C2 — blocking could make the comparison conditionally optimistic
**Severity: Critical.** A resolver cannot recover true matches omitted by candidate generation. Conditional classifier recall is not end-to-end recall.

**Disposition:** CLOSED. Production blocking is frozen and included in primary end-to-end evaluation. Candidate recall/pair completeness, reduction ratio, recall@K and blocking misses are reported. A common-candidate-set analysis is a secondary ablation only. Source: [[source-dasylva-goussanou-2021-blocking-false-negatives]].

### B-M1 — the benchmark lacked a cluster-closure criterion
**Severity: Major.** Calling a sampled entity “fully resolved” requires an explicit attempt to discover records the evaluated model did not propose.

**Disposition:** CLOSED. Cohort R uses model-independent retrieval routes and `cluster_closure_status`. Incomplete clusters are excluded from confirmatory global metrics.

### B-M2 — “new entity” behavior was implicit
**Severity: Major.** Deployment includes observations for entities absent from the reference graph. Forced matching can make a system look artificially complete.

**Disposition:** CLOSED. F6 now has F6a continuing-entity and F6b novel-entity subproblems. Operational action space is `LINK_EXISTING`, `CREATE_NEW`, `ABSTAIN`.

### B-M3 — graph mechanism and system performance were conflated
**Severity: Major.** If C3 uses a different candidate generator, any improvement could arise from retrieval rather than graph reasoning.

**Disposition:** CLOSED. Primary end-to-end comparison remains deployment realistic; a common-candidate-set secondary ablation isolates resolver/graph contribution. Graph-specific ablations remove temporal and relational features one family at a time.

## Reviewer C — ML validity, calibration, human factors and reproducibility, pass 1

### C-C1 — graph/train/test leakage remained possible
**Severity: Critical.** The prior “entity-disjoint and time-forward” wording did not say whether test-entity historical nodes could appear in the graph, whether graph embeddings were learned over future/test structure, or whether rarity/normalization statistics were fit globally.

**Disposition:** CLOSED. [[e1-benchmark-sampling-and-split-plan]] separates model-development identity disjointness from deployment-realistic pre-cutoff reference history. All learned transforms, embeddings, frequency tables, blocking rules, calibrators and thresholds are train/dev-only; explicit path-based graph leakage audit is required.

### C-M1 — calibration depended too heavily on ECE
**Severity: Major.** ECE is bin-dependent and does not characterize calibration structure.

**Disposition:** CLOSED. SAP adds calibration intercept, slope, smooth reliability curve and Brier score; ECE is secondary. Source: [[source-van-calster-2016-calibration-hierarchy]].

### C-M2 — abstention evaluation at one threshold could hide failure
**Severity: Major.** A single coverage point does not characterize selective performance.

**Disposition:** CLOSED. Full risk-coverage curves are required plus the preregistered operational point; generalized risk-coverage summaries are secondary. Source: [[source-traub-2024-selective-classification-evaluation]].

### C-M3 — human-in-loop reviewers could contaminate the gold standard
**Severity: Major.** If the same humans who create gold labels also constitute C4, the operational system is partly being evaluated against itself.

**Disposition:** CLOSED. Gold adjudicators and operational workflow reviewers are now separate roles. The workflow arm uses randomized case assignment, no same-reviewer same-case crossover, and independent frozen gold.

### C-M4 — human time comparison was vulnerable to carryover and reviewer effects
**Severity: Major.** Showing a reviewer the same case in manual and assisted conditions creates memory effects.

**Disposition:** CLOSED. Reviewers cross conditions across different cases; analysis is reviewer/case-block aware and reports distributions plus accuracy.

### C-M5 — model-selection multiplicity was not contained
**Severity: Major.** “Best non-manual condition” could become test-set model shopping.

**Disposition:** CLOSED. Eligible C2/C3 variants, hyperparameter budget, development criterion and tie-break are frozen; exactly one `C*` reaches confirmatory test.

## Pass 2 — residual review after revision

### R2-M1 — representativeness versus rare-failure discovery still needed explicit claim separation
**Severity: Major.** Even with design weights, mixing purposive chameleon/merger cases into a single test table would confuse readers.

**Disposition:** CLOSED. All final tables must name Cohort R/H/J. H is nonrepresentative by construction and never contributes to headline population metrics.

### R2-M2 — time-forward evaluation needed separate known versus novel entities
**Severity: Major.** A time-forward split containing only entities already present pre-cutoff would not test erroneous forced attachment of truly new carriers.

**Disposition:** CLOSED through F6a/F6b.

### R2-M3 — reviewer agreement statistic remained too vague
**Severity: Major.** A single chance-corrected statistic can behave oddly under skewed labels.

**Disposition:** CLOSED. Report observed and label-specific agreement plus Cohen's kappa and a prevalence-robust complement such as Gwet's AC1; no arbitrary reliability cutoff controls benchmark validity by itself. Persistent disagreement triggers reference-standard sensitivity analysis.

### R2-M4 — challenge corruption could accidentally change the real-world identity
**Severity: Major.** Treating a genuine ownership transition as “corruption” would alter semantics rather than degrade observation quality.

**Disposition:** CLOSED. Synthetic corruption is restricted to observation noise/missingness; genuine corporate events remain real temporal cases. Corruption distributions are calibrated to development discrepancies where possible.

## Pass 3 — final hostile review

### Critical findings open: 0
### Major findings open: 0

Remaining limitations are real empirical dependencies rather than correctable protocol defects:

1. the final target population cannot be broader than source/jurisdiction coverage actually sampled;
2. complete entity-cluster closure may be impossible for some carriers, and those cases must remain incomplete/unresolved;
3. numerical `P*`, `Delta*`, final sample size and decision-critical subgroup sizes require pilot data and PI/domain harm analysis;
4. external/jurisdiction validation may be limited by Phase I resources;
5. no design document can substitute for qualified human adjudicators or actual independent replication.

These are disclosed limitations, not hidden design freedoms.

## Academic-design verdict

**PASS FOR PREREGISTRATION / PILOT, subject to PI/domain sign-off and pilot-based numeric freeze.**

The revised E1 now has a defensible target population, probability-based representative benchmark, separate challenge cohort, entity-centric gold construction, explicit candidate-generation evaluation, leakage-controlled time/entity split, one hierarchical primary endpoint, design-aware uncertainty, cluster metrics, calibration/abstention evaluation, independent human-workflow arm, sample-size rule, and reproducibility contract.

That is sufficient to call the **design academically defensible** before data collection. It is not equivalent to peer-reviewed validation, and the design must be reopened if the pilot reveals systematic gold-label ambiguity, unachievable cluster closure, or insufficient sample precision.

## Core methodological sources

[[source-binette-2024-entity-centric-er-evaluation]] · [[source-lam-2026-ambiguity-aware-clerical-review]] · [[source-dasylva-goussanou-2021-blocking-false-negatives]] · [[source-chipperfield-2018-linkage-precision-recall-estimation]] · [[source-harron-2017-linkage-quality-guide]] · [[source-bailey-2019-record-linkage-bias]] · [[source-traub-2024-selective-classification-evaluation]] · [[source-van-calster-2016-calibration-hierarchy]] · [[source-dasylva-2016-clerical-review-quality]] · [[source-tripod-ai-2024-reporting-analogue]]
