---
type: programme
status: active
tags:
  - freight-trust
  - research-programme
  - strategy
---

# Freight Trust Infrastructure — Research Programme

Consolidated from seven source documents (proposal drafts, team notes, and one industry
report) into a single working programme. Sources are archived unmodified in
[raw/](raw/) and [raw/originals/](raw/originals/); this document is the canonical
synthesis and the one to keep editing going forward.

**Status (updated after first live research pass):** every load-bearing claim below has
now been checked against primary or secondary sources — see
[research/evidence.md](research/evidence.md) for full citations and confidence levels,
[research/GOALS.md](research/GOALS.md) for the research goals that drove this pass, and
[research/PLAN.md](research/PLAN.md) for what comes next. Two of the team's original
working assumptions turned out to need correction (§1, §5) — flagged inline below rather
than silently fixed, since the corrections change the SBIR framing.

## 1. Core Thesis

Freight logistics runs on fragmented trust. Carrier identity, safety compliance,
insurance validity, and operational responsibility are distributed across shippers,
brokers, carriers, drivers, facilities, and insurers — parties with asymmetric
information and no neutral, cross-party record of ground truth.

Two convergent problems make this urgent right now, and one legal event just made it
concrete:

- **Fraud** — carrier identity fraud and cargo theft cost the industry an estimated
  **$7–16B/year** (cargo shrinkage via fraudulent drivers alone: **$750M–$1B/year**).
- **Detention / dwell** — missed appointments and dock delays cost **~$15B/year**;
  drivers were detained at **39.3% of all stops in 2023**, representing **135M hours and
  $11.5B in lost productivity** (ATRI, 2024). Solving empty miles requires solving dwell.
- **Empty miles** — **16.7% of miles run are empty** (ATRI, 2025), and there is no
  cross-party orchestration layer that would let one operator's schedule inform another's.
- **Legal trigger (corrected)** — *Montgomery v. Caribe Transport II, LLC*, 608 U.S. ___
  (2026), No. 24-1238, decided 2026-05-14, 9-0 (Barrett writing, Kavanaugh concurring).
  **This was a preemption ruling, not a duty-of-care ruling**: the Court held that
  FAAAA's "safety exception" permits state-law negligent-hiring/negligent-selection
  claims against brokers — it cleared the path for these claims, it did not itself
  create or define the duty. The team's original framing ("SCOTUS established a duty of
  care") overstated the holding; the corrected framing is sharper for an SBIR pitch: *a
  claim type just became viable nationwide, and no standard exists yet for what
  satisfies it.* Kavanaugh's concurrence flags this gap directly. A first real-world
  test of the ruling's practical stakes: *Lipe v. Lupus Superior, LLC* (Dallas County,
  TX jury verdict, 2026-07-24, $604M, ~68% allocated to C.H. Robinson via a
  "borrowed-employee" theory; C.H. Robinson has stated it will appeal) — a separate,
  later case from Montgomery, not the same litigation.
  A private framework ("the CAVRA Standard," released 2026-06-18 by Cassandra Gaines) is
  trying to fill the definitional gap — **but Gaines is also founder/CEO of Carrier
  Assure**, one of this programme's named competitors (§5). CAVRA is a vendor's
  proprietary framework positioned as an industry standard, not a neutral one — this is
  a real strategic point in this programme's favor (a federally-anchored, genuinely
  neutral standard is a different value proposition than a vendor's), not just
  competitive noise. The claim that ASTM F49 reached out to incorporate CAVRA into a
  formal guide **could not be verified** — no reference to CAVRA appears in ASTM F49's
  current work-item list; treat as unconfirmed until checked directly with F49
  leadership. Full sourcing: [research/evidence.md](research/evidence.md) §G1/G1b/G5.

The working strategic hypothesis, carried over unchanged from the team's original framing:

> Logistics does not merely need fraud detection; it needs a computational duty-of-care
> layer that can establish trust, responsibility, and liability across fragmented
> transportation networks.

