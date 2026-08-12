---
type: evidence
status: active
schema_version: 1.0.0
confidence_default: mixed
updated: '2026-08-08'
tags:
- type/evidence
- lifecycle/active
- domain/freight
- audience/internal
- confidence/mixed
---
# Evidence Library

One entry per sourced claim, per the schema in [[05-agent-system/roster|05-agent-system/roster.md]].
Confidence: **primary** (official document/court record), **secondary** (trade press,
law-firm client alerts, vendor's own claims about itself), or **unverified** (single
weak source, or explicitly could-not-confirm). This file is the Rabbit Agent's output —
do not edit it into settled-sounding prose; that's the Synthesis Agent's job downstream.

Status key per goal: 🟢 primary-sourced · 🟡 secondary-only · 🔴 unverified/contradicted · ⚪ not started

**Pass 1 summary (three parallel research threads, completed same session):**
G1 🟢 (with a material correction — preemption ruling, not a duty-of-care definition),
G1b 🟡, G2 🟢, G3 🟡 (core facts primary, several details flagged unverified), G4 🟡,
G5 🟡 (plus an unverified sub-claim discarded), G6 🟡, G7 ⚪ not started, G8 🟡 (largely
unsourced as a direct claim), G9 not web-researchable. Two corrections to the team's
original working assumptions came out of this pass: the SCOTUS framing (§G1) and the
Proto-OKN funding total (§G3). Synthesized into `02-programme-strategy/research-programme.md` — see that
document for the consolidated, citable version of these findings.

---

## G1 — SCOTUS/court decision on broker duty of care — 🟢 (corrects prior framing)

