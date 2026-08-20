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
# E1 Benchmark Sampling and Split Plan

## Purpose

This plan separates three questions that must not be answered with the same convenience sample:

1. **Population performance:** how well does a frozen E1 system resolve carrier observations in the defined target universe?
2. **Scientific mechanism:** does graph/temporal evidence add value beyond deterministic and pairwise probabilistic linkage?
3. **Failure discovery:** how does the system behave on rare, adversarial, legally awkward, or corrupted cases?

The primary performance benchmark is probability-based and entity-centric. A separate challenge cohort is intentionally enriched for difficult cases. Challenge-cohort results are never presented as population prevalence or headline accuracy.

## 1. Target population and frame

Before sampling, freeze:

- `frame_snapshot_id` — the exact FMCSA Company Census snapshot used as the registration frame;
- `frame_date` — snapshot date;
- inclusion/exclusion rules (carrier roles in scope, U.S. jurisdictions, public-record retrievability, status window);
- all frame fields used for stratification;
- the count of frame records in each stratum.

The sampling frame is **FMCSA registration records**, not pre-assumed legal-person clusters. The adjudication process determines the underlying `LegalPerson` clusters. If two sampled registration anchors resolve to one legal person, the duplicate selection is retained in the sampling audit and handled in estimation rather than silently discarded.

### 1.1 Anchor multiplicity and analysis weights

After adjudication reveals the in-frame anchors belonging to each sampled legal person, compute
that person's design inclusion probability as the probability that **at least one** of its in-frame
registration anchors would be selected under the frozen stratified sampling design. Under
stratified sampling without replacement, calculate this from the frame stratum sizes, stratum
sample sizes, and the number of the person's anchors in each stratum; do not sum anchor inclusion
probabilities or count the same legal person once per sampled anchor. Entity-level cluster metrics
use a multiplicity-adjusted Horvitz-Thompson total or its preregistered Hájek ratio form with weight
`1 / pi_entity`. Observation-decision estimands use the inclusion probability induced by the same
entity-selection and frozen cluster-expansion rule. The preregistration must freeze the exact
formula, finite-population correction, ratio/total form, variance/replicate-weight implementation,
and handling of an entity whose full in-frame anchor multiplicity cannot be established.

Duplicate anchor selections remain in the audit manifest, but one entity's full contribution is
carried together once in each entity-level replicate. A simulation test with known duplicated
anchors must recover the generating finite-population estimand before the real holdout is opened.

The confirmatory target population must be stated narrowly enough that the benchmark can actually support it. Generalization outside sampled jurisdictions/source environments is not claimed without an additional validation cohort.

## 2. Cohort R — representative entity-centric evaluation cohort

### 2.1 Sampling design

Use a stratified probability sample of registration anchors. Initial strata are formed **only from pre-sampling frame variables**, for example:

- fleet-size band;
- active/inactive/recent-status band;
- jurisdiction/region;
- age/recency of latest registration update;
- carrier-role class if multiple role classes are in scope.

Do not stratify the representative cohort on a model's score. Every selected unit retains its inclusion probability `pi_i` and design weight `w_i = 1/pi_i`.

If rare but scientifically important strata would otherwise have too few units, disproportionate stratification is allowed, provided weights are retained and effective sample size is reported.

### 2.2 Entity-centric labeling

For every selected anchor, reviewers construct the **complete in-scope legal-person cluster** under the identity standard. The cluster is not defined by one model's candidate list. Cluster construction uses a broad, model-independent retrieval protocol across permitted authoritative sources and documented weak-field search routes.

Before case construction, freeze the source list, predicate-specific query templates, normalized
search keys, jurisdiction adapters, temporal windows, candidate ledger, and stopping rule. Closure
requires every permitted route to be attempted, every returned candidate to receive a documented
disposition, every evidence request to be resolved or logged as unavailable, and a final repeated
retrieval pass to yield no new in-scope candidate. An independent, blinded audit sample repeats the
frozen retrieval protocol without model outputs; its missed-candidate rate and disagreement are
reported. The pilot sets the audit-sample size and any numeric closure threshold before
confirmatory sampling.

A cluster is primary-evaluation eligible only after a closure audit records:

- all retrieval routes attempted;
- all source systems queried;
- known temporal coverage gaps;
- unresolved records/candidates;
- an explicit `cluster_closure_status` (`closed`, `provisionally_closed`, `incomplete`).

