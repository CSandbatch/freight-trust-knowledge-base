---
type: pitch-draft
status: draft
authority: NSF 26-510
tags:
  - nsf
  - sbir
  - project-pitch
---

# NSF Project Pitch — Draft

*Working draft, not submission-ready. Every bracketed placeholder — `[like this]` — is a fact the company must supply, confirm, or authorize in writing before this pitch can be submitted through Research.gov. Do not submit with any bracket unresolved. Character limits below are NSF's stated Project Pitch limits per the [[04 SBIR/NSF SBIR STTR Process and Readiness Guide]], §3: Technology Innovation 3,500 characters; Technical Objectives and Challenges 3,500 characters; Market Opportunity 1,750 characters; Company and Team 1,750 characters. Each field below is followed by an italicized, measured character count (not an estimate) confirming it fits under the NSF limit with headroom. Prose is written as flowing paragraphs, with no bullet lists, consistent with how the Project Pitch fields are actually rendered and reviewed.*

---

## 1. Technology Innovation

*(limit 3,500 characters)*

Freight transactions depend on evidence scattered across carriers, brokers, facilities, insurers, telematics providers, and public registrations, each holding its own partial, differently-trusted record of who a counterparty is and what actually happened at a facility. Existing verification and risk tools compress this fragmentation into a single score or alert that tells a user what to conclude but not why: what evidence the conclusion rests on, how confident it is, or how a wrong conclusion can be corrected. That opacity is increasingly consequential. FMCSA's own 2026 registration-modernization rollout has encountered publicly documented identity-verification and login failures, illustrating that entity resolution in freight remains an unsolved engineering problem even for a well-resourced federal system, not simply a business-process gap a better interface could close. In parallel, a 2026 U.S. Supreme Court ruling clarified that state-law negligent-selection claims against brokers are not preempted by federal law, while leaving no defined evidentiary standard for what reasonable carrier-selection care requires — creating direct demand for verification evidence that is traceable and defensible rather than a bare score.

This project will research and prototype a federated, provenance-preserving evidence graph for freight identity resolution and facility-event verification. The R&D integrates three elements existing point solutions do not combine: (1) calibrated entity resolution across incomplete, conflicting, and sometimes adversarially altered records, producing a confidence estimate rather than a binary match and abstaining when evidence is insufficient rather than forcing a decision; (2) event assertions carrying signed, source-attributed provenance — who observed a facility event, when, and under what permission — so a claim can be independently assessed rather than merely asserted; and (3) policy-enforced federation, in which source systems remain authoritative and data owners retain their raw records while the graph exposes only the permitted, purpose-limited evidence a given decision requires. Every output is designed to be contestable: a counterparty can challenge a claim, and the graph must represent the correction and its effect on downstream conclusions, not merely overwrite history.

The innovation is this decision substrate — not a dashboard or another data-integration layer. Publicly disclosed competitors in carrier and broker verification rely on proprietary, closed risk-scoring rather than attributable, cross-party evidence lineage; none claims a comparable entity-resolution or provenance-graph architecture. The technical premise draws on peer-reviewed work applying knowledge graphs to multi-hop supply-chain relationships and federated graph learning to privacy-preserving analysis, and is consistent with NIST's traceability meta-framework, which holds that defensible traceability requires trusted repositories, linked records, secure access, and event recording working together, not a graph database alone. Phase I will determine whether calibrated resolution, provenanced events, and governed federation can be made to work jointly under real data sparsity and conflicting evidence, at a reliability existing tools do not provide.

*Character count: 3,304 / 3,500 (94.4% of limit; 5.6% headroom).*

---

## 2. Technical Objectives and Challenges

*(limit 3,500 characters)*

Phase I will test four linked technical hypotheses, each with a falsifiable success criterion measured against a defined baseline rather than an aspirational claim. The baseline for comparison in every aim is the current manual/rules-based verification workflow and at least one concrete point-solution comparator — provisionally, a representative rules-based MC/DOT lookup workflow [additional specific point-solution comparators to be named once data access is confirmed] — so results show whether the proposed graph adds measurable value over existing practice, not only over an internal starting point.

