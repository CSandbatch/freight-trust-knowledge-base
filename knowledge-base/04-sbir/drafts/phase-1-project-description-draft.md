---
type: draft
status: draft
owner: PI + technical lead
authority: NSF 26-510
schema_version: 1.0.0
deliverable: Phase I Project Description
updated: 2026-08-18
tags:
- type/draft
- domain/freight
- domain/identity
- domain/provenance
- domain/federation
- domain/equity
- confidence/mixed
- audience/reviewer
- lifecycle/draft
---
# NSF SBIR Phase I Project Description (Draft)

**Working title:** Federated Evidence Graphs for Explainable Freight Identity and Facility-Event Verification

**Document scope note:** This is the core technical narrative for the Project Description component of a future Research.gov Phase I submission under NSF 26-510. It does not include the Project Summary, budget/justification, facilities statement, biographical sketches, current-and-pending support, data-management plan, or letters — those are separate required documents. Page-limit, formatting, and required-section rules must be reconfirmed against the PAPPG in effect on the submission deadline; the "commonly cited 15-page Project Description" figure has not been independently confirmed in this programme's evidence base [PLACEHOLDER — confirm current PAPPG Chapter II.D.2 page limit before formatting for submission — owner: grant lead].

**Evidentiary basis and confidence handling.** Every factual claim below is sourced to `03-research-evidence/evidence.md`, `03-research-evidence/luna-wide-net-synthesis.md`, or `04-sbir/sbir-evidence-refresh.md` and carries the source layer's confidence/verification status (primary / secondary / unverified). Per the standing review finding (`03-research-evidence/review-notes.md`, R-WN-01 and R-WN-06), this draft does **not** use the unverified $7–16B/year fraud-cost range as a load-bearing claim, and does **not** assert that the proposed system reduces fraud, detention, or empty miles at industry scale. Phase I is designed to test those questions at small scale; they are not premises of the argument. Where the programme's evidence base does not yet contain a fact needed for a rigorous proposal (named partners, actual datasets, specific personnel, exact thresholds), this draft uses a bracketed placeholder rather than inventing one. Aims 1–3's benchmark-construction and tooling claims are also sourced to two 2026-08-01 dataset scans: `03-research-evidence/dataset-scan-entity-resolution.md` (Aim 1) and `03-research-evidence/dataset-scan-event-provenance-and-federation.md` (Aims 2–3), each of which states explicitly what is confirmed-real-and-accessible versus paid/restricted versus not found at all.

---

## 1. Problem and significance

Freight transactions depend on identity and event records that are fragmented across carriers, brokers, shippers, facilities, insurers, and federal registration systems, with no shared, source-attributed, cross-party account of who a counterparty is or what happened at a given facility interaction. This Phase I proposal is scoped to a **single bounded beachhead workflow — carrier onboarding and identity verification** — stated here as a working default pending client confirmation. This is the instance best supported by the programme's current fraud evidence (TIA's April 2025 "State of Fraud in the Industry" member survey, 2025 CargoNet/Verisk cargo-theft data, and FMCSA's own Motus registration-fraud context, all per `sbir-evidence-refresh.md`) and it aligns with Aim 1. A related instance of the same fragmented-evidence problem — disputed facility events — is retained in Phase I only as Aim 2's research validation context, tested against simulated and permissioned event data; it is explicitly **not** a second Phase I commercial beachhead. It is a Phase II expansion candidate, contingent on the single-workflow pilot (Section 6) producing supporting evidence.

**(a) Carrier onboarding and identity verification — the Phase I beachhead.** A broker or shipper must decide whether to tender freight to a carrier it has not dealt with before, based on registration, insurance, and safety-history records held across separate systems. GAO-12-364 directly documents historical FMCSA matching of registration records to target possible chameleon applicants while warning that matching alone could not establish a chameleon carrier ([[03-research-evidence/source-gao-12-364-chameleon-carrier-matching]]). More recently, Motus introduced user-identity, company-account and business-verification functions; reported login/verification and deactivation-pause events show rollout risk, not direct evidence that Motus failed E1's narrower longitudinal legal-person-resolution task under corrupted or conflicting anchors. A directly relevant incumbent also exists: NMFTA launched **SCAC Verified** in February 2026, binding a verified natural-person identity to SCAC issuance and renewal for non-Class-8 carriers while explicitly disclaiming guaranteed fraud prevention. Phase I therefore does not test whether identity can be verified once; it tests whether source-attributed, time-aware and contestable records support safe legal-person resolution while preserving separate registrant, relationship, continuity and regulatory-disposition semantics ([[03-research-evidence/source-nmfta-scac-verified-and-standards-role]]). TIA and CargoNet/Verisk figures remain secondary industry context, not performance targets or proof that E1 will reduce fraud.

