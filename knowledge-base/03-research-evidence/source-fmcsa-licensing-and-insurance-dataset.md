---
type: source
status: active
schema_version: 1.0.0
source_class: dataset
verification: confirmed
accessed: 2026-08-07
updated: 2026-08-07
review_by: 2027-02-07
tags:
- type/source
- domain/freight
- domain/identity
- domain/data-access
- confidence/dataset
- audience/internal
- programme/g1
- lifecycle/active
- domain/regulatory
---
# FMCSA Licensing & Insurance — catalog record, successor files, and field list

The "daily difference feed" described secondhand in [[dataset-index]] is real, it is
confirmed verbatim, and it is **not** in the dataset the vault has been pointing at. The
record at `jeyh-5nsj` is an empty pointer to a website that has since been retired.

## Retrieval log

| Target | Route | Result |
|---|---|---|
| `https://data.transportation.gov/Trucking-and-Motorcoaches/Licensing-and-Insurance/jeyh-5nsj` | direct HTML fetch | **Failed again** — returned portal navigation, auth options, and branding only. The JS shell renders no dataset content to automated retrieval. |
| `https://data.transportation.gov/api/views/jeyh-5nsj.json` | Socrata metadata API | **HTTP 200, full metadata** |
| `https://data.transportation.gov/api/views/jeyh-5nsj/columns.json` | Socrata columns API | **HTTP 200 — empty array** |
| `https://catalog.data.gov/dataset/licensing-and-insurance` | `r.jina.ai` proxy | **HTTP 200, full record** |
| `https://li-public.fmcsa.dot.gov/LIVIEW/pkg_html.prc_limain` | `r.jina.ai` proxy | **HTTP 200** — retirement notice, no data functions described |

The Socrata **metadata API is the working route** past the JS shell. The HTML dataset page
remains unreadable to automated fetch; that failure mode is unchanged and should be treated
as permanent.

## What the `jeyh-5nsj` record establishes

Description, verbatim: **"Data collected through FMCSA's Licensing and Insurance programs
and information collections (BOC-3, OP-1, etc)."**

| Attribute | Value |
|---|---|
| Publisher | Federal Motor Carrier Safety Administration; owned by the FMCSA MCMIS team |
| Unique identifier | `DOT-99` |
| Category | Trucking and Motorcoaches |
| Update frequency | `R/P1D` — **daily** |
| Licence | **"Unknown License"**, per Project Open Data — `https://project-open-data.cio.gov/unknown-license/` |
| Public access level | Public |
| Created | 18 December 2018 |
| `rowsUpdatedAt` | 18 December 2018 — **identical to the creation timestamp** |
| Columns | **empty array** |
| Sole resource | `Licensing and Insurance`, TEXT/HTML, `http://li.fmcsa.dot.gov/` |
| Contact | `fmcsa.cdo@dot.gov`, 202-366-3397 |

**This is a link-only catalog stub.** It carries no columns, no rows, and no data — its
only resource is an HTML link out to the old L&I public website. The `rowsUpdatedAt` value
equalling the creation date confirms no data has ever moved through it. The declared "daily"
frequency describes the upstream system, not this record.

**And the link target is retired.** The L&I public site now carries, verbatim:

> "All current registration functionality-including new applications in URS, changes and
> filings via L&I (Public), and registration options in the FMCSA Portal-will be
> permanently retired on Thursday, May 14, at 8:00 PM ET."

with Motus launching "the following week". **The year is not printed in the retrieved
text** and is not asserted here. The same page carries an older notice: *"Effective December
2024, all insurance companies, financial institutions, and BOC-3 Blanket Agents using the
Licensing and Insurance Public website will be required to use Login.gov for Financial
responsibility filings and Form BOC-3 submissions."*

## The daily difference feed — confirmed, and located

The feed exists in the **Motus operating-authority file family**, not in `jeyh-5nsj`. Per
the FMCSA Open Data Program page (see [[source-fmcsa-mcmis-catalog]]), each of six Motus
files ships in two variants — an "All With History" baseline and a daily difference file
covering the past 24 hours — and:

> "Updated daily by 9:30 AM Eastern Time"
>
> "Daily difference files utilize blank strings to signal downstream drop/deletion events."

That blank-string convention is a real integration hazard and should be recorded wherever a
plan assumes the feed: a deletion is signalled by an empty value, not by a tombstone flag.

| File | Baseline (All With History) | Daily difference |
|---|---|---|
| Carrier | `inys-ebih` | `nakq-58th` |
| Insur | `c5y8-a4uz` | `x96h-evps` |
| InsHist | `3uet-3z4i` | `xe5s-wca7` |
| AuthHist | `yu5v-wbh6` | `dm5j-zc6c` |
| RevokeSuspend | `wb4f-neki` | `e67p-xyd5` |
| BOC3 | `6snj-ed7q` | (index page links the same ID for both — unverified) |

