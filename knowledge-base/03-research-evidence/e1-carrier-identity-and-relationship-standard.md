---
type: policy
status: candidate
schema_version: 1.0.0
updated: 2026-08-08
version: 1.0.0-rc1
owner: e1-protocol-owner
approval_required: principal-investigator-plus-domain-review
tags:
- type/policy
- domain/identity
- domain/regulatory
- domain/legal
- confidence/mixed
- audience/internal
- programme/e1
- lifecycle/candidate
---
# E1 Carrier Identity & Relationship Standard

**Version:** 1.0.0-rc1  
**Research cut-off:** 2026-08-08  
**Status:** freeze candidate after Research Agent + hostile Eval Agent pass; **not yet represented as PI/legal approval**.

This document defines the target variables for E1. Once the E1 corpus begins formal adjudication, changes to these definitions require a versioned amendment and re-adjudication impact review. They may not be changed silently after model performance is observed.

## 1. Scope

E1 asks whether source observations can be resolved to the correct carrier-related legal person and FMCSA registration identity, and whether relationships among distinct persons can be represented without collapsing them into one entity.

E1 **does not** determine:

- whether a carrier is fraudulent;
- whether a carrier is safe;
- whether a company should receive a load, contract, insurance policy, or operating authority;
- whether FMCSA should issue a §386.73 order;
- a legal conclusion of reincarnation in the absence of authoritative disposition.

## 2. Primary proposition

> A carrier identity is not a name, address, owner, truck, SCAC, MC number, company account, or risk score. For E1, the primary entity is the legally cognizable person to which sourced observations and regulatory registrations refer at a declared time. Other identifiers, roles, relationships, operational continuities, and regulatory dispositions are represented separately.

## 3. Core objects

### 3.1 Observation

A source-specific record or assertion. It is not truth by itself.

Required attributes:

- `observation_id`
- `source_id`
- `source_record_id` where available
- `observed_at`
- `valid_from`, `valid_to`, or explicit `valid_time_unknown`
- `predicate`
- `object/value`
- `extraction_method`
- `provenance`
- `sensitivity`
- `correction_status`

### 3.2 LegalPerson

An individual or legally cognizable organization that can be registered/recognized as a person under applicable law. This is E1 Task A's canonical identity object.

`LegalPerson` is not identical to:

- a trade name/DBA;
- a Motus user;
- a Motus company account;
- a USDOT number itself;
- an MC/operating-authority number;
- a SCAC;
- a fleet/equipment set;
- a parent corporate group;
- an “operating enterprise” spanning multiple legal persons.

### 3.3 CarrierRole

A time-bounded role held by a `LegalPerson`, such as for-hire motor carrier or private motor carrier in the relevant regulatory context. Roles permit the same legal person to hold multiple transportation-related registrations without creating multiple legal-person nodes.

### 3.4 FMCSARegistration

A registration record/status maintained by FMCSA for a person. Registration history is separate from the person and has valid/effective dates.

### 3.5 FMCSARegistrantContinuity

A continuity construct for FMCSA registration identity. It will normally align with legal-person identity, but it is separated because FMCSA's published sole-proprietor form-change policy can preserve a USDOT number across a change in form of business under narrowly specified continuity conditions.

### 3.6 RegulatoryIdentifier

A typed identifier such as USDOT. The identifier node must distinguish:

- authoritative assignment (`USDOT_ASSIGNED_TO`);
- observed/claimed use (`CLAIMS_USDOT`);
- status and dates.

A claimed identifier is not proof of assignment.

### 3.7 OperatingAuthority

FMCSA operating authority / MC/FF/MX registration as applicable. It is a regulatory authorization that can, in defined corporate transactions, be transferred or re-recorded. It is not the legal person.

### 3.8 TradeIdentifier and TradeName

Examples include SCAC and DBA/trade names. They identify or name a legal person in a defined system/context but are not themselves the person.

### 3.9 HumanActor

An individual user/agent/officer. Current Motus practice shows that one human user can access multiple company accounts. Human identity proofing therefore does not resolve company identity.

### 3.10 CompanyAccount

