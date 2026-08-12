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
- domain/equity
- confidence/primary
- audience/internal
- programme/g6
- programme/g8
- programme/aim-1
- lifecycle/active
---
# Source — OOIDA written testimony, US Senate, "Grand Theft Cargo" (2025-02-27)

## Citation

Pugh, Lewie (Executive Vice President, Owner-Operator Independent Drivers Association).
*Testimony before the United States Senate, Committee on Commerce, Science &
Transportation, Subcommittee on Surface Transportation, Freight, Pipelines, and Safety:
"Grand Theft Cargo: Examining a Costly Threat to Consumers to the U.S. Supply Chain."*
2025-02-27. 8 pages.

Retrieved in full 2026-08-07 (HTTP 200, PDF, read directly):
<https://www.commerce.senate.gov/wp-content/uploads/meetings/8E3F88AF-5F67-492B-B8CA-8F8009AA45A0/Lewie%20Pugh%20OOIDA%20Written%20Testimony.pdf>

Hearing page: <https://www.commerce.senate.gov/meetings/grand-theft-cargo-examining-the-costly-threat-to-consumers-and-the-u-s-supply-chain/>
(retrieved 2026-08-07). Chair: Sen. Todd Young. Full transcript published as S.Hrg. 119-126.

Witnesses: Chief Will Johnson (BNSF Railway Police); Robert Howell (Academy Sports and
Outdoors); Adam Blanchard (Tanager Logistics / Double Diamond Transport); Lewie Pugh
(OOIDA).

## Why this is the strongest association source in the scan

It is sworn congressional testimony, published by the committee, on the exact mechanisms
this programme proposes to address. It is `primary` in the strictest sense and it is
**additional to** the OOIDA broker-transparency comment already in [[evidence]] §G6.

## What the source establishes

### OOIDA's constituency (for the equity argument, G8)

> "OOIDA has approximately 150,000 members located in all fifty states that collectively
> own and operate more than 240,000 individual heavy-duty trucks."

> "Small trucking businesses, like those we represent, account for 96 percent of registered
> motor carriers in the United States"

### The disproportionate-burden claim — now directly sourced

[[evidence]] §G6 flags the small-carrier burden framing as "unverified/inferred," noting it
came from a consulting firm rather than OOIDA. **This testimony supplies the direct OOIDA
statement**, verbatim:

> "Unfortunately, small trucking businesses are both the most vulnerable to fraud and the
> least likely to be able to recover from an incident."

> "several OOIDA members have lost their entire business after falling prey to a single case
> of freight fraud. That's not hyperbole. While large carriers are better equipped to absorb
> the cost of fraud, it only takes a single occurrence to ruin a small trucking business."

**Precision required.** This establishes OOIDA's position that *fraud losses* fall
disproportionately on small carriers. It does **not** establish an OOIDA position that
*verification or compliance costs* scale badly with fleet size. Those are different claims.
The vault's G8 caveat should be narrowed, not removed.

### The identity-verification mechanism — directly load-bearing for Aim 1

OOIDA's account of *why* carrier identity theft is easy, verbatim:

> "Every motor carrier is assigned a USDOT Number, which, along with addresses and phone
> numbers, can be easily viewed on FMCSA's website. As a result, it is incredibly easy to
> take that information, hijack the authority of a legitimate motor carrier, acquire loads,
> and receive payments. To make matters worse, fraudsters can also assess the safety records
> of motor carriers to choose victims that are most likely to be selected by brokers."

This is a named association stating that **the public FMCSA registry is simultaneously the
identity substrate and the attack surface** — which is the precise problem an
identity-assurance layer is meant to solve, and a direct justification for building on the
FMCSA Company Census File (see [[dataset-fmca-company-census-file]]).

**Authority sale, with prices:**

> "Our members also fall victim to nefarious actors offering large payments – anywhere from
> $2,000 to $40,000 depending on the age and safety record of the motor carrier – to sell
> their authority."

This is a *market price for a laundered identity, priced on the safety record attached to
it.* It is the sharpest available evidence that carrier identity is a traded asset and that
a chameleon-carrier benchmark has a real adversary model. Treat the range as OOIDA's
characterization of member reports, not a survey.

**Four named fraud typologies**, useful as the label taxonomy for an adjudicated benchmark:

1. **Double brokering** — criminals pose as motor carriers to acquire loads, then pose as
   brokers to hire the actual hauler; the legitimate broker pays the fraudster.
2. **Broker identity theft** — theft of a broker's identity to tender a load; fake broker
   collects payment from the real broker and disappears.
3. **Reroute schemes** — mid-haul redirection to a new delivery address, often with extra
   payment offered, then transfer and theft.
4. **Carrier identity theft** — a carrier's authority is used to secure and divert a load;
   the legitimate carrier is held liable.

### Federal system gaps OOIDA names

- FMCSA's **July 2024 report on illegal broker activity**: OOIDA states the agency
  "indicated it lacked the data necessary to determine if fraudulent activity, including
  double brokering, negatively impacts highway safety."
- FMCSA "lacks the statutory authority to administratively adjudicate and assess civil
  penalties for violations," forcing referral to DOJ. OOIDA: "fraud complaints bounce from
  agency to agency without anyone taking responsibility."