This programme exists to prove or disprove that hypothesis with evidence — not assume it.

## 2. The Two Product/Research Angles (and why they're one programme)

Two threads run through the source material and need to be understood as one thesis
viewed from two altitudes, not two competing ideas:

**A. Freight Trust OKN (infrastructure / federal angle)** — an Open Knowledge Network,
per the NSF/OSTP 2022 roadmap, composed of interlinked knowledge graphs:
- *Carrier Credentialing Graph* — resolves USDOT number, EIN, owner identity, insurance,
  performance history, and broker relationships into one queryable profile; produces a
  **Freight Trust Index** and surfaces fraud patterns via network analysis (the same
  technique used for anti-money-laundering).
- *Facility Performance Knowledge Graph* — timestamped event graph (tendered → appointment
  → arrival → dock → loading → departure) that makes dwell/detention a matter of record
  rather than a dispute between carrier and shipper logs.
- Positioned as public infrastructure, not a vendor product — analogous to DOT's 1987
  on-time-disclosure mandate for airlines, and explicitly proposed as a candidate for
  NSF's Proto-OKN program (which has already funded ~30 use cases at $80M).

**B. Cross-Actor Orchestration (applied / product angle)** — a system for actually
*using* that trust/data layer to reduce empty miles and dwell in real time: matching
backhaul loads to returning trucks, modeling the profit-service-risk triangle explicitly
at each decision point, and treating the empty-mile problem as a **governance and
incentive problem**, not just a routing/visibility problem (Matt's thesis, `raw/trust-notes.md`).
Local optimization by each actor produces system-wide waste; someone has to govern the
full network, not just individual nodes.

**Why they're one programme:** the OKN is the trust/data substrate; cross-actor
orchestration is the first (and clearest) high-value application built on top of it. The
NSF SBIR angle should lead with the substrate (research novelty: dynamic trust
infrastructure, entity resolution, regulatory reasoning) and cite orchestration as the
proof-of-value use case, not the other way around — an "orchestration app" alone reads as
a product pitch, not research; the trust-graph framing is what makes it fundable as NSF
research rather than a logistics startup.

## 3. Stakeholder Landscape

| Stakeholder | Interest | Position (🟢 sourced / 🟡 partly sourced / 🔴 unverified) |
|---|---|---|
| FMCSA / DOT (Sean Duffy era) | Safety, fraud enforcement | 🟢 Confirmed active: launched "Motus" registration system (Federal Register 2026-04-29; full rollout 2026-05-14), explicitly framed as anti-fraud infrastructure by Duffy. Rollout has been rocky — deactivations paused since 2026-06-01 due to login/verification failures — which is itself evidence *for* this programme's thesis (FMCSA's own identity-verification infra is struggling with exactly the class of problem a carrier credentialing graph targets) |
| Brokers | Efficiency, liability exposure | 🟢 Post-*Montgomery*, negligent-selection claims are now viable nationwide; the $604M *Lipe v. Lupus Superior* verdict (2026-07-24, on appeal) shows real exposure. Brokers need a defensible due-diligence record but will resist anything that expands liability further than that |
| Carriers (legitimate) | Fair competition, reputation protection | 🟡 Directionally favorable (unchanged from initial assessment; not independently re-verified this pass) |
| Small carriers | Market access | 🟡 OOIDA (their clearest representative) frames fraud as an existential risk to small carriers, but a **direct OOIDA quote on verification/compliance costs disproportionately burdening small carriers was not found** — that specific equity framing is currently inferred, not sourced. Needs a better citation before use in any external-facing deliverable |
| Shippers | Reliability, loss reduction | 🟡 Directionally favorable (unchanged; not independently re-verified) |
| Insurers | Risk-adjusted underwriting | 🟡 Directionally favorable (unchanged; not independently re-verified) |
| Technology vendors | Market share | 🟢 **Confirmed differentiator**: of 13 named competitors, only project44 markets anything resembling graph technology (a proprietary "logistics data graph," not a neutral cross-party network); none position as neutral infrastructure. Only Truckstop.com (via its RMIS acquisition) spans both fraud-vetting and load-matching — everyone else is single-focus. Full breakdown in §5 |
| Industry associations | Represent member interests | 🟢 ATA publicly backs anti-fraud legislation (SAFER in Transport Act); OOIDA filed a formal comment on FMCSA's broker-transparency rulemaking (49 CFR 371, primary source); TCA backs CORCA (cargo-theft legislation); CVSA is active on inspection data-interoperability but silent on duty-of-care/detention; NPTC's position is inaccessible (members-only). None have been contacted directly yet — this table reflects public positions, not outreach |
| Standards bodies | Interoperability | 🟢 ASTM F49 is the most concretely active body found: new goods-movement process codes, transport-unit-identifier standards, and a conformity-assessment guide, all in 2026 — high-value ally, confirmed no CAVRA linkage. NMFTA's 2026 focus is cybersecurity/cargo-crime, not duty-of-care specifically, but publishes the freight OpenAPIs (eBOL, pickup/visibility, freight charges) this programme's ontology should align to |
| Lawyers / transportation law firms | Liability clarity, precedent-setting | 🟢 Actively organizing post-*Montgomery* (multiple law-firm client alerts within days of the ruling — Hinshaw, DLA Piper, Crowell & Moring, Honigman). The CAVRA Standard is a **vendor-authored** attempt to define the evidentiary bar (see §1 conflict-of-interest note) — a genuinely neutral alternative is a real differentiator, not just competitive noise |
| Law enforcement (FBI, DOJ, DHS) | Organized fraud/theft interdiction | 🔴 Unverified — no signal found on active interest, not researched this pass |

