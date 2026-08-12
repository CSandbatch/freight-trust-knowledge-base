---
type: moc
area: datasets
status: active
owner: dataset-registrar
version: 1.1.0
schema_version: 1.0.0
updated: 2026-08-07
tags:
- type/moc
- domain/freight
- domain/supply-chain
- confidence/mixed
- audience/internal
- lifecycle/active
- domain/knowledge-engineering
---
# Dataset Index

Every external data source, tool, and standard the programme has evaluated, with its
access route and what it can support. Consolidated from
[[dataset-scan-entity-resolution]] and [[dataset-scan-event-provenance-and-federation]]
(both compiled 2026-08-01) plus the eight dataset cards. One row — the SINTEF VRPTW
benchmark — originates in [[experiment-e5-orchestration-value]] rather than in any of
those three, and is marked accordingly in its verification cell.

**One dataset, one authoritative row.** Where a source appears in both scans with
different terms, reconcile here and file a `DRIFT-###`.

Verification vocabulary: `confirmed` (retrieved directly), `snippet-only` (search results
only), `retrieval-failed` (with mode), `not-attempted`.

**Verification is a retrieval record, not a source class.** The two scans mark confidence
differently. [[dataset-scan-entity-resolution]] publishes an explicit fetch log — five
artifacts were retrieved directly, everything else is search-derived — so its rows convert
cleanly. [[dataset-scan-event-provenance-and-federation]] marks each row
`primary`/`secondary`/`unverified` in evidence.md's *source-class* vocabulary and publishes
no fetch log, so `primary` there does **not** entail direct retrieval. Rows below carrying
`confirmed` on the strength of a `primary` marker are flagged inline and tracked as
`DRIFT-041`; do not read them as retrieved until L2 re-checks them.

**Audit note (2026-08-07).** This index was reconciled against its three source documents
under `GAP-013`. Twelve sources named in the scans had no row here, four dataset cards had
no representation at all, five verification markers claimed more than the scans record, and
four conflicts were filed rather than resolved. Details in [[drift-control]] `DRIFT-038` –
`DRIFT-041`.

**Refresh rule.** Anything priced, gated, or live carries `review_by` at three months
(2026-11-06). Stable federal datasets and published standards carry six (2027-02-06).
Loop L2 in [[agents-and-loops]] runs the refresh.

## Immediately usable — no agreement, no cost