**(b) Disputed facility events — Aim 2 research validation context, not a second Phase I beachhead.** ATRI's 2024 study page attributes to its 2023 industry-reported sample estimates that 39.3% of reported stops involved detention, with more than 135 million lost hours, $3.6 billion in direct expense and $11.5 billion in lost productivity. These are ATRI study estimates, not a federal population estimate or an E2 target. FMCSA continues to treat detention measurement—including separation of total facility dwell from delay outside ordinary loading/unloading—as an active research problem. The frequency and evidentiary form of real disputed-event adjudication remain unmeasured in this project; two-party unreconciled logs are a motivating scenario, not a verified prevalence claim. Phase I therefore evaluates source-attributed reconstruction and **injected trace anomaly/contradiction detection** on synthetic cases, with any permissioned partner holdout reported separately. It does not claim malicious tamper attribution, detention adjudication, or a second bounded pilot workflow.

**Why this now.** *Montgomery v. Caribe Transport II, LLC*, 608 U.S. ___ (2026), decided 9-0 on 2026-05-14 (primary source: Cornell LII, SCOTUSblog, Justia), held that the FAAAA's safety exception permits state-law negligent-hiring/negligent-selection claims against freight brokers — a preemption ruling, not a definition of what "reasonable care" in carrier selection requires. Justice Kavanaugh's concurrence explicitly flags that the Court left this standard undefined. This matters to the problem's urgency: a claim type that was contested is now viable nationwide, and no accepted evidentiary standard exists for what a defensible verification record should contain. It is not a claim that any technical system creates legal compliance. This project does not propose to define that legal standard; it proposes to test whether a technically rigorous evidence record — with provenance, calibrated uncertainty, and correction rights — can be built and evaluated for the underlying workflow that any such standard would have to rely on.

**What this project does not claim.** This is not a proposal for a universal risk score, a compliance certification, or a legal safe harbor. It does not assume, and Phase I will not conclude, that the proposed system reduces industry-wide fraud, detention, or empty miles — those require a pilot-scale test that this Phase I is structured to begin, not to complete.

## 2. Innovation and relation to prior art

**The technical bet.** The innovation is a joint requirement, not a new dashboard, score, or data integration. Four properties must hold simultaneously in one decision substrate: (1) entity-resolution outputs carry **calibrated uncertainty** rather than a binary match/no-match decision; (2) facility-event claims carry **provenance** — source, timestamp, submitting party, and permitted use — sufficient for independent assessment; (3) cross-party data access is **policy-enforced** at the field and purpose level rather than pooled; and (4) every consequential output is **contestable** — a participant can challenge a record, and the system can show that the correction changed downstream decision context. Each property has been demonstrated in isolation elsewhere (calibrated matching in record-linkage literature; provenance in supply-chain knowledge graphs; policy-based access control in general security systems). The open research question is whether they can be integrated into one coherent and *measurably* feasible pipeline for this domain. Phase I tests that integration against explicit benchmarks and failure conditions.

**Relation to prior art, by class.** The evidence review of this programme's competitive landscape (13 named commercial products, `evidence.md` G4) found that current tools cluster into three classes, none of which combine all four properties above:

- *Identity/fraud verification tools* typically produce a proprietary composite risk indicator (e.g., a letter grade or score) without exposing source-level provenance or a structured correction/appeal path to the party being scored.
- *Visibility and telematics platforms* capture operational events but as closed, single-vendor data — event records are not source-attributed or interoperable across the parties in a dispute, and calibrated uncertainty is not part of the product design.
- *Load-matching and market-data platforms* address a different problem (capacity/pricing discovery) and were not evaluated as a class for identity or event-provenance claims.

The evidence review found that of the named products, none publicly describe a knowledge-graph or formal entity-resolution architecture except one, which markets a proprietary "logistics data graph" that remains a closed, single-vendor asset rather than a neutral, cross-party federation (`evidence.md` G4). A separate emerging industry framework proposes vetting/evidentiary criteria for carrier selection; the evidence review found it was authored and released by an individual who is also the founder of one of the competitor products named above, and that a claimed connection to a formal standards body could not be confirmed (`evidence.md` G5). This project takes no position on that framework's merits. It notes only that a federally reviewed, independently evaluated research effort is a structurally different kind of artifact than a single vendor's proprietary framework. That distinction is part of this project's rationale; it is not a claim about any competitor's motives.

**Prior art this project builds on, not against.** E1 now explicitly recognizes substantial federal and industry prior art. GAO-12-364 demonstrated registration-data matching as a way to target applicants with chameleon attributes; FMCSA subsequently implemented match+motive screening and developed the Utility for Risk-Based Screening and Assessment (URSA), whose lineage includes a prior SBIR Phase I and an automated chameleon/reincarnation risk-assessment tool. In 2026, FMCSA's Motus separates individual identity verification from company-account/business verification, and NMFTA's SCAC Verified adds lifecycle-point natural-person verification to SCAC issuance/renewal. The project therefore does **not** claim that carrier screening, chameleon-risk matching, or point-in-time identity verification is novel. Its Aim 1 research question is narrower: whether a source-attributed, time-aware and contestable identity graph can improve **legal-person resolution under missing/corrupted/conflicting anchors while preserving separate registrant, ownership/succession, continuity and regulatory-disposition semantics**, calibrated uncertainty, and human abstention (`e1-identity-definition-research-report.md`; `e1-definition-freeze-review.md`). GLEIF's distinction between Level 1 “who is who” and Level 2 “who owns whom” is a useful organizational-identity analogue for that separation. NIST's traceability meta-framework (NIST IR 8536) likewise shapes Aim 2. None of these precedents is evidence that this specific integrated application will succeed; the aims below test it.