**Who pushes back, and why (unresolved — needs Review Agent + more Rabbit Agent evidence):**
- Brokers, if the duty-of-care standard the OKN embodies expands their liability beyond
  what they can control.
- Any platform with a proprietary carrier database, if a neutral federally-anchored
  alternative undercuts its data moat.
- Anyone skeptical that carriers/brokers will *actually* share data voluntarily — the
  entire OKN model depends on participation incentives that are asserted, not yet tested.

## 4. Regulatory & Legal Timeline

| Date | Actor | Action | Confidence |
|---|---|---|---|
| 1987 | DOT | Mandated public disclosure of airline on-time statistics | Historical precedent (not independently re-verified this pass) |
| 2022 | NSF / OSTP | Published "Open Knowledge Network Roadmap: Powering the Next Data Revolution" | Not independently re-verified this pass |
| 2023-03-23 | NSF | Posted Proto-OKN solicitation **NSF 23-571** ("Building the Prototype Open Knowledge Network"), deadline 2023-06-20 | 🟢 Primary. **Now archived** — 18 projects funded, ~$26.7M total. This is smaller than the team's working "~30 projects/$80M" figure, which is now flagged unverified/likely inflated |
| 2025 | White House | AI Action Plan | Not independently re-verified this pass |
| 2025-12-08 | FMCSA | Motus registration system Phase I launch (limited to insurers, financial-responsibility filers, transportation service providers) | 🟢 Primary (Federal Register) |
| 2026-03-09/10 | NIST | "Building the Supply Chain Open Knowledge Network" workshop | Origin point of this programme's OKN concept note |
| 2026-03-26 | FMCSA | Freight-fraud panel at Mid-America Trucking Show — agency states it must verify complainants are legitimate before acting on fraud reports | 🟡 Secondary (trade press w/ on-record quote) |
| 2026-04-29 | FMCSA / Federal Register | Formal notice of Motus availability (doc. 2026-08334) | 🟢 Primary |
| 2026-05-14 | U.S. Supreme Court | ***Montgomery v. Caribe Transport II, LLC***, 608 U.S. ___, No. 24-1238, 9-0 — FAAAA's safety exception permits state-law negligent-hiring/selection claims against brokers. **Preemption ruling, not a duty-of-care definition** — see §1 correction | 🟢 Primary |
| 2026-05-14 | FMCSA | Motus full rollout goes live for all regulated entities | 🟡 Secondary (site blocked automated fetch; corroborated via reprints) |
| 2026-05-19 | DOT / Sean Duffy | Formal press release framing Motus as anti-fraud infrastructure | 🟡 Secondary (same access issue) |
| 2026-05-22 | NSF | Posted current SBIR/STTR solicitation **NSF 26-510** | 🟢 Primary |
| 2026-06-02 | NSF | Project Pitch submission window opened (required gate before a full SBIR proposal can be invited) | 🟢 Primary |
| 2026-06-01 (ongoing) | FMCSA | Paused USDOT-number deactivations due to Motus login/verification failures | 🟢 Primary-adjacent (Truck News, corroborated by multiple outlets) |
| 2026-06-18 | Cassandra Gaines (Carrier Assure) | Released the CAVRA Standard | 🟡 Secondary — and see conflict-of-interest note in §1 |
| 2026-07-05 | FMCSA | Deactivation pause confirmed still in effect | 🟢 Primary-adjacent |
| 2026-07-24 | Dallas County, TX jury | ***Lipe v. Lupus Superior, LLC*** — $604M verdict, ~68% to C.H. Robinson; appeal announced | 🟡 Secondary (trade press; no docket located) |
| 2026-07-27 | NSF | First full-proposal deadline under NSF 26-510 (**likely already passed** — target 2026-11-04) | 🟢 Primary |