First, can the system resolve freight-entity identities — carriers, brokers, and facilities — across incomplete and conflicting records with calibrated uncertainty, rather than a single opaque match score? The technical risk is that freight identity data is sparse, inconsistently formatted across sources, and occasionally subject to deliberate obfuscation, such as registration changes intended to shed an adverse safety or claims history. Success will be measured against a held-out, permissioned benchmark using precision, recall, and calibration error relative to the manual-review baseline, with abstention counted as a correct outcome when evidence is insufficient, and with error reported by segment — including small-fleet carriers — rather than only in aggregate.

Second, can facility-event claims relevant to detention and dispute questions — appointment, arrival, gate, dock, and departure events — be linked to independently assessable provenance, and can tampering or contradiction between sources be detected? The risk is that event sources vary in trustworthiness and availability and that adversarial or simply erroneous records can masquerade as legitimate ones. Success will be measured by provenance-coverage of decision-relevant assertions in the test corpus and by detection rate on a constructed set of simulated contradiction and tampering cases.

Third, can the graph enforce purpose- and partner-specific data-sharing policy so a participant sees only evidence it is permitted to see, without requiring raw commercial data to be centralized? The risk is that overly strict enforcement destroys the graph's value while overly loose enforcement reproduces the disclosure risk that currently deters participation. Success will be measured through automated tests confirming that disallowed partner, field, and purpose combinations are consistently denied and logged for audit.

Fourth, can outputs remain contestable — can a challenged record be corrected or annotated, with that correction propagating to downstream decision context within a defined, measurable time — while reducing harmful false positives across carrier segments rather than only improving an aggregate accuracy number? The cross-cutting risk is that improving detection can worsen outcomes for legitimate small carriers if uncertainty, segment-level error, and correction are not treated as first-class technical requirements. This project treats that tension as a primary research question to be measured, not an assumption or an afterthought addressed later.

*Character count: 3,163 / 3,500 (90.4% of limit; 9.6% headroom).*

---

## 3. Market Opportunity

*(limit 1,750 characters)*