**Candidate methods (to be evaluated, not assumed).** This project treats the following as
candidates subject to comparative evaluation, not as pre-selected solutions: probabilistic
record linkage (e.g., Fellegi–Sunter-style models), graph-assisted matching, supervised
Transformer/cross-encoder matching, embedding retrieval, and a constrained generative-LLM
resolver for Aim 1; calibration approaches including Bayesian calibration and
conformal-prediction-style abstention sets for uncertainty quantification; signed or
verifiable-credential-style assertion structures for event provenance in Aim 2; and
attribute-based or purpose-based access control (ABAC/PBAC) policy languages for Aim 3.
The LLM candidate receives only frozen, source-attributed, pre-cutoff evidence, returns a
schema-constrained decision with input evidence IDs, and cannot supply gold labels or an
authoritative regulatory conclusion. Phase I's job is to determine which candidates, if any,
are feasible and performant enough on this domain's data to justify further investment. A
negative or mixed result on a specific candidate method is a valid and useful Phase I outcome.

## 3. Research Aim 1 — Calibrated, layered carrier identity resolution

**Identity standard.** Before benchmark construction, the project executed a dedicated source-
grounded definition pass over current statute/regulation and FMCSA practice. The resulting
`E1 Carrier Identity & Relationship Standard 1.0.0-rc1` rejects one binary “same carrier” label.
Task A resolves observations to a **legal person**. Task B separately represents authoritative
USDOT assignment and FMCSA registrant continuity. Task C represents ownership/control,
predecessor/successor transactions, and substantial continuity among distinct persons. Any
reincarnation/affiliate conclusion remains a separate regulatory-disposition layer. The RC1
standard has passed a hostile synthetic conformance review but remains subject to PI, freight-
domain, and counsel/domain freeze approval before gold labeling begins.

**Hypothesis.** Under anchor-masked/missing/corrupted and time-forward conditions, one
development-selected, calibrated, abstention-capable non-manual resolver can assign fragmented
carrier observations to the correct legal-person identity while meeting a preregistered
assignment-precision safety floor, then improve auto-resolution yield over deterministic rules
at the same safety policy and human-review budget, **without falsely merging affiliated,
successor, or operationally continuous but legally distinct entities**. Graph and LLM methods
are useful only if their incremental context improves that safety-first operating point without
creating those category errors.

**Why this is uncertain.** No public adjudicated U.S. freight-identity benchmark with the RC1
legal-person/registrant/relationship layers has been identified. At the same time, there is
significant prior art: GAO and FMCSA have long used registration matching for chameleon-risk
targeting, URSA automated risk assessment, and current Motus/SCAC processes verify identities at
registration or credential lifecycle points. E1 therefore tests a different uncertainty: whether
provenance, time, typed relationships, calibrated confidence, and abstention add measurable value
when authoritative anchors are incomplete, stale, conflicting, fraudulently claimed, or hidden.

**Experiment.** Build [[dataset-e1-adjudicated-carrier-identity-cases]] from the FMCSA Company
Census File plus predicate-specific authoritative evidence required by sampled cases, including
targeted state corporate records when a legal-person/transaction question cannot be settled from
FMCSA sources. The corpus stores canonical legal-person clusters rather than arbitrary pairwise
truth, then derives pair labels and separate Task B/Task C gold states. Two independent reviewers
label hard cases while blinded to model and candidate-generation scores; a third adjudicator
handles disagreements without erasing original votes. `UNRESOLVED` is a legitimate gold state.
Safety/enforcement/motive history is excluded from Task A identity adjudication and features.

Synthetic corruption remains useful, but only for controlled observation noise (typos, missing
fields, near-duplicate addresses, DBA/legal-name substitutions, corrupted or missing identifiers).
It is **not** used to manufacture authoritative chameleon ground truth. The benchmark also includes
real structural hard cases such as ownership changes, stock versus asset transactions, mergers,
operating-authority transfers, shared addresses/registered agents, claimed-versus-assigned USDOT
conflicts, and identity-impersonation scenarios. Regulatory reincarnation is represented only
where an authoritative agency/judicial disposition supports it.

All candidate methods run under identical feature regimes: **F0** anchor-visible control; **F1**
authoritative anchor masked; **F2** anchor missing; **F3** anchor corrupted; **F4** claimed-versus-
assigned identifier conflict; **F5** cross-registration relationship cases; **F6** time-forward.
F0 cannot be the headline result because exposing the same authoritative USDOT assignment used to
settle gold identity would reduce evaluation to identifier lookup. Compare deterministic,
probabilistic, graph-assisted, and constrained LLM resolver methods at matched
false-positive/coverage/review-budget operating points; add calibrated abstention/human review
as the deployment-like condition. The LLM is first tested after frozen candidate generation and
in a common-candidate-set ablation so retrieval gains cannot be mistaken for resolver gains.
Report
Task A precision/recall/F1, false-merge mechanisms, cluster consistency, calibration, coverage-
risk/abstention, blocking recall, review time, and subgroup performance by fleet size, record age,
missingness, weak-field collision, and graph degree. Task B/C metrics are reported separately and
are not allowed to inflate Task A results.

