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
- domain/identity
- domain/procurement
- confidence/vendor
- audience/internal
- programme/g4
- lifecycle/active
- domain/freight
- domain/data-access
---
# OpenCorporates pricing — primary page

Replaces the third-party aggregator figures previously carried in [[dataset-index]], which
were marked `secondary` and flagged for re-verification before budgeting.

## Citation

OpenCorporates. "Pricing." <https://opencorporates.com/pricing/> — retrieved 2026-08-07,
HTTP 200 on direct fetch. Independently re-fetched the same day through the `r.jina.ai`
text-extraction proxy of the same URL; both passes returned identical figures.

## What the source establishes, in its own terms

Four tiers. Three are published with prices; the fourth is not.

| Tier | Annual | Monthly | Monthly call quota | Daily call quota |
|---|---|---|---|---|
| Essentials | £2,250/year | £225/month | "Up to 500 API calls/mth" | "Up to 200 API calls/day" |
| Starter | £6,600/year | £660/month | "Up to 2,500 API calls/mth" | "Up to 500 API calls/day" |
| Basic | £12,000/year | £1,200/month | "Up to 5,000 API calls/mth" | "Up to 1,000 API calls/day" |
| Enterprise | custom quote | — | not stated | not stated |

All three published tiers state "Internal & external use" permitted.

**Bulk data is Enterprise-only.** Enterprise is the sole tier listing "Bulk-data delivery"
alongside "API access", an "Enterprise support plan", and the ability to "Choose your
jurisdictions". No price is published for it.

**The free at-scale route exists and is conditional.** OpenCorporates offers "free
at-scale access to our data" to "investigative journalists, NGOs, universities and
anti-crime-and-corruption research groups", for applicants with "a project or initiative to
improve the use, quality and understanding of legal-entity data — or to shine a light on
the business world for the greater good."

## Limits and scope

Vendor self-description of its own commercial terms. Prices are **in pounds sterling** and
the page publishes no USD equivalent; any dollar figure entering a budget is a conversion
this vault must show, at a stated rate and date, per [[methodology]] §2.

Two things the page does **not** establish, and which the vault must not infer:

- **No free tier is published on this page.** The "~50 requests/day free tier" figure
  currently in [[dataset-index]] is not corroborated here. It may exist in the API
  documentation rather than the pricing page, but as of this retrieval it is
  `unverified` and should not be cited from this card.
- **The public-benefit programme's terms are not stated here.** The page describes who may
  apply and what kind of project qualifies. It does not state the open-license
  republication condition attributed to it in [[dataset-index]], nor any quota, duration,
  or approval process. That condition remains `secondary`.

The published quotas are small in absolute terms — the top published tier is 5,000 calls
per month. A carrier-scale entity-resolution corpus is not reachable through any published
tier; it requires Enterprise bulk delivery at an unpublished price, or an approved
public-benefit grant. That is a **procurement risk with no published ceiling**, and it
should be represented as such rather than as a line-item estimate.

Commercial pricing is volatile. `review_by` set at six months.

## Consumers

[[dataset-index]] access-gated table, OpenCorporates row. E1 adjudicated-subset sourcing in
[[experiment-e1-entity-resolution-and-identity-assurance]] and
[[dataset-e1-adjudicated-carrier-identity-cases]].
