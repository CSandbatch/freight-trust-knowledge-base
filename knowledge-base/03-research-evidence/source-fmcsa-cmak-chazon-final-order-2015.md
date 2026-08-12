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
# FMCSA-2015-0170 — CMAK Logistics / Chazon Enterprises final §386.73 order

## Citation

Federal Motor Carrier Safety Administration, *In the Matter of CMAK Logistics, LLC (USDOT 2397095) and Chazon Enterprises, Inc. aka Anthony M Wainaina dba Chazon Enterprises (USDOT 1980615)*, Docket No. FMCSA-2015-0170, Final Order on Petition for Administrative Review of Operations Out-of-Service Order and Record Consolidation Order, July 10, 2015.

Official Regulations.gov attachment:
<https://downloads.regulations.gov/FMCSA-2015-0170-0005/attachment_1.pdf>

## What the source establishes

This is a concrete FMCSA adjudication applying 49 CFR §386.73 to two separately named entities with separate USDOT numbers. It is valuable to E1 because it demonstrates how the abstract regulation is actually used in a contested final agency decision.

The order states that the Field Administrator bore the burden, by a **preponderance of the evidence**, of proving that CMAK was a reincarnation or affiliate of Chazon created for an improper purpose. It repeats that the §386.73 continuity factors are a guide and that **no single factor is dispositive**; similarities among the listed factors do not necessarily establish reincarnation or affiliation.

The decision ultimately found that Chazon reincarnated as CMAK after Chazon ceased operations and CMAK continued them, and found improper-purpose grounds relating to avoidance of Chazon's safety rating/order and negative safety history. The petition for administrative review was denied, and the decision states that it constitutes the **Final Agency Order**.

## Temporal and relationship nuance

The order's discussion also makes two points directly relevant to E1's ontology:

- a reincarnation can involve an already-existing carrier assuming the identity or role of another carrier; and
- where both carriers continue to operate simultaneously, affiliation may exist until one ceases operations.

**Consequence:** relationship state depends on time. The same pair of legal persons can move through different regulatory/operational relationship states without ever becoming the same legal person.

## E1 consequences

- Keep `LegalPerson` nodes distinct from `FMCSA_FINAL_REINCARNATION_DISPOSITION`.
- Do not treat a factor match, graph score, or analytical `SUBSTANTIAL_CONTINUITY_SUPPORTED` edge as a final reincarnation finding.
- Preserve burden/procedural state when using final orders as gold evidence.
- Treat motive/avoidance as a separate regulatory-disposition component, not as Task A identity evidence.
- Add temporal tests where concurrent operation supports affiliation and later cessation/continuation supports a different relationship state.

## Consumers

[[e1-identity-definition-research-report]] · [[e1-identity-claims-ledger]] · [[e1-carrier-identity-and-relationship-standard]] · [[e1-definition-freeze-review]] · [[experiment-e1-entity-resolution-and-identity-assurance]]
