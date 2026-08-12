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

A cluster is primary-evaluation eligible only after a closure audit records:

- all retrieval routes attempted;
- all source systems queried;
- known temporal coverage gaps;
- unresolved records/candidates;
- an explicit `cluster_closure_status` (`closed`, `provisionally_closed`, `incomplete`).

`incomplete` clusters remain scientifically useful but are excluded from confirmatory global metrics and analyzed separately.

This follows the entity-centric logic of [[source-binette-2024-entity-centric-er-evaluation]]: fully resolved sampled entities permit sampling-aware estimation of pairwise and cluster metrics and reduce dependence on system-proposed pairs.

### 2.3 Probability-aware estimation

Population estimates are design-weighted. Naive precision/recall computed after disproportionate sampling are prohibited. The analysis preserves stratum, inclusion probability, and replicate-weight/bootstrap information.

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

## Sources

[[source-binette-2024-entity-centric-er-evaluation]] · [[source-lam-2026-ambiguity-aware-clerical-review]] · [[source-shang-2023-precision-recall-imbalanced-sampling]] · [[source-dasylva-goussanou-2021-blocking-false-negatives]] · [[source-bailey-2019-record-linkage-bias]]
