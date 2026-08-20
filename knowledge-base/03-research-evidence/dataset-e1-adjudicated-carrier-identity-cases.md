---
type: dataset
status: to-build
phase: phase-i
schema_version: 1.0.0
verification: not-attempted
access: to-build — created through blinded expert adjudication over permitted source records
licence: unresolved — redistribution depends on the rights of each incorporated source; source-derived fields and release rights must be tracked per case
updated: 2026-08-18
tags:
- type/dataset
- domain/identity
- domain/freight
- confidence/mixed
- audience/internal
- lifecycle/to-build
- programme/e1
---
# E1 Adjudicated Carrier Identity Cases

The adjudicated reference-standard corpus for E1. This dataset is intentionally **not** a “chameleon-carrier
list.” Its primary purpose is to evaluate whether observations can be assigned to the correct
legal-person identity and whether distinct but related entities can be represented without
being falsely merged.

Canonical specification: [[e1-carrier-identity-and-relationship-standard]]. Human procedure:
[[e1-adjudication-decision-tree]]. Machine-readable ontology: [[e1-identity-ontology.yaml]].
Synthetic conformance cases: [[e1-edge-case-suite.csv]]. State-source acquisition pilot: [[e1-state-corporate-source-access-memo]].

## Gold layers

1. **Task A — legal-person resolution.** Canonical entity clusters and derived pair labels:
   `SAME_LEGAL_PERSON`, `DISTINCT_LEGAL_PERSON`, `UNRESOLVED`, `OUT_OF_SCOPE`.
2. **Task B — FMCSA registration/identifier continuity.** Authoritative USDOT assignment,
   claimed-versus-assigned identifiers, and registrant-continuity states are stored separately
   from state-law legal-person identity.
3. **Task C — typed relationships among distinct persons.** Ownership/control, management,
   predecessor/successor, corporate transaction, and substantial-continuity relations use
   `SUPPORTED`, `REFUTED`, `UNKNOWN`, or `NOT_APPLICABLE` rather than being collapsed into
   identity.
4. **Regulatory disposition layer.** Reincarnation/affiliate findings are represented only
   when supported by an authoritative agency/judicial disposition with procedural status.
   Analyst screening candidates remain non-authoritative review states.

## Required case fields

At minimum: `case_id`; canonical legal-person cluster IDs; source-record IDs; source authority;
`observed_at`; `valid_from`/`valid_to` where knowable; feature cutoff; adjudication cutoff;
claimed identifiers; authoritative identifier assignments; names/DBAs; addresses; corporate
transaction evidence; relationship assertions; reviewer-1 label/rationale; reviewer-2
label/rationale; third-adjudicator disposition where required; unresolved reason; confidence;
PII/sensitivity flags; redistribution rights; correction history; benchmark split; feature regime;
sampled anchor IDs; anchor-to-entity multiplicity; anchor, entity, and observation inclusion
probabilities; cluster-closure status and exclusion reason; model action; action-specific outcome;
and false-attachment/false-new-cluster harm category.

## Construction rules

- Two reviewers label hard cases independently and without model output or candidate score.
- A third adjudicator resolves disagreements procedurally; original votes are preserved.
- `UNRESOLVED` is a valid gold state and is never silently converted to a negative.
- Canonical clusters, not arbitrary pair labels, are the source of truth for Task A so identity
  equivalence remains transitive.
- Later evidence may resolve retrospective gold truth, but anything later than the feature
  cutoff is masked from the model.
- Safety/enforcement/motive history is excluded from Task A identity labeling except when
  necessary to interpret an already-issued authoritative disposition.
- Model/LLM outputs, generated explanations, candidate ranks, embeddings, and inferred facts are
  excluded from gold construction and cluster closure. They are predictions, never source evidence.
- A claimed USDOT is not treated as an authoritative assignment.
- Weak fields such as address, phone, name similarity, shared insurer, or shared equipment are
  never individually dispositive.
- State-law identity/transaction facts use the competent official state source. Each sampled
  jurisdiction requires an access adapter; tax/right-to-transact status is not silently mapped to
  legal existence.
- When multiple sampled registration anchors resolve to one legal person, retain every selection
  in the audit but compute the legal person's probability of selection through at least one
  in-frame anchor. Entity-level metrics count the full cluster once under the multiplicity-adjusted
  weight specified in [[e1-benchmark-sampling-and-split-plan]].


## Benchmark cohorts and inferential use

The dataset is no longer treated as one undifferentiated collection of “hard cases.” Construction follows [[e1-benchmark-sampling-and-split-plan]]:

- **Cohort R:** probability-based entity-centric sample used for population performance estimation. Every sampled unit carries inclusion probability/design weight and cluster-closure status.
- **Cohort H:** purposive hard/adversarial/challenge cases; used for failure analysis only, never naive population precision/recall.
- **Cohort J:** optional jurisdiction/source-environment holdout for secondary external-validity assessment.

Within Cohort R, confirmatory evaluation distinguishes F6a continuing entities from F6b truly novel entities. Gold/model chronology and design-weighted analysis follow [[e1-statistical-analysis-and-preregistration-plan]].

The complete-case primary analysis estimates performance in the explicitly named
closure-eligible target population. The corpus retains all incomplete clusters and carries the
design-weighted closure-exclusion and frozen bounds/sensitivity inputs needed to assess whether
that restriction changes the conclusion; it must not silently present closure-eligible results as
performance over the unrestricted registration frame.

## Evaluation use

The corpus supports anchor-visible control tests plus anchor-masked, anchor-missing,
anchor-corrupted, claim-versus-assignment-conflict, cross-registration, entity-disjoint, and
time-forward evaluation regimes. Headline E1 performance must not be a trivial rediscovery of
an authoritative USDOT field used to construct the gold label.

Joint automatic-assignment outcomes are supplemented by separate `LINK_EXISTING` and
`CREATE_NEW` confusion fields so false attachments and false new-cluster decisions cannot cancel
or disappear inside one pooled precision estimate.

For C6 under [[method-llm-assisted-entity-resolution]], the corpus also stores access-controlled
feature-view manifests and frozen diagnostic memberships for repeated identical packets,
masked/randomized names or identifiers, chronology canaries, and inert prompt-injection strings.
These are model diagnostics, not new gold layers or representative strata. Any hosted-model
request/response artifact inherits the most restrictive input classification; the public corpus
does not acquire a right to redistribute prompts or responses containing restricted source data.

## Limits

No public, adjudicated U.S. freight benchmark with these layered labels has been identified in
the current evidence base. Historical GAO/FMCSA chameleon screening and current FMCSA/NMFTA
identity-verification systems are prior art, not gold labels for this corpus. A benchmark pass
does not authorize consequential carrier decisions.

- Linked experiment: [[experiment-e1-entity-resolution-and-identity-assurance]].
- Linked methods: [[method-deterministic-entity-matching]], [[method-probabilistic-entity-resolution]], [[method-graph-assisted-entity-resolution]], [[method-llm-assisted-entity-resolution]], [[method-expert-adjudication]].
- Research basis: [[e1-identity-definition-research-report]], [[e1-identity-claims-ledger]], [[e1-definition-freeze-review]].
