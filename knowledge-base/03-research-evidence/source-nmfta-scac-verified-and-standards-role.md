---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-08
updated: 2026-08-08
review_by: 2027-02-08
tags:
- type/source
- domain/freight
- domain/standards
- confidence/primary
- audience/internal
- programme/g5
- programme/g6
- lifecycle/active
- domain/identity
---
# Source — NMFTA: SCAC Verified, and NMFTA's actual standards remit

## Citation

National Motor Freight Traffic Association, Inc. (NMFTA).

1. *SCAC Verified — Identity-Verified Carrier Identification*.
   <https://scac.nmfta.org/scac-verified> (retrieved 2026-08-08, HTTP 200).
2. *SCAC Identity Verification — Why It's Required*. <https://scac.nmfta.org/id-verification>
   (retrieved 2026-08-08, HTTP 200).
3. *The Fight Against Freight Fraud Begins with One Change That Can Transform the Industry*.
   <https://nmfta.org/news/the-fight-against-freight-fraud-begins-with-one-change-that-can-transform-the-industry/>
   (retrieved 2026-08-08, HTTP 200).
4. *Why Cargo Theft Is a Shared Problem — and the Shared Solution That's Taking Shape*.
   <https://nmfta.org/news/why-cargo-theft-is-a-shared-problem-and-the-shared-solution-thats-taking-shape/>
   (retrieved 2026-08-08, HTTP 200).
5. *About NMFTA*. <https://nmfta.org/about/> (retrieved 2026-08-08, HTTP 200).

## What the source establishes

### NMFTA's institutional identity (`primary`)

NMFTA describes itself, verbatim: "Since 1956, the National Motor Freight Traffic
Association, Inc.® (NMFTA)™ has empowered for-hire motor carriers with the standards, tools,
and insights needed to move goods efficiently, securely, and reliably," and as "a trusted,
non-profit steward of the standards, data, and security practices the transportation industry
relies on."

The codes and standards it administers, per its own About page: **NMFC** (National Motor
Freight Classification), **SCAC** (Standard Carrier Alpha Code), **SPLC** (Standard Point
Location Code), **LTL and FTL API standards** through its Digital Standards Development
Council, and cybersecurity standards and research.

### SCAC Verified — a live carrier-identity verification programme (`primary`)

**This is the most directly competitive-or-complementary industry initiative found for Aim 1.**
NMFTA is, as of February 2026, operating an identity-verification layer on the freight
industry's most widely used carrier identifier.

Programme facts, from NMFTA's own SCAC portal:

| Attribute | Value (verbatim or direct) |
|---|---|
| Effective date | "Effective February 26, 2026, identity verification is required for non-Class 8 carriers only when applying for or renewing a SCAC." |
| Announced | 2026-02-10, at Manifest 2026, Las Vegas |
| What it adds | "SCAC Verified strengthens the industry's most widely used carrier identifier by adding identity verification at issuance and renewal." |
| Verification points | "Identity verification occurs at SCAC issuance and renewal" |
| What a verified status asserts | "a real individual completed identity verification during the SCAC issuance or renewal process" — "a verified identity signal tied to SCAC issuance and renewal" |
| Population in scope | Non-Class 8 carriers only — "all vehicles with a gross vehicle weight rating (GVWR) of 33,000 pounds or less" (box trucks, cargo vans, local delivery fleets, owner-operators). "Class 8 carriers do not need to complete ID verification at this time." |
| Method | Three steps: "Apply for or renew your SCAC," "Capture your ID," "Capture your selfie" — document-plus-selfie liveness check |
| Vendor | Persona, NMFTA's "trusted identity partner" |
| Fee | Additional $5; a failed verification requires re-payment to retry |
| Lookup | Third parties can "search and confirm SCAC status through the SCAC Verified platform" by SCAC, US DOT number, or company name. "Only status information is displayed." |

**NMFTA's own framing of what it has built** — the load-bearing phrases for this programme:
the change turns SCAC from "a static code into an identity-assured trust credential," creating
"a universal, checkable signal of trust at tender and pickup." NMFTA states that the prior
system's defect was that it "didn't verify the person behind the code," and that the rationale
is that "Identity misuse is a common factor in freight fraud."

Named attribution: **Holly Taylor, director of product, NMFTA** — "By binding a verified
identity to every SCAC lifecycle event, we're making impersonation and fictitious pickups
dramatically harder to pull off."

### Scope of NMFTA's fraud programme (`primary`)

Alongside SCAC Verified, NMFTA runs a **Freight Fraud Prevention Hub** (guidance, red flags,
education) and names the stakeholder categories it is trying to reach: carriers (Class 8 and
non-Class 8), brokers and 3PLs, shippers and private fleets, TMS platforms, insurers and
sureties, and industry associations. Threat types it names: "impersonation, double brokering,
and fictitious pickups."