All at `https://data.transportation.gov/Trucking-and-Motorcoaches/<name>/<id>/about_data`.

## Field list — retrieved

Both via the Socrata metadata API, HTTP 200, accessed 2026-08-07. Both declare
`R/P1D` (daily) and both show `rowsUpdatedAt` of 6 August 2026 — i.e. these records are
live, unlike `jeyh-5nsj`.

**Motus Carrier — All With History (`inys-ebih`).** Description: *"Records for all
carriers/brokers/freight forwarders with active, inactive, or pending operating
authorities."* 28 fields:

`docket_number`, `usdot_number`, `rfc_number`, `op_auth_type`, `op_auth_status`,
`min_cov_amount`, `cargo_req`, `bond_req`, `bipd_file`, `cargo_file`, `bond_file`,
`bus_undeliverable_mail`, `mail_undeliverable_mail`, `dba_name`, `legal_name`,
`bus_street_po`, `bus_colonia`, `bus_city`, `bus_state_code`, `bus_ctry_code`,
`bus_zip_code`, `bus_telno`, `mail_street_po`, `mail_colonia`, `mail_city`,
`mail_state_code`, `mail_ctry_code`, `mail_zip_code`.

Treat 28 as the count **as extracted**, not as a certified schema. The list ends cleanly on
a mailing-address field, which is a plausible natural end, but the extraction step could
have truncated a trailing block. Anyone building against this schema should re-pull
`https://data.transportation.gov/api/views/inys-ebih/columns.json` directly.

**Motus Insur — All With History (`c5y8-a4uz`).** Description: *"Records for
carrier/broker/freight forwarder active or pending individual insurance policies"*, linked
by docket number. 11 fields:

| Field | Type | Definition as published |
|---|---|---|
| `docket_number` | text | "Unique FMCSA alpha-numeric identifying for-hire motor carriers" |
| `usdot_number` | text | FMCSA registration number for interstate motor carriers |
| `ins_form_code` | text | 34=Cargo, 82=BI&PD, 83=Cargo, 84=Surety Bond, etc. |
| `ins_type_code` | text | 1=BI&PD, 2=Cargo, 3=Bond, 4=Trust Fund |
| `ins_class_code` | text | P=Primary, E=Excess, or full security limit designations |
| `max_cov_amount` | number | "BI&PD Maximum Dollar Limit" |
| `underl_lim_amount` | number | "BI&PD Underlying Dollar Limit" |
| `policy_no` | text | policy identifier |
| `effective_date` | text | effective date of the policy |
| `insurance_company_name` | text | insurer administering the policy |
| `trans_date` | text | date FMCSA received the policy |

## Limits and scope

**Currency amounts are in thousands.** `max_cov_amount` and `underl_lim_amount` are
published "in thousands". Any figure lifted from these fields into a vault claim must show
the multiplication.

**Dates are typed `text`, not `date`.** `effective_date` and `trans_date` are strings. No
format is declared in the metadata. Parsing behaviour is unverified and cannot be assumed.

**The licence is "Unknown License" on the catalog record.** For E1's purposes this is the
same unresolved question as the Company Census File: it does not establish a right to
redistribute the data with a benchmark. Do not read "Public access level: Public" as a
redistribution licence — those are different fields answering different questions.

**No row counts.** The metadata API returns none for these datasets.

**The `bus_*` / `mail_*` address split matters for E1.** Two independent address families
per carrier, plus two undeliverable-mail flags, is precisely the attribute structure the
FMCSA vetting report's Match Score consumes (see
[[source-fmcsa-chameleon-carrier-vetting-report]]). Note what is *absent*: no officer name,
no SSN, no EIN, no D&B number. Four of the seven Match Score attributes are **not in the
public file**. This is a hard constraint on what E1 can reproduce from open data, and it
should be stated in the experiment rather than discovered during it.

**The legacy/modern fork.** Legacy "All With History" archive files remain published
alongside the Motus files. Any longitudinal identity work spans a schema cutover. This card
does not establish how the two schemas map, and no plan should assume they do.

## Contradiction to report, not fix

[[dataset-index]] lists the L&I source as `https://catalog.data.gov/dataset/licensing-and-insurance`
with the failure mode "catalog page would not render past its JS shell". Both halves need
revision: the catalog page **does** render through the proxy route, and the dataset it
describes is an empty stub pointing at a retired website. The live data is in the Motus
files listed above. Whoever owns that table should repoint the row.

## Consumers

[[dataset-index]] retrieval-failure table, L&I row.
[[dataset-fmca-registration-insurance-safety-records]].
[[experiment-e1-entity-resolution-and-identity-assurance]].
[[source-fmcsa-mcmis-catalog]].
