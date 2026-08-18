---
type: evidence
status: current
schema_version: 1.0.0
updated: 2026-08-18
confidence_default: mixed
tags:
- type/evidence
- domain/identity
- domain/regulatory
- domain/legal
- confidence/mixed
- audience/internal
- programme/e1
- lifecycle/current
---
# E1 identity-definition research report — Research Agent execution

## Mission

Establish, from current authoritative sources, an operational definition of carrier identity and carrier-to-carrier relationship states precise enough to support a blinded Freight Trust E1 entity-resolution benchmark. This pass intentionally does **not** optimize an ML model and does not choose definitions because they are easy to predict.

Research cut-off: **2026-08-08**.

Design-history provenance: the user-supplied August 8 design transcript is normalized and
fingerprinted in [[../06-team-memory/mem-ft-000001-e1-carrier-identity-design-transcript]].
It records the initial reasoning and requested review loop, but it is not an authority for
the determinations below; the source map and claims ledger control factual support.

## Result in one sentence

The research rejects a single binary concept of “same carrier.” E1 must separate **legal-person identity**, **FMCSA registration continuity**, **identifier assignment/use**, **operating authority**, **ownership/control and corporate transactions**, **operational continuity**, and **regulatory reincarnation/affiliate dispositions**.

## Research passes

### Pass A — controlling motor-carrier law, regulation, and current FMCSA practice

Retrieved and compared:

- 49 U.S.C. §§ 13902, 31134, 31135;
- 49 CFR §§ 386.73, 390.5, and 385.1003;
- the 2012 final-rule preamble for § 386.73;
- current FMCSA USDOT identity/transfer guidance;
- current FMCSA operating-authority transfer guidance;
- FMCSA's 2025 eFOTM reincarnated/affiliated-carrier investigative instructions;
- current Motus user/profile/business verification materials.

This pass established the legal/regulatory object distinctions and the time/status requirements.

### Pass B — historical detection methods, current prior art, and adjudication analogues

Retrieved and compared:

- GAO-12-364;
- FMCSA's ARCHI report already in the vault;
- FMCSA URSA, including the earlier SBIR Phase I history and URS-1 integration;
- NMFTA SCAC Verified already in the vault;
- GLEIF Level 1/Level 2 legal-entity relationship architecture;
- Gupta et al. 2024 on multi-reviewer record-linkage gold standards;
- NIST SP 800-63A implementation material as a non-organizational identity-resolution analogue.

This pass established the candidate-generation/adjudication split, reviewer protocol, and novelty constraints.

### Pass C — adjudicative application and state-source operationalization

Retrieved and compared:

- the FMCSA-2015-0170 CMAK Logistics / Chazon Enterprises final §386.73 order;
- current Louisiana Secretary of State official business-search access;
- current Texas Secretary of State SOSDirect business-search/filing-history access; and
- current Texas Comptroller Franchise Tax Account Status guidance.

This pass tested whether the proposed identity/relationship separation survives an actual final FMCSA decision and whether the state-law source-of-truth rule can be implemented against real official registries. It did. It also disproved any assumption that state corporate evidence can be acquired nationally through one uniform interface.

### Saturation judgment

For the **definition layer**, the pass is provisionally saturated: the second pass changed evidence weighting, novelty, and adjudication controls but did not require another core equivalence class after the separation of `LegalPerson`, `FMCSARegistration`, `RegulatoryIdentifier`, `OperatingAuthority`, `HumanActor`, and relationship/disposition layers.

It is **not** saturated for all state-by-state corporate evidence acquisition. A Louisiana/Texas pilot now verifies the acquisition principle and exposes real access/cost differences, but additional jurisdictions must still be researched as benchmark cases are sampled. E1 v1.0 therefore freezes the source-of-truth semantics without pretending there is one national corporate-registry interface.

## Source map