**Important correction:** the team's working notes framed this as "SCOTUS established a
duty of care." That's imprecise. The actual holding is a **preemption ruling** — it
cleared the path for state-law negligent-hiring/selection claims against brokers; it did
**not** itself create or define a duty-of-care standard. `02-programme-strategy/research-programme.md` should be
updated to reflect this distinction — it materially changes how the "opportunity gap"
should be framed for an SBIR narrative (the gap is "no defined standard for a claim type
that's now viable," not "a newly imposed duty with no definition").

- **Claim:** *Montgomery v. Caribe Transport II, LLC*, 608 U.S. ___ (2026), No. 24-1238,
  decided 2026-05-14, 9-0, opinion by Barrett, concurrence by Kavanaugh (joined by Alito),
  reversing the Seventh Circuit. Holding: FAAAA's "safety exception"
  (49 U.S.C. §14501(c)(2)(A)) permits state-law negligent-hiring/negligent-selection
  claims against freight brokers — FAAAA preemption is not a categorical shield.
  **Confidence: primary.**
  Sources: [Cornell LII](https://www.law.cornell.edu/supremecourt/text/24-1238),
  [SCOTUSblog](https://www.scotusblog.com/2026/05/court-rules-freight-brokers-can-face-negligent-hiring-suits-under-state-law/),
  [Justia docket](https://supreme.justia.com/cases/federal/us/608/24-1238/).
- **Claim:** The Court did not define what "reasonable care" in carrier selection
  requires — no benchmark for investigation depth or how much weight a safety rating
  should carry. Kavanaugh's concurrence flags this gap directly. **This is the exact
  opening this research programme is built around — now confirmed from the primary
  source, not inferred.** Confidence: primary (holding itself) / secondary (practitioner
  commentary characterizing the gap — Hinshaw, DLA Piper client alerts, both May 2026).
  Sources: same as above, plus [Hinshaw](https://www.hinshawlaw.com/en/insights/hinshaw-alert/scotus-clears-road-to-negligent-hiring-selection-against-freight-brokers),
  [DLA Piper](https://www.dlapiper.com/en-us/insights/publications/2026/05/supreme-court-rules-freight-brokers-can-be-held-liable-under-state-negligence-law).
- **Caution:** one automated fetch produced a garbled line claiming the Court "assumed
  without deciding preemption" — this contradicts the actual 9-0 holding and has been
  discarded. Noted here so it isn't reintroduced by a future pass hitting the same source.

## G1b — C.H. Robinson $604M verdict — 🟡 secondary only, distinct from G1

- **Claim:** *Lipe v. Lupus Superior, LLC, et al.*, Dallas County, TX jury verdict,
  2026-07-24, $604M ($ split ~68% to C.H. Robinson via a "borrowed employee"/vicarious-
  liability theory), for a fatal March 2021 I-20 Mississippi crash. C.H. Robinson has
  stated intent to appeal. **This is a separate, later case from Montgomery** — it's the
  first major test of Montgomery's practical effect, not the same litigation the team's
  earlier note ("C.H. Robinson to appeal $604M verdict") may have been conflating with
  the SCOTUS ruling itself. Confidence: secondary — no court opinion/docket located
  directly, only trade press.
  Sources: [CCJ](https://www.ccjdigital.com/regulations/safety-compliance/article/15830826/ch-robinson-to-appeal-604-million-freight-broker-liability-verdict),
  [Transport Topics](https://www.ttnews.com/articles/ch-robinson-604m-verdict),
  [FreightWaves](https://www.freightwaves.com/news/c-h-robinson-hit-with-huge-nuclear-verdict-in-a-post-montgomery-world).
- **Unverified trivia:** reporting suggests C.H. Robinson may have originally been a
  co-defendant in *Montgomery* before dismissal at a lower court. Not confirmed against
  the actual docket — flag, don't cite.

## G5 — CAVRA Standard status — 🟡 secondary, one claim unverified

- **Claim:** Cassandra Gaines — transportation attorney, and (new fact not in prior team
  notes) **founder/CEO of Carrier Assure** — publicly released the CAVRA (Carrier
  Assessment, Verification, Risk, Accountability) Standard 2026-06-18 via an 800+
  attendee webinar. **Note the conflict of interest this creates**: Carrier Assure is
  also one of the thirteen rows on this programme's landscape list (twelve identified competitors plus one unresolved RMJ entry) (see G4) — CAVRA
  is a vendor's proprietary framework being positioned as an industry standard, not a
  neutral third-party one. This matters directly for how this programme should describe
  CAVRA in any SBIR narrative. Confidence: secondary.
  Sources: [FreightWaves](https://www.freightwaves.com/news/cassandra-gaines-unveils-trucking-industry-blueprint-for-carrier-selection),
  [Logistics Management](https://www.logisticsmgmt.com/article/new_cavra_standard_aims_to_guide_carrier_vetting_processes_after_supreme_courts_montgomery_ruling).
- **Claim:** CAVRA is a 54-page framework (four principles: assessment, verification,
  risk, accountability) covering safety/inspection history, fraud indicators, identity
  verification, double-brokering/"chameleon carrier" risk, and vetting-policy templates.
  Full document is gated (available only on request from Gaines) — not independently
  reviewed. Confidence: secondary/vendor-claimed.
  Source: [logisticsriskexpert.com/cavra-standard](https://www.logisticsriskexpert.com/cavra-standard/).
- **Claim (correction to prior team note):** the claim that ASTM F49 leadership reached
  out to Gaines about incorporating CAVRA into a formal ASTM guide **could not be
  verified**. No mention of ASTM, F49, or CAVRA appears together in F49's own committee
  materials or current work-item list (F3787, F3803/F3804, etc.), nor in CAVRA launch
  coverage. Confidence: **unverified — do not repeat as fact** without direct
  confirmation from ASTM F49 leadership (the original source was a secondhand team note,
  not a document).
  Source checked: [ASTM F49 committee page](https://www.astm.org/membership-participation/technical-committees/committee-f49)
  (site partially blocked automated fetch — findings based on search snippets and the
  [F49 brochure](https://mcsdocs.astm.org/committee-documents/F49%20Brochure%202025.pdf); worth a manual visit).

---

## G2 — FMCSA / Sean Duffy fraud initiative ("Motus") — 🟢 primary anchor + secondary color

- **Claim:** FMCSA/DOT held a freight-fraud panel at the Mid-America Trucking Show
  (Louisville), late March 2026 — FMCSA specialist Shannon Chelf stated the agency must
  first verify a complainant "is legit" before acting on fraud complaints, confirming the
  team's original framing. Confidence: secondary (trade press with a direct on-record
  quote; FMCSA/DOT sites blocked automated fetch).
  Source: [Overdrive, 2026-03-26](https://www.overdriveonline.com/regulations/article/15820691/fmcsa-announces-major-investigations-at-freight-fraud-panel).
- **Claim:** The system's official name is **"Motus: the U.S. DOT Registration
  System"** — confirms the team's prior note. Federal Register notice
  ("Availability of Motus, FMCSA's New Registration System," doc. 2026-08334,
  published 2026-04-29) confirms: Phase I launched 2025-12-08 (limited to insurers,
  financial-responsibility filers, transportation service providers); full availability
  to all regulated entities targeted for Q2 2026, retiring legacy systems (Unified
  Registration System, FMCSA Portal, MCMIS). **Confidence: primary** — this is the
  strongest anchor in this section.
  Source: [Federal Register, doc. 2026-08334](https://www.federalregister.gov/documents/2026/04/29/2026-08334/availability-of-motus-fmcsas-new-registration-system).
- **Claim:** Full rollout went live 2026-05-14; formal DOT/FMCSA press release
  2026-05-19 ("Trump's Transportation Secretary Sean P. Duffy Launches New Anti-Fraud
  Registration System"), quoting Duffy ("stop fraud dead in its tracks") and
  Administrator Derek Barrs. Confidence: **unverified/secondary** — fmcsa.dot.gov and
  transportation.gov returned HTTP 403 to automated fetch; reconstructed via
  search snippets and a trade-press reprint (NDTA). URLs exist; content not
  independently confirmed this pass — worth a manual visit.
- **Claim — current status (as of this research, ~Aug 2026):** rocky rollout. FMCSA
  **paused USDOT-number deactivations** (for carriers unable to complete biennial
  updates due to system issues) covering the period since 2026-06-01. Multiple
  independent outlets report ongoing login/identity-verification failures, insurance-
  status errors, and carriers mis-registered as Transportation Service Providers as of
  late July 2026. Confidence: secondary, but consistent across independent outlets
  (Truck News, FreightWaves, Overdrive, Land Line).
  Source: [Truck News, 2026-07-05](https://www.trucknews.com/transportation/fmcsa-pauses-deactivations-as-it-works-on-motus-issues/1003217922/).
- **Programme-relevance note:** Motus's rocky rollout (login failures, misregistration,
  paused deactivations) is itself evidence *for* this programme's thesis — FMCSA's own
  registration/verification infrastructure is struggling with basic identity resolution,
  which is exactly the class of problem a carrier credentialing graph targets. Worth
  citing directly in the SBIR "technology gap" framing once confirmed further.

## G3 — Current NSF SBIR/STTR solicitation + Proto-OKN status — 🟡 primary core facts, some unverified detail

- **Claim:** Current solicitation is **NSF 26-510**, "SBIR/STTR: Developing Deep
  Technologies that Advance U.S. Competitiveness and Security," posted 2026-05-22,
  replacing NSF 24-579/24-580/24-582. Confidence: **primary**.
  Source: [nsf.gov/.../nsf26-510/solicitation](https://www.nsf.gov/funding/opportunities/small-business-innovation-research-small-business-technology/nsf26-510/solicitation).
- **Claim:** Phase I: up to **$305,000**, 6–18 months, Standard Grant. **Requires a
  Project Pitch submission and an official NSF invitation before a full proposal can be
  submitted** — Project Pitch window opened 2026-06-02. This is a process gate the
  programme's plan didn't previously account for — Publishing Agent work should target
  the Project Pitch first, not a full proposal. Review criteria: Intellectual Merit,
  Broader Impacts, Commercial Potential (NSF's standard three-part SBIR/STTR review).
  Confidence: primary.
- **Claim:** Full-proposal deadline windows: 2026-07-27, 2026-11-04, 2027-03-04, then
  recurring quarterly. **The 2026-07-27 window has likely already passed by the time
  this is read** — target 2026-11-04 realistically. Confidence: primary.
  Source: [seedfund.nsf.gov/apply/full-proposal](https://seedfund.nsf.gov/apply/full-proposal/).
- **Claim — topic fit, unverified for 2026 currency:** the only topics/subtopics
  reference document found (`seedfund.nsf.gov/assets/files/applicants/combined-topics.pdf`)
  is explicitly labeled **for 2023 proposals** — stale. With that caveat, historically
  relevant topics were "Advanced Systems for Scalable Analytics (AA)" → subtopic AA4
  "Knowledge and Data Management Technologies," and "Cybersecurity and Authentication
  (CA)"; "Mobility (MO)" or catch-all "Other Topics (OT)" as freight-specific
  alternatives. **Must re-confirm the current 2026 topics list directly before
  submitting a Project Pitch** — topic fit determines which program director reviews it.
- **Claim — page limits/required sections: unverified.** seedfund.nsf.gov points to
  PAPPG Chapter II.D.2 rather than stating limits inline; the commonly-cited "15-page
  Project Description" was not independently confirmed against the current PAPPG this
  pass. **Flag: check PAPPG directly before drafting anything.**
- **Claim — Proto-OKN has no active follow-on.** The original solicitation **NSF
  23-571** ("Building the Prototype Open Knowledge Network," posted 2023-03-23,
  deadline 2023-06-20) is explicitly marked **"archived"** on nsf.gov. No successor
  Proto-OKN solicitation exists. It was **an 18-project, ~$26.7M one-time 2023 program**
  — this **does not match** the team's working figure of "~30 projects / $80M," which
  should be treated as likely inflated or conflated with a different total until
  independently reconfirmed. **This materially changes the SBIR framing**: there is no
  live Proto-OKN funding line to explicitly plug into — the pitch needs to stand on
  NSF 26-510 generally, citing Proto-OKN as *precedent*, not as an active funding
  vehicle. Confidence: primary for archived status and the 18-project/$26.7M figure;
  the team's $80M/30-project figure is now flagged as unverified/likely wrong.
  Sources: [NSF 23-571 solicitation](https://www.nsf.gov/funding/opportunities/proto-okn-building-prototype-open-knowledge-network/506169/nsf23-571/solicitation),
  [NSF 23-571 updates page](https://www.nsf.gov/funding/opportunities/proto-okn-building-prototype-open-knowledge-network/506169/updates).

## G4 — Competitor classification (13 companies) — 🟡 mostly secondary (vendor self-description)

None of the thirteen use anything resembling a knowledge graph or entity-resolution
architecture per public claims. That is a confirmed differentiator for the OKN framing,
not narrative color. **Only Truckstop.com (via RMIS) spans both fraud/vetting
and load-matching** — everyone else is single-focus. Confidence throughout: secondary
(vendor marketing sites) unless noted.

| Company | Focus | Graph-tech claim? | Positioning | Source |
|---|---|---|---|---|
| project44 | Visibility/orchestration, some carrier credential validation | **Yes** — markets a proprietary "logistics data graph," 259K+ carriers, 1.5B shipments/yr | Large single-vendor platform marketing network scale as quasi-infrastructure | [project44.com](https://www.project44.com/platform/tms/) |
| FourKites | Visibility/dwell analytics | No — Kafka streaming + AI, not graph DB | Single-vendor SaaS | [fourkites.com](https://www.fourkites.com/about/) |
| Highway | Carrier/broker identity fraud (two-sided: carriers can vet brokers too) | No public claim | Proprietary risk-scoring; positions as two-sided trust network but still closed | [highway.com](https://highway.com/press-releases/highway-unveils-highway-for-carriers---empowering-carriers-to-verify-brokers-and-combat-fraud) |
| Carrier Assure | Fraud/double-brokering risk scoring (A–F) | No | Add-on embedded in Descartes MyCarrierPortal/RMIS. **Note: this is CAVRA creator Cassandra Gaines' own company** — see G5 conflict-of-interest note | [carrierassure.com](https://www.carrierassure.com/how-it-works) |
| FreightValidate | Identity/fraud verification, MC/DOT/blocklist checks | No disclosed | Small SDVOSB SaaS (Nashville, founded 2023), partnered with AU10TIX for biometrics | [freightvalidate.com](https://freightvalidate.com/aboutus) |
| Tive | In-transit visibility/theft-damage (IoT hardware) | No | Single-vendor hardware+SaaS | [tive.com](https://www.tive.com/) |
| Samsara | Fleet visibility/safety/ELD compliance, broader than freight | No | Single-vendor SaaS, 10K+ customers | [samsara.com](https://www.samsara.com/products/telematics) |
| Motive | ELD/HOS compliance, dispatch | No | Single-vendor, 120K+ companies | [gomotive.com](https://gomotive.com/products/fleet-compliance/eld-compliance/) |
| DAT Freight & Analytics | Load-matching/market-rate data; now bundling visibility (Trucker Tools) + factoring (Outgo) via Convoy Platform acquisition (2025) | No | Roper-owned; ~$1T txn history in a proprietary warehouse; quasi-utility market role but still commercial | [dat.com](https://www.dat.com/company/news-events/news-releases/dat-2026-freight-focus-gradual-recovery-expected-for-transportation-providers-as-ai-reshapes-industry-operations) |
| Truckstop.com | **Both** load-matching (core board) **and** fraud/vetting (RMIS + "Risk Factors," RMIS acquired 2021) | No | Positions RMIS as industry-standard onboarding tool | [truckstop.com/blog/risk-factors](https://truckstop.com/blog/risk-factors/) |
| PTTR Load Board | Load-matching/tracking, drayage-focused, secondary counterparty verification | No | Small startup (~2019), spun out of a brokerage | [pttrloadboard.com](https://pttrloadboard.com/about-us/) |
| Amazon Relay | Load-matching/dispatch, Amazon-freight only | No | Explicitly single-vendor/closed, not cross-industry | [relay.amazon.com](https://relay.amazon.com/) |
| "RMJ" (as named in team notes) | — | — | **Could not identify.** Most likely intended: **RMIS** (Registry Monitoring Insurance Services, acquired by Truckstop.com 2021) — phonetically/contextually close, but this is an unverified guess, not a confirmed identification. | — |

## G6 — Association/standards-body positions — 🟡 mixed, one unverified/inaccessible

| Org | Position found | Confidence |
|---|---|---|
| ATA | Publicly supports the SAFER in Transport Act (2026) targeting "chameleon carriers"/cargo theft; CEO Chris Spear quoted in support | secondary (trade coverage; ATA's own statement page not directly fetched) — [truckinginfo.com](https://www.truckinginfo.com/news/fraud-fighting-legislation-targets-unscrupulous-brokers-carriers) |
| **OOIDA** | Filed a formal comment on FMCSA's broker-transparency rulemaking (49 CFR 371) demanding electronic transaction records within 48hrs and no contractual waiver of carrier access rights; President Todd Spencer: "the deck is stacked" against small-business truckers | **primary** — [ooida.com, 2025](https://www.ooida.com/2025/ooida-calls-for-stronger-broker-transparency-regs-to-protect-small-business-truckers/) |
| OOIDA (G8 equity claim) | The specific framing "verification/compliance costs disproportionately burden small carriers" is **not** a direct OOIDA quote found — it's inferred from secondary commentary (a consulting firm) plus OOIDA's general "one fraud event can ruin a small carrier" framing. **Flag as partially unverified** — don't cite as a direct OOIDA position without a better source. | unverified/inferred |
| TCA | Backs CORCA (Cargo Organized Retail Crime Act); President Jim Mullen quoted in support; notes 31% YoY rise in Q1 2026 "deceptive pickup" fraud | primary/secondary mix — [truckload.org](https://truckload.org/), [thetrucker.com](https://www.thetrucker.com/trucking-news/truckload-authority/government-affairs/gaining-ground-corca-legislation-could-be-a-valuable-tool-in-fight-against-cargo-theft) |
| CVSA | No detention/duty-of-care statement found. Active on data-interoperability: 2026 Out-of-Service Criteria (eff. 2026-04-01) added ELD-tampering violations; Level VIII Electronic Inspection program building real-time truck-to-roadside data exchange (no jurisdiction fully live yet) | primary — [cvsa.org](https://cvsa.org/news/2026-oosc/) |
| NPTC | **Unverified/inaccessible** — regulatory-updates content is members-only; no public statement confirmed either way | unverified |
| **ASTM F49** | Most concretely active org on interoperability: new goods-movement process codes and transport-unit-identifier standards (May 2026), a conformity-assessment guide (April 2026), and a Certificate-of-Authenticity guide (Nov 2025) — ASTM's first standard referencing distributed-ledger tech. **No CAVRA/duty-of-care work item found**, consistent with the G5 unverified-outreach flag. | primary — [astm.org/committee-f49](https://www.astm.org/membership-participation/technical-committees/committee-f49) |
| **NMFTA** | **SCAC Verified is live as of 26 Feb 2026**: identity verification is required at SCAC issuance/renewal for non-Class-8 carriers; NMFTA describes the result as a checkable identity signal and explicitly says it does not guarantee fraud prevention. The earlier working label "Cargo Crime Reduction Framework" was not reproduced in the 2026-08-08 source pass and should not be repeated as NMFTA nomenclature. No detention/duty-of-care position found. | **primary** — [[source-nmfta-scac-verified-and-standards-role]] |

## G7 — Data-sharing incentive precedent — 🟢 researched 2026-08-07/08

Primary analogues now documented include [[source-fincen-314b-information-sharing-safe-harbor]], [[source-cisa-2015-cyber-threat-sharing-liability-shield]], [[source-faa-asias-voluntary-safety-data-sharing]], and [[source-dot-airline-on-time-performance-reporting]]. The research also opened [[gap-register]]: lawful competitor information-sharing cannot be assumed from technical privacy controls alone; counsel must assess antitrust structure.

## G8 — Small-carrier equity angle (OOIDA) — 🟡 see G6 row above — largely unverified as a direct quote

## G9 — Status of four exploratory interviews — ⚪ not web-researchable; direct question to user/team