**Targets.** The development pilot will set and then freeze: assignment-precision floor `P*`;
minimum meaningful auto-resolution-yield improvement `Delta*`; the common human-review budget;
sample size/precision requirements; and the operating threshold. Calibration will be assessed
with intercept/in-the-large, slope, a smoothed reliability curve, Brier score and the complete
risk-coverage curve rather than reduced to one arbitrary “maximum calibration error.” These
quantities will be fixed before final evaluation and reported whether or not they are met. No
published benchmark result for this record type exists to anchor a target by analogy. The
Magellan/WDC/Febrl benchmarks and recent LLM entity-matching studies are methodological precedent
for *how* to compare methods; their product, bibliographic or person-record performance numbers
are not transferable targets for carrier legal-person identity.

**Scope limit on chameleon/reincarnation claims.** Phase I will not report a real-world chameleon-
carrier prevalence or detection rate from this benchmark. GAO/FMCSA matching is prior screening
art, not published gold pairs, and synthetic continuity scenarios are not agency findings. The
benchmark may include final authoritative dispositions as regulatory-disposition cases, but those
are evaluated separately from Task A identity equivalence. Analytical similarity/continuity can
only produce a review-candidate or supported-relationship state, never a self-issued regulatory
finding.

**Abstention logic.** Candidate approaches to evaluate: a fixed confidence-threshold abstain bucket, a conformal-prediction-style set-valued output, and a human-review referral queue for the abstained set. Phase I will report which (if any) produces an abstained set with a measurably higher error rate than the auto-resolved set — the property that makes abstention useful rather than cosmetic.

**Failure condition.** The approach fails Aim 1 if no candidate method beats the deterministic baseline at matched error cost, if calibration is no better than an uncalibrated baseline, or if error/abstention rates are materially worse for small-carrier segments without an identified mitigation — in which case Aim 1's output does not proceed into the Aim 3 integration as currently scoped, and Aim 1 cannot pass its Month 6 identity gate or proceed into the Month 9 integration gate as currently scoped.

## 4. Research Aim 2 — Event provenance and verification

**Hypothesis.** Facility events can be represented as source-attributed, time-aware assertions such that preregistered injected omissions, sequence anomalies and contradictions are detected above transparent baselines, reconstructed times/dwell intervals express uncertainty honestly, and correction lineage remains auditable. This is an anomaly/reconstruction hypothesis, not proof of malicious tampering or source truth.

**Why this is uncertain.** No adjudicated event-provenance benchmark exists yet (`review-notes.md` R-WN-04); it is unknown what fraction of real facility events can be captured with complete source/time metadata without imposing new manual data-entry burden on facility staff; adversarial modification patterns specific to this domain have not been characterized; and it is unknown whether correlating independent event assertions (facility log vs. telematics vs. driver-submitted timestamp) reliably distinguishes fraud/tampering from benign discrepancies such as clock skew or a legitimate appointment reschedule.

**Event/assertion schema (candidate design).** Each decision-relevant assertion records: event type (aligned where applicable to ASTM F49 goods-movement process terminology and NMFTA freight OpenAPI event vocabulary — an alignment choice, not a claim of formal ASTM endorsement), source system, submitting party, capture timestamp, an authority/verification level, a permitted-use/purpose tag, a confidence or verification status, and a correction/annotation history. Candidate mechanisms for tamper-evidence — a signed assertion, hash-chained log, or verifiable-credential-style structure — will be evaluated for engineering cost against detection benefit rather than assumed.

**Trust and threat model.** Phase I will explicitly define, and test against, a bounded adversary model: single-party record fabrication, backdated timestamps, replay or silent edit of an already-submitted assertion, and selective omission. It will also state a known limitation outright: collusive fabrication between the only two parties witnessing an event cannot be detected without an independent third signal. Phase I will report that as a structural limitation.

**Experiments.** No qualifying freight-specific public benchmark was located in the documented search through 2026-08-18; this is a scoped negative result, not proof of nonexistence. OpenEPCIS will generate schema-valid synthetic traces pinned to GS1 EPCIS 2.0.1/CBV 2.0.0 plus an explicit freight extension. BTS–ATRI county-pair percentiles constrain transit plausibility only; they contain no facility service/dwell truth. PDC supports hidden-truth synthetic process evaluation, while Nolle/BINet supplies the artificial Skip/Insert/Rework/Early/Late/Attribute anomaly-injection precedent; E2's freight threat operators are new project-defined choices. The corpus preserves separate canonical truth, observability truth and source observations. Event-level classification, trace-level omission detection and interval-censored dwell reconstruction use separate denominators. Any permissioned partner holdout uses agreement/adjudication and interval-coverage estimands unless independent truth exists, and is never pooled with the synthetic estimate.

