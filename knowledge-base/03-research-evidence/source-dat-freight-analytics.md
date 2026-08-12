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
- domain/orchestration
- domain/identity
- confidence/vendor
- audience/internal
- programme/g4
- lifecycle/active
---
# DAT Freight & Analytics — vendor product documentation

**Classification.** Architecture: **closed proprietary database; no knowledge-graph or
interoperability claim.** Primary focus: **routing/matching** (load board and rate
analytics), **with a secondary carrier-vetting product (CarrierWatch)**.

## Citation

DAT Freight & Analytics. "Products." <https://www.dat.com/products> — retrieved
2026-08-07.

DAT Freight & Analytics. "CarrierWatch." <https://www.dat.com/broker/carrierwatch> —
retrieved 2026-08-07.

## What the source establishes, in its own terms

Load board, verbatim: **"Get the most relevant matches for your business – the right load
for the right truck at the right price"**.

Rate data, verbatim: **"The industry standard in truckload pricing. Get the most accurate
insights into past, present and future freight rates."**

Carrier vetting — the CarrierWatch product, verbatim from the products page: **"Qualify
and monitor carriers with ease. Avoid dispatching out-of-service or unsafe carriers"**. The
CarrierWatch page states it monitors **"a carrier's MC authority, safety ratings, insurance
status"** and a carrier's **"DOT profile,"** including **"inspections, crash data,
insurance renewals and cancellations."**

## Axis-1 finding

Neither page mentions a knowledge graph, ontology, open standard, or interoperability
architecture. DAT's rate and transaction history is a proprietary warehouse sold as a
subscription product; its value proposition is exclusivity of coverage, not shared
infrastructure.

## Contradiction with the current G4 intro — reported, not fixed

[[evidence]] G4 states: "**Only Truckstop.com (via RMIS) spans both fraud/vetting and
load-matching** — everyone else is single-focus."

DAT's own site contradicts the "only" in that sentence. DAT operates a load board **and**
CarrierWatch, a carrier qualification and monitoring product. The current DAT row in G4
does not mention CarrierWatch at all.

The distinction that may rescue the original claim is real but must be stated explicitly
rather than implied: CarrierWatch as described is **compliance and safety monitoring** —
authority, insurance, safety ratings, crash and inspection data — and the CarrierWatch page
contains **no fraud or double-brokering language**, whereas Truckstop's RMIS explicitly
does. So DAT spans matching plus *vetting*; it does not clearly span matching plus *fraud
detection*. Filed for the human pass; this card does not amend G4.

## Limits and scope

Vendor self-description; not independent validation. "The industry standard in truckload
pricing" and "most accurate" are unsupported marketing superlatives and may not be cited as
findings. No coverage or accuracy figure is published on either page.

**Not confirmed by this retrieval:** the existing G4 row's claims about Trucker Tools,
Outgo factoring, a Convoy Platform acquisition in 2025, Roper ownership, and a "~$1T txn
history" figure do not appear on either page as retrieved. They need their own sources.

## Consumers

[[evidence]] G4 competitor table, DAT row; [[evidence]] G4 intro paragraph (contradiction
above).
