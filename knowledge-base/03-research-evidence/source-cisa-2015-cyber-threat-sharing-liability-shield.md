---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-07
updated: 2026-08-07
review_by: 2026-10-01
tags:
- type/source
- domain/adoption
- domain/federation
- domain/privacy
- confidence/primary
- audience/internal
- programme/g7
- programme/r-wn-02
- action/needs-verification
- lifecycle/active
- domain/freight
- domain/legal
---
# Source — CISA 2015: the liability shield as an isolated, expiring variable

The value of this precedent is not that it is the closest structural match to Freight
Trust — ASIAS is closer. It is that the shield here is a **separable, dated legal
instrument with a sunset clause**, which makes it the nearest thing available to a natural
experiment on whether legal protection is what produces sharing.

The statute is currently in force but expires 30 September 2026. `review_by` is set to that
date.

## Citation

Cybersecurity Information Sharing Act of 2015, enacted as Division N, Title I of the
Consolidated Appropriations Act, 2016; codified at 6 U.S.C. §§ 1501–1510.

| Provision | URL that worked | Verification |
|---|---|---|
| 6 U.S.C. § 1503 — Authorizations for preventing, detecting, analyzing, and mitigating cybersecurity threats | `https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title6-section1503&num=0&edition=prelim` | confirmed |
| 6 U.S.C. § 1504 — Sharing of information by the Federal Government | `https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title6-section1504&num=0&edition=prelim` | confirmed |
| 6 U.S.C. § 1505 — Protection from liability | `https://www.govinfo.gov/content/pkg/USCODE-2023-title6/html/USCODE-2023-title6-chap6-subchapI-sec1505.htm` | confirmed |
| 6 U.S.C. § 1510 — Effective period | `https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title6-section1510&num=0&edition=prelim` | confirmed; page currency shown as laws in effect 6 August 2026 |

## What the utility is

A framework for non-federal entities — private companies, including direct competitors — to
share "cyber threat indicators and defensive measures" with each other and with the federal
government, through federal and private hubs. 6 U.S.C. § 1503(c)(1):

> "A non-Federal entity may, for a cybersecurity purpose and consistent with the protection
> of classified information, share with, or receive from, any other non-Federal entity or
> the Federal Government a cyber threat indicator or defensive measure."

## What is shared

Cyber threat indicators and defensive measures. Contributor-side minimisation is mandatory
before sharing — § 1503(d)(2) requires removal of personal information "not directly
related to a cybersecurity threat." Same design pattern as ASIAS: the contributor
de-identifies, the hub does not.

## What caused participation — the load-bearing question

**Mechanism: a bundle of five statutory protections, all removable, none of them a
mandate.** Sharing is explicitly not compelled — § 1503(f) disclaims any obligation to
share, and § 1505(c) disclaims any duty created by receipt.

| Protection | Statutory locus | Effect |
|---|---|---|
| Liability shield | § 1505(a), (b) | "No cause of action shall lie or be maintained in any court against any private entity" for compliant monitoring; equivalent protection for compliant sharing and receiving |
| Antitrust exemption | § 1503(e)(1) | Exchange of threat indicators for cybersecurity purposes exempted from antitrust laws |
| FOIA exemption | § 1504(d)(3) | Shared indicators "deemed voluntarily shared information and exempt from disclosure under section 552 of title 5" and "withheld, without discretion, from the public under section 552(b)(3)(B) of title 5" |
| Non-waiver of privilege | § 1504(d)(1) | Provision to the Government "shall not constitute a waiver of any applicable privilege or protection provided by law, including trade secret protection" |
| Proprietary designation | § 1504(d)(2) | Information "shall be considered the commercial, financial, and proprietary information of such non-Federal entity when so designated by the originating non-Federal entity" |

Two of these have no counterpart in the ASIAS card and are directly load-bearing for
Freight Trust:

