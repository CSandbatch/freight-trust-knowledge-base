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
# Amazon Relay — vendor product documentation

**Classification.** Architecture: **closed by design — single-shipper marketplace,
explicitly non-interoperable; no knowledge-graph claim.** Primary focus:
**routing/matching** (Amazon's own freight only).

## Citation

Amazon Relay. <https://relay.amazon.com/> — retrieved 2026-08-07.

## What the source establishes, in its own terms

Matching mechanisms, verbatim:

- Load board — **"Cherry pick one-off spot freight loads—Amazon has facilities in every
  state."**
- Post A Truck — **"Post your minimum rate along with when and where you want to go for a
  chance to automatically book loads."**
- Auctions — **"Single or bulk bid on lanes with full transparency into each auction's
  remaining time."**
- Round-trip contracts — **"Secure full schedules and steady revenue in advance with single
  or multi-week contracts."**
- Equipment marketplace — **"Rent your company's unused trailers to Amazon to reduce idle
  time."**

Closure is stated explicitly by Amazon, verbatim: **"Amazon does not tender loads through
any third-party load boards."** Loads are available only through the Relay portal or mobile
app.

Carrier eligibility, verbatim: **"A DOT number, with interstate authority and that has been
active for a minimum of 180 days, and a valid MC number"**; an FMCSA safety rating of
**"Satisfactory," "None," or "Not Rated"**; BASIC score thresholds (e.g. Unsafe Driving
below 60%); and Commercial General Liability insurance of **"$1,000,000 per occurrence"**.

## Axis-1 finding — the strongest closed case in G4

Amazon Relay is the only entry on the G4 list whose own marketing states the
non-interoperability outright. **"Amazon does not tender loads through any third-party load
boards"** is a first-party declaration that the marketplace does not federate. There is no
knowledge graph, ontology, or open-standard claim.

The eligibility rules are a **gating policy over public FMCSA data**, not a fraud-detection
product. The 180-day authority age is a crude anti-chameleon heuristic; it is worth noting
as an existing industry practice the programme's benchmark could be measured against, but
it is a threshold rule, not detection.

## Limits and scope

Vendor self-description; not independent validation. Terms are Amazon's published
requirements as of the access date and change without notice — hence `review_by`. Scope is
Amazon-tendered freight only, so Relay is not comparable to open-market load boards on
volume or lane coverage.

## Consumers

[[evidence]] G4 competitor table, Amazon Relay row.