`incomplete` clusters remain scientifically useful but are excluded from the complete-case primary
analysis and analyzed separately. The primary estimand is explicitly named the
**closure-eligible target-population estimand**, not the unrestricted frame-population estimand.
Report the design-weighted closure rate and exclusion reasons overall and by preregistered stratum.
Also report preregistered conservative bounds that assign excluded observations the plausible
best/worst method outcomes; a development-fitted response-propensity adjustment may be secondary
only if its model and diagnostics are frozen before test access. If closure failure is systematic
or the bounds change the decision, no unrestricted population-performance claim is made.

This follows the entity-centric logic of [[source-binette-2024-entity-centric-er-evaluation]]: fully resolved sampled entities permit sampling-aware estimation of pairwise and cluster metrics and reduce dependence on system-proposed pairs.

### 2.3 Probability-aware estimation

Population estimates are design-weighted. Naive precision/recall computed after disproportionate sampling are prohibited. The analysis preserves stratum, inclusion probability, and replicate-weight/bootstrap information.

The analysis archive contains both anchor-level selection probabilities and the adjudication-
derived entity/observation inclusion probabilities. It reports the unweighted sample count,
weighted target-population denominator, effective sample size, number of duplicated sampled
anchors, and number of unique resolved legal persons.

When a clerical-review subsample is drawn from system outputs for monitoring, it has its own finite-population sampling design as described by [[source-lam-2026-ambiguity-aware-clerical-review]] and is not silently substituted for Cohort R.

## 3. Cohort H — hard/adversarial challenge cohort

Cohort H is purposive and may include:

- shared registered agents or high-degree addresses;
- family/common ownership with simultaneous legitimate carriers;
- mergers, stock acquisitions, asset sales and authority transfers;
- identity theft / claimed-versus-assigned USDOT conflicts;
- corporate-form changes and sole-proprietor edge cases;
- stale or contradictory sources;
- high name similarity among unrelated entities;
- real or synthetic missingness/corruption scenarios;
- authoritative reincarnation/affiliation cases for relation/disposition testing.
- inert prompt-injection strings embedded in untrusted name/address/narrative fields;
- chronology canaries and masked/randomized identifier/name variants for C6 contamination and
  feature-reliance diagnostics; and
- repeated identical packets used to measure C6 nondeterminism.

The existing [[e1-edge-case-suite.csv]] is a conformance component of Cohort H. Real cases are added under the same semantics.

**Rule:** Cohort H supports failure-mode claims, not estimates of population accuracy, prevalence, calibration, or fairness.

## 4. Cohort J — jurisdiction/external-validity holdout

If Phase I resources permit, reserve one or more jurisdictions or source-access environments from all model tuning. Evaluate the frozen model and source adapters there as a secondary external-validity test.

If a credible jurisdiction holdout cannot be constructed, E1 explicitly limits its generalization claim to the sampled source/jurisdiction environment. A multi-state sample alone is not automatically “external validation.”

## 5. Temporal and entity separation

E1 has two distinct concepts of “seen before” and they must not be conflated.

### 5.1 Model-development identity separation

No **gold labels** or reviewer-derived features from a confirmatory test legal person may be used to train, tune, calibrate, choose thresholds, learn blocking rules, learn normalization dictionaries, learn graph embeddings, or select hyperparameters.

Training/development legal persons and confirmatory test legal persons are disjoint at the label/model-development level.

### 5.2 Deployment-realistic reference history

A time-forward test may legitimately provide the resolver with **pre-cutoff public records for a test legal person**, because a production system would possess that history before a new observation arrives. Those records may be used only as frozen reference evidence available by `feature_cutoff`; they do not provide training labels for that entity.

This yields two time-forward subproblems:

- **F6a continuing-entity resolution:** a post-cutoff observation belongs to a legal person with pre-cutoff reference evidence.
- **F6b novel-entity detection:** a post-cutoff observation belongs to a legal person not present in the pre-cutoff reference graph; the correct system action is creation of a new cluster or abstention, not forced attachment.

Both are required for deployment realism.

## 6. Split chronology

Freeze dates before final adjudication results are exposed to model developers:

- `T_train_end` — latest date usable for fitting learned parameters;
- `T_dev_end` — latest date usable for tuning/calibration/model selection;
- `T_feature_cutoff` — latest evidence a deployed system is allowed to see for a given test observation;
- `T_test_start`, `T_test_end` — primary time-forward observation window;
- `T_adjudication_cutoff` — later evidence date allowed to establish retrospective gold truth.

Evidence between `T_feature_cutoff` and `T_adjudication_cutoff` is **gold-only** and never enters features, candidate generation, normalization statistics, graph structure, thresholds, or model selection.