| ID | Source | Class | Retrieved | What it controls |
|---|---|---|---|---|
| S01 | [[source-ecfr-386-73-reincarnated-carrier-standard]] | current regulation | confirmed | reincarnation, affiliation, factors, order status |
| S02 | [[source-federal-register-2012-reincarnated-carrier-rule-preamble]] | final-rule preamble | confirmed | totality, legitimate business changes, no single-factor shortcut |
| S03 | [[source-fmcsa-usdot-and-operating-authority-identity-guidance]] | current agency guidance | confirmed | USDOT legal-person continuity, sole-proprietor exception, OA transfer |
| S04 | [[source-us-code-motor-carrier-registration-relationship-disclosure]] | current statute | confirmed | registered person versus ownership/control/family relationships |
| S05 | [[source-ecfr-390-5-and-385-1003-identity-definitions]] | current regulation | confirmed | person/carrier/OA vocabulary and scope traps |
| S06 | [[source-gao-12-364-chameleon-carrier-matching]] | GAO | confirmed | matching as targeting; further investigation needed; weak-field collisions |
| S07 | [[source-fmcsa-chameleon-carrier-vetting-report]] | FMCSA | confirmed | ARCHI match + motive prior art |
| S08 | [[source-fmcsa-ursa-risk-screening-prior-art]] | FMCSA | confirmed | prior SBIR / automated chameleon-risk screening |
| S09 | [[source-fmcsa-efotm-reincarnated-carrier-investigation]] | FMCSA operational manual | confirmed | wide-net screening, chronology, counsel/evidence review |
| S10 | [[source-fmcsa-motus-identity-and-business-verification]] | current FMCSA system | confirmed | person profile, company account, business verification distinctions |
| S11 | [[source-nmfta-scac-verified-and-standards-role]] | industry primary | confirmed | SCAC/point-in-time person verification prior art |
| S12 | [[source-gleif-legal-entity-and-relationship-model]] | standards analogue | confirmed | “who is who” separated from “who owns whom” |
| S13 | [[source-gupta-2024-manual-record-linkage-gold-standard]] | peer reviewed | confirmed | two reviewers + third adjudicator; disagreement sensitivity |
| S14 | [[source-nist-800-63a-identity-resolution-analogue]] | standards analogue | confirmed | context, minimum evidence, source validation, conflict resolution |
| S15 | [[source-fmcsa-cmak-chazon-final-order-2015]] | final agency adjudication | confirmed | actual §386.73 burden, factor use, temporal relationship state, finality |
| S16 | [[source-state-corporate-registry-pilot-louisiana-texas]] | state primary-source access pilot | confirmed | official legal-person evidence paths, predicate boundaries, acquisition constraints |

## Determinations

### D1 — E1's primary identity object is a legally cognizable person, not a brand or loose enterprise

49 U.S.C. § 13902 and § 31134 register a **person**, while FMCSA guidance explicitly distinguishes a corporation as a legal person from its owners. A DBA/name, address, owner, equipment set, or public brand is therefore an attribute or relationship, not the entity itself.

**Rule:** `LegalPerson` is the primary identity node. A carrier is a `LegalPerson` holding a time-bounded `CarrierRole` / FMCSA registration state.

### D2 — ownership/control/family ties are relationships among distinct persons

The statutes require applicants to disclose common ownership, management, control, and familial relationships to **other** persons/carriers. § 31135 prohibits multiple persons from using these relationships to avoid compliance. This would make no sense if common ownership itself made the legal persons identical.

**Rule:** common ownership/control/management/family are edges, never identity equivalence by themselves.

### D3 — USDOT is an authoritative identity anchor but cannot be the benchmark's only ontology

Current FMCSA guidance says USDOT numbers belong to the same legal person and are not transferable. Corporate ownership can change while the corporation and USDOT remain the same; if the corporation dissolves and operations continue under a different company, the continuing company needs its own USDOT.

But FMCSA also publishes a sole-proprietor form-change exception in which a USDOT number may continue across a change in form of business when operations, officials, address, employees, and assets remain virtually identical.

**Rule:** store `legal_person_id` separately from `fmcsa_registrant_continuity_id`. Never encode a universal database invariant `USDOT == legal_person_id`.

### D4 — an observed identifier is a claim; authoritative assignment is a different fact

