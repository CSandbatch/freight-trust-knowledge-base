---
type: method
status: candidate
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/method
- domain/identity
- domain/regulatory
- confidence/mixed
- audience/internal
- programme/e1
- lifecycle/candidate
---
# E1 adjudication decision tree

Operational companion to [[e1-carrier-identity-and-relationship-standard]]. It is deliberately conservative: a hard case can end as `UNRESOLVED`.

## A. Case admissibility

1. **Define the question and time.** What two observations/entities are being compared, and what is `decision_as_of`?
2. **Confirm scope.** Does the case concern a legally cognizable person / FMCSA carrier-related registration? If not, `OUT_OF_SCOPE`.
3. **Check evidence sufficiency.** Is there at least one provenance-bearing source for each side? If no, `UNRESOLVED`.
4. **Separate observation claims from authoritative facts.** A website/tender/email claiming a USDOT is not an assignment record.

## B. Task A — same legal person?

### B1. Positive authoritative continuity

Is there competent evidence that both observations refer to the same legal person at the relevant time?

Examples:

- same state legal-entity identifier and entity survives a legal-name/officer/address change;
- same natural-person sole proprietor;
- same corporation before and after a stock sale where the corporation survives;
- official correction showing one source record was a spelling/format variant of the same legal person.

If yes → `SAME_LEGAL_PERSON`, with evidence IDs.

### B2. Authoritative distinctness

If B1 is not established, is there competent evidence of two distinct legal persons?

Examples:

- different concurrently existing state entities;
- seller and buyer in an asset sale;
- predecessor corporation dissolved and different/new corporation continues operations;
- parent and subsidiary;
- two carriers under common ownership/control.

If yes → `DISTINCT_LEGAL_PERSON`, then continue to Task C. Do **not** stop at “different” if a relationship is material.

### B3. Genuine ambiguity

If neither sameness nor distinctness can be defensibly established because sources are incomplete, stale, or conflicting → `UNRESOLVED`.

Do not force a negative label because the decisive source is unavailable.

## C. Task B — FMCSA registration / identifier continuity

1. What USDOT does the observation **claim**?
2. What legal person does the authoritative FMCSA/Motus record assign that USDOT to for the relevant period?
3. If they agree → `ASSIGNMENT_CONFIRMED`.
4. If the observation claims another person's USDOT → `ASSIGNMENT_CONTRADICTED`; retain the claim as evidence of possible impersonation/misuse, not identity.
5. If no competent assignment evidence is available → `UNRESOLVED`.
6. For a form-change/transaction case, determine whether FMCSA policy treats the registration as continuous separately from state-law legal-person continuity.

## D. Task C — relationships among distinct persons

Only run this branch if Task A is `DISTINCT_LEGAL_PERSON` or if relationship evidence is independently requested.

For every possible relation, label `SUPPORTED`, `REFUTED`, `UNKNOWN`, or `NOT_APPLICABLE`.

### D1. Common ownership/control/management/family

Use appropriate official/transaction/application evidence. Shared surname/address alone is insufficient.

### D2. Predecessor/successor / transaction

Determine whether a documented merger, acquisition, conversion, asset transfer, dissolution, or restructuring connects the entities. Record the event and direction.

### D3. Operational continuity

Consider the §386.73(c)-type evidence as **multi-source continuity evidence**:

- creation/dissolution chronology;
- ownership/management;
- address/contact;
- equipment;
- insurance;
- employees/drivers;
- facilities/assets;
- nature/scope/customers;
- public name/advertising;
- transaction consideration where applicable.

No single factor is dispositive. If multiple independent dated sources support continuity, `SUBSTANTIAL_CONTINUITY_SUPPORTED` may be recorded as an analytical relationship. If the evidence is equivocal, leave it `UNKNOWN`.

## E. Regulatory reincarnation / affiliation disposition

**Do not infer this from Task C alone.**

1. Is there a §386.73/FMCSA or controlling court document?
2. What is its procedural state: served, contested/stayed, final, rescinded?
3. Only a known authoritative final disposition may populate `FMCSA_FINAL_REINCARNATION_DISPOSITION` or `FMCSA_FINAL_AFFILIATE_DISPOSITION`.
4. A model/reviewer may identify a `REINCARNATION_REVIEW_CANDIDATE`, but it is explicitly non-authoritative and excluded from Task A.

## F. Conflict checklist before final label

Before signing a case, the reviewer must answer:

- Did I mistake an owner for the company?
- Did I mistake a DBA/brand for a legal person?
- Did I use a claimed USDOT as if FMCSA assigned it?
- Did I mistake MC/OA transfer for entity identity?
- Did I use safety/enforcement motive to decide sameness?
- Did I treat state “active/dissolved” and FMCSA registration status as the same predicate?
- Did I use evidence dated after the model feature cutoff in a model-visible field?
- Did I infer non-relationship merely from missing evidence?
- Did I collapse a successor/affiliate because its records were consolidated?
- Would my decision still hold if the company had a clean safety history?

If any answer reveals a category error, reopen the case.

## G. Required reviewer output

Every adjudication records:

- Task A label and confidence category;
- Task B label if applicable;
- Task C relation states if applicable;
- source IDs and claim IDs relied upon;
- rationale in factual, non-accusatory language;
- evidence conflicts;
- evidence sought but unavailable;
- what would resolve an `UNRESOLVED` case;
- reviewer ID/version/time;
- whether any source was post-feature-cutoff and therefore label-only.

## Sources

[[source-ecfr-386-73-reincarnated-carrier-standard]] · [[source-federal-register-2012-reincarnated-carrier-rule-preamble]] · [[source-fmcsa-usdot-and-operating-authority-identity-guidance]] · [[source-gao-12-364-chameleon-carrier-matching]] · [[source-fmcsa-efotm-reincarnated-carrier-investigation]] · [[source-gupta-2024-manual-record-linkage-gold-standard]]