Full sourcing in [research/evidence.md](research/evidence.md). Remaining gaps: PAPPG
page-limit/section requirements (needs direct check), current 2026 SBIR topic-area list
(only a stale 2023 version was found), and independent confirmation of the Proto-OKN
$80M/30-project figure.

## 5. Technology / Competitive Landscape

Researched — see full table with sources in
[research/evidence.md §G4](research/evidence.md). Headline finding: **the "neutral,
federally-backed, cross-party infrastructure" framing is a confirmed real differentiator,
not narrative color.** Of thirteen named companies, only project44 markets anything
resembling graph technology (a proprietary "logistics data graph" — still a closed,
single-vendor asset, not a neutral network), and none position themselves as neutral
cross-industry infrastructure. Every other named competitor is a conventional relational/
ML-scoring product.

Second finding: the landscape is split almost cleanly by problem area — most companies do
either fraud/identity verification (Highway, Carrier Assure, FreightValidate) **or**
visibility/detention (FourKites, Tive, Samsara, Motive) **or** load-matching (DAT, PTTR,
Amazon Relay). **Only Truckstop.com (via its 2021 RMIS acquisition) spans both fraud-
vetting and load-matching** — no one currently spans fraud *and* detention *and* matching
the way this programme's OKN concept (carrier credentialing graph + facility performance
graph, feeding a cross-actor orchestration layer) would.

Correction: "RMJ," named in the original team notes, could not be identified as an actual
company. The most plausible intended reference is **RMIS** (Registry Monitoring Insurance
Services, acquired by Truckstop.com in 2021) — phonetically and contextually close, but
this is an unverified guess, not a confirmed identification.

Also note (§1, §3): Carrier Assure — one of these thirteen competitors — is the company
founded by Cassandra Gaines, author of the CAVRA Standard. That standard is not a neutral
industry framework; it's a competitor's product positioned as one.

## 6. Vocabulary / Domain Model (from Cross-Actor Orchestration notes)

Working ontology sketch, to be formalized by the OKN's central ontology (§7):

- **Load** — has pickup location, destination, time window.
- **Trucker/Driver** — mobile actor, bound by Hours-of-Service (HOS) constraints; runs
  virgin loads or backhauls.
- **Station** — port, warehouse, distribution center, terminal; place where an activity
  happens.
- **Chassis / container** — physical unit moved through the network; can be a lag source
  if unavailable at time of need.
- **Journey (lateral)** — the path a load takes location to location to final mile.
- **Terrain (vertical)** — the stack at each location: at ports, on the road, at
  destination, at the warehouse, at final-mile delivery.
