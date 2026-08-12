---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-07
updated: 2026-08-07
review_by: 2027-02-07
tags:
- type/source
- domain/freight
- domain/identity
- domain/equity
- confidence/primary
- audience/internal
- programme/g6
- action/needs-verification
- lifecycle/active
---
# Source — NASTC White Paper on Freight Fraud

## Citation

National Association of Small Trucking Companies. *NASTC White Paper on Freight Fraud*.
Author: David Owen (NASTC President). Published on NASTC's own site.
<https://nastc.com/nastc-white-paper-on-freight-fraud/> (retrieved 2026-08-07, HTTP 200).

**Date unresolved.** The page as rendered shows "January 5" with no visible year. A search
snippet returned "January 24, 2025." These conflict and neither was confirmed on the page
itself. Recorded as *date uncertain, January, year most likely 2025* — do not print a
specific date in reviewer-facing prose without re-checking. `action/needs-verification`
applies to the date only; the content was retrieved.

## What the source establishes

NASTC — the trade association for small trucking companies — has a **published, first-party
position paper on freight fraud**. This is a genuine position, not inclusion by
plausibility.

**Definition of double brokering, verbatim:** "the broker hires one carrier, but a different
carrier hauls the load, unbeknownst to the original carrier."

**The identity-substrate problem, verbatim:** "fraudsters can quickly, easily pose as a
carrier, a broker, or both." The paper cites cases where criminals **purchased MC numbers**
to impersonate legitimate companies — the same authority-sale mechanism OOIDA describes
independently in [[source-ooida-senate-testimony-grand-theft-cargo]]. Two associations
converging on the same mechanism from different constituencies is worth noting.

**Two case illustrations given in the paper:**
- A California operator ran for three months and "double brokered over $1.9 million in
  freight charges" before disappearing with the proceeds.
- A Tijuana-based fraudster stole a legitimate carrier's identity, "posed as a shipper and
  re-brokered the same loads to other carriers."

**Position on FMCSA's complaint system.** NASTC characterizes FMCSA's National Consumer
Complaint Database as "not maintained closely or timely enough to be effective," with
minimal enforcement follow-up. **This independently corroborates OOIDA's NCCDB assessment**
and reinforces the warning against using NCCDB as a label source for a fraud benchmark.

**NASTC's primary ask, verbatim:** "The industry consensus solution is that OIG establish a
permanent task force focused on law enforcement in this area of transportation crimes."
NASTC's position is that enforcement should sit with the DOT **Office of Inspector General**
rather than FMCSA, on the grounds that FMCSA "lacks sufficient authority, resources, and
mission focus."

**Documented collective action.** Reported in trade coverage (`secondary`, not retrieved
first-hand): NASTC circulated a letter of support among lawmakers carrying signatures of
**more than 300 NASTC member companies**, including many owner-operators, stating
"Criminals are becoming more brazen" and that "this crime spree will only continue to get
worse until existing antifraud laws are effectively, consistently enforced." Attribute to
trade press; the letter itself was not retrieved.

## Quantitative claim — provenance missing

| Figure | Stated basis | Assessment |
|---|---|---|
| ~3,500 annual instances of freight fraud | **None given.** The paper does not identify who estimated it, over what period, or across what population. NASTC adds only that it "understates actual occurrences." | **Unusable as a quantity.** Do not cite. May be cited only as *"NASTC characterizes published counts as understating the problem."* |
| "$1.9 million in freight charges" (California case) | Case narrative | Single-case illustration, not a population figure |

Per [[methodology]] §2, the 3,500 figure is a number without a traceable source and is
refused admission as a quantitative claim.

## Limits and scope

- Advocacy white paper by the association's president. States NASTC's position and selected
  cases. Not a study.
- Publication date unresolved (above).
- NASTC's position addresses **enforcement architecture** — who prosecutes — not data
  standards, identity verification technology, or measurement. It is not evidence of
  demand for a verification infrastructure; it is evidence of demand for prosecution
  capacity. Do not overstate the alignment.
- NASTC did **not** sign the April 2026 DOJ cargo-theft coalition letter (see
  [[source-doj-cargo-theft-coalition-letter]] for the complete signatory list), which is
  consistent with its distinct OIG-focused ask.

## Vault notes depending on this

[[evidence]] §G6 (new row — NASTC was absent from the table) · [[goals]] G6 ·
[[gap-register]] `GAP-008`