**Targets.** [TARGET — set after simulated case-set design: injected anomaly/contradiction detection rate at a defined false-alarm ceiling]; 100% provenance-metadata completeness in the test corpus (a structural target, testable independent of external data quality); [TARGET — set after workflow prototyping: correction-latency ceiling].

**Failure condition.** Aim 2 fails if detection performance is not meaningfully better than a naive single-source discrepancy check, or if the correction workflow cannot demonstrate a downstream context update within the target time — in which case the event-provenance component does not proceed into the integrated pilot (Section 6) without redesign.

## 5. Research Aim 3 — Governed federation and contestability

**Hypothesis.** A policy-enforcement layer can restrict cross-party evidence access to permitted partner/field/purpose combinations — with source systems remaining authoritative and federated by default, not pooled — while supporting an end-to-end correction and appeal path, without requiring raw commercial data to leave a participant's environment.

**Why this is uncertain.** No worked participation/incentive mechanism for freight-specific data sharing currently exists in this programme's evidence base (research goal G7/G12, open) — a dedicated dataset/benchmark scan checked whether federated-learning benchmark literature (LEAF, FedML, Flower) addresses this question and confirmed it does not: those are ML-training-computation benchmarks, not participation-economics research (`dataset-scan-event-provenance-and-federation.md`); this gap requires direct stakeholder research, not a dataset, and stays open. The trade-off between policy granularity and practical usability for this domain is untested; whether an audit log can be simultaneously tamper-evident and respectful of partner confidentiality constraints is untested; and redress-workflow latency under realistic multi-party conditions is unknown.

**Policy model (candidates).** Attribute-based access control (ABAC), purpose-based access control, and capability-token-based schemes will be evaluated as candidates against this domain's access patterns — no architecture is pre-selected. NIST's own open-source Policy Machine (the Next Generation Access Control, or NGAC, reference implementation — `usnistgov/policy-machine-core` and `policy-machine-pdp`) is identified as a concrete, government-built, freely available ABAC/NGAC enforcement engine that can be configured with freight-specific partner-type, field-category, and purpose attributes rather than requiring an enforcement engine to be built from scratch; NIST SP 800-178 provides a direct, primary-source comparison of XACML and NGAC to inform this evaluation.

**Enforcement tests.** The project will define neutral test tuples `(policy version, request, expected domain decision, expected audit event, rationale)` inspired by access-control test practice. XACML and NGAC are different policy models: an NGAC lane uses NGAC-native policies/tests; an XACML lane uses an actual pinned XACML PDP and maps XACML's `Permit`, `Deny`, `Indeterminate` and `NotApplicable` plus obligations into the project's domain decisions. Cross-engine comparison is permitted only after an explicit semantic crosswalk. OASIS publishes test material but explicitly does not operate an XACML certification programme, so no result will be called OASIS certification. High-severity rules are exhaustively tested; remaining attribute combinations use preregistered covering arrays, boundary/conflict and mutation tests with reported coverage.

**Audit design.** A policy-enforcement point records every received attempt before and after PDP evaluation—including authentication failures, malformed requests, indeterminate/not-applicable decisions, timeouts and errors—and reconciles that ledger against responses and engine events. JWT authentication with pinned issuer/audience is required; unauthenticated and sandbox modes are forbidden outside isolated negative tests. Hash chaining supplies post-hoc alteration evidence under stated trust assumptions, not authenticity, confidentiality, complete capture, trusted time, nonrepudiation or truncation resistance by itself.

**Redress prototype.** A scripted challenge case must correct or annotate the record, or preserve an unresolved disagreement, while prior history remains auditable and authorized downstream context visibly updates. The 30-day reinvestigation rule in 15 U.S.C. §1681i is directly verifiable but applies to consumer reporting agencies under its statutory conditions; it is an adjacent reporting precedent, not a freight legal right or imported latency target. NIST Privacy Framework and SP 800-63A-4 redress guidance provide technical/governance design analogues. The freight threshold remains a preregistered Phase I choice.

**Privacy threat model.** Phase I will explicitly enumerate leakage channels that could persist even under policy enforcement — metadata/inference leakage, re-identification via cross-referencing of permitted fields, and insider misuse — and will state which are addressed by structural controls within Phase I scope and which would require Phase II hardening. The enumeration is the Phase I deliverable. Phase I does not claim a solved privacy problem.

**Failure condition.** Aim 3 fails if the policy layer cannot demonstrably block disallowed combinations in automated testing, if the correction/appeal path cannot be shown to change downstream decision context, or if the privacy threat model identifies a leakage class with no feasible Phase I mitigation — in which case federation and redress claims are scoped down for Phase II rather than carried into the integrated pilot as currently designed.

## 6. Integration and bounded pilot

**The workflow.** The three aims share an evidence architecture, but only Aims 1 and 3 integrate in the **single bounded pilot workflow** named in Section 1(a): carrier onboarding/identity verification by a broker or shipper before tendering freight — the working-default beachhead, pending client confirmation. Aim 2's event-provenance and injected anomaly/contradiction methods (Section 4) are developed and evaluated separately in Phase I against simulated data and, only under an executed data-use instrument, permissioned facility-event data. Disputed facility events (Section 1(b)) are **not** integrated into this bounded pilot as a second workflow in Phase I — that integration is a Phase II expansion candidate, contingent on this Phase I's results (Section 10).

