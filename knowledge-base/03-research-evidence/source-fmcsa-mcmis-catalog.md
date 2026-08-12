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
- domain/data-access
- confidence/primary
- audience/internal
- programme/g1
- lifecycle/active
- domain/identity
- domain/regulatory
---
# FMCSA MCMIS Catalog — retired URL, and the page that replaced it

Two findings, and they must not be collapsed. The URL the vault has been citing is **gone**,
not blocked. The information it held is **published, free, and now retrieved** at a
successor URL.

## The requested URL is retired

<https://www.fmcsa.dot.gov/registration/mcmis-catalog> — direct fetch returns **HTTP 403**,
as previously recorded. Fetched again 2026-08-07 through the `r.jina.ai` text-extraction
proxy, which reached fmcsa.dot.gov successfully and received an **HTTP 404 "Page Not
Found"** response rendering FMCSA's own navigation chrome.

The whole `/registration/mcmis-catalog*` tree returns 404 through the same route:

| URL | Status via proxy |
|---|---|
| `/registration/mcmis-catalog` | 404 |
| `/registration/mcmis-catalog-crash-file-documentation` | 404 |
| `/registration/mcmis-catalog-and-documentation-inspection-file-overview` | 404 |
| `/registration/mcmis-catalog/mcmis-catalog-census-file` | 404 |
| `/registration/mcmis-catalog-census-file-data-element-definitions` | 404 |
| `/registration/mcmis-catalog-description-Ordering-Options` | 404 |

These URLs still appear in search-engine indexes with titles and, in one case, a "last
updated January 4, 2024" attribution. **The index is stale.** The pages do not resolve.

The 404 is load-bearing evidence that this is a genuine retirement rather than a bot block:
a *different* FMCSA page (below) was retrieved successfully through the identical route on
the same day. The proxy can reach fmcsa.dot.gov. The catalog pages are not there.

The earlier `verification: retrieval-failed / HTTP 403` record was therefore **describing
the wrong failure**. The 403 is an edge bot-block that masks a 404 behind it. Any vault
text implying the MCMIS Catalog is a live page that automated tooling merely cannot read
should be corrected.

## The successor page, retrieved

Federal Motor Carrier Safety Administration. "FMCSA Open Data Program."
<https://www.fmcsa.dot.gov/registration/fmcsa-data-dissemination-program> — retrieved
2026-08-07 via the `r.jina.ai` proxy of that URL, HTTP 200, full content returned. Two
passes with different prompts returned consistent content.

### What it establishes, in its own terms

**Price.** The files are provided **"at no charge to the public"**. This retires the
"fee / CD-ROM / MCMIS Data Dissemination Program" model described in older secondary
literature. There is no ordering process; access is by download from the DOT Open Data
Portal at `data.transportation.gov`.

**Format.** All files are **"comma delimited"**, one record per row.

**The files offered**, grouped as the page groups them:

| Group | Files |
|---|---|
| Entities with a USDOT Number | Company Census File; Crash File; Vehicle Inspection File; Inspections Per Unit; Vehicle Inspections and Violations; Special Studies; Inspections and Citations |
| Entities with Operating Authority — modern (Motus) | Carrier; Insur; InsHist; BOC3; AuthHist; RevokeSuspend — each in an "All With History" baseline **and** a daily difference variant |
| Entities with Operating Authority — legacy archive | Carrier, Insur, ActPendInsur, AuthHist, BOC3, InsHist, Rejected, Revocation — all "All With History" |
| Safety Measurement System — input | Motor Carrier Census; Inspection; Crash; Violation |
| Safety Measurement System — output | AB Pass; C Pass; AB PassProperty; C PassProperty |
| New Entrant Safety Assurance | Out of Service Orders |

**Refresh cadence**, verbatim:

- USDOT-number files: *"The 'Entities with a USDOT Number' datasets are generated from a
  24-hour old database, which are updated daily and usually available on the DOT - Data
  Portal by 12:00 PM EST."*
- Operating-authority (Motus) files: *"Updated daily by 9:30 AM Eastern Time"*, with
  *"Daily difference files utilize blank strings to signal downstream drop/deletion
  events."*
- SMS: monthly snapshots taken *"on the third or last Friday of each month"*, usually
  posted *"by the 15th of the next month"*.
- Out of Service Orders: *"updated from a 24-hours old database"*.

**Documentation.** A "Data Dictionary and Schematic" is attached to each dataset's portal
page, not to this index page.

**Dataset URLs relevant to E1.** Company Census File —
`https://data.transportation.gov/Trucking-and-Motorcoaches/Company-Census-File/az4n-8mr2/about_data`.
Crash File — `.../Crash-File/aayw-vxb3/about_data`. Vehicle Inspection File —
`.../Vehicle-Inspection-File/fx4q-ay7w/about_data`.

## Limits and scope

The refresh cadences are the agency's **stated intent**, not measured availability. This
card does not establish that the files actually land by 9:30 AM or 12:00 PM, nor that any
given day's file is complete.

The page states price and format. It does **not** state a licence, and it does not resolve
the open question in [[dataset-index]] about whether the Company Census File may be
redistributed with a benchmark. That question stays open; see the L&I card for the parallel
"Unknown License" finding on the DOT portal side.

Row counts, historical depth, and per-field definitions are not on this page. They live on
the individual dataset pages, which are separate retrievals.

`review_by` at six months: FMCSA is mid-migration to Motus and this page has already
absorbed one URL structure. It will move again.

## Consumers

[[dataset-index]] retrieval-failure table, MCMIS Catalog row.
[[dataset-fmca-company-census-file]].
[[dataset-fmca-registration-insurance-safety-records]].
[[experiment-e1-entity-resolution-and-identity-assurance]].
