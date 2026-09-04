---
type: draft
status: draft
owner: PI + grant lead
authority: NSF 26-510
schema_version: 1.0.0
deliverable: NSF Project Pitch
updated: 2026-08-18
tags:
- type/draft
- domain/freight
- domain/identity
- domain/provenance
- domain/federation
- confidence/mixed
- audience/reviewer
- lifecycle/draft
---
# NSF Project Pitch — Draft

*Working draft, not submission-ready. Every bracketed placeholder — `[like this]` — is a fact the company must supply, confirm, or authorize in writing before this pitch can be submitted through Research.gov. Do not submit with any bracket unresolved. Character limits below are NSF's stated Project Pitch limits per the [[04-sbir/nsf-sbir-sttr-process-and-readiness-guide]], §3: Technology Innovation 3,500 characters; Technical Objectives and Challenges 3,500 characters; Market Opportunity 1,750 characters; Company and Team 1,750 characters. Each field below is followed by an italicized, measured character count (not an estimate) confirming it fits under the NSF limit with headroom. Prose is written as flowing paragraphs, with no bullet lists, consistent with how the Project Pitch fields are rendered and reviewed.*

---

## 1. Technology Innovation

*(limit 3,500 characters)*

Freight transactions depend on evidence scattered across carriers, brokers, facilities, insurers, telematics providers, and public registrations, each holding a partial record of who a counterparty is and what happened. Existing verification and risk tools often compress that fragmentation into a score or alert rather than a source-attributed, contestable evidence record. The problem is not simply unverified identity: FMCSA already has substantial prior art, including automated chameleon/reincarnation risk screening through URSA and, in 2026, Motus identity and business verification; NMFTA also operates SCAC Verified. The unresolved engineering question is whether identity can be reconstructed coherently over time when authoritative anchors are missing, stale, conflicting, or fraudulently claimed, while preserving the distinction between the same legal person and a merely related, successor, affiliated, or operationally continuous entity. In parallel, a 2026 U.S. Supreme Court ruling clarified that state-law negligent-selection claims against brokers are not preempted by federal law while leaving the evidentiary standard for reasonable carrier-selection care undefined, increasing the value of traceable rather than bare-score verification evidence.

This project will research and prototype a federated, provenance-preserving evidence graph for freight identity resolution and facility-event verification. The R&D integrates three elements that existing point solutions do not publicly combine: (1) calibrated, abstention-capable legal-person resolution across incomplete and conflicting records, with FMCSA registrant continuity, identifier assignment/use, corporate relationships, and regulatory dispositions represented separately rather than collapsed into “same carrier”; (2) event assertions carrying source, time, submitting party, permission, and correction history so a claim can be independently assessed; and (3) policy-enforced federation, in which source systems remain authoritative and data owners retain raw records while exposing only purpose-limited evidence. Every consequential output must be contestable and correction-aware.

The innovation is this evaluated decision substrate, not first-of-kind carrier screening, a dashboard, or another data-integration layer. It builds on FMCSA/GAO screening prior art, current Motus/SCAC identity assurance, GLEIF’s separation of entity identity from ownership relationships, record-linkage methods, supply-chain knowledge graphs, and NIST traceability/access-control work. Phase I asks whether these ingredients can be integrated into a coherent freight evidence system whose identity layer remains accurate under degraded identifiers, whose relational graph does not falsely merge distinct companies, and whose uncertainty, provenance, access, and redress behavior can be measured against explicit failure conditions.

*Character count: 2,903 / 3,500 (82.9% of limit; 17.1% headroom).*

---

## 2. Technical Objectives and Challenges

*(limit 3,500 characters)*

Phase I will test four linked technical hypotheses against defined baselines. For Aim 1, the baseline is the current manual/rules workflow plus deterministic field matching; FMCSA URSA/Motus and NMFTA SCAC Verified are treated as prior art/comparators where their publicly documented scope permits, not as straw men.