**What a Phase I-scale demonstration is.** Integration of the Aim 1 and Aim 3 components (entity resolution and governed federation/policy enforcement) into a single test pipeline scoped to the carrier onboarding/identity-verification workflow, run against the adjudicated identity benchmark (Section 3), public/synthetic records, and partner records only after an executed authorization/data-use instrument records the permitted purpose. A nonbinding pilot-interest statement is commercialization evidence, not data-use permission. Aim 2's provenance/anomaly components are evaluated separately against the Section 4 simulated event-provenance benchmark and are not required to run live inside this bounded pilot. This is a technical-feasibility demonstration of the integrated pipeline's behavior on defined test cases, for one named workflow.

**What it explicitly is not.** Not a nationwide or production deployment; not a claim that fraud, detention, or empty miles are reduced at industry scale; not a compliance or legal-standard product; and not a two-workflow pilot — disputed facility-event handling remains Aim 2's research validation context in Phase I, not a second bounded commercial workflow. Any operational-outcome claim below applies only to the bounded pilot's test cases within the carrier onboarding/identity-verification workflow.

**Measurable operational outcome.** Resolution-time improvement (or a defined equivalent measure) relative to a documented manual/status-quo carrier-onboarding baseline workflow, measured on n = [PLACEHOLDER — test-case count] cases within the bounded pilot, target: [TARGET — set after baseline workflow is documented]. This outcome is reported as a bounded-pilot finding, not extrapolated to the broader market.

## 7. Work plan and milestones

Phase I is planned for a 12-month period of performance within NSF 26-510's allowable 6–18 month range [PLACEHOLDER — confirm final requested duration against budget and PI-effort planning].

| Months | Activity | Depends on |
|---|---|---|
| 1–2 | Finalize data-rights/partner map; draft provenance schema and threat model (Aim 2); draft benchmark protocol (Aims 1–2) | Pilot-interest and data-access commitments in place |
| 2–4 | Construct and adjudicate identity-resolution and facility-event benchmark cases | Months 1–2 protocol |
| 3–6 | Implement and evaluate Aim 1 baseline and candidate entity-resolution methods; run calibration and error-slice analysis | Benchmark (Months 2–4) |
| 4–7 | Implement Aim 2 event schema and simulated alteration/anomaly/contradiction case set; run detection experiments | Provenance schema (Months 1–2); benchmark (Months 2–4) |
| 6–9 | Implement Aim 3 policy model prototype and automated enforcement test suite; build audit log | Aim 1 schemas stable enough for the bounded Aims 1+3 integration |
| 8–10 | Build and run scripted redress/correction workflow (spans Aims 2 and 3) | Aim 2 correction hooks; Aim 3 policy/audit layer |
| 9–11 | Integrate Aims 1 and 3 into the bounded-pilot pipeline (Section 6); run end-to-end tests on benchmark/public/synthetic data and only separately authorized partner data | Aims 1 and 3 individually meeting go/no-go criteria; executed data-use instrument for any partner records |
| 10–12 | Run error-disparity/equity analysis across all aims; compile final benchmark and evaluation report; consolidate commercialization evidence; produce go/no-go assessment and Phase II plan | All prior milestones |

**Milestone table with quantitative go/no-go criteria**

| Milestone | Target month | Quantitative go/no-go criterion | Why it matters |
|---|---|---|---|
| Provenance schema and threat model complete | 2 | Every decision-relevant assertion type in the test corpus records source, timestamp, permitted use, confidence, and correction status | Prevents an opaque score from becoming the product |
| Benchmark constructed and adjudicated | 4 | Adjudicated identity and event case sets exist with documented labeling protocol and inter-adjudicator agreement measure [TARGET — set once adjudication protocol is final] | Nothing downstream is measurable without this |
| Entity-resolution feasibility (Aim 1) | 6 | Beats the deterministic baseline at a matched operating point on the held-out set; reports calibration and fleet-size error slices, not only aggregate accuracy | Tests whether the claimed innovation adds measurable value |
| Event-reconstruction/anomaly feasibility (Aim 2) | 7 | Detects a defined share of injected anomaly/contradiction cases at a defined false-alarm ceiling and reports reconstruction uncertainty; preserves an auditable evidence trail for every test case | Tests reconstruction and anomaly handling, not malicious intent or source truth |
| Federation policy enforcement (Aim 3) | 9 | 100% denial and 100% audit-log capture of disallowed partner/field/purpose combinations in automated tests | Tests the privacy and commercial-boundary claims directly |
| Redress workflow demonstrated | 10 | Scripted challenge case results in a corrected/annotated record with downstream context change within [TARGET] time | Makes contestability measurable, not aspirational |
| Integrated bounded-pilot run | 11 | Aims 1 and 3 pipeline completes on n = [PLACEHOLDER] authorized benchmark test cases; Aim 2 remains a separately reported research validation | Tests the named onboarding pipeline without silently adding a second workflow |
| Equity and disparity analysis complete | 12 | Error/abstention/false-positive rates reported by fleet-size segment for Aims 1 and 3, with any disparity and proposed mitigation stated explicitly | Converts a generic equity claim into an assessable result |
| Commercial evidence consolidated | 12 | [PLACEHOLDER — count] structured discovery interviews and [PLACEHOLDER — count] nonbinding pilot-interest statements documented | Tests the beachhead, not the technical work alone |