## Limits and scope

- **The programme verifies a natural person at a lifecycle event; it does not verify ongoing
  operational legitimacy.** NMFTA says so itself: a verified designation "explicitly does not
  guarantee fraud prevention." This is the precise gap this programme's continuous,
  evidence-based trust model addresses — SCAC Verified is a point-in-time binding, not a
  standing assertion about behaviour.
- **Population is narrow.** Non-Class 8 only. Class 8 carriers are outside it, on the stated
  reasoning that they already hold FMCSA identifiers (USDOT/MC). Chameleon-carrier behaviour
  documented elsewhere in this vault involves entities that *do* hold USDOT numbers — so
  SCAC Verified does not, by design, reach that population.
- **Figures cited by NMFTA are third-party and heterogeneous.** Its fraud article aggregates
  $6.6B annualised cargo-theft cost (truckingresearch.org), $520,000 average annual carrier
  theft losses and $1.84M average annual LSP losses (scdigest.com), 27% 2024 increase and 22%
  forecast 2025 rise (NICB), a "1,500% increase since 2021," and a 65% rise in fraud reports
  Sept 2024–Feb 2025 (TIA, April 2025). Its cargo-theft article cites 27% YoY and >$200,000
  average loss per case (CargoNet 2024) and "up to $35 billion" annually (NICB). **These come
  from different populations, periods, and methods and must not be combined or restated as
  NMFTA findings.** They are NMFTA quoting others.
- Some NMFTA newsroom items sit behind a member login. The press-release page
  (`nmfta.org/news/nmfta-to-launch-scac-verified-…`) rendered only its lede for automated
  retrieval; the substantive programme detail above was taken from the public SCAC portal
  (`scac.nmfta.org`), which returned full content.

## Negative findings — confirmed absences

**NMFTA holds no position on detention or dwell measurement.** Searched 2026-08-08: web search
`NMFTA detention dwell time position statement driver detention`, plus nmfta.org About and the
two fraud/cargo-theft articles. Detention, dwell, and facility-time measurement do not appear
in any NMFTA publication surfaced. The detention search returned only FMCSA and DOT OIG
material. NMFTA's remit is classification, codes, APIs, cybersecurity, and now identity — not
shipper-facility performance.

**No NMFTA position on broker transparency (49 CFR 371) was found** in the same scan.

## Correction / corroboration of what the vault already asserts

- [[evidence]] §G6 records NMFTA as running "a Cargo Crime Reduction Framework + new SCAC
  verification initiative." **The SCAC verification initiative is confirmed and now fully
  documented above. The name "Cargo Crime Reduction Framework" was not reproduced by this
  scan** — NMFTA's own cargo-theft article does not use that title; it describes SCAC Verified
  plus the Freight Fraud Prevention Hub as the components of a shared approach. Reported as a
  probable naming error, not corrected here (scope boundary).
- [[freight-trust-client-master-brief]] and [[dataset-scan-event-provenance-and-federation]]
  pair "ASTM F49 and NMFTA" as joint standards-alignment targets. **That pairing is
  defensible but should not be read as an institutional link.** NMFTA is a standards-setting
  body in its own right (NMFC, SCAC, SPLC, LTL/FTL APIs); **no evidence was found in this scan
  that NMFTA participates in ASTM Committee F49**, and [[source-astm-f49-committee]] does not
  record NMFTA among F49's work items or stakeholders. Searched 2026-08-08:
  `NMFTA ASTM F49 "Digital Information in the Supply Chain" participation standards` — no
  result linked the two bodies. Treat them as **two separate alignment targets** with
  non-overlapping remits: F49 owns goods-movement status codes and terminology; NMFTA owns
  carrier and location identifiers and now identity assurance on one of them.

## Consequence for the programme

NMFTA is the **strongest incumbent** found in the carrier-identity space and must be named as
prior art, not omitted. But its programme is a one-time identity binding on a subset of
carriers, self-described as not a fraud guarantee, with no behavioural or event dimension.
The first-of-kind claim should be narrowed accordingly: not "no one verifies carrier identity"
but *no incumbent maintains a continuously updated, provenance-bearing, contestable trust
record across carrier identity and facility events.* SCAC Verified also demonstrates
**industry appetite and willingness to pay** ($5, mandatory at renewal, accepted by a national
standards body) — useful for the participation assumption in
[[experiment-e4-participation-and-small-carrier-equity]].

## Vault notes depending on this

[[evidence]] §G6 (NMFTA row — flag the "Cargo Crime Reduction Framework" name) · [[goals]] G5,
G6 · [[gap-register]] `GAP-008` · [[source-astm-f49-committee]] ·
[[dataset-scan-event-provenance-and-federation]] · [[freight-trust-client-master-brief]]
