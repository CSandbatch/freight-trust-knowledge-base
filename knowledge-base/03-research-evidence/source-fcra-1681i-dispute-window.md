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
- domain/legal
- domain/governance
- confidence/primary
- audience/internal
- programme/g8
- lifecycle/active
- domain/freight
- domain/privacy
---
# FCRA dispute-investigation window — 15 U.S.C. §1681i

Closes the `unverified` status on the "30-day" figure recorded in [[dataset-index]] and
used to frame E3's correction-latency target.

## Citation

United States Code, Title 15, §1681i — *Procedure in case of disputed accuracy* (Fair
Credit Reporting Act §611).

Retrieved 2026-08-07 from two independent primary hosts, both returning identical
statutory language:

- Cornell Legal Information Institute — <https://www.law.cornell.edu/uscode/text/15/1681i>
  (direct fetch, HTTP 200)
- Office of the Law Revision Counsel, U.S. House of Representatives —
  <https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title15-section1681i&num=0&edition=prelim>
  (direct fetch, HTTP 200)

## What the source establishes, in its own terms

**The base window is 30 days, not a norm or a guideline but a statutory deadline.**
§1681i(a)(1)(A) requires the consumer reporting agency to

> "conduct a reasonable reinvestigation to determine whether the disputed information is
> inaccurate and record the current status of the disputed information, or delete the item
> from the file in accordance with paragraph (5), **before the end of the 30-day period
> beginning on the date on which the agency receives the notice of the dispute**"

and to do so **"free of charge"**.

**The window is extensible to 45 days on one specific trigger.** §1681i(a)(1)(B):

> "the 30-day period described in subparagraph (A) may be extended for not more than 15
> additional days if the consumer reporting agency receives information from the consumer
> during that 30-day period that is relevant to the reinvestigation"

**The extension is barred once the disputed item is already resolved.**
§1681i(a)(1)(C):

> "Subparagraph (B) shall not apply to any reinvestigation in which, during the 30-day
> period described in subparagraph (A), the information that is the subject of the
> reinvestigation is found to be inaccurate or incomplete or the consumer reporting agency
> determines that the information cannot be verified"

**Correction is mandatory on an adverse finding.** §1681i(a)(5)(A) requires the agency to

> "promptly delete that item of information from the file of the consumer, or modify that
> item of information, as appropriate, based on the results of the reinvestigation"

**Notification carries its own clock.** §1681i(a)(6)(A) requires written notice of the
results

> "not later than 5 business days after the completion of the reinvestigation"

## Limits and scope

This is the statute governing **consumer reporting agencies** under the Fair Credit
Reporting Act. It does not govern freight carrier registries, brokers, or any FMCSA
system, and nothing in it creates an obligation on the programme's proposed architecture.

Its value to this vault is as a **designed and legislated correction-latency precedent** —
an existing legal regime in which a data subject's dispute triggers a bounded
investigation, a mandatory correction, and a bounded notification. Cited as an analogue for
E3's correction-latency target, it is methodology transfer, not a performance benchmark.
Per [[methodology]] §2, the 30-day figure may not be imported as a *target* for freight
correction latency merely because it is the number Congress chose for credit reporting.

Note also that the "30 days" figure circulating in secondary sources is **incomplete**, not
wrong. The full statutory structure is 30 days, extensible to 45 on a single defined
trigger, plus 5 business days for notice. Any vault text stating a flat "30-day FCRA
window" is understating the outer bound by up to 20 days.

Retrieved in the `prelim` edition of the U.S. Code. `review_by` set at one year because
statutory text is amendable.

## Consumers

[[dataset-index]] retrieval-failure table, FCRA row — this card supersedes its `unverified`
status. E3 correction-latency framing in
[[experiment-e3-federated-access-and-policy-enforcement]].