FMCSA warns that use of a USDOT number by anyone other than the assigned person can lead to inactivation. A number printed on a tender, email, website, or other commercial document therefore proves only that the source **claimed/used** that number.

**Rule:** `Observation --CLAIMS_USDOT--> RegulatoryIdentifier` is distinct from `RegulatoryIdentifier --ASSIGNED_TO--> LegalPerson` based on FMCSA authority.

### D5 — operating authority is not person identity

FMCSA permits operating-authority transfers in legitimate whole-operation corporate transactions while retaining the distinction between the old and new entity.

**Rule:** MC/OA identifiers and transfer events cannot serve as legal-person equivalence keys.

### D6 — affiliation, substantial continuity, succession, and identity are different predicates

§ 386.73 defines reincarnation through substantial continuity and affiliation through common ownership/control. The regulation speaks of “entities” and can consolidate records across them. The final-rule preamble explicitly addresses legitimately separate, commonly owned fleets.

**Rule:** keep distinct nodes; type the relationship. Never collapse a successor or affiliate into its predecessor merely because FMCSA can consolidate records.

### D7 — reincarnation is a regulatory/legal disposition layer, not the core entity-resolution label

§ 386.73 requires both continuity/affiliation evidence and an avoidance context for the actual out-of-service or record-consolidation proceeding. Orders also have procedural states and can be reviewed/stayed/rescinded.

**Rule:** E1 can label `REINCARNATION_CONFIRMED` only from an authoritative final agency/judicial disposition whose status is known. Analysts may label `REINCARNATION_REVIEW_CANDIDATE`, but that is a triage state and is excluded from legal-person ground truth.

### D8 — motive and safety history must be quarantined from Task A

GAO and ARCHI used match + motive as a screening construct. That is established prior art and is useful for enforcement targeting, but E1's scientific question is whether identity can be resolved. Letting bad safety history influence “same person” labels creates circularity and a foreseeable false-association hazard.

**Rule:** safety, enforcement, bankruptcy, and negative-history motive are masked from Task A adjudicators and Task A feature sets unless needed solely to interpret a final agency disposition. They may be studied in a separately declared downstream task.

### D9 — candidate generation is not adjudication

GAO states that matching alone cannot positively identify chameleon carriers and gives legitimate asset purchases/name collisions as examples. FMCSA's eFOTM similarly describes screening as a wide-net lead generator followed by investigation, evidence gathering, chronology, and legal coordination.

**Rule:** candidate-generation signals are never promoted automatically to gold labels.

### D10 — time is part of identity evidence

Company name, officers, addresses, ownership, authority, registration status, equipment, insurance, and operations all change. § 386.73 itself relies on creation/dissolution dates and chronology; current FMCSA registration guidance differentiates what survives transactions.

**Rule:** every material claim carries both `valid_time` (when it is asserted to be true) and `observed_at` (when the source was retrieved/observed). The benchmark has a declared `as_of` decision time.

### D11 — retrospective gold-standard evidence and model-visible evidence must be separated

A future filing or final agency order can legitimately help researchers determine retrospectively what relationship existed, but a deployment-time model could not have seen it.

**Rule:** the corpus may preserve later evidence for gold-standard adjudication, but each experimental condition receives a time-cut feature view. Any post-cutoff evidence is label-only and cannot leak into model input.

### D12 — “motor carrier” is too context-sensitive to be the ontology's equality class

49 CFR § 390.5 defines “motor carrier” broadly enough in that subchapter to include agents, officers, representatives, and certain employees. E1 needs a narrower object.

**Rule:** use `LegalPerson`, `FMCSARegisteredPerson`, and `CarrierRole`; do not make “motor carrier” the class whose instances are tested for equality without specifying the regulatory context.

### D13 — human user identity and business identity are separate

Motus gives an individual one user profile, which can access multiple company accounts; company accounts undergo business verification and manage registrations.

**Rule:** `HumanActor`, `CompanyAccount`, `LegalPerson`, and `FMCSARegistration` are separate node classes.

### D14 — identity and ownership separation has a mature external analogue