A digital account/container used to administer business information, users, and registrations. It is not the legal person or registration itself.

### 3.11 CorporateTransaction

A dated merger, acquisition, stock sale, asset purchase, conversion, reorganization, dissolution, or related event. Transactions create relationship evidence and may or may not change legal-person identity.

### 3.12 AgencyDisposition

A served, stayed, final, rescinded, or otherwise status-bearing agency/court action. §386.73 record consolidation or reincarnation/affiliate findings are represented as dispositions/events, never as permission to merge legal-person nodes.

## 4. Identity and relationship predicates

### 4.1 Equivalence predicates

`SAME_LEGAL_PERSON_AS`

- reflexive: yes
- symmetric: yes
- transitive: yes
- meaning: two observations/entities resolve to the same legal person for the relevant time interval.

`SAME_FMCSA_REGISTRANT_CONTINUITY_AS`

- reflexive: yes
- symmetric within a defined continuity interval: yes
- transitive within the same continuity definition: yes
- meaning: records belong to the same FMCSA registrant continuity chain under authoritative registration policy.
- must not be assumed identical to `SAME_LEGAL_PERSON_AS` in every edge case.

### 4.2 Identifier/name predicates

- `USDOT_ASSIGNED_TO`
- `CLAIMS_USDOT`
- `OPERATING_AUTHORITY_HELD_BY`
- `OPERATING_AUTHORITY_TRANSFERRED_TO`
- `SCAC_ASSIGNED_TO`
- `DBA_OF`
- `FORMER_NAME_OF`

### 4.3 Corporate / control predicates

- `OWNED_BY`
- `CONTROLLED_BY`
- `MANAGED_BY`
- `AFFILIATED_WITH`
- `PREDECESSOR_OF`
- `SUCCESSOR_OF`
- `MERGED_INTO`
- `ACQUIRED_BY`
- `ASSET_TRANSFER_TO`
- `CONVERTED_TO`

These do not imply legal-person equivalence unless authoritative evidence shows the same legal person survived the transaction.

### 4.4 Operational-continuity evidence predicates

- `SHARES_ADDRESS_WITH`
- `SHARES_CONTACT_WITH`
- `SHARES_EQUIPMENT_WITH`
- `SHARES_INSURANCE_WITH`
- `SHARES_EMPLOYEES_WITH`
- `SHARES_FACILITY_WITH`
- `SHARES_CUSTOMERS_WITH`
- `SIMILAR_PUBLIC_NAME_TO`
- `SUBSTANTIAL_CONTINUITY_SUPPORTED`

`SUBSTANTIAL_CONTINUITY_SUPPORTED` is an adjudicated analytical relationship backed by multiple relevant facts. It is **not** a legal-person equality relation and is not itself a final FMCSA reincarnation finding.

### 4.5 Regulatory/disposition predicates

- `FMCSA_REINCARNATION_ORDER_SERVED`
- `FMCSA_AFFILIATE_ORDER_SERVED`
- `FMCSA_RECORD_CONSOLIDATION_ORDER_SERVED`
- `FMCSA_ORDER_STAYED`
- `FMCSA_FINAL_REINCARNATION_DISPOSITION`
- `FMCSA_FINAL_AFFILIATE_DISPOSITION`
- `FMCSA_RECORDS_CONSOLIDATED`
- `FMCSA_ORDER_RESCINDED`

An analytical state `REINCARNATION_REVIEW_CANDIDATE` may be used for triage but must be explicitly non-authoritative.

## 5. Benchmark tasks and labels

### Task A — Legal-person resolution (primary)

Given two observations or an observation and a canonical entity, label:

- `SAME_LEGAL_PERSON`
- `DISTINCT_LEGAL_PERSON`
- `UNRESOLVED`
- `OUT_OF_SCOPE`

**Do not use `UNRELATED` as the negative identity label.** Two persons can be legally distinct while strongly related.

### Task B — FMCSA registrant/identifier continuity

Determine:

