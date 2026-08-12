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
- domain/privacy
- confidence/mixed
- audience/internal
- programme/g7
- programme/r-wn-02
- action/needs-verification
- lifecycle/active
- domain/freight
- domain/legal
---
# Source — USA PATRIOT Act § 314(b) safe harbor: the banking leg, and why the KYC-utility question came back empty

Two findings in one card, because they belong together. The banking precedent that *is*
documented from primary sources is a liability safe harbor for competitor-to-competitor
information sharing. The banking precedent the task originally asked for — a shared KYC
utility with a documented cause of participation — was searched for and **not found in
primary or peer-reviewed form**. The absence is recorded below with its scope.

## Part 1 — What was confirmed: 31 CFR § 1010.540

### Citation

31 CFR § 1010.540, "Voluntary information sharing among financial institutions,"
implementing section 314(b) of the USA PATRIOT Act (Pub. L. 107-56).
URL that worked: `https://www.govinfo.gov/content/pkg/CFR-2023-title31-vol3/xml/CFR-2023-title31-vol3-sec1010-540.xml`
(2023 CFR annual edition.)

### What it permits, who participates, what is shared

Financial institutions and associations of financial institutions may

> "transmit, receive, or otherwise share information … regarding individuals, entities,
> organizations, and countries for purposes of identifying and, where appropriate,
> reporting activities that the financial institution or association suspects may involve
> possible terrorist activity or money laundering."

Participation is voluntary and is gated by an annual filing: an institution or association
intending to share "shall submit to FinCEN a notice," effective for one year and renewable.
There is no neutral hub required by the regulation — sharing may be bilateral, or through
an association.

### What caused participation — the mechanism

**Mechanism: statutory liability safe harbor, conditional on procedural compliance.**
Verbatim:

> "A financial institution or association of financial institutions that shares information
> pursuant to paragraph (b) of this section shall be protected from liability for such
> sharing, or for any failure to provide notice of such sharing, to the full extent
> provided in subsection 314(b) of Public Law 107–56."

And the condition that makes it a *conditional* shield rather than a blanket one — the
protection does not apply "to the extent such institution or association fails to comply
with paragraphs (b)(2), (b)(3), or (b)(4) of this section."

The design point for Freight Trust: the shield is not automatic on membership. It attaches
to a specific, verifiable procedural discipline — register, verify counterparty
registration, use the information only for the stated purpose, protect its
confidentiality. That is a compliance-conditional shield, and it is testable as a
participation offer in a way that a general assurance of confidentiality is not.

Note also that the shield covers **failure to provide notice of the sharing** — i.e. the
institution is protected against a claim by the customer whose information moved. In the
freight analogue the equivalent question is whether a broker sharing a carrier's
performance record is protected from that carrier's claim. No source in this vault
addresses that.

### Limits and scope

- Population: U.S. financial institutions subject to the Bank Secrecy Act. Read from the
  2023 CFR annual edition; later amendments unverified.
- Purpose scope is narrow and statutory — suspected money laundering or terrorist activity.
  FinCEN guidance is reported to have extended the reading to fraud (see failed retrievals
  below), but that extension is **not confirmed here**. Do not represent § 314(b) as a
  general-purpose commercial information-sharing permission; it is not one.
- The regulation establishes that Congress and Treasury judged a shield necessary. It does
  not measure participation, and no participation figure was retrieved.

### Retrieval failures on the FinCEN guidance

| Target | Route | Outcome |
|---|---|---|
| FinCEN § 314(b) Fact Sheet (issue date reported as 12 June 2026) | `https://www.fincen.gov/system/files/shared/314bfactsheet.pdf` | request timed out at 60s |
| Same, alternate host path | `https://fincen.gov/sites/default/files/shared/314bfactsheet.pdf` | request timed out at 60s |
| FinCEN § 314(b) Fact Sheet, December 2020 version | `https://www.fincen.gov/system/files/2026-06/314bfactsheet-12-2020.pdf` | request timed out at 60s |
| FinCEN news release, "FinCEN Guidance Clarifies 314(b) Information Sharing" | `https://www.fincen.gov/news/news-releases/fincen-guidance-clarifies-314b-information-sharing` | request timed out at 60s |

**Snippet-only, recorded as a lead:** search results indicate FinCEN issued an updated
§ 314(b) fact sheet on 12 June 2026, replacing the December 2020 version, clarifying that
the safe harbor extends to fraud and other specified unlawful activities and that real-time
sharing is permitted. **The fact sheet itself was not retrieved.** Nothing in that summary
is admitted as fact here. The regulatory text above is what this card supports.

## Part 2 — Confirmed absence: no primary or peer-reviewed account of why banks joined a shared KYC utility

The task named "a banking/financial KYC utility — e.g. SWIFT's KYC Registry" as a candidate
precedent. It was searched and rejected. Recording the scope so the search is not silently
repeated.

**Searched on:** 2026-08-07.
**Terms used:** `"KYC Registry" SWIFT participation mandatory regulatory requirement banks
independent evaluation peer-reviewed`; and, in the course of the § 314(b) work,
`FinCEN 314(b) safe harbor information sharing between financial institutions fact sheet`.
**Where:** general web search, with follow-through intended to the issuing body's own
domain.

**What came back:** the retrievable material on the SWIFT KYC Registry is `swift.com`
product and press-release pages, plus trade press (FinTech Futures, Global Trade Review,
Bank Systems & Technology). Under [[source-policy]], SWIFT describing the adoption of
SWIFT's own product is `vendor` class and cannot serve as independent validation of a
participation mechanism. Search results surfaced **no** independent evaluation and **no**
peer-reviewed study of the registry.

**Two things the search did establish, both snippet-only and not load-bearing:**
performing KYC on correspondents is itself a regulatory requirement, but joining the SWIFT
registry specifically is not — participation in the registry is voluntary. If that holds,
the causal structure would be *regulatory obligation on the underlying activity, with a
voluntary commercial utility competing to be the cheapest way to discharge it* — which is
cost-pressure-under-a-mandate, a fourth mechanism distinct from the three in G7. That is an
interesting hypothesis and it is **not evidenced**. It would need a primary or independent
source before it goes anywhere near a proposal.

**The finding, stated at the right strength:** in this scan, no primary or peer-reviewed
source was found that establishes what caused banks to participate in the SWIFT KYC
Registry. This is a confirmed absence *for the search scope described above only*. It is
not a claim that no such source exists — the scan did not cover the academic databases,
central-bank publications, or supervisory literature where one would plausibly sit. A
targeted search of BIS, FATF, and the ECB/Federal Reserve supervisory publications, and of
the AML/compliance research literature, has **not been attempted** and is the obvious next
step if the banking leg is needed.

## What this supports

- G7 in [[goals]] — the banking branch, partially. The mechanism found is a
  compliance-conditional liability safe harbor, not a neutral utility.
- R-WN-02 in [[review-notes]] — the compliance-conditional structure of the shield is
  directly usable in a predefined reciprocal offer.
- Records the SWIFT KYC Registry as searched and rejected, so the negative finding is not
  re-derived.

## Related

[[source-cisa-2015-cyber-threat-sharing-liability-shield]] · [[source-faa-asias-voluntary-safety-data-sharing]] · [[source-dot-airline-on-time-performance-reporting]] · [[source-policy]]
