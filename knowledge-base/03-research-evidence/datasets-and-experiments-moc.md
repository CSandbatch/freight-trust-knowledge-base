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
3. **Policy cases**: `(policy, request, expected decision)` triples covering permitted and
   disallowed partner, field, and purpose combinations.
4. **Metadata and governance**: provenance, license, consent, sensitivity, retention,
   redaction, adjudicator agreement, and known limitations for every case.


## E1 identity specification package (RC1)

- [[e1-identity-definition-research-report]] — source-grounded Research Agent execution.
- [[e1-identity-claims-ledger]] — auditable determination ledger.
- [[e1-carrier-identity-and-relationship-standard]] — human semantic contract, `1.0.0-rc1`.
- [[e1-identity-ontology.yaml]] — machine-readable object/relation semantics.
- [[e1-adjudication-decision-tree]] — reviewer procedure.
- [[e1-edge-case-suite.csv]] — 60 synthetic conformance/adversarial cases.
- [[e1-definition-freeze-review]] · [[e1-state-corporate-source-access-memo]] — hostile Eval Agent findings and second-pass verdict.

The initial loose “same carrier” formulation failed hostile review with eight Critical and eleven
Major findings. RC1 has no open Critical/Major design defect in the synthetic conformance suite,
but remains **unfrozen** pending PI, freight/FMCSA-domain, counsel/domain, and adjudicator-training
gates.

## Experiment entries

Shared standard: [[experiment-protocol-standard]].

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
| E1 — identity | R-WN-04, R-WN-03, R-WN-05; G14, G13 | Current FMCSA legal/registration rules; GAO/ARCHI/URSA prior art; GLEIF identity-vs-relationship analogue; multi-reviewer gold-label methodology; Company Census File + corruption/blocking methods | Layered identity standard + ontology; adjudicated legal-person corpus; split/feature-regime manifests; error taxonomy | RC1 complete; PI/domain/counsel freeze, adjudicator panel/COI, first state source-access memo |
| E2 — event provenance | R-WN-04; G14, G11 | OpenEPCIS generator (Apache 2.0) over GS1 EPCIS 2.0/CBV 2.0; Process Discovery Contest and Nolle-tradition anomaly injection; BTS–ATRI travel times; NIST IR 8536; NIST SP 800-188 | Event ontology and data contract, base-trace generator, anomaly-injection manifest, hidden-label set | Case count and taxonomy; C5 partner access |
| E3 — governed federation | R-WN-03; G11, G13 | NIST Policy Machine (NGAC reference implementation); OASIS/AT&T XACML conformance format; NIST SP 800-162 / 800-178 / 800-192; GLEIF governance analogue; FCRA and Oversight Board as reporting precedents | Policy catalogue, attribute dictionary, versioned conformance suite, audit-integrity evidence | Plain-language policy authoring (legal/commercial judgment) |
| E4 — participation and equity | R-WN-02, R-WN-05; G7, G12, G8 | Imai/Jiang/Malani on interference; GAO-16-401R (99.1% small carriers); OOIDA's 49 CFR 371 comment. **Negative finding:** LEAF/FedML/Flower were checked and address none of this | Recruitment/consent protocol, spillover map, burden codebook, refusal analysis | Named pilot participants; fleet-size band definitions |
| E5 — orchestration value | Improvement item 1 (demote, don't discard); R-WN-01; G10 | SINTEF VRPTW benchmark instances for solver validation; agent-based empty-truck-trip modelling precedent; E2's dwell and E3's constraints as inputs | Scenario and constraint specification, validated simulator, ablation and Pareto results | E2/E3/E4 outputs; Phase I-versus-II scoping decision |

Two provenance facts apply across all five and should not be lost in the detail. The
2026-08-01 scans established several **confirmed absences** — no public adjudicated carrier-
identity benchmark with the layered E1 labels, no freight-specific facility-event benchmark,
no participation-economics answer in the federated-learning literature. The 2026-08-08 E1
research simultaneously established substantial **prior art in chameleon screening and
point-in-time identity verification** (GAO/ARCHI/URSA, Motus, SCAC Verified). The novelty claim
must therefore concern the evaluated benchmark/provenance/relationship architecture, not the
existence of carrier identity screening itself.
Several sources also remain **unverified in this evidence base** — the FMCSA L&I and
MCMIS catalog pages (HTTP 403 or JS shell), the Company Census File's licence text, PIERS's
terms, and FCRA's exact statutory window. None of them is load-bearing for any experiment,
and each is flagged inline where it appears.

## Method entries

- [[method-deterministic-entity-matching]]
- [[method-probabilistic-entity-resolution]]
- [[method-graph-assisted-entity-resolution]]
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

Every record needs: `case_id`, `entity_or_event_id`, `source_id`, `observed_at`, `valid_from`,
`valid_to`, `claim_type`, `value_or_hash`, `confidence`, `access_purpose`, `consent_or_basis`,
`label_status`, `adjudication_status`, `correction_status`, `retention_until`, and `version`.

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
| G0 — protocol freeze | Schemas, labels, baselines, thresholds, governance approval | Build benchmark |
| G1 — identity feasibility | E1 results and subgroup analysis | Continue, revise, or stop identity aim |
| G2 — event feasibility | E2 results and provenance completeness | Continue, revise, or stop event aim |
| G3 — federation feasibility | E3 policy and audit test results | Continue to partner pilot or redesign |
| G4 — participation | E4 adoption and equity results | Scale, change incentives, or stop |
| G5 — application value | E5 bounded workflow result | Consider Phase II orchestration |

## Open decisions

- Final case counts after protocol review; the layered label ontology is RC1 and changes now require controlled amendment.
- PI/domain/counsel freeze of the E1 identity standard; adjudicator composition and conflict-of-interest rules.
- Freight-specific correction-latency threshold.
- Minimum acceptable subgroup sample size for small carriers.
- First permissioned partner and facility-event feed.
- Whether E5 belongs in Phase I or is reserved for Phase II.

## E1 validation architecture

[[e1-academic-design-review]] · [[e1-benchmark-sampling-and-split-plan]] · [[e1-statistical-analysis-and-preregistration-plan]] · [[e1-reporting-and-reproducibility-checklist]]

- [[03-research-evidence/e1-academic-design-conformance-report]]