## 8. Team and resources

*All names, roles, and commitments below are structural placeholders describing the roles and effort the work plan requires. No individual is named without a confirmed, signed employment/effort commitment.*

| Role | Responsibility | Effort | Notes |
|---|---|---|---|
| **Ellie Young — Principal Investigator** | Overall technical direction; Aim 1 (entity resolution) design and evaluation; NSF PI-of-record | [OPEN — effort % and employment commitment; owner: Ellie Young/Common Action; DEC-002] | PI identity confirmed 2026-08-08; eligibility depends on the applicable NSF employment/effort rule at award and throughout performance |
| [Technical lead — data/provenance/security] | Aim 2 schema, threat model, reconstruction/anomaly experiments; Aim 3 audit-log design | [PLACEHOLDER] | |
| [Technical lead — policy/access systems] | Aim 3 policy-model prototyping and enforcement test suite | [PLACEHOLDER] | May be the same person as above depending on final team composition |
| **Russell Berry — Research & Knowledge Architecture Lead** | Evidence/ontology architecture; benchmark and experiment specification support; provenance/source governance; technical and proposal synthesis | [OPEN — effort %, compensation, and employment/consultant classification; owner: Common Action; DEC-010] | Working programme role; not an invented corporate title or employment classification |
| [Product/commercial lead] | Bounded-pilot workflow definition, pilot-interest partner engagement, commercialization evidence (interviews, pilot-interest statements) | [PLACEHOLDER] | |
| [Domain/freight SME — consultant or named partner] | Benchmark adjudication support; validity review of event schema against real facility operations | [PLACEHOLDER — consultant vs. subaward terms] | Only to be named once a specific, written engagement exists |
| [Legal/privacy advisor] | Review of privacy threat model, data-rights terms, and non-reliance/scope language | [PLACEHOLDER] | |

**Facilities and data access.** [PLACEHOLDER — computing environment and any pilot environment access; owner: data/product lead + counsel]. The FMCSA Company Census File is publicly downloadable and can seed Aim 1 acquisition, but its catalog licence remains `Unknown License`; derived benchmark redistribution and each joined source require rights review. NIST Policy Machine is available under its repository licence as one NGAC implementation candidate, not a certified or zero-dependency service. OASIS XACML material informs a separate XACML-native lane and cannot be run against NGAC without an explicit adapter/crosswalk. No partner, bulk state-registry/OpenCorporates access, ATRI raw GPS data, PIERS data or live facility API is treated as secured without written authorization.

## 9. Broader impacts

**Small-business status is not a fleet-size distribution.** GAO-16-401R reports FMCSA's estimate that approximately 99.1% of regulated motor carriers meet one of the applicable SBA small-business standards. It does not show that 99.1% are owner-operators, very small fleets or resource-constrained firms. Aim 1 and Aim 3 will report outcomes by preregistered power-unit bands and direct capacity/burden measures; those bands require a defined MCMIS population and current distribution analysis. Structured discovery must include genuinely small operators, but interview quotas and thresholds remain placeholders until the recruitment frame is approved.

**No automated indicator decides eligibility, pricing, contracting, or liability without human review.** Aim 3's enforcement suite and redress prototype test this as a design constraint: the automated pipeline's outputs feed a review step, and the correction/appeal path is evaluated for whether it works when exercised.

**No-paywall basic verification.** Whether a no-cost basic verification tier is technically and operationally sustainable within the pipeline (i.e., does not require degrading it for small carriers to remain feasible) is tested as part of the bounded pilot (Section 6), not assumed.

**Data minimization by design.** Aim 3's policy-enforcement tests directly measure whether the system can be shown to grant only the minimum necessary fields for a stated purpose, with a full audit trail of what was requested, by whom, and why.

**Record access is a live concern; Freight Trust correction latency remains a hypothesis.** OOIDA's 2025 broker-transparency position supports timely access to transaction records and opposition to waiver of that access. It does not establish demand for correction of Freight Trust records or supply a correction-latency threshold. The correction and appeal mechanism is a project governance choice that Aim 3 tests and E4 must validate with participants.

**Reusable, interoperable pattern beyond one company's product.** The event schema's alignment with ASTM F49 goods-movement process terminology and NMFTA's freight OpenAPI vocabulary, and the provenance design's alignment with NIST's traceability meta-framework (NIST IR 8536), are chosen so that a successful Phase I result produces a pattern other efforts could adopt, not only a proprietary artifact.

## 10. Phase II trajectory

