---
type: evidence
status: current
schema_version: 1.0.0
updated: 2026-08-08
confidence_default: mixed
tags:
- type/evidence
- domain/identity
- domain/regulatory
- confidence/mixed
- audience/internal
- programme/e1
- lifecycle/current
---
# E1 identity claims ledger

Claim-level ledger supporting [[e1-carrier-identity-and-relationship-standard]]. Source IDs resolve through [[e1-identity-definition-research-report]]. “Normative consequence” is an E1 design decision derived from the cited claim; it is not represented as law unless the source itself is law/regulation.

| Claim | Sourced proposition | Source | Authority | Confidence | Normative consequence for E1 |
|---|---|---|---|---|---|
| ID-R-001 | 49 U.S.C. §13902 registers a **person** as a motor carrier and requires a USDOT number. | S04 | statute | high | Primary entity target is a person/legal person, not brand or address. |
| ID-R-002 | §13902 separately requires disclosure of common ownership/management/control/familial relationships with other carriers/applicants. | S04 | statute | high | Relationship is not identity equivalence. |
| ID-R-003 | §31134 registers an employer/person and requires a USDOT number for interstate CMV operations. | S04 | statute | high | FMCSA registrant and USDOT assignment are explicit objects. |
| ID-R-004 | §31134 separately addresses relationships through common ownership/management/control/family. | S04 | statute | high | Preserve related distinct persons. |
| ID-R-005 | §31135 prohibits two or more persons/carriers from using common ownership/management/control/family to avoid or conceal noncompliance. | S04 | statute | high | Common control can connect multiple persons; it does not merge them. |
| ID-R-006 | 49 CFR §390.5 defines “person” to include individuals and business organizations. | S05 | regulation | high | `LegalPerson` includes natural and organizational persons where relevant. |
| ID-R-007 | §390.5's “motor carrier” definition can include agents/officers/representatives/certain employees in its subchapter. | S05 | regulation | high | Do not use unscoped `MotorCarrier` as identity-equivalence class. |
| ID-R-008 | §390.5 separately defines operating authority as registration under specified authorities. | S05 | regulation | high | OA is not the entity. |
| ID-R-009 | FMCSA's 2026 bulletin says a USDOT number belongs to the same legal person and is nontransferable. | S03 | current agency guidance | high | Authoritative assignment is a strong identity anchor. |
| ID-R-010 | A corporation may change owners while the corporation and USDOT remain the same. | S03 | current agency guidance | high | Ownership change does not imply new identity. |
| ID-R-011 | If a corporation dissolves and operations continue under another/new company, the continuing company needs its own USDOT. | S03 | current agency guidance | high | Operational continuity does not itself preserve legal-person/USDOT identity. |
| ID-R-012 | A sole proprietor's buyer needs a different USDOT because the natural person cannot be transferred. | S03 | current agency guidance | high | Asset/business sale is not legal-person identity. |
| ID-R-013 | FMCSA's published form-change FAQ permits a sole proprietor to keep USDOT continuity in a narrow virtually-identical-operation conversion. | S03 | agency policy | high | Separate legal-person identity from FMCSA registrant continuity. |
| ID-R-014 | New entities ordinarily obtain their own operating authority, but whole-operation corporate transactions can support OA transfer. | S03 | current agency guidance | high | OA identifier/transfer cannot be a same-person key. |
| ID-R-015 | FMCSA can inactivate USDOT use by someone other than the assigned legal person. | S03 | current agency guidance | high | Distinguish `CLAIMS_USDOT` from `USDOT_ASSIGNED_TO`. |
| ID-R-016 | §386.73 defines reincarnation by substantial continuity such that one entity is a continuation of another. | S01 | regulation | high | Continuity relation is separate from legal-person equality. |
| ID-R-017 | §386.73 defines affiliation by common ownership and/or common control of business operations. | S01 | regulation | high | `AFFILIATED_WITH` is a relationship, not identity. |
| ID-R-018 | §386.73 lists motive/business purpose among the factors considered. | S01 | regulation | high | Motive belongs only in regulatory-disposition layer. |
| ID-R-019 | §386.73 lists previous safety history among factors considered. | S01 | regulation | high | Safety history is not Task A identity ground truth. |
| ID-R-020 | §386.73 lists creation/dissolution dates. | S01 | regulation | high | Time and corporate lifecycle must be represented. |
| ID-R-021 | §386.73 lists common ownership and management. | S01 | regulation | high | Graph edge features are plausible, but not identity dispositive. |
| ID-R-022 | §386.73 lists shared addresses/contact details. | S01 | regulation | high | Address/phone/email are evidence, not keys. |
| ID-R-023 | §386.73 lists equipment continuity. | S01 | regulation | high | Equipment edges require time/provenance. |
| ID-R-024 | §386.73 lists insurance continuity. | S01 | regulation | high | Insurance is relationship evidence, not identity. |
| ID-R-025 | §386.73 lists employees/drivers/facilities/operations/customers/name/advertising. | S01 | regulation | high | Multi-relational evidence may support continuity; no single field proves sameness. |
| ID-R-026 | §386.73 allows FMCSA to consolidate records of current/affiliated/previous entities. | S01 | regulation | high | Record consolidation is an agency event, not node collapse. |
| ID-R-027 | §386.73 orders have service, review, stay, finality, and rescission states. | S01 | regulation | high | Regulatory labels need procedural status and time. |
| ID-R-028 | The 2012 rule preamble says legitimately separate commonly owned fleets may share many factors. | S02 | regulatory preamble | high | Shared relationships cannot force identity/reincarnation. |
| ID-R-029 | The preamble says legitimate business changes not undertaken to evade FMCSA are not the target. | S02 | regulatory preamble | high | Corporate transaction semantics need non-fraud outcomes. |
| ID-R-030 | The preamble says all relevant information is considered and no one factor/source is necessarily more significant. | S02 | regulatory preamble | high | Do not encode a fake FMCSA universal field-weighting rule. |
| ID-R-031 | GAO states data matching alone cannot positively identify a chameleon carrier. | S06 | GAO | high | Candidate generation is not adjudication. |
| ID-R-032 | GAO gives legitimate vehicle purchase and same-name coincidence as false-link examples. | S06 | GAO | high | Hard negatives must include legitimate overlap. |
| ID-R-033 | GAO required both a record match and a defined motive for its “chameleon attributes” screen. | S06 | GAO | high | Historical screening target differs from legal-person identity. |
| ID-R-034 | GAO's address field produced orders of magnitude more pair matches than strong numeric IDs. | S06 | GAO | high | Shared-address bias must be explicitly stress-tested. |
| ID-R-035 | GAO says further investigation/legal process is needed to confirm chameleon status. | S06 | GAO | high | Do not label analytical candidates as confirmed reincarnation. |
| ID-R-036 | FMCSA ARCHI used a match score plus motive score. | S07 | FMCSA report | high | Match+motive is prior art, not E1 novelty. |
| ID-R-037 | ARCHI's published report lacks precision/recall/FPR/labeled ground truth. | S07 | FMCSA report | high | Published evaluation/benchmark gap remains plausible. |
| ID-R-038 | FMCSA reports an earlier SBIR Phase I studying automated high-risk/reincarnated-carrier identification. | S08 | FMCSA | high | E1 cannot claim first SBIR on automated chameleon screening. |
| ID-R-039 | FMCSA reports URSA algorithm/software performed automatic chameleon/reincarnation risk assessment. | S08 | FMCSA | high | Automated risk screening is established prior art. |
| ID-R-040 | FMCSA reports URSA integration into URS-1 in 2016. | S08 | FMCSA | high | Proposal must acknowledge implementation prior art. |
| ID-R-041 | eFOTM says address/phone/owner overlap can be first indications of possible reincarnation/affiliation. | S09 | FMCSA operational manual | high | These are candidate-generation signals. |
| ID-R-042 | eFOTM directs investigators to focus on operational control and §386.73(c), gather evidence, and coordinate with counsel. | S09 | FMCSA operational manual | high | Automated output is not a substitute for legal determination. |
| ID-R-043 | eFOTM characterizes screening as a wide-net tool whose results require analysis. | S09 | FMCSA operational manual | high | E1 requires abstention/review and error analysis. |
| ID-R-044 | Motus gives each individual a user profile and allows one user to access multiple company accounts. | S10 | current FMCSA system | high | `HumanActor` != `CompanyAccount` != `LegalPerson`. |
| ID-R-045 | Motus company accounts require business information/verification and manage registrations/users. | S10 | current FMCSA system | high | Business-account verification is separate from longitudinal legal-entity resolution. |
| ID-R-046 | Motus uses identity verification/business-address validation as current anti-fraud controls. | S10 | current FMCSA system | high | Point-of-registration verification is not E1 novelty. |
| ID-R-047 | NMFTA SCAC Verified binds verified individual identity at SCAC issuance/renewal for its stated population. | S11 | industry primary | high | Trade-identifier identity verification is current prior art. |
| ID-R-048 | NMFTA says SCAC Verified does not guarantee fraud prevention. | S11 | industry primary | high | Point-in-time credential verification != longitudinal trust record. |
| ID-R-049 | GLEIF separates Level 1 legal-entity “who is who” from Level 2 “who owns whom.” | S12 | standards analogue | high for analogue | External architecture check supports separate identity/relationship layers. |
| ID-R-050 | Gupta et al. used two independent reviewers and a third adjudicator; reviewer discordance affected gold standards. | S13 | peer reviewed | high | Multi-reviewer adjudication and disagreement preservation required. |
| ID-R-051 | NIST frames identity resolution as unique resolution in a defined population/context. | S14 | standards analogue | high for analogue | E1 labels need declared context and as-of time. |
| ID-R-052 | NIST distinguishes self-asserted attributes from evidence traceable to issuing sources and recommends additional evidence for conflicts. | S14 | standards analogue | high for analogue | Preserve claims/provenance; conflicts can remain unresolved. |
| ID-R-053 | State corporate status and FMCSA registration status answer different predicates. | S01/S03/S04 | synthesis | high | Do not interpret “active” across systems as one field. |
| ID-R-054 | Retrospective evidence can resolve gold truth while being unavailable at prediction time. | S01/S09 | methodological synthesis | high | Gold evidence and model-visible feature views require separate cutoffs. |
| ID-R-055 | No authoritative source found creates a universal numeric threshold for “substantial continuity.” | S01/S02/S09 | confirmed negative within reviewed sources | medium-high | Do not invent a pseudo-legal threshold; use documented adjudication rubric. |
| ID-R-056 | No reviewed authority says a common address, common owner, or same equipment by itself establishes legal-person identity. | S01/S02/S06/S09 | confirmed negative within reviewed sources | high | Single-field automatic merges prohibited. |
| ID-R-057 | A final FMCSA disposition can concern distinct current, affiliated, and previous entities whose records are consolidated. | S01 | regulation | high | Preserve entities even after agency record consolidation. |
| ID-R-058 | The benchmark's most defensible reusable output is legal-person clusters plus typed relationship edges, not a single chameleon yes/no label. | S01-S14 | synthesis | high | Adopt multi-layer corpus schema. |
| ID-R-059 | The CMAK/Chazon final order states the §386.73 factors are guides and no single factor is dispositive; similarities do not necessarily establish reincarnation/affiliation. | S15 | final agency adjudication | high | Do not encode any single continuity factor as a legal/dispositive merge rule. |
| ID-R-060 | The CMAK/Chazon decision required a preponderance showing of reincarnation/affiliation plus improper purpose and ended as a Final Agency Order. | S15 | final agency adjudication | high | `REINCARNATION_CONFIRMED` requires status-bearing authoritative disposition, not model similarity. |
| ID-R-061 | The order explains that simultaneous operation may support affiliation until one carrier ceases, after which continuation can support a reincarnation analysis. | S15 | final agency adjudication | high | Relationship labels must be time-indexed; a pair can change relationship state without becoming one legal person. |
| ID-R-062 | Louisiana SOS exposes official business search by entity name, charter/trade-registration/name-reservation number, and officer/agent. | S16 | state primary | high | Louisiana cases can use an official state identifier/evidence path rather than vendor identity. |
| ID-R-063 | Texas SOSDirect provides official entity search, filing history, status information, and document/certificate access with per-search/document mechanics and fees. | S16 | state primary | high | State-record acquisition cost/access must be tracked and cannot be assumed free/bulk. |
| ID-R-064 | Texas Comptroller Franchise Tax Account Status describes the right to transact business and explicitly distinguishes Secretary-of-State filings used for entity-file actions. | S16 | state primary | high | Tax/right-to-transact status is a separate predicate and cannot silently stand in for legal formation/existence/transaction history. |
