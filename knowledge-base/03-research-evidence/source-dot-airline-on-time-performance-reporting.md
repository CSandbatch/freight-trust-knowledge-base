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
- domain/adoption
- domain/federation
- confidence/primary
- audience/internal
- programme/g7
- programme/r-wn-02
- action/needs-verification
- lifecycle/active
- domain/freight
---
# Source — U.S. DOT airline on-time performance reporting: the mandate case

The contrast case to [[source-faa-asias-voluntary-safety-data-sharing]]. Same industry,
same government, same carriers — and the mechanism is the opposite one. Airlines report
operational performance to a neutral government aggregator because a regulation compels
them to, backed by civil penalties. Nothing about neutrality, reciprocity or trust is doing
the work here.

Holding both cases lets the programme state the choice honestly: a freight evidence graph
gets participation either by shield-plus-benefit (ASIAS) or by rule (Part 234). It has
neither by default.

## Citation

| Instrument | URL that worked | Verification |
|---|---|---|
| 14 CFR Part 234, Airline Service Quality Performance Reports | `https://www.govinfo.gov/content/pkg/CFR-2023-title14-vol4/xml/CFR-2023-title14-vol4-part234.xml` | confirmed (2023 CFR annual edition) |
| 49 U.S.C. § 41708, Reports | `https://www.govinfo.gov/content/pkg/USCODE-2023-title49/html/USCODE-2023-title49-subtitleVII-partA-subpartii-chap417-subchapI-sec41708.htm` | confirmed |
| 49 U.S.C. § 46301, Civil penalties | `https://www.govinfo.gov/content/pkg/USCODE-2023-title49/html/USCODE-2023-title49-subtitleVII-partA-subpartiv-chap463-sec46301.htm` | confirmed |

## What the utility is

A monthly administrative collection run by a neutral federal aggregator. 14 CFR § 234.1,
verbatim:

> "The purpose of this part is to set forth required data that certain air carriers must
> submit to the Department and to computer reservations system vendors in computerized
> form, except as otherwise provided, so that information on air carriers' quality of
> service can be made available to consumers of air transportation. This part also requires
> that service quality data be disclosed directly to consumers."

The aggregator is the Office of Airline Information within the Bureau of Transportation
Statistics. Unlike ASIAS, the output is **published**, not pooled privately.

## Who participates

Defined by a revenue threshold, not by choice. 14 CFR § 234.3:

> "For air transportation taking place on or after January 1, 2018, this part applies to
> reportable flights as defined in § 234.2 that are held out to the public by certificated
> air carriers that account for at least 0.5 percent of domestic scheduled passenger
> revenues."

§ 234.2 defines a reporting carrier for post-2018 air transportation as "an air carrier
certificated under 49 U.S.C. 41102 that accounted for at least 0.5 percent of domestic
scheduled-passenger revenus [sic — spelling as printed in the CFR] in the most recently
reported 12-month period as defined by the Department's Office of Airline Information."

The threshold was lowered from 1 percent to 0.5 percent effective 1 January 2018 — a
regulatory decision to *widen* the participant set, not a market outcome.

## What is shared

14 CFR § 234.4:

> "Each reporting carrier shall file BTS Form 234 'On-Time Flight Performance Report' with
> the Office of Airline Information of the Department's Bureau of Transportation Statistics
> on a monthly basis, setting forth the information for each of its reportable flights
> operated by the reporting carrier and held out to the public on the reporting carrier's
> Web site and the Web sites of major online travel agencies, or in other generally
> recognized sources of schedule information."

Per-flight records: carrier and flight number, published and actual departure/arrival
times, delay magnitudes with causal codes, cancellation reason categories, diverted-flight
detail. This is flight-level operational data of the kind a carrier would ordinarily treat
as competitively sensitive — and it is published.

## What caused participation — the load-bearing question

**Mechanism: regulatory mandate, with a statutory civil-penalty backstop.**

The obligation is created by rule, not agreement. The verb in § 234.4 is "shall file."

Authority chain, confirmed end to end:

1. Part 234's authority citation, verbatim from the CFR: **"49 U.S.C. 329, 41708, and 41709."**
2. 49 U.S.C. § 41708 empowers the Secretary of Transportation to require air carriers to
   file "annual, monthly, periodical, and special reports" to the extent the Secretary
   "finds necessary to carry out this subpart."