- whether a claimed USDOT is authoritatively assigned to the represented legal person at the relevant time;
- whether two registration observations belong to the same FMCSA registrant-continuity chain;
- whether identifier continuity and legal-person continuity diverge under an explicit FMCSA policy exception.

Labels:

- `ASSIGNMENT_CONFIRMED`
- `ASSIGNMENT_CONTRADICTED`
- `REGISTRANT_CONTINUITY_SAME`
- `REGISTRANT_CONTINUITY_DISTINCT`
- `UNRESOLVED`

### Task C — Relationship resolution among distinct persons

For each typed relationship, record a truth state:

- `SUPPORTED`
- `REFUTED`
- `UNKNOWN`
- `NOT_APPLICABLE`

This prevents “we did not find evidence” from becoming “the relationship does not exist.”

### Regulatory disposition layer

Only authoritative procedural outcomes can populate “confirmed” regulatory labels. Analytical similarity/continuity scores remain separate.

## 6. Adjudication target time

Every case declares:

- `decision_as_of` — the time at which the identity/relationship question is posed;
- `feature_cutoff` — latest evidence visible to the model;
- `adjudication_cutoff` — latest evidence allowed to establish retrospective gold truth;
- `disposition_status_as_of` where a regulatory order is involved.

The adjudication cutoff may be later than the feature cutoff. Any evidence later than `feature_cutoff` is **label-only** and must be cryptographically or procedurally excluded from the model input.

## 7. Source authority is predicate-specific

No global “source A always beats source B” rule is valid.

- state legal existence/formation/name change/merger/conversion/dissolution → relevant state authority/document;
- USDOT assignment and FMCSA status → FMCSA/Motus authoritative record;
- operating authority → FMCSA authoritative record;
- SCAC → NMFTA;
- final reincarnation/affiliate disposition → final FMCSA/court record;
- ownership/control → appropriate official filings/transaction records/application disclosures;
- operational continuity → multiple dated provenance-bearing records.

Commercial/vendor/party records may generate observations and candidates but do not override the controlling authority for a predicate they do not govern. State implementation is jurisdiction-specific: see [[e1-state-corporate-source-access-memo]]. A tax/franchise “active/right to transact” flag is not automatically a legal-existence or corporate-transaction predicate.

## 8. Conflict rules

1. Keep both sourced claims.
2. Confirm they concern the same predicate and time before calling them contradictory.
3. Prefer the competent issuing/recording authority for that predicate.
4. If competent authorities genuinely conflict and cannot be resolved, assign `UNRESOLVED`.
5. Missing data never becomes a negative fact.
6. A later correction does not erase the earlier observation; it changes its status and validity interval.
7. Adjudicators must state why a source was considered authoritative, stale, contradicted, or insufficient.

## 9. Hard prohibitions

The following rules are safety and validity requirements, not optional implementation preferences.

### P1 — no automatic legal-person merge from one weak relational field

Never merge solely because of same/similar:

- name;
- address;
- phone/email;
- owner/officer;
- insurer;
- equipment;
- employee/driver;
- customer;
- registered agent;
- website/domain.

### P2 — no motive contamination of Task A

Safety history, enforcement action, bankruptcy, civil penalties, crash history, or “bad actor” labels do not determine legal-person identity.

### P3 — no MC/OA identity shortcut

Operating authority can transfer; it cannot be treated as a person-equivalence key.

### P4 — no record-consolidation node collapse

Agency record consolidation is represented as an agency action over distinct/current/previous/affiliated entities.

### P5 — no hidden future evidence

No post-feature-cutoff field, relationship, order, or corrected record is visible to the tested model.

### P6 — no forced binary label

When competent evidence does not resolve the question, `UNRESOLVED` is the correct gold label.

### P7 — no authoritative “chameleon” conclusion from model output

A model may output a review candidate or relationship probability. It does not create a regulatory determination.

### P8 — no benchmark tautology

If an authoritative USDOT assignment is used to construct the gold label, the scientific test cannot simultaneously expose the same perfect key as an uncontrolled model feature and then claim meaningful entity-resolution performance.

## 10. Feature regimes

Every published result identifies which regime it uses.

