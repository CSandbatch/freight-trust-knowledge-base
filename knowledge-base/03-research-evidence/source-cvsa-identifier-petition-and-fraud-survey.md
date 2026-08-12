---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-08
updated: 2026-08-08
review_by: 2026-11-08
tags:
- type/source
- domain/freight
- domain/regulatory
- confidence/mixed
- audience/internal
- programme/g6
- lifecycle/active
---
# Source — CVSA: the electronic-identifier petition, and a policy position still being formed

## Citation

**Primary, confirmed.** U.S. Department of Transportation, Federal Motor Carrier Safety
Administration. *Unique Electronic Identification of Commercial Motor Vehicles* (advance notice
of proposed rulemaking), 87 FR 58049–58053, September 23, 2022, Docket No. FMCSA-2022-0062.
Retrieved in full 2026-08-08 from
<https://www.govinfo.gov/content/pkg/FR-2022-09-23/html/2022-20643.htm> (HTTP 200, read
directly). This is the federal record of CVSA's petition for rulemaking.

**Secondary, for CVSA's current activity.** Land Line Media, "Survey asks truckers how to
fight cargo theft, chameleon carriers," **2026-08-06**,
<https://landline.media/survey-asks-truckers-how-to-fight-cargo-theft-chameleon-carriers/>
(retrieved 2026-08-08, HTTP 200).

**Retrieval failures.** See table below. `cvsa.org` returns HTTP 403 to automated retrieval
across all paths attempted, including its policy pages and its own PDFs — so no CVSA position
document was read from CVSA's own domain in this scan.

## What the source establishes

### CVSA has a long-standing, formally filed position on electronic vehicle identification (`primary`)

FMCSA's ANPRM exists **because CVSA petitioned for it**. Per the Federal Register, CVSA
petitioned on **July 26, 2010** for FMCSA to require that "every commercial motor
vehicle...used in interstate commerce be equipped with an electronic device capable of
communicating a unique ID number when queried by a law enforcement roadside system."

CVSA's stated rationale, verbatim from the FR summary of the petition: implementation would
"facilitate efficiency and efficacy in the roadside inspection program by more fully enabling
roadside enforcement agencies to target their efforts at high-risk operators, while at the same
time, providing an incentive for safe and legal operations."

CVSA "did not recommend specific technologies" but supplied "minimum suggested functional
requirements."

**On misidentification — attribution matters.** The FR text states that existing licence-plate
and USDOT-number reader systems "may not always capture the license plate or USDOT number
accurately. These issues may result in compliant carriers being stopped for roadside
inspections and, conversely, non-compliant or high-risk carriers being excluded from roadside
inspections." **This is FMCSA's characterisation in the ANPRM, not a quotation of CVSA.** Cite
it as FMCSA's, not CVSA's.

### CVSA's position on cargo theft, carrier identity theft, and reincarnated carriers does not yet exist — it is being formed right now (`secondary`)

As of **2026-08-06**, CVSA is running an anonymous industry survey on cargo theft, freight
fraud, and reincarnated ("chameleon") carriers. Land Line quotes CVSA's stated purpose,
verbatim: "As cases of these complex problems become more prevalent in the CMV industry, CVSA
is working to form the Alliance's policy positions and identify solutions to these issues."

Survey instrument: <https://www.surveymonkey.com/r/DKPKJY8>. Responses requested by
**2026-08-08** (extended from 2026-07-31). Reported survey content includes ranking the top
three issues affecting the industry from a list of cargo theft, financial theft, identity
theft, cargo fraud, data/information theft, and chameleon carriers, and describing steps
currently taken to prevent cargo theft, freight fraud, and identity theft. Results are stated
to inform CVSA's "recommendations and future strategies to address these issues across North
America."

The Ontario Trucking Association circulated the same survey under the title "CVSA Cargo Theft,
Motor Carrier Identity Theft and Reincarnated Carriers – Associate Member Survey"
(<https://ontruck.org/share-your-input-cvsa-cargo-theft-motor-carrier-identity-theft-and-reincarnated-carriers-associate-member-survey/>
— **HTTP 403, not retrieved**; title known from the search index only, `snippet-only`).

## Limits and scope

