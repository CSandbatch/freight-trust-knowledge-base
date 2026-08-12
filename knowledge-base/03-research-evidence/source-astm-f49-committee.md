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
- domain/supply-chain
- domain/provenance
- domain/freight
- confidence/primary
- audience/internal
- programme/g5
- programme/g6
- lifecycle/active
- domain/standards
---
# Source — ASTM International Committee F49, Digital Information in the Supply Chain

## Citation

ASTM International. *Committee F49 on Digital Information in the Supply Chain* (committee
brochure), dated April 2025. Retrieved in full 2026-08-07 from
<https://mcsdocs.astm.org/committee-documents/F49%20Brochure%202025.pdf> (HTTP 200, PDF,
2 pages, read directly).

Supporting: ASTM International, *F3803-26, Standard Guide for Applying Goods Movement
Process Codes in Common Approaches to Transport Management*. Store record retrieved
2026-08-07 from <https://store.astm.org/f3803-26.html> (HTTP 200).

## What the source establishes

**Committee identity and governance.** F49 was formed in October 2022. It meets twice a
year, April and October, "with about 40 members attending over two days of technical
meetings." Membership at the brochure's date: 100. Standards publish in the Annual Book of
ASTM Standards, Volume 10.04. Six technical subcommittees. Leadership: Chair Jeffrey G.
Weiss; Vice-chair Jack B. Crumbly; Membership Secretary Drew Zabrocki; Secretary Robert
Handfield.

**Scope, verbatim:**

> "The promotion of knowledge, stimulation of research, and the development of standards
> and specifications, formulation of definitions and terminology, and development of
> recommended practices and guides related to the sharing and use of digital information in
> the supply chain. The Committee will coordinate with any other ASTM Technical Committees
> and other standards development organizations (SDO) with related interests and ensure
> that the standards are technology and vendor neutral, and the standards development
> process is consistent with WTO principles."

**Complete work-item list as of April 2025** — this is the load-bearing part, because it is
an exhaustive enumeration from the committee itself:

| Subcommittee | Designation | Title |
|---|---|---|
| F49.01 Terminology | F3682 | Standard Terminology for Goods Movement Process (GMP) Precise Foundational Definitions |
| F49.01 | WK87871 | Standard Terminology for Supply Chain Key Terms |
| F49.01 | WK88617 | Standard Terminology for NSAC Recommended Minimum Required Data Set |
| F49.01 | WK88966 | Standard Terminology for Supply Chain Stakeholders |
| F49.01 | WK90204 | Standard Terminology for DOT FLOW Initiative Data Elements |
| F49.01 | WK95024 | Standard Terminology for Supply Chain Location |
| F49.04 Recommended Practices, Guides, Specifications | WK87207 | Standard Practice for Container Availability |
| F49.04 | WK92031 | Standard Guide for the Goods Movement Process Statuses |
| F49.05 Enabling Technology | WK94483 | Standard Guide for Developing Evaluation Rubrics to Support Ontology-Based Classification of Emerging Technologies in the Digital Supply Chain |
| F49.06 Clarity, Measurement, Authenticity | D8558 | Standard Guide for Verification of a Certificate of Authentication Used to Track Products through Their Supply Chain by Utilizing Blockchain Technology |
| Technical report | TR5-EB | Resolving Data Language Barriers across Maritime Standards Vocabularies |

**Subcommittee scopes directly relevant to this programme:**

- **F49.05 Enabling Technology** names the technologies it will assess: "Blockchain, API,
  eBL, IoT, Knowlededge Graphs, AI" [*sic*, brochure spelling]. Knowledge graphs are named
  in an ASTM subcommittee scope — this is the clearest hook between F49 and this
  programme's architecture.
- **F49.06 Clarity, Measurement Accuracy, and Authenticity of Information** scope, verbatim:
  "to develop standards for the supply chain to ensure the clarity, accuracy, and
  authenticity of information, including measurements and supporting data relating to
  efficiency, security, health and safety, **identity**, product characteristics or their
  related processes and production methods, conformity assessment, and ESG factors, as well
  as related claims." (emphasis added). "Identity" appears in scope — but of *information
  about goods*, in a supply-chain-wide sense; no motor-carrier identity work item exists
  under it.