1. **F0 Anchor-visible:** authoritative identifier visible; control/sanity condition.
2. **F1 Anchor-masked:** USDOT/strong decisive identifier hidden from model, retained for adjudication.
3. **F2 Anchor-missing:** naturally missing decisive identifier.
4. **F3 Anchor-corrupted:** controlled typo/transposition/staleness.
5. **F4 Claim-versus-assignment conflict:** observed commercial record claims an identifier that official evidence assigns elsewhere.
6. **F5 Cross-registration relationship:** distinct USDOT/legal-person entities with possible affiliation/succession/continuity.
7. **F6 Time-forward:** only records available before the declared cutoff.

F0 is not a headline result. F1–F6 carry the scientific burden.

## 11. Human adjudication procedure

### 11.1 Case construction

Candidate-generation staff may use broad signals to find hard cases. They do not assign final labels and their heuristic score is hidden from adjudicators.

### 11.2 Reviewer training

Reviewers complete a versioned training set containing obvious matches, hard negatives, legitimate corporate changes, common-ownership cases, identifier misuse, and unresolved cases. Training errors and bias patterns are reviewed before live adjudication.

### 11.3 Independent review

Every hard case receives two independent primary reviews. Reviewers see the standardized evidence packet and source provenance but not:

- model outputs;
- candidate-generation score;
- downstream fraud/safety risk score;
- the other reviewer's vote.

### 11.4 Third adjudication

A third independent reviewer adjudicates disagreements. The final record preserves both original votes, their rationales, timestamps, and the adjudicator's disposition.

### 11.5 Agreement reporting

Report:

- raw agreement;
- chance-corrected agreement where appropriate;
- disagreement rate by case type;
- adjudicator overturn rate;
- sensitivity analyses treating disputed cases as alternate labels/excluded cases.

### 11.6 Reviewer abstention

A reviewer can select `UNRESOLVED` and state what evidence would be needed. The third reviewer is not required to force a binary answer.

## 12. Evidence packet

Each packet should contain, where lawful and available:

- source record snapshots and dates;
- authoritative legal name/entity status evidence;
- USDOT assignment/status evidence;
- operating-authority record separately;
- DBA/trade identifiers;
- dated address/contact records;
- ownership/officer/management evidence;
- transaction/formation/dissolution documents;
- equipment/insurance/employee/facility continuity evidence as applicable;
- conflicts/staleness annotations;
- chronology;
- evidence unavailable/attempted retrieval log.

For Task A, remove irrelevant adverse-history/motive material unless necessary to interpret an authoritative disposition document.

## 13. Minimal corpus schema

Required case-level fields:

`case_id`, `case_version`, `task`, `decision_as_of`, `feature_cutoff`, `adjudication_cutoff`, `sampling_stratum`, `difficulty_stratum`, `subgroup_stratum`, `candidate_generation_method`, `candidate_generation_score_hidden`, `reviewer_1_label`, `reviewer_2_label`, `adjudicator_label`, `final_label`, `agreement_state`, `adjudication_rationale`, `evidence_needed_if_unresolved`, `source_ids`, `provenance`, `sensitivity`, `redistribution_status`.

Required observation-level fields:

`observation_id`, `source_id`, `source_record_id`, `observed_at`, `valid_from`, `valid_to`, `predicate`, `raw_value_or_protected_reference`, `normalized_value`, `claim_status`, `source_authority_for_predicate`, `correction_status`, `feature_visibility_regime`.

Required entity/relationship fields:

`legal_person_id`, `fmcsa_registrant_continuity_id`, `relationship_type`, `relationship_truth_state`, `relationship_valid_from`, `relationship_valid_to`, `relationship_evidence_ids`, `disposition_status`.

## 14. Benchmark output form

The gold corpus is **not just a list of record pairs**. It comprises:

1. legal-person entity clusters;
2. pairwise labels derivable from those clusters;
3. FMCSA registrant-continuity assignments;
4. typed relationship edges among distinct persons;
5. source observations/provenance;
6. reviewer votes and uncertainty;
7. feature-view manifests that define what each model condition may see.