The Phase I beachhead is carrier onboarding and identity verification — a working default pending client confirmation, best supported by current fraud evidence (TIA's 2025 fraud survey; 2025 CargoNet theft data) and aligned with Aim 1. The initial buyer hypothesis is [buyer segment — e.g., freight brokers and/or carrier-onboarding teams; confirm via discovery] who bear direct cost and legal exposure from unreliable counterparty verification, sharpened by a 2026 U.S. Supreme Court ruling holding that state-law negligent-selection claims against brokers are not preempted by federal law, while leaving no defined evidentiary standard for reasonable carrier-selection care. Disputed facility-event evidence remains Aim 2's research context in Phase I, not a second commercial beachhead.

Current alternatives are manual reference checks, proprietary risk-scoring products, and vendor-authored vetting frameworks, none built on attributable, cross-party evidence with correction and appeal designed in; no publicly disclosed competitor claims an entity-resolution or evidence-graph architecture comparable to the one proposed here. The commercial thesis is that reducing avoidable verification labor and costly misclassification, while producing evidence defensible in a dispute, creates value a closed score cannot.

Before submission this beachhead will be validated with [N — target five to ten] structured discovery interviews across brokers, carriers, and facility contacts, and [M] written, nonbinding pilot-interest statements from named organizations. [Insert current interview/pilot-letter status and count.]

*Character count: 1,619 / 1,750 (92.5% of limit; 7.5% headroom).*

---

## 4. Company and Team

*(limit 1,750 characters)*

[Company legal name] is a U.S. small business developing a federated evidence-and-provenance platform for freight identity and facility-event verification. [PI name, title, and relevant background] will serve as Principal Investigator, meeting NSF's required employment and effort commitment at the time of award. [Name/role] leads data, security, and entity-resolution engineering; [name/role] leads freight-domain and commercial strategy. [Optional named partner] contributes [defined capability — domain expertise, data access, or an evaluation environment] under [SBIR consultant or subcontract] terms; no partnership is represented here beyond what is committed in writing. The team's access to lawful evaluation data — [describe the specific dataset, partner, or permission that will support Phase I benchmarking] — will be confirmed and documented before submission, consistent with NSF's expectation that data rights are resolved rather than assumed. This Phase I award will fund the R&D needed to establish both technical feasibility and the commercial evidence required to pursue a Phase II-scale product and pilot expansion.

*Character count: 1,135 / 1,750 (64.9% of limit; 35.1% headroom — kept lean because most of this field is placeholder scaffolding; expand only with true, confirmed facts, not filler.)*

---

## Facts required before submission

Every bracket above must be resolved with a real, verifiable fact — never filled with a plausible-sounding guess. This table lists each placeholder, which field it lives in, and who is accountable for supplying it.

| Placeholder | Field | What is needed | Who must supply it |
|---|---|---|---|
| Company legal name | Company and Team | Exact legal name as it will appear in SAM.gov/Research.gov | CEO / counsel |
| PI name, title, background | Company and Team | Named individual who will meet NSF's 51%-employment PI rule at award; true, verifiable background | CEO + proposed PI |
| Data/security/entity-resolution lead (name/role) | Company and Team | Named person, real role, real qualifications | CEO / PI |
| Freight-domain/commercial lead (name/role) | Company and Team | Named person, real role, real qualifications | CEO / PI |
| Named partner and defined capability | Company and Team | Only include if a partner has actually committed in writing (consultant or subcontract terms); omit entirely if not yet real | PI + partner lead / counsel |
| Specific dataset/partner/permission for Phase I benchmarking | Company and Team | Description of lawfully obtainable evaluation data and who authorized its use | Product/data lead + counsel |
| Buyer segment (brokers vs. carrier-onboarding teams vs. other), within the carrier onboarding/identity-verification beachhead | Market Opportunity | Confirmed first-buyer hypothesis from actual discovery, not assumption; the beachhead workflow itself (carrier onboarding/identity verification) is a working default pending client confirmation | Commercial lead |
| Interview count (N) | Market Opportunity | Actual number of structured discovery interviews completed (guide recommends five to ten before submission); status of G9's "four exploratory interviews" should be confirmed and reconciled with this count | Commercial lead |
| Pilot-interest statement count (M) and named organizations | Market Opportunity | Actual number of written, nonbinding pilot-interest statements obtained, and from whom | Commercial lead + counsel |
| Interview/pilot-letter status narrative | Market Opportunity | One sentence stating what has been done to date vs. what remains before submission | Commercial lead |
| Baseline point-solution comparators | Technical Objectives and Challenges | Names of specific existing tools/workflows to benchmark against, once data access allows a fair comparison | PI + technical lead |

## Reviewer self-check

NSF's Project Pitch screening maps to the same three review criteria used at full proposal — Intellectual Merit, Broader Impacts, Commercial Potential — plus a threshold check on whether the submission describes genuine, high-risk R&D rather than a product pitch. Use this table to confirm each field answers its intended screening question before submission.

| Field | Primary NSF screening question it must answer | Where the draft answers it |
|---|---|---|
| Technology Innovation | Is this a scientific/engineering innovation, and why are existing methods inadequate? | Names the three-part technical combination (calibrated resolution, provenanced events, policy-enforced federation) and explains why closed scoring tools and a struggling federal registration system leave this unsolved. |
| Technical Objectives and Challenges | Are the unknowns, hypotheses, measurable objectives, and technical risks clear and falsifiable? | States four testable hypotheses, each with a named risk and a measurable, baseline-relative success criterion. |
| Market Opportunity | Who is the first buyer, what is the unmet pain, what are the alternatives, and how will the beachhead be validated? | Names a buyer hypothesis tied to a dated legal driver, states the alternatives and why they fall short, and commits to a specific (bracketed) discovery and pilot-letter validation plan. |
| Company and Team | Can this specific company and team execute the R&D and carry it toward commercialization? | Structures PI, technical, and commercial roles and data access as named commitments — currently placeholders pending real facts, deliberately not fabricated. |

