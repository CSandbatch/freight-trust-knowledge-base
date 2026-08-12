---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-07
updated: 2026-08-07
review_by: 2027-08-07
tags:
- type/source
- domain/adoption
- domain/federation
- domain/privacy
- confidence/primary
- audience/internal
- programme/g7
- programme/r-wn-02
- lifecycle/active
- domain/freight
---
# Source — FAA ASIAS: competing airlines sharing proprietary operational data with a neutral intermediary

The closest structural analogue found for the Freight Trust participation problem. Direct
competitors contribute confidential, commercially sensitive operational data to a
third-party-held pooled repository, and the participation mechanism is documented in
primary federal sources rather than inferred.

## Citation

U.S. Department of Transportation, Office of Inspector General. *FAA Has Made Progress in
Implementing ASIAS, but Work Remains To Better Predict, Prioritize, and Communicate Safety
Risks.* Report No. AV2021022, March 10, 2021.
URL that worked: `https://www.oig.dot.gov/sites/default/files/FAA%20ASIAS%20Final%20Report%20-%2003.10.2021.pdf`
Retrieved as PDF and read directly. Audit mandated by the FAA Reauthorization Act of 2018
(Pub. L. No. 115-254).

Supporting statute and regulation, retrieved separately and independently:

| Instrument | URL that worked | Verification |
|---|---|---|
| 49 U.S.C. § 40123, Protection of voluntarily submitted information | `https://www.govinfo.gov/content/pkg/USCODE-2023-title49/html/USCODE-2023-title49-subtitleVII-partA-subparti-chap401-sec40123.htm` | confirmed |
| 14 CFR Part 193, Protection of Voluntarily Submitted Information | `https://www.govinfo.gov/content/pkg/CFR-2023-title14-vol3/xml/CFR-2023-title14-vol3-part193.xml` | confirmed |

## What the utility is

ASIAS — Aviation Safety Information Analysis and Sharing. Per OIG (p. 1):

> "In 2007, FAA contracted with the MITRE Corporation (MITRE) to develop the Aviation
> Safety Information Analysis and Sharing (ASIAS) program to advance safety by sharing
> safety data and other information."

> "ASIAS serves as the central repository of both public sector and internal FAA databases,
> as well as proprietary (i.e., confidential or 'protected') data, such as information from
> voluntary safety programs, including Flight Operational Quality Assurance (FOQA), the
> Aviation Safety Action Program (ASAP), and the Air Traffic Safety Action program (ATSAP)."

MITRE is not a regulator and not a competitor. OIG footnote 1 (p. 1): "MITRE Corporation
manages a research and development center for FAA, the Center for Advanced Aviation System
Development. MITRE has continued to have a role in maintaining and integrating ASIAS data."
This is the neutral-intermediary position the Freight Trust design assumes.

The program comprised 104 data sources at the time of audit (p. 3).

## Who participates

Per OIG (p. 5) and Exhibit D (p. 27), as of September 1, 2020:

| Category | Count |
|---|---|
| Commercial air carriers | 41 |
| General aviation operators | 125 |
| Industry associations, labor, flight training, MRO, government | listed, not counted |

> "by September 2020, ASIAS grew to include data from 41 airlines, which according to FAA
> represents 99 percent of air carrier operations."

Exhibit D names direct commercial rivals in the same pool: American Airlines, Delta Air
Lines, United Airlines, Southwest Airlines, JetBlue Airways, Spirit Airlines, Alaska
Airlines, Frontier Airlines, plus cargo competitors FedEx Express, United Parcel Service,
Atlas Air/Polar Air Cargo and ABX Air. Labor organizations are also participants (ALPA,
IPA, IBT — International Brotherhood of Teamsters, SWAPA, NATCA).

The presence of both carriers and the Teamsters at the same table is directly relevant to
the freight case, where OOIDA and driver-side interests sit opposite carrier management.

## What is shared

Confidential operator-sourced data: FOQA (digital flight data recorded off aircraft
recorders) and ASAP (free-text employee-submitted safety reports), plus ATSAP from FAA air
traffic. Non-confidential sources include NTSB and BTS databases (p. 3, Table 1 p. 4).

De-identification is done by the contributor before transmission, not by the hub (p. 4–5):

> "Air carriers remove aircrew and company identifying information before submitting data
> to ensure that data contributors cannot be uniquely identified."

## What caused participation — the load-bearing question

Four mechanisms operate together. None of them is "the platform was neutral."

**1. Statutory protection from disclosure (the shield).** 49 U.S.C. § 40123(a), verbatim:

> "Notwithstanding any other provision of law, neither the Administrator of the Federal
> Aviation Administration, nor any agency receiving information from the Administrator,
> shall disclose voluntarily-provided safety or security related information if the
> Administrator finds that— (1) the disclosure of the information would inhibit the
> voluntary provision of that type of information and that the receipt of that type of
> information aids in fulfilling the Administrator's safety and security responsibilities;
> and (2) withholding such information from disclosure would be consistent with the
> Administrator's safety and security responsibilities."

The causal logic is written into the statutory test itself: the finding the Administrator
must make is that *disclosure would inhibit voluntary provision*. Congress named the
chilling effect as the thing the shield exists to prevent. Implemented at 14 CFR § 193.7,
which adds: "The FAA does not disclose information that is designated as protected under
this part in response to a FOIA request."