- **NCCDB** (National Consumer Complaint Database) is "an ineffective tool," with
  non-response discouraging reporting and thereby suppressing FMCSA's own understanding of
  scope. **This is a measured-data-quality warning for anyone planning to use NCCDB as a
  label source.**
- Cites **GAO-23-105972** (2023-09-19), *Motor Carrier Operations: Improvements Needed to
  Federal System for Collecting and Addressing Complaints against Truck, Moving, and Bus
  Companies*, <https://www.gao.gov/assets/d23105972.pdf>, quoting: "FMCSA has not designed
  sufficient controls to help ensure its policy for reviewing complaints related to motor
  carriers is followed." 14 recommendations; FMCSA agreed with 13; implementation deferred
  to FY2026.
- The **new Federal Registration System** "is expected to include features such as identity
  verification software, new business verification processes, and information edit checks
  that can reduce fraud." OOIDA supports the intent but states it remains "skeptical that
  they will achieve their objectives," and warns the updates "must be implemented in a
  user-friendly fashion that protects motor carriers' personal data and prioritizes
  cybersecurity best practices."

### Broker transparency, 49 CFR 371.3 — the mechanism, in OOIDA's words

Two named evasion routes:

1. Contractual waiver. OOIDA quotes an actual clause from "one of the nation's largest
   brokers" (broker name redacted in the testimony): "[Redacted] shall not be required to
   disclose the amount of its broker's commission to Carrier, and Carrier expressly waives
   its right to receive and review information, including broker's commission information,
   pursuant to 49 CFR §371.3."
2. Access friction. "some only allow a carrier to access records at the broker's office
   during normal business hours."

Timeline OOIDA states: Petition for Rulemaking filed **May 2020**, requesting electronic
transaction records within **48 hours** and a ban on waiver clauses; granted; rulemaking
launched **August 2020**; NPRM published **November 2024**; comment period closed
**2025-03-20**. OOIDA states the NPRM "did not include the two significant reforms we
recommended."

**Broker bonds:** MAP-21 (2012) set a $75,000 minimum. FMCSA's 2023 final rule suspending
authority when security falls below that was scheduled for 2025-01-16 and delayed a year
"because the New Registration System is still not ready."

**Legislation supported:** S. 337, Household Goods Shipping Consumer Protection Act
(Fischer, R-NE / Duckworth, D-IL) — would restore FMCSA civil-penalty authority over
unauthorized brokers, require physical addresses for brokers, and "compel the agency to
analyze trends and commonalities among companies applying for shipping authority to identify
potentially bad actors before they commit fraud."

## Quantitative claims — provenance stated, and it is thin

| Figure | OOIDA's attribution | Assessment |
|---|---|---|
| Fraud "increasing by 600% over the course of just 5 months between 2022 and 2023" | *State of Fraud in the Industry*, Transportation Intermediaries Association, 2024 | TIA is a **broker trade association**. Base, numerator, population and method are unstated. Do not cite as a rate of change. |
| "these crimes cost our industry roughly $1 billion annually" | same TIA 2024 report | Unstated method; not independently verified. Flag `[UNVERIFIED]` if used at all. |
| "$2,000 to $40,000" to sell authority | OOIDA member reports | Anecdotal range, no sample. Illustrative only. |
| "96 percent of registered motor carriers" are small businesses | not attributed in testimony | Plausible against FMCSA census but **unsourced here**. Verify against the Company Census File before use. |

Per [[methodology]] §2, none of these may be admitted as load-bearing without their own
primary source. They are recorded here so that a later agent finds the attribution chain
already mapped rather than re-deriving it.

## Limits and scope

- Advocacy testimony. It states OOIDA's positions and its members' reported experience. It
  is not a study, a survey, or an administrative record.
- Dated 2025-02-27. The broker-transparency rulemaking has moved since (a second NPRM was
  reported expected May 2026); this testimony predates that.
- The FMCSA July 2024 illegal-broker-activity report and GAO-23-105972 are cited *through*
  OOIDA and were not independently retrieved in this scan. Retrieve GAO-23-105972 directly
  before citing its findings — the URL is in the footnote above.
- Land Line Media is OOIDA's own publication. Where it is used, it is first-party
  reporting, not independent corroboration.

## Related OOIDA activity found but not independently retrieved

- Written comments to **DOT docket DOT-OST-2025-1326**, RFI on protecting the supply chain
  from cargo theft, signed by President Todd Spencer, reported 2025-10-20 by Land Line
  Media. `regulations.gov` returned HTTP 403 to automated retrieval; the comment itself was
  not read. `verification: snippet-only` — do not quote it.
- OOIDA comments supporting FMCSA detention-time data collection, citing a 2018 DOT OIG
  report. **Not retrieved.** The OIG figures circulating in trade coverage ($1.1–1.3B lost
  driver earnings; 6.2% crash-rate increase per 15 minutes of dwell) belong to the
  contested detention-cost family flagged in [[methodology]] §2 and must not be used
  without retrieving the OIG report itself.

## Vault notes depending on this

[[evidence]] §G6 (OOIDA rows), §G8 · [[goals]] G6, G8 · [[gap-register]] `GAP-008`,
`GAP-005` · [[dataset-fmca-company-census-file]] ·
[[dataset-e1-adjudicated-carrier-identity-cases]] ·
[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[experiment-e4-participation-and-small-carrier-equity]]