First, can the system assign fragmented carrier observations to the correct legal person under missing, corrupted, conflicting, or fraudulently claimed identifiers with calibrated uncertainty, without falsely merging affiliated, successor, or operationally continuous but legally distinct entities? The adjudicated reference corpus will use canonical legal-person clusters plus separate FMCSA identifier/registrant-continuity and typed relationship labels. Two independent reviewers will label hard cases, a third will adjudicate disagreements, and UNRESOLVED is valid. All methods will be tested under anchor-visible control, anchor-masked, anchor-missing, anchor-corrupted, claimed-vs-assigned conflict, cross-registration, and time-forward regimes. Success is hierarchical: the selected method's design-weighted automatic-assignment precision lower bound must first meet a preregistered safety floor; only then may its paired yield gain over transparent deterministic rules exceed a preregistered minimum at the same review budget. LINK_EXISTING and CREATE_NEW harms, calibration, abstention, cluster consistency and subgroup slices are reported separately.

Second, can facility-event assertions carry independently assessable provenance, and can preregistered injected omissions, sequence anomalies and contradictions be detected while dwell uncertainty is represented honestly? Success is measured against hidden synthetic truth and transparent baselines; it is not malicious-tamper attribution or real-facility validation.

Third, can an authenticated policy-enforcement point apply an approved partner/field/purpose policy without centralizing raw commercial data? Success requires zero frozen high-severity false allows, legitimate critical workflows to pass or route to declared review, and independent reconciliation of every received attempt—including authentication failures and engine errors—with its audit record. This is pinned-policy conformance, not legal compliance.

Fourth, can a challenged record be corrected or annotated with that correction visibly propagating to downstream context, while avoiding a system that improves aggregate detection by imposing disproportionate false-positive or review burden on legitimate small carriers? Success requires a measurable correction path plus subgroup guardrails.

A method fails if it cannot beat the relevant baseline at matched error cost, if calibration/abstention is unusable, if graph context creates related-entity false merges, if policy tests leak disallowed evidence, or if subgroup harms remain material and unexplained.

*Character count: 2,925 / 3,500 (83.6% of limit; 16.4% headroom).*

---

## 3. Market Opportunity

*(limit 1,750 characters)*