This permits pair-level metrics without sacrificing cluster consistency.

## 15. Consistency constraints

- `SAME_LEGAL_PERSON` must be transitive across a declared time interval.
- A legal person cannot be both `SAME_LEGAL_PERSON` and `DISTINCT_LEGAL_PERSON` for the same pair/time/version.
- `PREDECESSOR_OF` is directional.
- `SUCCESSOR_OF` is the inverse of `PREDECESSOR_OF`.
- `AFFILIATED_WITH` is treated as symmetric only when the underlying adjudicated definition is symmetric; granular ownership/control edges remain directional where possible.
- `CLAIMS_USDOT` does not entail `USDOT_ASSIGNED_TO`.
- `OPERATING_AUTHORITY_TRANSFERRED_TO` does not entail `SAME_LEGAL_PERSON`.
- `FMCSA_RECORDS_CONSOLIDATED` does not entail `SAME_LEGAL_PERSON`.
- `SUBSTANTIAL_CONTINUITY_SUPPORTED` does not entail `REINCARNATION_CONFIRMED`.

## 16. Data minimization and sensitive fields

- SSNs are excluded from E1 collection unless a later ethics/legal protocol explicitly changes this; no current design depends on them.
- EIN/tax identifiers require necessity, lawful access, access control, and redistribution review.
- Do not expose sensitive personal/familial fields in a public benchmark where hashed/derived structure can answer the research question.
- Public/internal benchmark views may differ; the release manifest documents all redactions and transformations.

## 17. Edge-case conformance

The standard is unit-tested by [[e1-edge-case-suite.csv]]. Any future standard change must rerun those tests and add cases for the new rule.

## 18. Prior-art boundary

E1 may not claim first-of-kind status for automated chameleon-carrier matching/risk screening, match+motive approaches, point-of-registration identity verification, or SCAC identity verification. See [[source-fmcsa-ursa-risk-screening-prior-art]], [[source-fmcsa-chameleon-carrier-vetting-report]], [[source-fmcsa-motus-identity-and-business-verification]], and [[source-nmfta-scac-verified-and-standards-role]].

A defensible novelty hypothesis is the **evaluated provenance-bearing identity-and-relationship substrate and benchmark**, not the mere existence of matching automation.

## 19. Amendment rule

After formal PI freeze:

- PATCH: clarifies wording without changing labels;
- MINOR: adds a relationship or source rule without changing Task A equivalence semantics; affected cases are rerun;
- MAJOR: changes `LegalPerson`, registrant-continuity semantics, label meanings, or allowed evidence; all affected gold labels and prior performance claims must be reevaluated.

Every amendment records date, requester, source/evidence, cases affected, and whether the held-out test set has already been observed.

## 20. Freeze criteria

This RC may become `1.0.0 frozen` only when:

1. PI accepts the scientific target;
2. a freight/FMCSA-domain reviewer confirms the terminology is operationally sensible;
3. counsel/domain review confirms that the standard does not imply an unauthorized legal determination;
4. the edge-case suite has no open Critical/Major evaluator failure;
5. adjudicator training packet and reviewer conflict rules exist;
6. source-access/licensing rules for the first sampled jurisdictions are known. Louisiana/Texas access has been piloted; each additional sampled jurisdiction requires the same adapter memo before adjudication.

## References

[[e1-identity-definition-research-report]] · [[e1-identity-claims-ledger]] · [[e1-definition-freeze-review]] · [[e1-state-corporate-source-access-memo]] · [[source-ecfr-386-73-reincarnated-carrier-standard]] · [[source-fmcsa-cmak-chazon-final-order-2015]] · [[source-fmcsa-usdot-and-operating-authority-identity-guidance]] · [[source-us-code-motor-carrier-registration-relationship-disclosure]] · [[source-gao-12-364-chameleon-carrier-matching]] · [[source-fmcsa-ursa-risk-screening-prior-art]] · [[source-fmcsa-motus-identity-and-business-verification]] · [[source-state-corporate-registry-pilot-louisiana-texas]] · [[source-gupta-2024-manual-record-linkage-gold-standard]]
