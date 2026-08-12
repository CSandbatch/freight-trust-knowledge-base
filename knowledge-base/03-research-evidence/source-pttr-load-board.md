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
- confidence/vendor
- audience/internal
- programme/g4
- lifecycle/active
---
# PTTR Load Board — vendor product documentation

**Classification.** Architecture: **closed proprietary platform; no knowledge-graph or
interoperability claim.** Primary focus: **routing/matching** (load board, drayage
emphasis), with carrier verification as an access gate rather than a product.

## Citation

PTTR Load Board. "About Us." <https://pttrloadboard.com/about-us/> — retrieved 2026-08-07.

## What the source establishes, in its own terms

Stated purpose, verbatim: **"to make freight movement faster, clearer, and more accessible
for everyone in the logistics chain."**

The platform functions as a load board, with drayage loads as a distinct service line.

On verification: PTTR states it requires all carriers to hold active MC and DOT numbers
verified through the **FMCSA SAFER** system before registration is permitted, and states
verbatim: **"We strictly prohibit unverified carriers from using the platform."**

Founding year stated on the page: **2019**. No founder is named.

## Axis-1 and axis-2 findings

No knowledge graph, ontology, open standard, or interoperability claim appears on the page.

The SAFER check is an **onboarding gate**, not a fraud-detection product. It is a lookup
against a public federal register at registration time — it does not persist a risk
assessment, monitor for change, or resolve identity across registrations. Placing PTTR on
the fraud-detection axis on the strength of that gate would overstate what the page says.
Axis 2 is routing/matching.

That distinction is worth keeping because it is the same one the programme rests on: a
point-in-time authority check and continuous identity assurance are different capabilities,
and the incumbent landscape mostly offers the former.

## Limits and scope

Vendor self-description; not independent validation. Small company; no volume, coverage, or
user-count figure is published. The About Us page is thin and undated apart from the
founding year.

**Not confirmed by this retrieval:** the existing G4 row's claim that PTTR was "spun out of
a brokerage" does not appear on the About Us page as retrieved.

## Consumers

[[evidence]] G4 competitor table, PTTR Load Board row.