- **The antitrust exemption.** Competing carriers and brokers pooling operational data
  raises exactly the information-exchange concern that antitrust law addresses. CISA 2015
  is primary-source evidence that Congress judged an express exemption necessary before
  competitors would share. The Freight Trust design has no such exemption and no source in
  this vault has yet addressed the antitrust exposure of a broker/carrier data pool. That
  is a live gap, not a solved problem.
- **Originator-controlled proprietary designation.** The contributor, not the hub,
  designates its contribution as commercial and proprietary. This is an implementable
  access-control primitive.

**The sunset is the mechanism test.** 6 U.S.C. § 1510(a), verbatim as currently in force:

> "this subchapter and the amendments made by this subchapter shall be effective during the
> period beginning on December 18, 2015 and ending on September 30, 2026."

Congress attached an expiry to the protections rather than to the sharing activity itself.
Sharing threat data was never illegal; only the shield expires. So the repeated fight to
reauthorise it is itself evidence about what practitioners believe drives participation.

**Mechanism classification for G7:** *liability shield, with antitrust exemption and
disclosure protection.* No mandate. No neutral-intermediary requirement — the statute
authorises peer-to-peer as well as hub sharing, which distinguishes it from ASIAS and from
the Freight Trust model.

## Limits and scope

- Population: U.S. non-federal entities sharing cyber threat information. Period: 18
  December 2015 to 30 September 2026 as currently enacted.
- The statute establishes what protections Congress provided and that it provided them
  deliberately. It does **not** measure how many entities shared, or whether sharing volume
  responded to the protections. No participation dataset was retrieved. Any claim that the
  shield *worked* is unsupported by what is in this card.
- Cyber threat indicators are closer to a public good than freight operational data is.
  A shared indicator has near-zero competitive cost to the sharer and positive externality
  to everyone; a lane-level dwell time or rate does not. The mechanism transfers; the
  cost-benefit ratio facing the participant does not. Do not present this precedent as
  showing that a shield alone suffices where the withheld data has direct commercial value.

## Snippet-only — the 2025 lapse and 2026 reauthorisation

The following is **snippet-only** and is recorded as a lead, not admitted as fact. Search
results dated October 2025 through February 2026 (Mayer Brown, Covington's Inside Privacy,
Hunton, Davis Wright Tremaine, Norton Rose's Data Protection Report — all secondary legal
commentary, none retrieved in full) state that CISA 2015 lapsed on 30 September 2025, was
restored by short-term extension to 30 January 2026, and was then reauthorised through 30
September 2026 in a funding bill enacted 3 February 2026, by amending the sunset date in
6 U.S.C. § 1510(a).

What is **confirmed**: § 1510(a) currently reads "September 30, 2026," on a
`uscode.house.gov` page showing currency as of 6 August 2026. The lapse-and-restoration
narrative is consistent with that but was not verified against a public law.

Two things to do before any of this is cited outward, filed as follow-up rather than
resolved here:

1. Obtain the public law that amended § 1510(a) and confirm the lapse period.
2. Find any measurement of sharing volume across the lapse. If such a measurement exists,
   it is the closest thing to direct evidence on the shield-causes-participation question
   that this scan has identified anywhere. If it does not exist, that absence is itself
   worth recording.

`https://www.congress.gov/crs-product/IF12959` (CRS In Focus, *The Cybersecurity
Information Sharing Act of 2015: Expiring Provisions*) returned **HTTP 403 Forbidden**. It
is the obvious primary-adjacent route and should be retried.

## What this supports

- G7 in [[goals]] — the liability-shield branch, with the antitrust dimension that neither
  the ASIAS nor the Part 234 precedent surfaces.
- R-WN-02 in [[review-notes]] — originator-controlled proprietary designation is a
  concrete, predefinable reciprocal offer.
- [[experiment-e3-federated-access-and-policy-enforcement]] — originator-designated
  proprietary status as a policy attribute.

## Related

[[source-faa-asias-voluntary-safety-data-sharing]] · [[source-dot-airline-on-time-performance-reporting]] · [[source-fincen-314b-information-sharing-safe-harbor]]