GLEIF explicitly separates Level 1 “who is who” legal-entity data from Level 2 “who owns whom” relationship data.

**Rule:** this is an architecture sanity check, not a controlling trucking authority.

### D15 — gold labels require more than one reviewer for hard cases

Gupta et al. found meaningful reviewer discordance and used two independent reviewers with a third adjudicator. One reviewer was an extreme outlier in one dataset, illustrating how a gold standard can inherit reviewer error.

**Rule:** hard E1 cases receive two independent votes and third-party adjudication when votes disagree; original votes and uncertainty are retained.

### D16 — actual FMCSA adjudication validates the identity/relationship/disposition separation

The CMAK/Chazon final order applied §386.73 to separately named entities with separate USDOT numbers, treated the continuity factors as non-dispositive guides, required an improper-purpose showing, and ultimately issued a Final Agency Order finding reincarnation. Its discussion also recognizes that simultaneous operations can support affiliation before one entity ceases and another continues the operation.

**Rule:** a final reincarnation disposition is an authoritative status-bearing edge/event about distinct persons, not an instruction to collapse those persons into one legal-person node. Relationship truth is time-indexed.

### D17 — state legal-person evidence requires jurisdiction-specific acquisition adapters

The Louisiana and Texas pilot confirms that official state evidence exists but is exposed through materially different access models. Louisiana provides a public official search with anti-automation controls; Texas routes entity/file history through SOSDirect with session/payment mechanics, while the Texas Comptroller separately exposes a tax/right-to-transact status that is explicitly not a substitute for Secretary-of-State filing history.

**Rule:** freeze national semantics, not a fictitious national registry interface. Each sampled state requires an access memo identifying the competent source, identifier, predicates, costs, automation constraints, and redistribution posture.

## Primary E1 tasks after research

### Task A — Legal-person resolution

Map source observations to a `LegalPerson` cluster at an explicit as-of time.

Allowed outcomes for an observation pair:

- `SAME_LEGAL_PERSON`
- `DISTINCT_LEGAL_PERSON`
- `UNRESOLVED`
- `OUT_OF_SCOPE`

This is the primary scientific entity-resolution target.

### Task B — FMCSA registrant / identifier continuity

Resolve USDOT assignment and FMCSA registration continuity separately from legal-person identity. This task exists because identifier claims can be wrong and because published FMCSA policy contains a narrow sole-proprietor form-change continuity exception.

### Task C — Relationship resolution among distinct persons

Where Task A says “distinct,” separately record supported relationships such as ownership/control, predecessor/successor, transaction, or substantial operational continuity. Absence of evidence is `UNKNOWN`, not automatically `UNRELATED`.

### Regulatory disposition layer — not a general ML target in E1

FMCSA final order, affiliate/reincarnation determination, record consolidation, stay, and rescission are authoritative events. A non-authoritative analytical suspicion is recorded as a review candidate and excluded from Task A equivalence labels.

## Source-of-truth matrix

There is no single universal source hierarchy. Authority is **predicate-specific**.

| Predicate | Preferred authoritative source | Secondary evidence | Never dispositive by itself |
|---|---|---|---|
| State-law legal formation/status | relevant Secretary of State / formation, merger, conversion, dissolution filing | certified transaction documents | vendor aggregator, name similarity |
| USDOT assignment | FMCSA/Motus official registration record | dated FMCSA public extract | USDOT printed on tender/email/site |
| FMCSA registration status | FMCSA/Motus | archived official extract | state corporate status |
| Operating authority | FMCSA/Motus/L&I official record | transaction/transfer documentation | USDOT equality |
| DBA/trade name | official filing or authoritative registrant record | website/contract/document | name string alone |
| ownership/control | official filings/application disclosures/transaction records appropriate to jurisdiction | corroborated public records | same surname/address alone |
| equipment continuity | title/lease/registration/inspection records appropriate to case | operational records | same VIN observed once without provenance |
| insurance continuity | authoritative carrier/insurer/FMCSA insurance record | policy/COI with provenance | broker/vendor assertion alone |
| substantial continuity | multi-source adjudication under written rubric | §386.73 factors | any single factor |
| reincarnation/affiliate regulatory finding | final FMCSA agency order / controlling court disposition | served/stayed order with explicit status | model score, analyst conclusion |
| SCAC assignment/verification | NMFTA | carrier-supplied evidence | inference from company name |