If Phase I's go/no-go milestones (Section 7) are met — entity resolution beating baseline with acceptable calibration and no unmitigated small-carrier disparity, event reconstruction/anomaly detection meeting its declared synthetic gates with an auditable trail, and federation/redress demonstrably enforceable and contestable — Phase II would be justified in pursuing a larger-scale, multi-partner pilot using real multi-party data flows under negotiated data-rights agreements; an expanded, independently adjudicated benchmark; hardened privacy/security mitigations; and commercialization validation involving paying pilot customers rather than nonbinding interest statements. Phase I results alone would not justify deployment or go-to-market.

---

## How this document maps to NSF criteria

| NSF criterion | Where a reviewer finds the answer |
|---|---|
| Intellectual Merit | Sections 2–5: the four-property integration argument (Section 2), and each aim's hypothesis, uncertainty, experiment, metric, and failure condition (Sections 3–5) |
| Broader Impacts | Section 9, with quantitative measurement commitments; also Section 3's fleet-size error-slice requirement and Section 5's privacy threat model |
| Commercial Potential | Section 1 (problem grounding and urgency), Section 6 (bounded pilot and measurable operational outcome), Section 7's "commercial evidence consolidated" milestone, and Section 10 (Phase II trajectory) |
| Novelty vs. prior art | Section 2 ("Relation to prior art, by class" and "Prior art this project builds on") |
| Feasibility and risk management | Every aim's "why this is uncertain" and "failure condition" (Sections 3–5); Section 7's go/no-go milestone table |
| Team capability | Section 8 |

## Placeholder register

| Placeholder | Location | What's needed | Owner |
|---|---|---|---|
| GAO/ATRI freshness check | Sections 1 and 9 | Recheck the verified primary pages immediately before submission; preserve GAO's SBA-standard and ATRI's industry-study limitations | Research lead / grant lead |
| Facility dwell calibration | Section 4 | Obtain permissioned facility data or retain authored sensitivity priors; BTS county-pair travel time is not facility dwell truth | Research/data lead |
| Freight correction-latency target | Section 5 | Set from prototype and participant/governance review; do not import FCRA's consumer-reporting deadline | Legal/research lead |
| Beachhead-workflow confirmation | Section 1, Section 6 | Carrier onboarding/identity verification is set as the single Phase I bounded pilot workflow as a **working default** by internal review (best supported by current fraud evidence and Aim 1 alignment); this has not yet been confirmed by the client and should be before submission | Commercial lead + client |
| PAPPG page-limit/format confirmation | Header scope note | Current PAPPG Chapter II.D.2 requirements at submission | Grant lead |
| Requested Phase I duration (6–18 months) | Section 7 | Final decision once budget/PI-effort plan is set | PI + grant lead |
| Additional identity-resolution data sources beyond the confirmed FMCSA Company Census File — OpenCorporates bulk/paid access or state-registry cross-reference — plus final labeling-protocol sign-off | Section 3 | Lawful, permissioned data-source agreements; the Company Census File itself is confirmed and does not require this | Data/product lead + counsel |
| Precision/recall/calibration numeric targets (Aim 1) | Section 3 | Set after benchmark and baseline are built | PI + technical lead |
| Simulated alteration/anomaly/contradiction case count and taxonomy (Aim 2) | Section 4 | Finalize with benchmark protocol | Technical lead (provenance) |
| Anomaly-detection rate and correction-latency numeric targets (Aim 2) | Section 4 | Set after case-set design and workflow prototyping | Technical lead (provenance) |
| Correction-visibility latency target (Aim 3) | Section 5 | Set after redress prototype is built | Technical lead (policy/access) |
| Named pilot-interest participants | Section 6 | Signed, nonbinding pilot-interest documentation | Commercial lead |
| Bounded-pilot test-case count (n) and resolution-time target | Section 6 | Set after baseline manual workflow is documented | PI + commercial lead |
| Inter-adjudicator agreement target for benchmark | Section 7 milestone table | Set once adjudication protocol is final | Technical lead + data lead |
| Integrated pilot test-case count (n) | Section 7 milestone table | Depends on benchmark and pilot-partner scope | PI + commercial lead |
| Discovery-interview and pilot-interest-statement counts | Section 7 milestone table | Complete structured customer discovery | Commercial lead |
| PI effort %, employment commitment | Section 8 | Ellie Young is confirmed as PI; confirm the applicable NSF employment/effort eligibility facts | Common Action + Ellie Young |
| Russell Berry effort %, compensation, classification | Section 8 | Confirm working-project role as senior/key personnel, employee, consultant, or other permissible category and enter actual effort/rate | Common Action + PI |
| Technical leads (provenance/security; policy/access) — names and effort | Section 8 | Team confirmed | CEO |
| Product/commercial lead — name and effort | Section 8 | Team confirmed | CEO |
| Domain SME / consultant or subaward partner | Section 8 | Written engagement terms (consultant vs. subaward) | PI + counsel |
| Legal/privacy advisor | Section 8 | Engagement confirmed | CEO + counsel |
| Computing environment and any pilot-environment access (data sources for Aims 1 and 3 are now confirmed; see Section 8) | Section 8 | Computing environment; pilot-partner data access authorization | Data/product lead + counsel |
| Fleet-size segment bracket definitions | Section 9 | Define brackets used for equity/disparity reporting | PI + technical lead |