| Source | Publisher | Access | Licence | Verification | Supports | Used by |
|---|---|---|---|---|---|---|
| [FMCSA Company Census File](https://catalog.data.gov/dataset/company-census-file) · [direct CSV](https://data.transportation.gov/api/v3/views/az4n-8mr2/export.csv?accessType=DOWNLOAD) | FMCSA / data.transportation.gov | Bulk download, CSV/JSON/XML via Socrata; no login, no API key, no agreement | Metadata licence field reads **"unknown"**; presumed public domain under 17 U.S.C. §105 but **not stated** — confirm, do not assume | `confirmed` — catalog page fetched directly; "last updated" 30 July 2026 | Clean seed entities for E1: legal/DBA name, USDOT number, address, entity type, status. Carrier size fields make fleet-size disaggregation feasible | E1, [[dataset-fmca-company-census-file]] |
| [BTS–ATRI Freight Mobility Initiative](https://data.bts.gov/Trucking-and-Motorcoaches/BTS-ATRI-Freight-Mobility-Initiative-County-to-cou/uta5-4eu5) | BTS | Free download, data.bts.gov Socrata, CSV/API | **Two layers, neither confirmed.** BTS-side: "standard public-domain federal data policy" per the scan, but the landing page did not return full metadata to automated fetch and no licence text was read. Upstream: the product is derived from ATRI's proprietary panel and **the ATRI terms are not stated on the BTS page at all** — confirm both before redistributing anything derived from it | `confirmed` for the product's existence; `snippet-only` for licence; scan class is "secondary/primary mix" | Travel-time calibration only. Derived from ~350,000 unique tractors, 2018–2024, aggregated to county pairs | E2, E5, [[dataset-bts-truck-travel-time-data]] |
| [GS1 EPCIS / CBV 2.0](https://www.gs1.org/standards/epcis) | GS1 | Free standard | Royalty-free per GS1 | `confirmed` (scan class `primary`; see `DRIFT-041`) | The event model for Aim 2: what/when/where/why plus business step | E2, E5 |
| [OpenEPCIS Test Data Generator](https://github.com/openepcis/epcis-testdata-generator) | OpenEPCIS | Open source, local generation | **Apache 2.0** | `confirmed` (scan class `primary`; see `DRIFT-041`) | Configurable synthetic EPCIS 2.0 / CBV 2.0 JSON-LD event sequences, today, at no cost. **The tool, not the corpus** — the generated logs are a separate to-build artifact | E2, E5, [[dataset-openepcis-generated-event-logs]] |
| [NIST Policy Machine](https://github.com/usnistgov/policy-machine-core) · [PDP](https://github.com/usnistgov/policy-machine-pdp) | NIST | Open source | NIST open-source terms (usnistgov GitHub org; **specific licence file not read**) | `confirmed` (scan class `primary`; see `DRIFT-041`) | The Aim 3 enforcement engine itself — NGAC reference implementation with PDP and EPP over gRPC | E3, [[dataset-nist-policy-machine-xacml-cases]] |
| [OASIS XACML 3.0 conformance tests](https://github.com/authzforce/core/tree/develop/pdp-testutils/src/test/resources/conformance/xacml-3.0-from-2.0-ct) | OASIS (originally AT&T) / AuthzForce | Free, public | OASIS committee material; Apache-licensed reuse in AuthzForce Core | `confirmed` (scan class `primary`; see `DRIFT-041`) | The `(policy, request, expected decision)` triple format for the E3 suite | E3, [[dataset-nist-policy-machine-xacml-cases]] |
| [NIST SP 800-162](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf) · [800-178](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-178.pdf) · [800-192](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-192.pdf) | NIST | Free PDFs | Public domain (NIST Special Publications) | `confirmed` (scan class `primary`; see `DRIFT-041`) | ABAC definitions; XACML-vs-NGAC comparison informing the un-preselected policy model; verification and test methods | E3 |
| [Process Discovery Contest 2020 / 2021](https://data.4tu.nl/articles/dataset/Process_Discovery_Contest_2020/14626020) | 4TU.ResearchData | Free download, DOI-cited | Open academic (4TU.ResearchData, DOI-assigned) | `confirmed` (scan class `primary`; see `DRIFT-041`) | The labeled-anomaly-injection methodology for E2 — 192–480 synthetic training logs plus ground-truth models and test logs **per year**, across both the 2020 and 2021 editions | E2 |
| [recordlinkage toolkit / Febrl data](https://github.com/J535D165/recordlinkage) | J535D165 | `pip install`; datasets ship with the package | Open source (BSD/GPL-family, **not re-verified**) | `confirmed` — repo fetched directly, on the ER scan's fetch log | Corruption methodology and a probabilistic-linkage baseline. 4 datasets, 1,000–10,000 records each. Person records — method transfers, content does not | E1 |
| [Gecko](https://github.com/ul-mds/gecko) | ul-mds (Medical Data Science group) | `pip`-installable | Open source; **specific licence not named in the scan** | `confirmed` — repo fetched directly, on the ER scan's fetch log | Best-maintained generate-then-corrupt engine found. Self-described beta; no built-in company-name or MC/DOT corruption, so person-name tables must be replaced with carrier-specific ones | E1 |
| [GeCo](https://github.com/kdurril/geco_synth) (Tran, Vatsalan & Christen, SIGMOD 2013) | Original ANU tool; community forks | Forks on GitHub (`kdurril/geco_synth`, `dobraczka/GeCoWrapper`) | Academic open source; per-fork terms not confirmed | `snippet-only` | Gecko's predecessor and the origin of the frequency-table-driven corruption pattern. **Superseded** — built for Python 2.7, no active development since 2013. Registered so it is not rediscovered as a fresh lead | E1 (superseded by Gecko) |
| [dedupe](https://github.com/dedupeio/dedupe) | dedupeio | `pip install` | MIT-family (scan's characterization, not a read licence file) | `snippet-only` — **not on the ER scan's fetch log**; described from PyPI/docs presence | A candidate matching method with active-learning labeling, not a benchmark generator | E1 |
| [Magellan / py_entitymatching / deepmatcher datasets](https://github.com/anhaidgroup/deepmatcher/blob/master/Datasets.md) | anhaidgroup (Mudgal et al., SIGMOD 2018) | Public repo + Magellan data repository | Academic open release | `snippet-only` — **not on the ER scan's fetch log** | The clean-vs-"dirty" variant construction pattern. 13 benchmark tasks, 3:1:1 splits. **Its precision/recall numbers must not be imported as targets** | E1 |
| [WDC Product Data Corpus](http://www.webdatacommons.org/largescaleproductcorpus/) | Univ. Mannheim | Public download | Open academic release | `snippet-only` — **not on the ER scan's fetch log** | The small-adjudicated-gold-standard-from-large-weak-corpus pattern: 4,400 manually verified pairs drawn from 26M+ offers | E1 |
| [NCVR linkage benchmark](https://hpi.de/naumann/projects/repeatability/datasets/ncvoters-dataset.html) | NC State Board of Elections; HPI repeatability project | Public FTP (`ftp://alt.ncsbe.gov/data/`), free | Public record | `snippet-only` — referenced *via* the HPI repeatability page; **not on the ER scan's fetch log** | **The highest-value analog found.** Real, not synthetic. Ground truth from researchers periodically re-downloading a public registry and using a persistent ID (NCID) — structurally what re-pulling FMCSA data over time would do | E1 |
| [IoT-23](https://www.stratosphereips.org/datasets-iot23) / TON_IoT | Stratosphere Lab; UNSW | Free download | Open academic (Stratosphere for IoT-23; UNSW for TON_IoT) | `confirmed` (scan class `primary`; see `DRIFT-041`) | Precedent for labeled tampering datasets outside process mining. No freight semantics | E2 |
| PLG / PLG2 / RT-PLG synthetic process-log generators | Academic (PLG2 is the maintained successor) | Via published papers and repositories; no single canonical download confirmed | Academic/open tooling; **redistribution terms vary by release and were not confirmed** | `snippet-only` — scan states these were "not independently verified as currently maintained/downloadable" | Same role as PDC: generate a clean base sequence, then apply the field's anomaly-injection methodology. A fallback if PDC's logs prove unsuitable, not a first choice | E2 |
| [Flower](https://flower.ai/) / FedML | Flower Labs; FedML | Free, open source | Open source; specific licences not confirmed | `snippet-only` — scan states project sites were "not independently fetched this pass" | **Optional stretch scaffold only.** Would host a cross-party *computation* demo. E3's core hypothesis is fully testable with the Policy Machine and an XACML-style suite alone — neither is a dependency | E3 (optional) |
| [ISOMORPH](https://github.com/tuhinsahai/ISOMORPH) | arXiv:2605.12768 | Free, open source | **MIT** | `confirmed` (scan class `primary`; see `DRIFT-041`) | Evidence that open supply-chain digital-twin tooling is active. Wrong unit — inventory/order/demand flow between echelons, not facility events | E2 (weak analog) |
| [NIST DP Synthetic Data Challenge assets](https://github.com/usnistgov/Differential-Privacy-Synthetic-Data-Challenge-assets) | NIST | Free, open source | Open (usnistgov GitHub org; specific licence not read) | `confirmed` (scan class `primary`; see `DRIFT-041`) | One privacy leakage class: re-identification risk in released synthetic/aggregate output. Does **not** address metadata/inference leakage or insider misuse. **Currently relied on in E3 with no provenance row — see `DRIFT-015`** | E3 (optional) |
| [LEAF](https://arxiv.org/abs/1812.01097) | arXiv | Open source | Open academic | `confirmed` (scan class `primary`; see `DRIFT-041`) | A benchmark-packaging template only. Evaluates ML training under federation, not policy enforcement | E3 (structure only) |
| [SINTEF VRPTW benchmark](https://www.sintef.no/projectweb/top/vrptw/100-customers/) | SINTEF | Free (per E5's prose; access route not independently established) | "Public research resource" — **asserted, not read**. No licence text has been retrieved | `not-attempted` — **appears in neither scan nor any dataset card.** Its only vault origin is [[experiment-e5-orchestration-value]]'s method-provenance table. The prior `confirmed` marker had no retrieval behind it. See `DRIFT-040` | Solver sanity-checking before freight-specific scenarios, so solver quality is not confused with architecture value | E5 |

## Access-gated — registration, agreement, or payment required

**None of these is a Phase I dependency.** They are registered so that no plan quietly
assumes them.

| Source | Gate | Who controls it | What it would give | Status |
|---|---|---|---|---|
| [ATRI Freight Performance Measures](https://truckingresearch.org/2012/02/freight-performance-measures/) — raw GPS panel | Negotiated data-sharing agreement; no self-service download | ATRI | The closest real analog to facility arrival/departure telematics. Billions of points, ~1M trucks, 10+ years | **Hard blocker.** See `DRIFT-005` — this row lost evidentiary content in an uncommitted edit |
| [PIERS](https://www.spglobal.com/marketintelligence/en/mi/products/piers.html) | Paid commercial licence; pricing unpublished, sales-gated | S&P Global | Bill-of-lading-level US waterborne trade events | `retrieval-failed` (HTTP 403). Terms are `snippet-only` |
| [OpenCorporates](https://opencorporates.com/pricing/) | Free tier rate-limited to ~50 requests/day and 200/month, and **requires open-licence share-alike republication of derived data**; bulk needs a paid plan (Essentials £2,250/yr · Starter £6,600/yr · Basic £12,000/yr · Enterprise on request) **or** a free at-scale grant for journalists, NGOs, universities and anti-corruption researchers — which is an *application*, and its eligibility terms have not been read | OpenCorporates | Company formation dates, officers, addresses, LEI/TIN/EIN across 140+ jurisdictions — the independent identity signal E1's adjudicated subset needs. US coverage varies by state and was not verified per state | Prices are `secondary` — confirmed via third-party aggregators (Zephira.ai, Datarade), **not OpenCorporates' own pricing page, which was never fetched**. Treat as indicative; re-verify before budgeting. Do not assume the research grant applies |
| [FMCSA SAFER Company Snapshot](https://safer.fmcsa.dot.gov) | No bulk product. Ad-hoc single-carrier query only (`safer.fmcsa.dot.gov/query.asp`), server-rendered HTML. The data.transportation.gov "SAFER Company Snapshot" listings are landing pages pointing back at the live system, **not hosted bulk datasets**. A bulk corpus would require scripted querying, whose terms-of-use position is unverified | FMCSA | Company ID, size, commodity info, safety rating, out-of-service inspection summary, crash history — per carrier, live | `snippet-only` for terms. Access mechanism corroborated by third-party sources (a `dot-safer-fmcsa-api` repo, a `browse.sh` skill doc), **not** by FMCSA's own terms page. **Gate is legal, not technical**: scripted bulk use is not confirmed as permitted and needs review before it enters any plan |
| [APM Terminals API Store](https://developer.apmterminals.com/) | Account + app registration + OAuth 2.0 bearer tokens; in practice a customer relationship. Terms are **not** stated as free or open | APM Terminals | Vessel schedule, import-container availability/status, gate and truck-appointment create/update/cancel, per-container and per-appointment granularity | Docs are public and read; live data is gated. Scan class `secondary` (vendor developer portal). Informs the E2 schema now, at no cost. Feeds [[dataset-permissioned-terminal-facility-event-feed]] |
| [Port Houston Data Integration](https://porthouston.com/toolbox/container-terminals/data-integration/) · [payload spec PDF](https://porthouston.com/wp-content/uploads/2025/07/AppoinmentPayloads.pdf) | Registration via api@porthouston.com for credentials; **terms not published** | Port Houston | Terminal appointment create/update/cancel and gate events via the Execution and Visibility Platform | Docs are public and read; live data is gated. Scan class `secondary`. Second independent schema cross-check. Feeds [[dataset-permissioned-terminal-facility-event-feed]] |
| [STB Carload Waybill Sample](https://www.stb.gov/reports-data/waybill/) | Restricted by STB rule to specific authorized uses — sensitive shipping and revenue data | STB | Stratified sample of US rail carload waybills | Not usable without an authorized arrangement. `primary` for the restriction itself |
| State Secretary of State registries | Fragmented — 50 states plus DC, separate systems, some free web search, some paid bulk-file programmes, formats vary | Each state | Formation date, registered agent, officers/managers, active/dissolved/administratively-dissolved status — the "new company, old carrier" discontinuity signal | `not-attempted` per state; **no state was individually researched**. OpenCorporates is the practical aggregation layer, and it carries its own gate above |

## Retrieval failures — the L2 refresh queue

Every one of these is currently cited from search snippets or not at all. `GAP-002`.

| Source | Failure mode | Why it matters |
|---|---|---|
| [FMCSA MCMIS Catalog](https://www.fmcsa.dot.gov/registration/mcmis-catalog) | HTTP 403 to automated fetch | Crash and inspection files — the safety-history signal behind GAO's second chameleon prong. Access mechanism, cadence and licence are all **unconfirmed**; driver-identifying fields are said to be excluded. Backs [[dataset-fmca-registration-insurance-safety-records]] |
| [FMCSA Licensing & Insurance](https://catalog.data.gov/dataset/licensing-and-insurance) · [portal listing](https://data.transportation.gov/Trucking-and-Motorcoaches/Licensing-and-Insurance/jeyh-5nsj) | Catalog page would not render past its JS shell | The daily-difference feed — a change log rather than a snapshot, which is what registration-churn detection actually needs. ~330,000+ authority holders per FMCSA's own description. **Fields, cadence and licence unconfirmed**; the scan declined to assume the census file's public-domain posture carries over. Backs [[dataset-fmca-registration-insurance-safety-records]], whose card asserts access terms this row does not support — see `DRIFT-039` |
| FMCSA, *Implementation of Methodology to Identify Chameleon Carriers* (Report to Congress) | HTTP 403 | Publicly posted and unread. Cite only as "this report exists" until retrieved |
| FMCSA Company Census File licence text | Metadata says "unknown" | Determines whether the seed corpus can be redistributed with the benchmark |
| FCRA dispute window, 15 U.S.C. §1681i | Not fetched from statute | The 30-day figure is `unverified`; it frames E3's correction-latency target |
| S&P Global PIERS terms | HTTP 403 | Only affects whether the source can be ruled out cleanly |
| [FMCSA Data Dissemination / Open Data Program](https://www.fmcsa.dot.gov/registration/fmcsa-data-dissemination-program) | HTTP 403 to automated fetch, per [[dataset-scan-entity-resolution]]'s fetch log — while [[dataset-scan-event-provenance-and-federation]] lists the same page as `primary` public documentation. **The two scans disagree**; see `DRIFT-038` | The umbrella terms page for all FMCSA bulk data. Until it is read, the access and redistribution terms for the census file, L&I and MCMIS are inferred rather than known |

## Evaluated and set aside — real and accessible, wrong unit of analysis

Registered so they are not rediscovered as fresh leads. Each is free and obtainable; none
answers a question the programme is asking.

| Source | Publisher | Access | Licence | Verification | Why it is set aside |
|---|---|---|---|---|---|
| [BTS Freight Analysis Framework (FAF) v5.7](https://www.bts.gov/faf/) | BTS | Free download tool plus visualization platform | "Public federal statistical product" per the scan; text not read | `snippet-only` (scan class `primary`) | State and metro freight-flow tonnage, value and ton-miles by mode. Aggregate flow statistics — no event-level or facility-level record, so nothing for tamper-detection design |
| [USACE Waterborne Commerce Statistics Center](https://www.iwr.usace.army.mil/About/Technical-Centers/WCSC-Waterborne-Commerce-Statistics-Center/) · [NDC portal](https://ndc.ops.usace.army.mil/wcsc/webpub/) | USACE / IWR | Free via W-DAPP and the NDC web portal | "US federal public data" per the scan; text not read | `snippet-only` (scan class `primary`) | Vessel trips and cargo tonnage by port and waterway, monthly and annual. Aggregate commodity tonnage, not vessel-call or terminal-gate events with source attribution |
| [FRA Data Portal](https://dataportal.fra.dot.gov/) | FRA | Public API; Form 54 accident/incident and Form 57 grade-crossing datasets | "Public federal data" per the scan; text not read | `snippet-only` (scan class `primary`) | Rail safety and accident reporting. Not shipment or terminal-dwell events |
| [FMCSA ELD data-transfer spec](https://www.fmcsa.dot.gov/hours-service/elds/eld-data-transfer-handout) | FMCSA | Public documentation | Public federal documentation | `snippet-only`; the companion Open Data Program page returned 403 — see `DRIFT-038` | **A format standard, not a dataset.** Defines what a driver-side HOS/telematics record must look like on demand to enforcement. No public bulk sample of actual ELD records was located. Schema reference only |
| [DataCo Smart Supply Chain](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis) | Mendeley Data V5 (2019); Kaggle mirrors | Free download | Mendeley Data licence (open, citation requested); Kaggle mirrors under their own dataset-specific licences — **two different licences for the same content, neither read** | `snippet-only` — located via search | It does carry fraud and late-delivery-risk labels, which is rare. But the unit is order/transaction, not facility event or dock timestamp, and it is not freight-trucking-specific. Useful only as evidence that labeled-fraud methodology exists in the wider supply-chain literature |
| [Meta Oversight Board case decisions](https://www.oversightboard.com/) | Oversight Board | Free public case reports and some aggregate statistics | Public publication; **not a structured downloadable dataset** | `snippet-only` (scan class `secondary`) | Not a dataset — a corpus of individual case reports. Value is the reporting *pattern* for a correction workflow: overturn rate, appeal volume, elapsed-time framing. Roughly 75 decisions 2021–Jan 2024 |
| Algorithmic recourse literature (e.g. [arXiv:2605.11373](https://arxiv.org/pdf/2605.11373)) | arXiv | Free | Open academic | n/a | **Not a dataset — a literature.** Belongs with `source-scout`. It concerns reversing a *model's* decision, not correcting a *factual record* and propagating the correction, which is what E3's redress workflow does |

## To build, or partner-dependent

Four artifacts the programme intends to have and does not yet. Three carry `to-build` or
`partner-dependent` cards; the fourth is the corpus the OpenEPCIS generator would produce,
which its card describes but which nobody has generated. Indexed here because a card
without an index row is how an assumed dependency gets into a plan.

| Dataset | Status | How it would be built | Licence of the build path | What it could establish | What it could not |
|---|---|---|---|---|---|
| [[dataset-e1-adjudicated-carrier-identity-cases]] | `to-build` | Blinded adjudication over permitted FMCSA seed records plus predicate-specific authoritative evidence (including targeted state corporate records where a sampled case requires them); governed by the E1 RC1 identity standard | Rights tracked per incorporated source/case; redistribution remains a separate release decision rather than being inferred from one seed dataset | Task A legal-person resolution; Task B identifier/registrant continuity; Task C typed relationships; calibration/abstention; reviewer agreement | Real-world chameleon prevalence or fraud-detection rate. Regulatory reincarnation is a separate disposition layer, not the primary gold label |
| [[dataset-openepcis-generated-event-logs]] (the corpus, derived) | `candidate`, corpus not yet generated | OpenEPCIS generator (Apache 2.0, row above) emitting the E2 schema, with inter-event timing calibrated against the BTS-ATRI product, then PDC-style labeled anomaly injection across four threat classes | Apache 2.0 tooling. **Output licence inherits the calibration input** — the BTS-ATRI upstream terms are unread, so a corpus calibrated on it may not be freely redistributable | Detection and false-alarm rate against a labeled tamper set; 100% provenance-metadata completeness; correction-workflow latency. A feasibility result | External validity. Synthetic timing is not facility ground truth. Per methodology, synthetic data supports feasibility claims only |
| [[dataset-permissioned-terminal-facility-event-feed]] | `partner-dependent` | A credentialed relationship with a terminal operator — APM Terminals or Port Houston are the two documented routes, both gated (see above) — or an ATRI data-sharing agreement | Unknown. Neither operator publishes terms; ATRI's are negotiated per agreement | Holdout validation of the E2 schema and provenance reconstruction against real events | Nothing yet. **Not a Phase I dependency, and nothing currently in the plan may assume it.** Availability, coverage and data rights are all open |
| [[dataset-partner-participation-burden-log]] | `to-build` | Consent-based collection from participating carriers, brokers, facilities and reviewers during a pilot | Consent-governed; instrument and consent terms not yet drafted | Reciprocal value, retention, and small-carrier burden by fleet-size band | Representativeness. Sample size depends entirely on recruitment. This is the G7/G12 participation-economics gap, and **no dataset found in either scan touches it** — see `GAP-004` |

## Confirmed absent

Findings, not gaps in the search. The proposal's first-of-kind argument rests on them.

| What does not exist | Scope of the search | Consequence |
|---|---|---|
| A public adjudicated carrier-identity benchmark with E1's legal-person/registrant/relationship layers | Public, academic, GAO/FMCSA, and commercial source scan | No such benchmark identified. GAO/FMCSA do provide substantial **screening prior art**, so E1 must not equate benchmark absence with absence of prior methods |
| A freight-specific facility-event benchmark | Public, academic, commercial | E2 builds one; G14 is greenfield |
| Historical/longitudinal MCS-150 snapshots (2000–2019) | MuckRock FOIA 2019-3095 marked "Fully Granted" (5 Feb 2021) released only a scanned image and correspondence; FMCSA said it "can't go as far back as requested" | No ready-made history for tracking reincorporation. A new narrow FOIA is possible but cannot be a dependency |
| Any participation-economics answer in the federated-learning literature | LEAF, FedML and Flower all checked. They are ML-training benchmarks; none addresses *why* a carrier or broker would participate | G7/G12 need stakeholder research or an adjacent-industry precedent (banking KYC utilities, airline on-time reporting), not a dataset. [[dataset-partner-participation-burden-log]] is the to-build answer. `GAP-004` |

## Unresolved leads

- **NIST ACPT / ACTS** (combinatorial access-control policy test generation) — referenced
  in secondary sources describing SP 800-192-era tooling; a direct fetch of the current
  NIST page did not surface it by name. Do not treat as available.
- **IBM Food Trust** — commercial, no public sample dataset located.
- **TradeLens** — discontinued Q1 2023, no dataset released. Value is narrative: a real
  freight provenance platform reached 175+ organizations and failed for governance and
  trust reasons, not technical ones.

## Card coverage

Each of the eight dataset cards in `03-research-evidence/`, and where it lands here. Kept
so the next audit is a diff rather than a re-read.

| Card | Card status | Represented by |
|---|---|---|
| [[dataset-fmca-company-census-file]] | `candidate` | Immediately usable — FMCSA Company Census File. Licence caveat also queued in Retrieval failures |
| [[dataset-fmca-registration-insurance-safety-records]] | `candidate` | Retrieval failures — FMCSA L&I and MCMIS Catalog rows. **The card's status is more confident than the evidence**; `DRIFT-039` |
| [[dataset-e1-adjudicated-carrier-identity-cases]] | `to-build` | To build — plus the Confirmed absent row that makes it necessary |
| [[dataset-openepcis-generated-event-logs]] | `candidate` | Immediately usable (the generator) plus To build (the corpus). Two objects, two rows, cross-referenced |
| [[dataset-bts-truck-travel-time-data]] | `candidate` | Immediately usable — BTS-ATRI Freight Mobility Initiative |
| [[dataset-permissioned-terminal-facility-event-feed]] | `partner-dependent` | To build / partner-dependent, fed by the APM Terminals and Port Houston gated rows |
| [[dataset-nist-policy-machine-xacml-cases]] | `candidate` | Immediately usable — NIST Policy Machine and OASIS XACML conformance rows |
| [[dataset-partner-participation-burden-log]] | `to-build` | To build — plus the Confirmed absent row for the federated-learning literature |

## Related

[[meta-moc]] · [[dataset-scan-entity-resolution]] · [[dataset-scan-event-provenance-and-federation]] · [[datasets-and-experiments-moc]] · [[gap-register]] · [[drift-control]] · [[methodology]]
