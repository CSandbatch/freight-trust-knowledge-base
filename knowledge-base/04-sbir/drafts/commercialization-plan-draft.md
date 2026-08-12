---
type: draft
status: draft
owner: commercial lead
authority: NSF 26-510
schema_version: 1.0.0
deliverable: Commercialization Plan
updated: 2026-08-08
tags:
- type/draft
- domain/freight
- domain/identity
- domain/adoption
- confidence/mixed
- audience/reviewer
- lifecycle/draft
---
# Commercialization Plan Draft

*Beachhead-first commercialization draft supporting the Commercial Potential review criterion under NSF 26-510. This draft follows the market-opportunity direction in [[nsf-sbir-sttr-process-and-readiness-guide#3. Project Pitch: the required first submission]] and the workstream framing in [[01-client-briefs/freight-trust-client-master-brief#Dataset and experiment backbone]]. It intentionally starts narrow: NSF review rewards a focused beachhead and real customer-discovery evidence over a broad platform narrative — see the failure pattern warning in [[nsf-sbir-sttr-process-and-readiness-guide#6. Review rubric translated for this programme]] against "writing an enormous market narrative without identifying the first buyer, workflow, integration path, and commercial alternative."*

## 1. Initial buyer hypothesis (beachhead)

| Element              | Hypothesis                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| First buyer segment  | Broker/carrier networks handling counterparty onboarding, fraud screening, and disputed-event (e.g., detention) workflows, per [[01-client-briefs/freight-trust-client-master-brief#Proposed system]].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |     |
| First workflow       | **Carrier onboarding / identity verification** — resolved as the single Phase I beachhead, per [[nsf-sbir-sttr-process-and-readiness-guide#8. What can be done now, before an invitation]]'s instruction to "pick one testable workflow, not all of them." This is a **working default pending client confirmation**, chosen because it is best supported by current fraud evidence (TIA's 2025 fraud survey, 2025 CargoNet/Verisk theft data, FMCSA registration-fraud context) and aligns directly with Aim 1. Disputed facility-event (detention) evidence handling remains Aim 2's research validation context in Phase I (simulated/permissioned data) and is a Phase II expansion candidate, **not** a second Phase I beachhead — see [[phase-1-project-description-draft#6. Integration and bounded pilot]]. |     |
| Beneficiary/user     | [ROLE PLACEHOLDER — e.g., broker onboarding/compliance staff, carrier safety staff, or facility dock/dispute staff]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |     |
| Why this buyer first | Brokers and carrier networks sit at the point of highest documented friction: verification labor, fraud exposure, and disputed-event cost, and are named as a high-need, moderate-to-high-willingness stakeholder segment in [[01-client-briefs/freight-trust-client-master-brief#Stakeholders and pushback]].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |     |

## 2. Quantified pain (beachhead workflow)

| Pain dimension | Evidence available now | Status |
|---|---|---|
| Identity-verification/fraud exposure (primary beachhead pain — carrier onboarding/identity verification) | TIA's April 2025 "State of Fraud in the Industry" member survey: 83% of respondent brokerages experienced ≥3 distinct fraud types within six months; 22% lost more than $200,000 to fraud in the prior six months (secondary — industry member survey, standard industry-cited benchmark, per `sbir-evidence-refresh.md`). CargoNet/Verisk: an estimated $725 million in 2025 cargo-theft losses, up 60% year-over-year (secondary, per `sbir-evidence-refresh.md`). GAO-12-364 documented historical FMCSA coverage/resource constraints on identifying carriers evading detection through changed identities **[VERIFY: GAO citation not independently re-verified this pass — see Proposal Review Notes Blocking Finding #7]**; FMCSA's Motus registration system (broad launch May 2026) signals identity assurance as a live public-infrastructure priority. | Documented at the industry/regulatory level with 2025-current fraud-specific data; buyer-specific cost of fraud/onboarding friction is not yet quantified. |
| Detention-related cost and hours (Aim 2 research-validation context — not the Phase I beachhead) | A widely repeated figure (39.3% of stops involved detention; 135.9 million lost hours; $3.6B direct expenses; $11.5B productivity losses for for-hire trucking) is attributed to "ATRI" but **[UNVERIFIED — SBIR Evidence Refresh found this figure may trace to an older ATRI detention study circa 2019–2020; do not attribute to "ATRI 2023" or any current year without primary-PDF confirmation]**. The separately-verified ATRI 2025 Operational Costs Update reports non-fuel marginal cost of $1.779/mile (highest ever recorded) and roughly 1.5–2 hours average dwell time per stop, figures vary by source [confirm exact dwell-time figure against the primary ATRI PDF; 1h38m vs. 1h49m discrepancy unresolved]. | Retained only as context for Aim 2's research-validation instance, not as a quantified beachhead-pain claim; still needs company-specific translation if the facility-event instance advances to Phase II. |
| Buyer-specific verification labor cost (hours, headcount, cost per onboarding event) | Not in the vault. | **[QUANTIFIED PAIN PLACEHOLDER — must come from discovery interviews, not estimated.]** |
| Buyer-specific disputed-event/detention resolution cost (time-to-resolution, dollar exposure per dispute) — Phase II expansion-candidate evidence, not the Phase I beachhead pain claim | Not in the vault at buyer-specific granularity. | **[QUANTIFIED PAIN PLACEHOLDER — retained for Phase II expansion planning only; not load-bearing for the Phase I beachhead's commercial case.]** |
| Legal/liability exposure context | *Montgomery v. Caribe Transport II, LLC* (14 May 2026): FAAAA does not preempt state-law negligent-selection claims against brokers under the safety exception; no universal reasonable-care standard was defined. [[01-client-briefs/freight-trust-client-master-brief#Why now]] | Relevant context for broker urgency; not a quantified pain figure and not a claim of legal safe-harbor value. |

The frequently repeated industry-wide annual freight-fraud cost figure is explicitly flagged in the master brief as contextual only, pending independent verification of its source methodology, and should **not** be used as a quantified pain claim in the proposal ([[01-client-briefs/freight-trust-client-master-brief#Boundaries]]).

## 3. Alternatives (by class, not by named competitor)

| Alternative class | What it does | Where it falls short relative to the beachhead workflow |
|---|---|---|
| Manual checks | Staff manually call, look up, or cross-reference registries/references during onboarding or dispute review. | Labor-intensive, inconsistent, no structured provenance or audit trail. |
| FMCSA URSA / historical chameleon-risk screening | FMCSA previously developed and deployed automated risk-based screening for likely chameleon/reincarnated applicants; the published lineage includes an earlier SBIR Phase I. | Establishes direct federal prior art. Freight Trust cannot claim first automated chameleon screening; differentiation must be provenance, layered identity/relationship semantics, contestability, and cross-party evidence architecture. |
| FMCSA Motus / registration identity + business verification | Motus uses individual identity verification and company/business verification in the current registration lifecycle. | Current public-sector incumbent for registration-stage verification; Freight Trust must complement rather than duplicate official registration identity proofing. |
| SCAC Verified / point-in-time identity assurance | NMFTA binds a verified natural-person identity to SCAC issuance and renewal for non-Class-8 carriers and exposes a checkable verified status. | Direct incumbent prior art that validates demand for identity assurance, but NMFTA explicitly does not guarantee fraud prevention; it is lifecycle-point verification rather than a continuously updated, provenance-bearing record joining identity to later operational events. |
| Point data providers | Single-source data feeds (e.g., a registry lookup or a safety-history pull) consumed independently. | Fragmented; no cross-source resolution, no unified provenance, no contestability mechanism. |
| Credit/fraud scoring tools | Proprietary risk or credit scores applied to a counterparty. | Often an opaque binary score; does not preserve source lineage, uncertainty, or a correction/appeal path — the specific gap this program targets per [[01-client-briefs/freight-trust-client-master-brief#Competitive and technical position]]. |
| Internal rules engines | Buyer-built if/then logic layered on internal and purchased data. | Brittle to novel fraud patterns, does not generalize across partners, and is not designed for cross-party evidence sharing. |
| [ADDITIONAL CLASS PLACEHOLDER — e.g., existing visibility/telematics platforms extending into verification] | [DESCRIPTION PLACEHOLDER] | [GAP PLACEHOLDER] |

Programme positioning is an explainable, cross-party evidence and provenance layer that complements these classes rather than replacing them; it is explicitly **not** another closed risk score or visibility portal ([[01-client-briefs/freight-trust-client-master-brief#Competitive and technical position]]).

## 4. Business-model hypotheses

| Hypothesis | Description | Status |
|---|---|---|
| Per-verification/transaction fee | Buyer pays per onboarding check or per event-provenance lookup. | Untested — [BUSINESS MODEL PLACEHOLDER, requires discovery validation]. |
| Subscription/platform access | Buyer pays recurring fee for ongoing access to the evidence graph and dispute-support tooling. | Untested — [BUSINESS MODEL PLACEHOLDER]. |
| Tiered access by fleet size / basic-access safeguard | A no/low-cost basic verification tier to avoid excluding small carriers, consistent with the equity concern in [[01-client-briefs/freight-trust-client-master-brief#Governance and redress]] ("Basic verification access should not become a pay-to-participate barrier for small carriers"). | Directional constraint, not a priced model yet — [PRICING FLOOR PLACEHOLDER]. |
| Data-contribution/reciprocal-value model | Partners who contribute event/identity evidence receive preferential access or reduced fees. | Aligned with the "reciprocal incentives" governance component in [[01-client-briefs/freight-trust-client-master-brief#Proposed system]]; untested — [MODEL DETAIL PLACEHOLDER]. |

## 5. Pricing hypothesis (placeholder)

**[PRICING HYPOTHESIS PLACEHOLDER — no pricing figure exists in the vault.]** Any specific per-check, per-seat, or subscription price must be derived from discovery-interview willingness-to-pay data and validated against buyer-segment economics (verification labor cost avoided, dispute-resolution cost avoided) before it appears in a submitted proposal. Do not substitute an assumed number.

## 6. Route to market

| Stage | Approach |
|---|---|
| Beachhead validation | Structured discovery interviews and pilot-interest conversations with [TARGET COUNT PLACEHOLDER — guide suggests 5–10 interviews and 2 written pilot-interest statements, per [[nsf-sbir-sttr-process-and-readiness-guide#3. Project Pitch: the required first submission]]] broker/carrier/facility contacts. |
| Bounded pilot | One carrier cohort, one broker/shipper cohort, one or two facilities, per the pilot roadmap in [[01-client-briefs/freight-trust-client-master-brief#Recommended pilot]] — measuring evidence quality and participant outcomes before any expansion. |
| Expansion gate | Pilot must pass predeclared thresholds (evidence quality, participation, equity) before expanding toward coordination/load-matching use cases ([[01-client-briefs/freight-trust-client-master-brief#Recommended pilot]]); load matching/market data is explicitly a later application, not a Phase I claim ([[01-client-briefs/freight-trust-client-master-brief#Competitive and technical position]]). |
| Channel | [CHANNEL PLACEHOLDER — direct sales to brokers/carriers, partnership with existing platform, association/standards-body introduction (e.g., via ASTM F49/NMFTA alignment)]. |

## 7. Competition and differentiation

- **Competitive frame**: explicitly name **FMCSA URSA**, **FMCSA Motus**, and **NMFTA SCAC Verified** as directly relevant prior art. The proposal must not imply that automated chameleon screening, registration-stage identity/business verification, or lifecycle-point identity verification is novel.
- **Differentiation claim**: an explainable, source-attributed, contestable evidence layer — preserving provenance, confidence, and a correction/appeal path — rather than an opaque score or a closed visibility portal. This is the same differentiation the technical Innovation section must substantiate (see [[technical-risk-register]] and [[nsf-sbir-sttr-process-and-readiness-guide#5. Full Phase I proposal: build around proof, not aspiration]]).
- **Standards alignment**: positioning aligns with, rather than competes against, ASTM F49 terminology and NMFTA freight interfaces where applicable ([[01-client-briefs/freight-trust-client-master-brief#Competitive and technical position]]), which may support go-to-market credibility with associations/standards bodies.
- **Non-claims**: this is not a universal risk score, not a legal-compliance certification, and not a claim of automatic fraud/detention/empty-mile reduction ([[01-client-briefs/freight-trust-client-master-brief#Boundaries]]) — commercialization messaging must not overstate beyond what Phase I can prove.

## 8. Financing path

| Stage | Hypothesis |
|---|---|
| Phase I (this award) | Up to $305,000, 6–18 months (this draft assumes 12), funds feasibility proof, not commercial scale-up (NSF 26-510; [[nsf-sbir-sttr-process-and-readiness-guide]]). |
| Bridge / non-dilutive | [PLACEHOLDER — e.g., state matching programs or other federal non-dilutive funding]. Note: Technical and Business Assistance (TABA, up to $6,500) is **part of the Phase I award itself**, budgeted inside the $305,000 base (see [[phase-1-budget-and-justification-draft#Technical and Business Assistance (TABA) — budgeted inside the $305,000 base]]) — it is not a separate bridge-financing stage and should not be counted as additional non-dilutive capital beyond Phase I. |
| Phase II | NSF Phase II decision typically considered 6–24 months after Phase I start, per the process map in [[nsf-sbir-sttr-process-and-readiness-guide]]; contingent on Phase I technical results and pilot/commercial evidence. |
| Private financing | [FINANCING PLAN PLACEHOLDER — no committed investor, round, or valuation exists in the vault; do not assert one]. |

## 9. Commercial evidence still required

- [ ] Structured discovery interviews (target count per the guide: 5–10) with named beachhead-segment contacts, recorded per the interview-record process in [[data-management-plan-draft]]. Reconcile this count with [[project-pitch-draft#Facts required before submission]]'s note that "G9's 'four exploratory interviews'" status should be confirmed and reconciled with the count used here — the two documents must not end up citing different interview counts.
- [ ] Written, credible, nonbinding pilot-interest statements (target: at least 2), from real named organizations willing to be cited, not vague endorsements ([[nsf-sbir-sttr-process-and-readiness-guide#8. What can be done now, before an invitation]]).
- [ ] Buyer-specific quantified pain figures (verification labor cost, dispute/detention resolution cost/time) replacing the current placeholders in Section 2.
- [ ] Willingness-to-pay / pricing signal from discovery interviews, to replace the Section 5 placeholder.
- [ ] Named-competitor / adjacent-platform competitive analysis, if not already produced under the market/standards workstream (G4–G6) referenced in [[01-client-briefs/freight-trust-client-master-brief#Dataset and experiment backbone]].
- [ ] Client confirmation of the first beachhead workflow — Section 1 currently sets carrier onboarding/identity verification as a **working default** chosen by internal review, not yet confirmed directly with the client.
- [ ] Any channel-partner or association conversations (e.g., ASTM F49/NMFTA engagement) actually underway, if to be cited.

## Related notes

- [[nsf-sbir-sttr-process-and-readiness-guide]]
- [[01-client-briefs/freight-trust-client-master-brief]]
- [[phase-1-budget-and-justification-draft]]
- [[data-management-plan-draft]]
- [[technical-risk-register]]
- [[04-sbir/sbir-moc]]