- **The 2010 petition is about identifying a *vehicle* to an *enforcement officer*, not about
  qualifying a *motor carrier* to a *shipper or broker*.** Its purpose is roadside inspection
  targeting. It is adjacent evidence that a recognised enforcement body regards reliable
  machine-readable identity as a precondition for risk-based targeting — not evidence of a
  CVSA position on commercial carrier vetting.
- The petition is **sixteen years old** and the rulemaking did not proceed. Its current status
  was not established from a CVSA source in this scan.
- CVSA's separate **Universal Electronic Identifier** advocacy — a manufacturing requirement
  sought in highway-bill reauthorisation — appears in search results referencing a CVSA
  reauthorisation white paper (`cvsa.org/wp-content/uploads/Universal-ID-CVSA-Reauthorization-Paper.pdf`).
  **That document was not retrieved** (403 direct; Wayback snapshot exists at
  `20250630132350` but `web.archive.org` is not fetchable from this environment). CVSA's
  reauthorisation position is therefore `snippet-only` and must not be quoted.
- The survey finding is `secondary` and, critically, **it establishes the absence of a position
  rather than a position.** Do not write "CVSA's position on chameleon carriers is X."
- CVSA's own *Guardian* magazine, Second Quarter 2025, carries cargo theft among its topics
  (confirmed from the Issuu listing for `cvsaorg`); **the article text was not retrieved** and
  its contents may not be characterised.

## Retrieval failures

| URL attempted | Result | Alternative tried |
|---|---|---|
| `cvsa.org/policy/` | HTTP 403 | — |
| `cvsa.org/policy/reauthorization/` | HTTP 403 | — |
| `cvsa.org/wp-content/uploads/Universal-ID-CVSA-Reauthorization-Paper.pdf` | HTTP 403 | Wayback snapshot located (`20250630132350`) but `web.archive.org` unfetchable from this environment |
| `cvsa.org/wp-content/uploads/CVSA-Comments-Unique-Electronic-Vehicle-Identifier-ANPRM.pdf` | HTTP 403 | Substituted the FMCSA ANPRM itself via govinfo — succeeded |
| `cvsa.org/inspections/level-viii-definition-purpose/` | HTTP 403 | — |
| `www.cvsa.org/news/cargo-theft-fraud-survey/` | HTTP 403 | Land Line (secondary) used instead |
| `ontruck.org/share-your-input-cvsa-…` | HTTP 403 | — |
| `federalregister.gov/documents/2022/09/23/2022-20643/…` | HTTP 302 to `unblock.federalregister.gov` | govinfo.gov mirror of the same FR document — succeeded |
| `issuu.com/cvsaorg/docs/cvsa_guardian_magazine_second_quarter_2025` | HTTP 200 but article body not rendered (metadata/nav only) | — |

`cvsa.org` should be treated as **not automatable**. Anything needed from CVSA's own domain
requires manual retrieval by a human.

## Negative findings — confirmed absences

**No CVSA position on detention or dwell time was found.** Searched 2026-08-08: web search
`CVSA position detention time drivers duty of care shipper facility statement`. Results
returned FMCSA studies, a PrePass Safety Alliance commentary, and trade explainers — no CVSA
statement. This corroborates [[evidence]] §G6, which already records "No detention/duty-of-care
statement found" for CVSA. CVSA's remit is roadside enforcement uniformity; shipper-facility
time is outside it.

**No CVSA position on broker transparency was found** in the same scan.

## Consequence for the programme

CVSA is the **best-timed engagement target of the thirteen bodies in G6**. It has publicly
stated it is forming policy positions on exactly the three problems this programme addresses —
cargo theft, motor-carrier identity theft, reincarnated carriers — with an open input channel
whose stated deadline is 2026-08-08. Whether that window is still open is a team decision, not
an agent one; it is filed here as a live opportunity with a date. CVSA's 2010 petition also
supplies a defensible precedent that an enforcement body has *already* argued that unreliable
identity capture degrades risk-based targeting — a framing this programme can build on.

## Vault notes depending on this

[[evidence]] §G6 (CVSA row — corroborated on detention absence; extend with the identifier
petition and the open survey) · [[goals]] G6 · [[gap-register]] `GAP-008` ·
[[source-ata-chameleon-carrier-position]] · [[source-nmfta-scac-verified-and-standards-role]]