The Phase I beachhead is carrier onboarding and identity verification — a working default pending client confirmation, best supported by current fraud evidence (TIA's 2025 fraud survey; 2025 CargoNet theft data) and aligned with Aim 1. The initial buyer hypothesis is [buyer segment — e.g., freight brokers and/or carrier-onboarding teams; confirm via discovery] who bear direct cost from unreliable counterparty verification, sharpened by a 2026 U.S. Supreme Court ruling holding that state-law negligent-selection claims against brokers are not preempted by federal law, while leaving no defined evidentiary standard for reasonable carrier-selection care. Disputed facility-event evidence remains Aim 2's research context in Phase I, not a second commercial beachhead.

Current alternatives are manual reference checks, proprietary risk-scoring products, and vendor-authored vetting frameworks, none built on attributable, cross-party evidence with correction and appeal designed in; no publicly disclosed competitor claims an entity-resolution or evidence-graph architecture comparable to the one proposed here. The commercial thesis is that reducing avoidable verification labor and costly misclassification, while producing evidence defensible in a dispute, creates value a closed score cannot.

Before submission this beachhead will be validated with [N — target five to ten] structured discovery interviews across brokers, carriers, and facility contacts, and [M] written, nonbinding pilot-interest statements from named organizations. [Insert current interview/pilot-letter status and count.]

Arkansas's documented research network supplies discovery routes, not evidence of demand, access, endorsement, or partnership.

*Character count: 1,731 / 1,750 (98.9% of limit; 1.1% headroom).*

---

## 4. Company and Team

*(limit 1,750 characters)*

BellHill is the intended applicant for this Project Pitch; its exact registered name, legal form, ownership, affiliate status and SBIR/STTR eligibility require documentary confirmation before submission. Russell Berry is the working Principal Investigator and Research & Knowledge Architecture Lead, responsible for technical direction, evidence and ontology architecture, provenance/source governance, benchmark specification support, and technical/proposal synthesis. His résumé, majority-employment compliance, project effort, work authorization, compensation and research-security evidence remain open. [OPEN: name/role for data, security, and entity-resolution engineering where duties do not duplicate the PI's scope — owner: BellHill/PI.] [OPEN: product/commercial lead, if distinct — owner: BellHill/PI.] [Optional named partner] contributes [defined capability] only under documented terms; no partnership is represented here beyond a written commitment. Access to [specific lawful evaluation data or environment] must likewise be documented before submission.

*Character count: 1,069 / 1,750 (61.1% of limit; 38.9% headroom).*

---

## Facts required before submission

Every bracket above must be resolved with a real, verifiable fact — never filled with a plausible-sounding guess. This table lists each placeholder, which field it lives in, and who is accountable for supplying it.

| Placeholder | Field | What is needed | Who must supply it |
|---|---|---|---|
| Registered legal name / legal form | Company and Team | BellHill is the intended applicant; verify exact registered name, entity type, ownership/affiliates and eligibility in SAM.gov/Research.gov | BellHill / counsel |
| PI title/background and employment/effort eligibility | Company and Team | Russell Berry is the working PI and architecture lead; supply résumé, ≥51% employment evidence, compliant project effort, work authorization, compensation and research-security review | BellHill + Russell Berry |
| Data/security/entity-resolution lead (name/role) | Company and Team | Named person, real role and qualifications; include only if duties do not duplicate Russell Berry's PI/architecture scope | BellHill / PI |
| Freight-domain/commercial lead (name/role) | Company and Team | Named person, real role, real qualifications | CEO / PI |
| Named partner and defined capability | Company and Team | Only include if a partner has actually committed in writing (consultant or subcontract terms); omit entirely if not yet real | PI + partner lead / counsel |
| Specific dataset/partner/permission for Phase I benchmarking | Company and Team | Description of lawfully obtainable evaluation data and who authorized its use | Product/data lead + counsel |
| Buyer segment (brokers vs. carrier-onboarding teams vs. other), within the carrier onboarding/identity-verification beachhead | Market Opportunity | Confirmed first-buyer hypothesis from actual discovery, not assumption; the beachhead workflow itself (carrier onboarding/identity verification) is a working default pending client confirmation | Commercial lead |
| Interview count (N) | Market Opportunity | Actual number of structured discovery interviews completed (guide recommends five to ten before submission); status of G9's "four exploratory interviews" should be confirmed and reconciled with this count | Commercial lead |
| Pilot-interest statement count (M) and named organizations | Market Opportunity | Actual number of written, nonbinding pilot-interest statements obtained, and from whom | Commercial lead + counsel |
| Interview/pilot-letter status narrative | Market Opportunity | One sentence stating what has been done to date vs. what remains before submission | Commercial lead |
| Baseline point-solution comparators | Technical Objectives and Challenges | Names of specific existing tools/workflows to benchmark against, once data access allows a fair comparison | PI + technical lead |

## Reviewer self-check

NSF's Project Pitch screening maps to the same three review criteria used at full proposal — Intellectual Merit, Broader Impacts, Commercial Potential — plus a threshold check on whether the submission describes high-risk R&D rather than a product pitch. Use this table to confirm each field answers its intended screening question before submission.

| Field | Primary NSF screening question it must answer | Where the draft answers it |
|---|---|---|
| Technology Innovation | Is this a scientific/engineering innovation, and why are existing methods inadequate? | Names the three-part technical combination (calibrated resolution, provenanced events, policy-enforced federation) and explains why closed scoring tools and a struggling federal registration system leave this unsolved. |
| Technical Objectives and Challenges | Are the unknowns, hypotheses, measurable objectives, and technical risks clear and falsifiable? | States four testable hypotheses, each with a named risk and a measurable, baseline-relative success criterion. |
| Market Opportunity | Who is the first buyer, what is the unmet pain, what are the alternatives, and how will the beachhead be validated? | Names a buyer hypothesis tied to a dated legal driver, states the alternatives and why they fall short, and commits to a specific (bracketed) discovery and pilot-letter validation plan. |
| Company and Team | Can this specific company and team execute the R&D and carry it toward commercialization? | Structures PI, technical, and commercial roles and data access as named commitments — currently placeholders pending real facts, deliberately not fabricated. |
