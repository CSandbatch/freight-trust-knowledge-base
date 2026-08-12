---
type: source
status: active
schema_version: 1.0.0
source_class: vendor
verification: retrieval-failed
accessed: 2026-08-07
updated: 2026-08-07
review_by: 2027-02-07
tags:
- type/source
- domain/freight
- domain/procurement
- confidence/vendor
- audience/internal
- programme/g1
- lifecycle/active
- domain/data-access
---
# PIERS (S&P Global) — licence terms remain unobtainable

The requested page could not be retrieved by any route attempted. A different S&P Global
page **was** retrieved, and it establishes the useful thing: **S&P Global does not publish
PIERS pricing anywhere public.** That is a confirmed negative finding, and it is enough to
close the procurement question without ever seeing a number.

`verification: retrieval-failed` is retained deliberately, because the target artefact —
actual licence terms — was not obtained. The negative finding below is separately sourced
and does not upgrade this card.

## Retrieval log

| Target | Route | Result |
|---|---|---|
| `https://www.spglobal.com/marketintelligence/en/mi/products/piers.html` | direct fetch | **HTTP 403 Forbidden**, body not returned |
| same URL | `r.jina.ai` proxy | **HTTP 403** — proxy reached the origin and received *"You don't have permission to access"* |
| `https://www.spglobal.com/market-intelligence/en/solutions/products/piers` | `r.jina.ai` proxy | **HTTP 403**, access-denied page with an error reference number |
| `https://www.marketplace.spglobal.com/en/datasets/bill-of-lading-piers-(277)` | direct fetch | Title only — *"Bill Of Lading Piers \| S&P Global Marketplace"* — no body content |
| same URL | `r.jina.ai` proxy | **HTTP 200, content returned** |
| `web.archive.org` | — | **Not attempted.** The fetch tool is blocked from web.archive.org in this environment. Recorded as an untried route, not a failed one. |

The failure mode is **unchanged from the prior record**: HTTP 403 on the product page. What
is new is that the 403 now reproduces through an independent proxy with a distinct network
path, which means it is an origin-side access policy rather than a transient block on this
environment's egress. Treat `spglobal.com/marketintelligence` as **permanently unavailable
to automated retrieval**.

## What was retrieved, and what it establishes

S&P Global Marketplace. "Bill of Lading (PIERS) Dataset."
<https://www.marketplace.spglobal.com/en/datasets/bill-of-lading-piers-(277)> — retrieved
2026-08-07 via `r.jina.ai` proxy.

**The negative finding, from S&P Global's own product listing:** the page carries **no
pricing and no licence terms**. It routes the reader to a "Request More Information" button
and to `customercare@spglobal.com`. Pricing is obtained only through a sales conversation.

Product attributes the page does state, verbatim:

| Attribute | As published |
|---|---|
| Coverage | "U.S. waterborne import and export trade data covering 100% of U.S. port locations" |
| Countries | "Coverage of 213 trading countries" |
| International markets | "13 international markets" — Central America, Chile, Ecuador, India, Mexico, Peru, Vietnam among them |
| History | "Historical coverage from 2003"; "Earliest Significant Coverage" 2003 |
| Update frequency | "Daily" reporting, "Daily" latency |
| Delivery | "Feed" via FTP |

## Limits and scope

Vendor self-description of its own product. **Not independent market validation of
anything**, and specifically not evidence about bill-of-lading data quality, completeness,
or fitness for entity resolution.

The coverage figures above are S&P Global's marketing claims. "100% of U.S. port locations"
is unaudited and uncorroborated; the count of international markets differs between S&P
pages (13 on the marketplace listing; other S&P surfaces have been described secondhand as
18). **That discrepancy is preserved here as a discrepancy, not resolved.** Neither figure
is load-bearing for this programme.

Any figure describing PIERS volume — e.g. bills of lading processed per day — currently in
the vault came from search snippets, not from a retrieved S&P page. It stays
`snippet-only`. Nothing on this card corroborates it.

## Consequence for the programme

The procurement question is answerable without the number. PIERS pricing is **unpublished
and sales-gated**, which makes it unbudgetable in a Phase I proposal and unresolvable within
the proposal timeline. It can be **ruled out cleanly on that basis alone**, which is what
[[dataset-index]] already says it needs from this source. No further retrieval attempts are
warranted.

`review_by` at six months only because [[dataset-index]] carries this row; there is no
expectation the terms will become public.

## Consumers

[[dataset-index]] access-gated table and retrieval-failure table, PIERS rows.