- **Governance question, unresolved**: who governs the *portion* of the process at each
  stage — the port, the trucker, the trucking company/"operator," or a dispatcher/AI
  system? Every stage requires managing the profit-service-risk triangle; nobody currently
  owns that trade-off explicitly (Matt's thesis).

Key process pattern already documented: overseas shipper → port arrival → dock (subject to
slot availability lag) → unload (subject to chassis-availability lag) → storage → trucker
pickup (subject to appointment/wait lag) → delivery → backhaul match → return trip. Every
transition is a place lag/dwell can be introduced and where governance could reduce it.

Trailer pooling works well at ports specifically because port service windows are already
loose and dwell is already unpredictable — the caution flagged in source notes is not to
assume pooling transfers directly to tighter, more predictable service environments.

## 7. Technical Architecture (from OKN Pilot concept note)

Three-dimensional framework:
1. **Technical Architecture** — hybrid open system with connected closed nodes
   (per-company graphs); semantic triple store, possible property-graph integration,
   possibly a hybrid with high-volume stores (Hadoop/Map-Reduce) depending on scale.
2. **Data & Semantics** — shared ontologies (RDF/OWL) built in sight of ASTM F49's Goods
   Movement Process terminology and existing freight OpenAPIs (eBOL, pickup/visibility,
   freight charges via NMFTA).
3. **Governance & Incentives** — stewardship model, trust boundaries, data
   public-vs-local rules, anti-competitive-behavior guardrails. **This is the least
   developed dimension in all source material and the one the Review Agent should press
   hardest** — the entire model assumes voluntary multi-party data sharing without a
   worked-out incentive mechanism.

## 7A. Evidence-Based Refinement of the Programme Claim

The current evidence strengthens the case for a research programme, while narrowing what
can responsibly be claimed before a pilot. Detention is a material and measurable freight
operations problem: ATRI estimates 39.3% of stops involved detention in 2023, with 135.9M
lost hours and $11.5B in productivity losses. FMCSA continues to study how detention can
be measured and separated from normal dwell. These numbers establish problem relevance;
they do **not** establish that this programme will reduce detention or empty miles.

The more rigorous thesis is therefore: build and evaluate a **federated, provenance-
preserving decision-support layer** that joins authoritative credential evidence and
permissioned facility-event records. Its first outcomes are verification accuracy,
resolution time, event completeness, dispute time, participation, and equity—not a
unqualified industry-wide “Trust Index.” The system may produce optional, explainable
indicators, but no score should control eligibility, pricing, contracting, or liability
without human review and a correction path.

This framing has technical precedent in peer-reviewed supply-chain knowledge-graph and
federated-learning work, plus NIST's traceability meta-framework. It also has a governance
precedent in federated mobility data spaces and shared legal-entity identity utilities.
Those precedents make the research question credible, not pre-solved. Full sourcing,
falsifiable hypotheses, pilot measures, and residual gaps are in
[research/LUNA_WIDE_NET_SYNTHESIS.md](research/LUNA_WIDE_NET_SYNTHESIS.md).

## 8. Open Research Questions

**Resolved this pass** (full detail in [research/evidence.md](research/evidence.md)):

1. ✅ FMCSA/Duffy activity — Motus registration system, primary-sourced timeline (§4).
2. ✅ The legal decision is *Montgomery v. Caribe Transport II* — a preemption ruling,
   not a duty-of-care definition (§1). Correction, not just confirmation.
3. ✅ CAVRA Standard is Cassandra Gaines' own framework; she also founded competitor
   Carrier Assure — it's vendor-authored, not neutral (§1, §5).
4. ✅ None of the 13 named competitors use real knowledge-graph technology; the neutral-
   infrastructure framing is a confirmed differentiator (§5).
5. ✅ NSF's current solicitation is NSF 26-510; Proto-OKN (NSF 23-571) is archived with
   no successor — the team's "$80M/30 projects" figure is likely wrong (actual: ~$26.7M/
   18 projects) and needs re-verification before citing publicly (§4, §9).

