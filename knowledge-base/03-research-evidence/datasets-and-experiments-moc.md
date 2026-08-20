---
type: moc
area: datasets-and-experiments
status: active
schema_version: 1.0.0
tags:
- type/moc
- lifecycle/active
- domain/freight
---
# Datasets & Experiments MOC

This is the dedicated evidence-to-experiment backbone for the Freight Trust programme.
It turns the broad project claim into testable work: build an adjudicated identity and
facility-event benchmark, test governed federation, and measure whether the proposed
workflow improves decisions without imposing unfair burden on small carriers.

## Why this buttresses the case

The project does not need to prove that a trust layer automatically eliminates fraud,
detention, or empty miles. It needs to show that the central technical uncertainty is
measurable, that no suitable freight benchmark currently exists, and that Phase I can
produce a reusable evaluation asset with explicit failure conditions.

## Dataset entries

- [[dataset-fmca-company-census-file]]
- [[dataset-fmca-registration-insurance-safety-records]]
- [[dataset-e1-adjudicated-carrier-identity-cases]]
- [[dataset-openepcis-generated-event-logs]]
- [[dataset-bts-truck-travel-time-data]]
- [[dataset-permissioned-terminal-facility-event-feed]]
- [[dataset-nist-policy-machine-xacml-cases]]
- [[dataset-partner-participation-burden-log]]

Hard constraints: no freight-specific facility-event benchmark or public adjudicated carrier-identity benchmark with E1's layered legal-person/continuity/relationship labels has been identified. Restricted telematics and paid trade data are not dependencies
for Phase I. Synthetic data is acceptable for feasibility; any external validity claim must
be labeled as permissioned or not yet tested.

## Benchmark package

The benchmark should ship as four versioned artifacts:

1. **Identity cases**: canonical legal-person clusters plus derived pair labels; separate
   FMCSA identifier/registrant-continuity states; typed relationships among distinct entities;
   source records, temporal cutoffs, reviewer-level votes, and `UNRESOLVED` states. Regulatory
   reincarnation/affiliate findings are a separate disposition layer, not identity equivalence.
2. **Event cases**: ordered event traces for tender, appointment, arrival, dock, loading,
   departure, and delivery, with missing, delayed, duplicated, contradictory, and tampered
   variants.
3. **Policy cases**: neutral `(policy version, request, expected domain decision, expected
   audit event, rationale)` tuples with authority, effective date and engine-adapter mapping.
4. **Metadata and governance**: provenance, license, consent, sensitivity, retention,
   redaction, adjudicator agreement, and known limitations for every case.


## E1 identity specification package (RC1)

- [[e1-identity-definition-research-report]] — source-grounded Research Agent execution.
- [[e1-identity-claims-ledger]] — auditable determination ledger.
- [[e1-carrier-identity-and-relationship-standard]] — human semantic contract, `1.0.0-rc1`.
- [[e1-identity-ontology.yaml]] — machine-readable object/relation semantics.
- [[e1-adjudication-decision-tree]] — reviewer procedure.
- [[e1-edge-case-suite.csv]] — 70 synthetic conformance/adversarial cases.
- [[e1-definition-freeze-review]] · [[e1-state-corporate-source-access-memo]] — hostile Eval Agent findings and second-pass verdict.

The initial loose “same carrier” formulation failed hostile review with eight Critical and eleven
Major findings. RC1 has no open Critical/Major design defect in the synthetic conformance suite,
but remains **unfrozen** pending PI, freight/FMCSA-domain, counsel/domain, and adjudicator-training
gates.

## Experiment entries

Shared standard: [[experiment-protocol-standard]].

Portfolio contract: [[integrated-e1-e5-research-programme]]. E1 orientation:
[[e1-experiment-brief-and-readiness-map]].

Execution bridge: [[aws-experiment-execution-and-findings-plan]] — CPU-first AWS runtime,
accelerator promotion gates, reproducible run packets, and findings ingestion.

Build bridge: [[e1-e5-build-readiness-and-run-contract]] — shared implementation boundary,
manifest, experiment-specific first slices, fixture gates and build/pilot/confirmatory states.