## Evidence-conflict policy

1. Preserve conflicting claims; do not overwrite one with another.
2. Compare predicates before calling a conflict. “State entity dissolved” and “FMCSA registration active” can both be true because they describe different systems.
3. Mark source time, effective/valid time, and retrieval time.
4. If two competent authoritative sources genuinely conflict on the same predicate/time and no controlling source resolves them, label `UNRESOLVED` and record the conflict.
5. Missing evidence is not negative evidence.
6. A stale authoritative source remains authoritative for what it reported **at its time**, not necessarily for the present.

## Feature / label separation

A benchmark can accidentally become trivial if the same authoritative identifier used to construct gold labels is exposed to the model. E1 therefore needs predeclared feature regimes:

- **Anchor-visible control:** authoritative USDOT and high-confidence IDs visible; sanity test, not the headline scientific result.
- **Anchor-masked:** USDOT removed from model-visible fields while adjudicators may use it for ground truth.
- **Anchor-missing/corrupted:** controlled missing/typo/claimed-identifier cases.
- **Claim-versus-assignment:** commercial record claims a USDOT that authoritative FMCSA evidence assigns elsewhere.
- **Cross-USDOT relation:** legally distinct persons with different USDOTs, evaluated only on relationship reconstruction.

The E1 headline result should come from the regimes that actually test resolution under ambiguity, not from simple identifier equality.

## PII and sensitive-field rule

Historical government matching work used SSNs/EINs and other strong identifiers. E1 does **not** inherit those fields automatically. Following data-minimization principles and the programme's governance posture:

- do not collect SSNs for E1;
- collect EIN/tax identifiers only if lawful, necessary, permissioned, and approved in the data-management protocol;
- prefer public/entity-level authoritative identifiers and state registration identifiers;
- hash or suppress sensitive values in distributable benchmark views;
- record why each field is necessary and who can access it.

## Prior-art correction to the programme

The source review materially narrows the novelty claim:

- GAO already published multi-field carrier matching plus motive as a targeting method.
- FMCSA already built ARCHI.
- FMCSA states an earlier SBIR Phase I studied automated reincarnated-carrier screening, and URSA was subsequently implemented/integrated into URS-1.
- Motus now performs individual identity and business verification in current registration workflows.
- NMFTA SCAC Verified adds point-in-time identity verification to SCAC issuance/renewal.

Therefore E1 is **not** novel because it uses algorithms to detect chameleon carriers or because it verifies carrier identity at registration. The defensible R&D proposition is narrower: a measured, temporally explicit, provenance-preserving identity-and-relationship resolution substrate with a reusable adjudicated benchmark, uncertainty/abstention, evidence packets, correction, and published error analysis.

## Open questions that remain after Step 1 research

These do not block the ontology but do block corpus construction or final protocol freeze:

1. Which state jurisdictions will be sampled first, and what official corporate-record fields are available in each?
2. Which public FMCSA/Motus extracts preserve enough history for time-forward adjudication without a new FOIA?
3. Which relationship fields can be redistributed in the benchmark under source terms/licensing?
4. What exact evidence threshold will the human panel use for `SUBSTANTIAL_CONTINUITY_SUPPORTED` when no FMCSA order exists? The standard requires multi-source evidence but intentionally does not invent a numeric legal-like threshold.
5. Whether the PI/counsel wants any reincarnation-risk analysis inside E1 at all, or reserves it for a later, clearly separate experiment.

## Research Agent recommendation

Adopt [[e1-carrier-identity-and-relationship-standard]] as the **v1.0 freeze candidate**, subject to PI/domain/legal review. Build the benchmark around Task A legal-person clusters and Task B registration continuity; treat Task C relationship edges as a secondary structured output; keep motive and regulatory reincarnation dispositions outside the primary identity label.
