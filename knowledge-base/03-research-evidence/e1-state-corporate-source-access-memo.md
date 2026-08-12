---
type: evidence
status: current
schema_version: 1.0.0
updated: 2026-08-08
confidence_default: primary
tags:
- type/evidence
- domain/identity
- domain/legal
- domain/data-access
- confidence/primary
- audience/internal
- programme/e1
- lifecycle/current
---
# E1 state corporate-source access memo — Louisiana/Texas pilot

## Purpose

Test whether the Step 1 source-of-truth rule — “use the relevant state authority for state-law legal-person formation/status/transaction facts” — can be operationalized against real official access paths without substituting a commercial aggregator.

This is an **access and predicate memo**, not an opinion on state corporate law and not authorization for automated scraping.

## Louisiana

**Authoritative access point:** Louisiana Secretary of State Commercial Division business-filing search.

**Observed search keys:** entity name; charter/trade-registration/name-reservation number; officer/agent name.

**Operational constraint:** the public search uses reCAPTCHA. For E1, that means case-level human retrieval is presently supportable, but automated bulk acquisition cannot be assumed and must receive a separate terms/access review.

**Adjudication use:** where a Louisiana legal person is sampled, record the state charter/entity identifier and the exact filing/status evidence used. Do not use the company's display name as the canonical key.

## Texas

**Authoritative access point:** Texas Secretary of State SOSDirect / Business & Public Filings Division.

**Observed capabilities:** entity search, status/entity information, filing history, imaged filings, plain/certified copies, certificates of fact.

**Operational constraints:** SOSDirect uses session/account/payment mechanics; official instructions state a $1 search fee and additional document-copy/certification fees. National benchmark costing therefore needs a state-record acquisition line item.

**Auxiliary source:** Texas Comptroller Franchise Tax Account Status. This is useful for the entity's right to transact business under the tax regime, but the Comptroller explicitly distinguishes this status from Secretary-of-State filings needed for reinstatement/termination and related entity-file facts.

**Adjudication use:** use SOS filings for formation, name change, merger/conversion, termination, reinstatement, and filing-history propositions. Preserve Comptroller status as its own predicate; do not map it to `LEGAL_PERSON_EXISTS=true/false` without supporting state-law evidence.

## Cross-jurisdiction rule established by the pilot

The E1 standard can freeze the **semantic rule** nationally but cannot freeze one national state-registry acquisition implementation. Each sampled jurisdiction requires a small adapter memo stating:

1. authoritative custodian;
2. official entity identifier(s);
3. searchable fields;
4. filing/status documents available;
5. temporal/history coverage;
6. access mechanics and costs;
7. automation/API/anti-bot constraints;
8. redistribution/licensing constraints;
9. predicates the source is competent to establish; and
10. known ambiguity or lag.

## Benchmark storage rule

For every state-derived adjudication fact, preserve at minimum:

```yaml
jurisdiction: US-LA | US-TX | ...
authority: official agency name
state_entity_id: jurisdiction-specific canonical identifier
predicate: formation | status | name_change | merger | conversion | termination | reinstatement | officer | agent | ...
asserted_value: ...
valid_at_or_period: ...
retrieved_at: ...
source_document_id: ...
source_locator: ...
retrieval_method: human_web | paid_portal | api | certified_copy | ...
redistributable: yes | no | unknown
review_notes: ...
```

The corpus may distribute the **derived adjudication label and provenance metadata** even where the underlying document itself cannot be redistributed, subject to counsel/data-management review.

## Result

**Pilot passes the source-of-truth rule but disproves a uniform-access assumption.** Louisiana and Texas both provide authoritative state evidence, but they expose it differently enough that state-adapter work is a real E1 acquisition cost and should be measured rather than hidden.

Related: [[source-state-corporate-registry-pilot-louisiana-texas]] · [[e1-carrier-identity-and-relationship-standard]] · [[dataset-e1-adjudicated-carrier-identity-cases]]
