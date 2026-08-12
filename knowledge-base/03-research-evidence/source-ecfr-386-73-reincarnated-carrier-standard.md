---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-08
updated: 2026-08-08
review_by: 2027-02-08
tags:
- type/source
- domain/identity
- domain/regulatory
- domain/legal
- confidence/primary
- audience/internal
- programme/e1
- lifecycle/active
---
# 49 CFR § 386.73 — Reincarnated carriers, affiliates, and record consolidation

## Citation

Electronic Code of Federal Regulations, Title 49, § 386.73, *Operations out of service and record consolidation proceedings (reincarnated carriers)*. Current text retrieved 2026-08-08; eCFR displayed Title 49 as current through 2026-08-06.

<https://www.ecfr.gov/current/title-49/subtitle-B/chapter-III/subchapter-B/part-386/subpart-F/section-386.73>

## What the source establishes

This is the controlling current regulatory text for FMCSA's reincarnated-carrier and affiliate record-consolidation proceedings. It is not an entity-resolution benchmark specification, but it is the strongest source for what a Freight Trust identity ontology must **not** collapse.

The regulation distinguishes two concepts:

- **Reincarnation:** FMCSA may determine that entities are reincarnated where there is "substantial continuity" such that one is merely a continuation of the other.
- **Affiliation:** FMCSA may determine entities are affiliates where business operations are under common ownership and/or common control.

The distinction matters because both concepts relate **entities**; neither definition says the entities become the same legal person.

The rule also requires an avoidance context before FMCSA issues an out-of-service or record-consolidation order: operation under a new identity or affiliate must be used to avoid an FMCSA order, statutory/regulatory requirement, civil penalty, enforcement action, or linkage to negative compliance history.

## Thirteen continuity / relationship factors

Section 386.73(c) permits FMCSA to consider, among other things:

1. purpose or motive, including the stated business purpose;
2. previous safety performance history;
3. consideration exchanged for transferred assets;
4. creation/dissolution or cessation dates;
5. common ownership;
6. common officers and management;
7. shared physical/mailing addresses, phones, fax, or email;
8. shared motor-vehicle equipment;
9. insurance continuity/common coverage;
10. common drivers and employees;
11. continued facilities and physical assets;
12. continuity/commonality of operations and customers; and
13. advertising, corporate name, and public holding-out.

Section 386.73(d) also permits review of management structures, financial records, corporate filings, asset/title history, employee records, insurance records, and other relevant operational information.

## Procedural status is part of the evidence

An order does not automatically become final when served. Under the current rule it ordinarily becomes a Final Agency Order on the 21st day unless administrative review is timely requested; a timely petition stays the disputed order pending review unless the Agency Decisionmaker vacates the stay. Rescission is separately available.

**Consequence for E1:** an FMCSA order must carry procedural status and dates. `ORDER_SERVED`, `ORDER_STAYED`, `FINAL_AGENCY_ORDER`, and `ORDER_RESCINDED` are not interchangeable evidence states.

## Ontology consequences

- `SAME_LEGAL_PERSON` must remain separate from `SUBSTANTIAL_CONTINUITY_WITH`.
- `AFFILIATED_WITH` must remain separate from both identity and reincarnation.
- A record-consolidation order is a **regulatory event/disposition**, not permission to collapse the corresponding legal-person nodes.
- `REINCARNATION_CONFIRMED` in an E1 corpus requires an authoritative final disposition, not an analyst's similarity score.
- Motive / adverse history is not an identity attribute and must not contaminate the gold label for Task A legal-person resolution.

## Consumers

[[e1-carrier-identity-and-relationship-standard]] · [[e1-identity-claims-ledger]] · [[e1-definition-freeze-review]] · [[experiment-e1-entity-resolution-and-identity-assurance]]
