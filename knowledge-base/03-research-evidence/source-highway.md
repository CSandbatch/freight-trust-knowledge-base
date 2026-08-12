---
type: source
status: active
schema_version: 1.0.0
source_class: vendor
verification: confirmed
accessed: 2026-08-07
updated: 2026-08-07
review_by: 2027-02-07
tags:
- type/source
- domain/freight
- domain/identity
- confidence/vendor
- audience/internal
- programme/g4
- lifecycle/active
---
# Highway — vendor product documentation

**Classification.** Architecture: **closed proprietary database; trademarked in-house
"Carrier Identity® Engine", no knowledge-graph or interoperability claim.** Primary focus:
**fraud detection** (carrier identity verification).

## Citation

Highway. "It all starts with Carrier Identity." <https://highway.com/> — retrieved
2026-08-07.

## What the source establishes, in its own terms

Highway states its function is to let brokers **"verify identity, authorize participation,
and enforce their carrier standard throughout the lifecycle of every load."** It describes
**"continuous verification throughout every freight transaction"**, **"validating identity,
authority, capability, insurance, and driver participation before, during, and after every
load."**

Performance claims, verbatim: **"99.9% fraud reduction when process is followed"**, a
customer case of **"92% percent reduction in freight fraud"**, and **"up to $100K
protection on qualifying shipments"** under a Performance Guarantee.

The architecture is presented as **"one platform"** with **"multiple layers of trust"**,
built on the trademarked **"Carrier Identity® Engine"**.

## Axis-1 finding

No knowledge graph, ontology, open data standard, or interoperability architecture is
claimed. Integration with third-party TMS and ELD platforms is stated, but the verification
store itself is presented as a proprietary competitive asset. The trademark on the engine
name is itself evidence of enclosure rather than shared infrastructure.

Note for whoever folds this into G4: the existing row credits Highway with being
"two-sided" (carriers can vet brokers). That is a *market-side* property, not an
architectural one. A two-sided proprietary database is still a proprietary database, and
this card classifies on architecture.

## Limits and scope

Vendor self-description; not independent validation. The 99.9% and 92% figures are
company-stated, carry the conditional **"when process is followed"**, and disclose no
denominator, population, period, or method. They may not be cited as measured fraud-
reduction performance.

## Consumers

[[evidence]] G4 competitor table, Highway row.
