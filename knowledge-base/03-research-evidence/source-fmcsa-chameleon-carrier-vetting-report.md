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
- domain/freight
- domain/identity
- domain/regulatory
- confidence/primary
- audience/internal
- programme/g1
- lifecycle/active
- domain/regulatory
---
# FMCSA — risk-based vetting methodology to identify chameleon carriers (Report to Congress)

The report the vault has been citing as "this report exists". It has now been read. It is
the closest thing to a published government methodology for chameleon-carrier detection,
and it directly constrains what E1 can claim to be novel.

## Citation

Federal Motor Carrier Safety Administration. *The Implementation of a Risk-Based Vetting
Methodology to Identify Chameleon Carriers Applying for Operating Authority — Report to
Congress.* Submitted pursuant to Senate Report 112-157 accompanying the Transportation,
Housing and Urban Development, and Related Agencies Appropriations Bill, 2013.

PDF: <https://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/Implementation-of-Methodology-to-Identify-Chameleon-Carriers-Report-to-Congress-508.pdf>

Landing page: <https://www.fmcsa.dot.gov/mission/policy/implementation-risk-based-vetting-methodology-identify-chameleon-carriers-applying>

**Retrieval route.** Direct fetch of the PDF returned HTTP 403 — the same block recorded
previously. Retrieval succeeded through the `r.jina.ai` text-extraction proxy of the
identical PDF URL, which returns the document's own text. Two independent passes were run
with different prompts; both returned consistent title, quotations, and figures.

**Date caution.** No publication date is printed in the document body. The HTTP response
carried a `Last-Modified` of 13 Dec 2019, which is a server file timestamp and not a
publication date. The FMCSA landing page rendered without a posting date. The report's
content places it after the CY2013 application data was loaded. **The publication date is
therefore unconfirmed and must not be asserted.** Cite it as undated, submitted under a
FY2013 appropriations directive.

## What the source establishes, in its own terms

**FMCSA built a working prototype, not just a methodology.** The report names it:

> "This prototype module, named ARCHI (Application Review and Chameleon Investigation),
> currently resides in PHMSA's HIP environment."

**The methodology is a two-score screen — similarity plus motive.** This is the load-
bearing structural finding. Detection is not a single match score; it requires both that a
new applicant *resembles* a prior entity and that the prior entity had *reason to
disappear*.

*Match Score* is computed from identity-attribute overlap between the applicant and prior
carriers: carrier name, officer name, Social Security Number, Employer Identification
Number, Dun & Bradstreet number, telephone number, and address. The threshold is explicit:

> "companies with a Match Score of 1.5 or greater are identified as potentially having
> chameleon characteristics"

*Motive Score* is computed from evidence of prior adverse history on the matched entity:
bankruptcy declarations, severe crashes involving injury or death, FMCSA fines,
out-of-service orders, imminent hazard orders, and unsatisfactory or unfit safety ratings.

The two combine into the flagging rule. ARCHI colour-codes applications having

> "at least one matching company with a Match Score > 1.5 and a Motive Score ≥ 1."

**The regulatory hook is 49 CFR §386.73**, addressing carriers that affiliate or
reincarnate to avoid compliance with FMCSA requirements. Operating-authority authority is
49 U.S.C. §13902.

**The pilot population is small and dated.**

> "The ARCHI was uploaded with a large set of recent operating authority applications from
> Calendar Year 2013 (3,742) and was linked to FMCSA systems to receive weekly updates..."

**The reported result is qualitative, not measured.**

> "A preliminary analysis of the trial data runs indicated that the prototype tool
> generally is successful in providing a risk-based screening methodology, although
> refinements are needed..."

## Limits and scope

**The report publishes no performance figures.** No precision, no recall, no count of
applications flagged, no denials, no revocations, no false-positive rate, no labelled
ground truth. "Generally is successful" is the strongest outcome statement in the document.
That phrase may be quoted; it may not be converted into any numeric claim.

**3,742 is a pilot input count, not an incidence figure.** It is the number of CY2013
operating-authority applications loaded into the prototype. It says nothing about how many
were chameleons. It must never be cited as a population of chameleon carriers.

**No definition of "chameleon carrier" is given.** The document describes the behaviour —
reincarnation and affiliation to evade compliance — but supplies no formal definition. The
vault's [[glossary]] entry cannot be sourced to this report.

**The report is a status report on a prototype in another agency's environment.** ARCHI
resided in PHMSA's HIP environment at the time of writing. Whether it was ever deployed
into production operating-authority vetting is not established by this document, and this
card does not support any claim that it was.

## What this changes for the programme

The two-score structure — identity similarity gated by adverse-history motive — is
**published prior art from the regulator itself**. E1 cannot claim the *idea* of combining
match and motive as novel. What remains defensibly first-of-kind is what this report
conspicuously lacks: a labelled evaluation corpus and any published measurement. FMCSA
built a screen and reported that it seemed to work. Nobody published the numbers.

This strengthens rather than weakens the benchmark argument, and the proposal should make
that turn explicitly rather than continuing to cite the report as unread.

## Contradiction to report, not fix

[[dataset-index]] "Confirmed absent" table states, in the scope column for the labelled
chameleon-carrier dataset, that "the FMCSA report is unread". That is now false. The
underlying **negative finding still holds** — this report publishes no labelled pairs and
no matched-case data — but the scope statement needs rewriting by whoever owns that table.

## Consumers

[[dataset-index]] retrieval-failure table and "Confirmed absent" table.
[[experiment-e1-entity-resolution-and-identity-assurance]].
[[dataset-e1-adjudicated-carrier-identity-cases]]. [[glossary]] chameleon-carrier entry.