**Still open:**

6. What incentivizes a broker or carrier to share data with a neutral third party, given
   that opacity can currently function as a liability shield? (G7 — not yet researched;
   the Review Agent's sharpest standing objection, since the whole OKN model assumes
   this without direct evidence.)
7. Who represents small carriers' interests on compliance-cost equity specifically? OOIDA
   is active on broker-transparency rulemaking generally, but **no direct OOIDA quote on
   verification-cost burden was found** — the equity framing is currently inferred, not
   sourced (G8).
8. Exact NSF 2026 SBIR topic-area fit, current PAPPG page limits/required sections, and
   independent confirmation of the Proto-OKN funding total — all flagged unverified in
   the research pass and need direct confirmation before any Publishing Agent drafting
   starts (see §4, §9).
9. Has anyone from ASTM F49, NMFTA, or the named industry associations been contacted
   directly yet? Status of the four exploratory interviews from the original OKN pilot
   note (carrier/shipper veteran, startup-carrier executive, Fortune 500 safety leader,
   TMS software expert) — **this is a direct question for the user/team, not
   web-researchable.**

## 9. Deliverables (per the agent roster's Publishing Agent, see [agents/ROSTER.md](agents/ROSTER.md))

1. Logistics Duty of Care Intelligence Report (~50pp)
2. Stakeholder and Opposition Map (~15pp)
3. Regulatory Timeline (standalone, feeds visualization)
4. Technology/Competitive Landscape (standalone)
5. **NSF Project Pitch** (not a full concept memo — NSF 26-510 requires a Project Pitch
   submission and an NSF invitation *before* a full proposal can even be submitted; this
   is a process gate the original plan didn't account for. Target this format first)
6. SBIR Draft Sections — structure to be confirmed against the actual PAPPG requirements
   (§8) once retrieved, rather than assumed as Problem/Innovation/Technical Approach/
   Market/Commercialization

## 10. Source Provenance

| Section above | Primary source(s) |
|---|---|
| §1, §3 (fraud/detention figures), §7 | `raw/okn-pilot-trust-infrastructure.md` |
| §2B, §6 | `raw/cross-actor-orchestration-app-planning.md`, `raw/trust-notes.md` |
| §1, §3, §4, §5 (legal, regulatory, competitive — corrected/sourced) | [research/evidence.md](research/evidence.md), built from live web research per [research/GOALS.md](research/GOALS.md) |
| §8 research questions, agent pipeline design | `raw/agent-framework-plan.md`, `raw/ellieconvo.md` |
| Empty-mile/detention statistics | `raw/atri-operational-costs-of-trucking-2026.md` (verify page-level citations before quoting externally — extraction is machine-OCR'd from the PDF and page-level accuracy has not been spot-checked) |

## 11. Next Actions

1. **Direct question to the user/team** (§8, item 9) — not web-researchable: status of
   the four exploratory interviews, and whether anyone has contacted ASTM F49, NMFTA, or
   the named associations yet.
2. Research G7 (data-sharing incentive precedent) and G8 (small-carrier equity —
   currently inferred, not sourced) — the two remaining open research goals.
3. Before any Publishing Agent drafting starts: directly confirm the current NSF 2026
   SBIR topic-area list (only a stale 2023 version was found), PAPPG page-limit/section
   requirements, and the Proto-OKN funding total (team's "$80M/30 projects" figure
   conflicts with the archived solicitation's own "~$26.7M/18 projects").
4. Target the **NSF Project Pitch** (window opened 2026-06-02) as the first concrete
   deliverable, not a full proposal — full-proposal deadlines are 2026-11-04 or
   2027-03-04 (2026-07-27 has likely passed).
5. Manually verify the ASTM F49–CAVRA outreach claim directly with F49 leadership if
   this programme wants to pursue coordination rather than independent positioning.
6. Spot-check the ATRI PDF extraction (`raw/atri-operational-costs-of-trucking-2026.md`)
   against the original for any figure cited externally.