3. 49 U.S.C. § 46301(a)(1) makes a person "liable to the United States Government for a
   civil penalty of not more than $25,000 (or $1,100 if the person is an individual or
   small business concern)" for violations of, among others, "chapter 417 (except sections
   41703, 41704, 41710, 41713, and 41714)" and regulations issued under it. Section 41708
   sits in chapter 417 and is not carved out, so Part 234 violations fall inside the
   penalty framework.

Note the statutory dollar figures are the ones printed in the U.S. Code; DOT applies
inflation-adjusted maxima by separate rule, which was not retrieved.

**The voluntary tail is small and structured.** § 234.7 permits opt-in reporting:

> "(a) In addition to the data for each reportable flight required to be reported by this
> part, a reporting carrier may report to DOT for every other nonstop domestic flight that
> it schedules, the reportable flight data specified in this part. (b) Any air carrier that
> is not a reporting carrier may file the data specified in this part for every reportable
> flight that it schedules, or for every nonstop domestic flight that it schedules."

With a lock-in condition: "A carrier that files a voluntary report must continue to do so
for a period of not less than 12 consecutive months." This is the most directly usable
design detail for freight — a voluntary tier exists, but it is bounded by a minimum
commitment period so that carriers cannot report selectively in good months. Worth
carrying into the participation protocol.

**Mechanism classification for G7:** *mandate.* No liability shield, no reciprocal
benefit, no confidentiality — the data is published against the reporting carrier's name.

## Limits and scope

- Population: certificated U.S. air carriers above 0.5 percent of domestic scheduled
  passenger revenue. Period: threshold current since 1 January 2018; regulatory text read
  from the **2023 annual CFR edition**. The current eCFR text was not retrieved (see
  below), so amendments after the 2023 edition are unverified. `review_by` set short for
  this reason and the note carries `action/needs-verification`.
- These are administrative records with a legal filing obligation, not survey or modeled
  data.
- The regulation establishes that reporting is compelled. It does **not** establish that
  compulsion was *necessary* — no counterfactual is available, and no source found in this
  scan tests whether these carriers would have reported absent the rule.
- The transfer to freight is not clean. DOT has certificating authority over air carriers
  and an existing filing relationship. The Freight Trust programme has no equivalent
  authority over brokers, shippers or facilities. Citing this precedent as *achievable*
  rather than as *the alternative mechanism* would overstate it.

## Retrieval notes

Three retrieval failures, recorded rather than worked around:

| Target | Route | Outcome |
|---|---|---|
| Current Part 234 text | `https://www.ecfr.gov/current/title-14/chapter-II/subchapter-A/part-234` | HTTP 302 redirect to `unblock.federalregister.gov`; not retrieved |
| BTS explainer "Number 14 — On-Time Reporting" | `https://www.bts.gov/topics/airlines-and-airports/number-14-time-reporting` | HTTP 403 Forbidden |
| DOT consent order, Frontier Airlines, Order 2025-1-2 | `https://www.transportation.gov/sites/dot.gov/files/2025-01/Frontier%20Airlines%20Consent%20Order%202025-1-2.pdf` | HTTP 403 Forbidden |

Wayback Machine was unavailable to this agent as an alternative route.

**Snippet-only, not admitted as fact.** Search results indicate DOT has issued consent
orders assessing civil penalties for Part 234 violations — a Frontier Airlines order
(2025-1-2, concerning § 234.11 website display of on-time performance) and a 2008 US
Airways order (reportedly $50,000, Part 234 and 49 U.S.C. § 41712). **Neither order was
retrieved.** These are recorded here as leads only. The enforcement *authority* above is
confirmed from the U.S. Code; a worked enforcement *example* is not, and must not be cited
as one until an order is actually obtained.

## What this supports

- G7 in [[goals]] — the mandate branch of the three-way mechanism question.
- R-WN-02 in [[review-notes]] — supplies the § 234.7 minimum-commitment-period device for
  the participation protocol.
- [[experiment-e4-participation-and-small-carrier-equity]] — a bounded voluntary tier with
  a 12-month floor is a testable participation condition.
- [[dataset-bts-truck-travel-time-data]] — same aggregator (BTS), different collection
  authority; do not conflate the two.

## Related

[[source-faa-asias-voluntary-safety-data-sharing]] · [[source-cisa-2015-cyber-threat-sharing-liability-shield]]