## 7. Leakage controls

All learned or data-adaptive transformations are fit inside training/development only, including:

- token/name frequency tables;
- address rarity/high-degree thresholds;
- phonetic/fuzzy-match thresholds if tuned;
- missing-value models;
- learned blocking rules;
- graph embeddings;
- supervised feature encoders;
- probability calibrators;
- thresholds and abstention policy.

For C6, this also includes prompt/example selection, evidence serialization, model/provider
selection, embedding index construction, output parsing, retry/fallback behavior, score
extraction, cluster reconciliation, and any external calibrator. Hosted-model public-record
memorization is an additional, incompletely controllable leakage channel: C6 receives no tools or
outside retrieval and must run the masked/randomized-identifier and chronology diagnostics in
[[method-llm-assisted-entity-resolution]], with residual pretraining contamination disclosed.

The preprocessing artifact is versioned and applied unchanged to the test set.

For graph methods, a leakage audit traverses all paths from test nodes to training labels and flags:

- future edges;
- reviewer-created edges;
- duplicated source records across splits;
- embeddings trained over post-cutoff graph structure;
- label-derived cluster IDs encoded as features;
- test-derived degree/frequency statistics.

## 8. Candidate generation / blocking

End-to-end E1 includes candidate generation. Each method's production candidate generator is frozen before the test run.

Report:

- candidate recall / pair completeness;
- recall@K where candidate ranking exists;
- reduction ratio / candidate-set size;
- latency and memory cost;
- downstream match recall conditional on candidate generation;
- end-to-end recall including blocking misses.

A secondary **common-candidate-set** analysis supplies the same broad candidate union to C1-C3 to isolate resolver/scoring differences. It is an ablation, not the primary deployment result.

C6 uses that same candidate union for its resolver comparison. A separate frozen end-to-end C6
view may use embedding or other learned retrieval, but it reports its own candidate recall,
candidate volume, latency, cost and blocking misses. A richer narrative or graph evidence view is
an explicit evidence-interface ablation; it cannot be described as a fair resolver comparison to
a structured-field baseline.

See [[source-dasylva-goussanou-2021-blocking-false-negatives]].

## 9. Sample-size planning

Do not choose a benchmark size by convention. Run a development-only pilot to estimate:

- cluster-size distribution;
- proportion of continuing versus novel entities;
- expected automatic-assignment precision and recall;
- reviewer disagreement;
- design effect from stratification/clustering;
- prevalence of key error mechanisms;
- likely subgroup effective sample sizes.

Then use simulation under the actual sampling design to select a confirmatory sample that achieves predeclared precision goals for the primary estimands and the planned method contrast. The target CI width, safety precision floor `P*`, clinically/operationally meaningful recall improvement `Delta*`, power/assurance target if hypothesis testing is used, and maximum review budget are frozen **before confirmatory labels are released to the modeling team**.

A sample-size re-estimation may use blinded nuisance quantities only if the rule is preregistered.

## 10. Challenge corruptions

Synthetic corruption is secondary. Corruption functions must distinguish observation noise from genuine business events. For example, typographical name corruption is noise; an ownership transfer is a real temporal event and cannot be simulated as a typo-like perturbation.

Where possible, corruption distributions are calibrated to empirical disagreement/missingness rates observed in development data. Severity levels and random seeds are frozen before test evaluation.

## 11. Freeze artifacts

Before G1/data lock, publish internally:

- frame manifest and hash;
- stratum counts;
- sampled IDs and inclusion probabilities in access-controlled form;
- cluster-closure checklist;
- split and chronology manifest;
- train/dev/test entity-disjoint audit;
- F6a/F6b membership;
- challenge-cohort provenance;
- candidate-generation configurations;
- sampling-weight / replicate-weight file.
- anchor-to-entity multiplicity table, entity/observation inclusion-probability derivation, and
  simulation recovery test;
- cluster-retrieval protocol, stopping log, independent closure-audit sample, design-weighted
  closure exclusions, and frozen bounds/sensitivity specification;
- C6 model/provider/prompt/schema/evidence-view/reconciliation manifest, L0-L7 assignment,
  data-egress approval, and frozen repeat/masking/injection diagnostic membership.

## Sources

[[source-binette-2024-entity-centric-er-evaluation]] · [[source-lam-2026-ambiguity-aware-clerical-review]] · [[source-shang-2023-precision-recall-imbalanced-sampling]] · [[source-dasylva-goussanou-2021-blocking-false-negatives]] · [[source-bailey-2019-record-linkage-bias]]