- **F49.03 Essential Data Elements** organizes data elements by numbered goods-movement
  stages (200-300 Posted to Pre-Booked, 300-400 Pre-Booked to Booked, 400-500 Booked to En
  Route, 700-800 Delivered to Invoiced, 800-900 Invoiced to Archived). Note the brochure
  prints "400-500 Booked to En Route" twice and omits a 500-700 band — a typesetting
  defect in the source, recorded here so it is not mistaken for a finding.
- **F49.04** use cases are enumerated and are maritime/container-centric: FMC MDTI use
  cases, Earliest Return Date, Empty Container Returns, Container Availability, FCL/LCL.

**F3803-26** (retrieved from store.astm.org): approved 2026, jurisdiction F49.04, priced
at $80.00 USD, PDF, sign-in required. Abstract, verbatim in part: "The guide will describe
how events occurring in the goods movement process will result in goods movement process
codes (GMPC) indicating the status of (or even a milestone for) a transport unit." This
confirms the direction of F49's actual published output: **event/status codes for transport
units**, not entity trust or carrier qualification.

## Negative findings

**Confirmed absence, April 2025 work-item list.** Across all six subcommittees and eleven
enumerated items, there is **no** work item on: carrier vetting, carrier selection, broker
duty of care, motor-carrier identity verification, chameleon carriers, freight fraud,
double brokering, detention, or dwell time. Not one of those terms appears anywhere in the
brochure.

**Confirmed absence, CAVRA.** No mention of CAVRA, Carrier Assure, or Cassandra Gaines
appears in the brochure. See [[source-cavra-and-bavra-standards]] for the full search scope
on the CAVRA/ASTM question.

**Scope limit on both absences.** The brochure is dated **April 2025**. It cannot speak to
work items registered after that date. `astm.org` returns HTTP 403 to automated retrieval
(see failure table), so no current work-item list was obtainable in this scan. The
statement the vault may make is: *as of ASTM's own April 2025 committee brochure, F49 had
no carrier-vetting, identity-verification, or detention work item; the position after April
2025 is unverified.*

## Failure modes recorded

| URL | Result | Alternative tried |
|---|---|---|
| `astm.org/membership-participation/technical-committees/committee-f49` | HTTP 403 | Wayback Machine — no archived snapshot available |
| `astm.org/news/new-suite-of-supply-chain-standards` | HTTP 403 | — |
| `mcsdocs.astm.org/committee-documents/F49 Brochure 2026.pdf` | HTTP 403 (2026 edition may not exist at that path) | 2025 brochure retrieved instead |
| `sn.astm.org/update/supply-chain-goods-movement-process.html` | DNS failure (`ENOTFOUND`) | — |
| `na.eventscloud.com/website/70168/F49/` | HTTP 200 but agenda content behind report generators; no work items visible | — |

`mcsdocs.astm.org` and `store.astm.org` both serve automated requests; `www.astm.org`,
`sn.astm.org` and `newsroom.astm.org` did not. Future retrieval should start with the two
that work.

## Limits and scope

- The brochure is promotional material, but it is ASTM's own and enumerates work items
  explicitly, which is what makes the absence finding usable. It is not a ballot record.
- F3803-26's full text is paywalled at $80. Only the store abstract was read.
- Membership count (100) and meeting cadence are as of April 2025 and will drift.

## Consequence for the programme

F49 is the most architecturally adjacent standards body found — its F49.05 scope names
knowledge graphs, and F49.06 covers information authenticity — but its actual work programme
is goods-movement status codes and terminology, container-availability practices, and a
blockchain certificate-of-authentication guide. **There is no incumbent standard occupying
the carrier-identity or facility-event-provenance space this programme proposes.** That is
a positive finding for first-of-kind positioning and an argument for F49 as a coordination
target rather than a competitor.

## Vault notes depending on this

[[evidence]] §G5, §G6 · [[goals]] G5, G6 · [[gap-register]] `GAP-008` ·
[[source-cavra-and-bavra-standards]]