- [[experiment-e1-entity-resolution-and-identity-assurance]]
- [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]]
- [[experiment-e3-federated-access-and-policy-enforcement]]
- [[experiment-e4-participation-and-small-carrier-equity]]
- [[experiment-e5-orchestration-value]]

## Experiment provenance at a glance

Each experiment file now carries a full **Provenance / What it adds / Why we are using it**
block: the finding that forced it, the origin and licence of every input, the intellectual
lineage of every method, the reason behind each design choice, the counterfactual if it were
dropped, and the alternatives considered and rejected. This table is the index into those
blocks.

| Experiment | Forced by | External lineage it borrows from | Durable artifact it leaves | Blocked by |
|---|---|---|---|---|
| E1 — identity | R-WN-04, R-WN-03, R-WN-05; G14, G13 | Current FMCSA legal/registration rules; GAO/ARCHI/URSA prior art; GLEIF identity-vs-relationship analogue; multi-reviewer gold-label methodology; Company Census File + corruption/blocking methods; Fellegi-Sunter, Ditto, MatchGPT/ComEM and GraLMatch learned-method precedents | Layered identity standard + ontology; adjudicated legal-person corpus; split/feature-regime manifests; deterministic/probabilistic/graph/LLM comparison; error taxonomy | RC1 complete; PI/domain/counsel freeze, reviewer pilot, benchmark construction, C1/C2 implementation, and C6 readiness gap |
| E2 — event provenance | R-WN-04; G14, G11 | OpenEPCIS over pinned GS1 EPCIS 2.0.1/CBV 2.0.0; PDC hidden-truth process evaluation; Nolle/BINet artificial anomaly injection; BTS–ATRI transit percentiles; NIST privacy/traceability guidance | Freight event profile, separate canonical/observability/source traces, generator and injection manifests, reconstruction/anomaly/privacy report | Numeric gates, freight threat operators, privacy release model; optional C5 partner access |
| E3 — governed federation | R-WN-03; G11, G13 | NIST NGAC Policy Machine as one implementation; OASIS XACML as a separate policy model; NIST access-control verification/audit/privacy guidance | Authority-backed policy catalogue, neutral domain-decision test corpus, authenticated engine/adapter results, independently reconciled audit/correction evidence | Policy authority/legal-commercial review, engine lane, identity provider/JWKS, numeric coverage/privacy gates |
| E4 — participation and equity | R-WN-02, R-WN-05; G7, G12, G8 | Imai/Jiang/Malani interference design; GAO's SBA-standard estimate; Common Rule/NSF institutional review; OOIDA record-access position | Public instrument/schema, recruitment/exposure flow and disclosure-controlled aggregate burden/comprehension/refusal report | Institutional determination, private data store, named participants, assignment/exposure map, fleet/capacity strata and budget |
| E5 — orchestration value | Improvement item 1; R-WN-01; G10 | Solomon/SINTEF solver validation, HOS rules, stochastic/multiobjective/collaborative VRP and agent-based empty-trip precedents | Scenario/constraint specification, validated simulator, crossed policy/stress/reporting results, ablations and Pareto sets | Formal solver/HOS/equity/uncertainty gates; upstream outputs or labeled priors; Phase II execution scope |

Two provenance facts apply across all five and should not be lost in the detail. The documented
searches through 2026-08-18 located no qualifying public adjudicated carrier-identity benchmark
with the layered E1 labels, no qualifying public freight facility-event benchmark, and no
participation-economics answer in the reviewed federated-learning benchmark literature. These
are bounded negative-search findings, not proof of universal nonexistence. E1
research simultaneously established substantial **prior art in chameleon screening and
point-in-time identity verification** (GAO/ARCHI/URSA, Motus, SCAC Verified). The novelty claim
must therefore concern the evaluated benchmark/provenance/relationship architecture, not the
existence of carrier identity screening itself.
Current Motus successor records and FCRA's statutory text are now directly verified. The Company
Census and Motus catalog licence remains `Unknown License`; old L&I/MCMIS retrieval failures stay
as dated history; PIERS terms and redistribution rights for a joined benchmark remain unresolved.

## Method entries