**2. A firewall between the pool and the regulator's own enforcement arm.** This is the
sharpest finding in the OIG report and the one most transferable to freight (p. 20):

> "Further, FAA told us that ASIAS was never intended to be an oversight tool as the
> information provided by stakeholders is from voluntary safety programs. For that reason,
> the Agency has been cautious in disseminating it to the oversight workforce."

The regulator deliberately withholds the pooled confidential data from its own inspectors.
OIG treats this as a program *deficiency* to be partially remedied (Recommendation 2), but
records it as the operating rationale. FAA accepted the recommendation only to disseminate
*aggregated, national-level* metrics — not participant-identified data.

**3. Non-punitive treatment at the point of submission.** OIG footnote 3 (p. 1) defines
ASAP as:

> "a voluntary safety program for air carrier and repair station employees to self-report
> safety violations to air carriers and FAA without fear of reprisal through legal or
> disciplinary actions."

The individual submitter is immunised, not only the firm.

**4. Reciprocal benefit available nowhere else, gated on membership** (p. 19):

> "One key benefit of nationwide trends is the ability to benchmark an air carrier's
> performance against aggregate nationwide trends, which includes other carriers.
> Benchmarking can be used to support operational safety assessments as part of an SMS and
> a proactive safety culture but are only accessible by the carriers based on the
> governance of the ASIAS program."

Membership is the only route to the national comparator. OIG also records the corroborating
negative: without it, "when a problem is identified at a carrier, an inspector has to call
other operators to see if they are having the same problem" (p. 19).

**5. Contractual instrument.** OIG footnote 7 (p. 4): "ASIAS participants sign a Memorandum
of Understanding with MITRE outlining the responsibilities between parties for the
collection, storage, use, and dissemination of shared data." The MOU is with the neutral
intermediary, not with the regulator and not bilaterally between competitors.

**Governance** is shared, not agency-run (p. 5): "The ASIAS Executive Board (AEB) oversees
the ASIAS program. The Board includes representatives from various FAA offices, the
National Aeronautics and Space Administration (NASA), commercial airlines, manufacturers,
and labor organizations."

**Mechanism classification for G7:** *liability shield + enforcement firewall + exclusive
reciprocal benefit, under shared governance.* Not a mandate — participation is voluntary
throughout. Not market pressure alone.

## Limits and scope

- Population: U.S. commercial and general aviation operators. Period: program launched
  2007; participant counts are as of 1 September 2020; report published 10 March 2021.
- "99 percent of air carrier operations" is **FAA's characterisation as reported by OIG**,
  not an independently computed OIG figure. The report attributes it: "which according to
  FAA represents 99 percent." Do not restate it as an audited number.
- The 41-airline and 125-operator counts are administrative records (participant roster),
  not estimates.
- The report does **not** contain a survey of carriers asking why they joined. The causal
  claims above rest on (a) statutory text stating the incentive rationale, (b) the agency's
  own explanation of why it firewalls the data, and (c) the documented exclusivity of the
  benchmark benefit. This is strong circumstantial evidence of mechanism, not a measured
  attribution. A study that *measured* the participation decision was not found in this
  scan.
- ASIAS is a safety-data pool with no direct commercial-rivalry payoff to withholding in
  the way a freight rate or lane-level dwell figure has. The analogy transfers on structure
  (neutral hub, competitor contributors, confidentiality, exclusivity of the aggregate) and
  on mechanism, not on the commercial stakes.
- Time-sensitive elements: participant counts, and the ASIAS 2.0/3.0 schedule (OIG records
  a 2-year delay and a 2025 target for ASIAS 3.0, p. 16). Do not cite the roadmap as
  current.

## Retrieval notes

`https://www.faa.gov/sites/faa.gov/files/2021-11/FAA_Report_on_Aviation_Safety_Information_Analysis_and_Sharing_ASIAS_03312020.pdf`
returned **HTTP 403 Forbidden**; the FAA-authored ASIAS report was not obtained. So did
`https://www.faa.gov/sites/faa.gov/files/2022-11/14CFR_Part193.pdf`; Part 193 was obtained
instead from govinfo. A PHMSA-hosted FAA ASIAS briefing deck downloaded but did not yield
extractable text. None of those failures affects the claims above, all of which come from
the OIG report, the U.S. Code, or the CFR.

## What this supports

- G7 in [[goals]] — the first analogous precedent with a documented participation mechanism.
- R-WN-02 in [[review-notes]] — supplies candidate reciprocal offers to predefine and
  measure: enforcement firewall, disclosure shield, membership-gated national benchmark.
- [[experiment-e4-participation-and-small-carrier-equity]] — the exclusivity-of-aggregate
  lever is testable as a participation offer.
- [[experiment-e3-federated-access-and-policy-enforcement]] — contributor-side
  de-identification before transmission is an implementable design precedent.

## Related

[[source-dot-airline-on-time-performance-reporting]] · [[source-cisa-2015-cyber-threat-sharing-liability-shield]] · [[source-fincen-314b-information-sharing-safe-harbor]]