- [[method-deterministic-entity-matching]]
- [[method-probabilistic-entity-resolution]]
- [[method-graph-assisted-entity-resolution]]
- [[method-llm-assisted-entity-resolution]]
- [[method-expert-adjudication]]
- [[method-event-log-generation-and-anomaly-injection]]
- [[method-provenance-aware-event-reconstruction]]
- [[method-travel-time-calibration]]
- [[method-policy-conformance-testing]]
- [[method-hash-chained-audit-logging]]
- [[method-staged-participation-and-equity-evaluation]]
- [[method-synthetic-orchestration-simulation]]

## Experimental controls

- Freeze a dataset and protocol version before evaluating a model.
- Separate train, development, adjudication, and holdout cases by entity and time where possible.
- Publish baselines before publishing improvements.
- Predeclare thresholds, subgroup cuts, and stopping rules.
- Keep synthetic labels hidden from the system under test.
- Report abstentions, missingness, confidence intervals, and unresolved cases.
- Use a human adjudication panel for gold labels and record inter-rater agreement.
- Treat partner data as federated by default; centralize only derived, permissioned artifacts.

## Minimum data contract

Every exchanged record needs: `case_id`, `entity_or_event_id`, `source_id`, `observed_at`,
`valid_from`, `valid_to`, `claim_type`, `value_or_hash`, uncertainty semantics,
`access_purpose`, `consent_or_basis`, `label_status`, `adjudication_status`,
`correction_status`, `retention_until`, producer run/schema version, rights/classification and
content hash. See [[integrated-e1-e5-research-programme#Versioned interface contract]].

Raw/pseudonymized participant, partner, adjudication and restricted records stay outside this
public Git corpus. The vault may contain public schemas, synthetic examples and disclosure-
controlled aggregates only.

## Evidence and provenance links

- [[dataset-scan-entity-resolution]] - source and tooling scan for Aim 1.
- [[dataset-scan-event-provenance-and-federation]] - source and tooling scan for Aims 2 and 3.
- [[evidence]] - claim-level confidence and citations.
- [[goals]] - success criterion.
- [[04-sbir/drafts/phase-1-project-description-draft]] - proposal mapping.
- [[04-sbir/drafts/data-management-plan-draft]] - retention, sharing, and redress requirements.

## Decision gates

| Gate | Evidence required | Decision |
|---|---|---|
| `DG-P0` — common lock | Schemas, authority, rights, baselines, estimands, thresholds and governance approval | Build benchmark/pilot artifacts |
| `DG-E1` — identity feasibility | E1 safety/yield result, subgroup/closure/reference-standard analyses | Continue, narrow or stop identity capability |
| `DG-E2` — event feasibility | E2 scoped synthetic result, uncertainty and privacy/utility review; partner holdout separate | Continue event research or redesign |
| `DG-E3` — governed access | Authenticated policy, audit-reconciliation, correction and privacy results | Continue to bounded E1+E3 integration or redesign |
| `DG-E4` — participation | Institutionally approved recruited-frame burden/comprehension evidence | Fund powered study, redesign offers or stop |
| `DG-E5` — application value | Valid solver and bounded deployable-policy result with safety/service/distribution gates | Consider Phase II orchestration |

## Open decisions

- Final case counts after protocol review; the layered label ontology is RC1 and changes now require controlled amendment.
- PI/domain/counsel freeze of the E1 identity standard; adjudicator composition and conflict-of-interest rules.
- Freight-specific correction-latency threshold.
- Minimum acceptable subgroup sample size for small carriers.
- First permissioned partner and facility-event feed.
- Whether resources justify more than an E5 specification/CPU smoke test in Phase I; full
  execution defaults to Phase II unless the work plan, budget and upstream gates are amended.
- Whether C6 passes its frozen development promotion gates and may compete for `C*`; exact
  model/checkpoint, provider, evidence-egress approval, calibration interface and cost ceiling
  remain open under [[09-meta/gaps/gap-018-e1-llm-readiness]].

## E1 validation architecture

[[e1-academic-design-review]] · [[e1-benchmark-sampling-and-split-plan]] · [[e1-statistical-analysis-and-preregistration-plan]] · [[e1-reporting-and-reproducibility-checklist]]

- [[03-research-evidence/e1-academic-design-conformance-report]]
- [[method-llm-assisted-entity-resolution]] · [[09-meta/decisions/dec-013-llm-e1-challenger]] ·
  [[09-meta/gaps/gap-018-e1-llm-readiness]]
