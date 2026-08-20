---
type: strategy-note
status: active
schema_version: 1.0.0
updated: '2026-08-18'
tags:
- type/strategy-note
- domain/freight
- domain/identity
- domain/provenance
- domain/federation
- domain/orchestration
- domain/adoption
- lifecycle/active
---
# Freight Trust Infrastructure — Research Programme

This is the canonical synthesis of the project brief, operating model, freight-trust
concept, cross-actor orchestration thesis, and industry-cost context. Raw intake material
has been retired from the active vault; important inputs have been promoted here and into
the evidence register, agent-system notes, and datasets-and-experiments MOC.

**Status (updated after the 2026-08-18 E1–E5 Rabbit review):** the programme mixes confirmed
primary facts, peer-reviewed method precedents, secondary/vendor context, scoped negative
searches, protocol choices and unrun hypotheses. Their confidence and limitations remain
explicit rather than being described collectively as “checked.” See
[[03-research-evidence/evidence|03-research-evidence/evidence.md]] for full citations and confidence levels,
[[03-research-evidence/goals|03-research-evidence/goals.md]] for the research goals that drove this pass, and
[[03-research-evidence/plan|03-research-evidence/plan.md]] for what comes next. Two of the team's original
working assumptions turned out to need correction (§1, §5), and the controlling experiment
interfaces and claim ladder are now in [[03-research-evidence/integrated-e1-e5-research-programme]].

## 1. Core Thesis

Freight logistics runs on fragmented trust. Carrier identity, safety compliance,
insurance validity, and operational responsibility are distributed across shippers,
brokers, carriers, drivers, facilities, and insurers — parties with asymmetric
information and no neutral, cross-party record of ground truth.

Two convergent problems make this urgent right now, and one legal event just made it
concrete:

- **Fraud** — public enforcement, industry and carrier-association sources document carrier-
  identity abuse and cargo theft, but this programme does not use the older `$7–16B` and
  `$750M–$1B` figures as a validated population baseline.
- **Detention / dwell** — [[03-research-evidence/source-atri-fmcsa-driver-detention]] verifies
  ATRI's 2024 page reporting estimates for its 2023 industry sample (39.3% of reported stops,
  more than 135M lost hours, $3.6B direct expense and $11.5B productivity loss). These are not
  federal population estimates, and FMCSA still treats separation of dwell from detention as a
  measurement problem.
- **Empty miles** — empty movements are an observed freight-efficiency problem, but their level
  depends on the declared dataset, population and definition; E5 does not import a single
  industry percentage as its result or assume an orchestration layer will reduce it.
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
  proprietary framework positioned as an industry standard, not a neutral one. That is
  a real strategic point in this programme's favor, not just competitive noise: a
  proposed neutral, interoperable evidence layer could offer a different value proposition than a
  vendor's. The claim that ASTM F49 reached out to incorporate CAVRA into a
  formal guide **could not be verified** — no reference to CAVRA appears in ASTM F49's
  current work-item list; treat as unconfirmed until checked directly with F49
  leadership. Full sourcing: [[03-research-evidence/evidence|03-research-evidence/evidence.md]] §G1/G1b/G5.

The working strategic hypothesis, carried over unchanged from the team's original framing:

> Logistics does not merely need fraud detection; it needs a computational duty-of-care
> layer that can establish trust, responsibility, and liability across fragmented
> transportation networks.

This programme exists to prove or disprove that hypothesis with evidence — not assume it.

## 2. The Two Product/Research Angles (and why they're one programme)

Two threads run through the programme. They are one thesis seen from two
altitudes, not two competing ideas:

**A. Freight Trust OKN (infrastructure / federal angle)** — an Open Knowledge Network,
per the NSF/OSTP 2022 roadmap, composed of interlinked knowledge graphs:
- *Carrier Credentialing Graph* — separately represents legal-person resolution, authoritative
  identifier assignment/use, typed ownership/control/succession relationships, insurance and
  performance assertions, source/time, corrections, and uncertainty. E1 does not ingest a
  universal EIN field, collapse relationships into identity, produce a Freight Trust Index, or
  issue fraud/risk determinations.
- *Facility Performance Knowledge Graph* — timestamped event graph (tendered → appointment
  → arrival → dock → loading → departure) that makes dwell/detention a matter of record
  rather than a dispute between carrier and shipper logs.
- Positioned as public infrastructure, not a vendor product — analogous to DOT's 1987
  on-time-disclosure mandate for airlines, and explicitly proposed as a candidate for
  NSF's Proto-OKN programme. The verified 2023 inaugural cohort was 18 projects totaling about
  $26.7M; the older “~30 use cases at $80M” figure is not used.

**B. Cross-Actor Orchestration (applied / product angle)** — a system for actually
*using* that trust/data layer to reduce empty miles and dwell in real time: matching
backhaul loads to returning trucks, modeling the profit-service-risk triangle explicitly
at each decision point, and treating the empty-mile problem as a **governance and
incentive problem**, not just a routing/visibility problem: local optimization by each
actor produces system-wide waste, so decision authority and aligned scorecards must be
explicit. Someone has to govern the full network, not just individual nodes.

**Why they're one programme:** the OKN is the trust/data substrate; cross-actor
orchestration is the first (and clearest) high-value application built on top of it. The
NSF SBIR angle should lead with the substrate (research novelty: dynamic trust
infrastructure, entity resolution, regulatory reasoning) and cite orchestration as the
proof-of-value use case, not the other way around. An "orchestration app" alone reads as
a product pitch, not research; the trust-graph framing is what makes it fundable as NSF
research rather than a logistics startup.

## 3. Stakeholder Landscape

| Stakeholder | Interest | Position (🟢 sourced / 🟡 partly sourced / 🔴 unverified) |
|---|---|---|
| FMCSA / DOT (Sean Duffy era) | Safety, fraud enforcement | 🟢 Motus system objects, identity/business-verification functions and the 2026 availability notice are primary-sourced. Reported login/verification and deactivation-pause events establish rollout and implementation risk; they do **not** directly prove E1's narrower longitudinal legal-person-resolution problem under corrupted/conflicting anchors. |
| Brokers | Efficiency, liability exposure | 🟢 Post-*Montgomery*, negligent-selection claims are now viable nationwide; the $604M *Lipe v. Lupus Superior* verdict (2026-07-24, on appeal) shows real exposure. Brokers need a defensible due-diligence record but will resist anything that expands liability further than that |
| Carriers (legitimate) | Fair competition, reputation protection | 🟡 Directionally favorable (unchanged from initial assessment; not independently re-verified this pass) |
| Small carriers | Market access | 🟡 OOIDA (their clearest representative) frames fraud as an existential risk to small carriers, but a **direct OOIDA quote on verification/compliance costs disproportionately burdening small carriers was not found** — that specific equity framing is currently inferred, not sourced. Needs a better citation before use in any external-facing deliverable |
| Shippers | Reliability, loss reduction | 🟡 Directionally favorable (unchanged; not independently re-verified) |
| Insurers | Risk-adjusted underwriting | 🟡 Directionally favorable (unchanged; not independently re-verified) |
| Technology vendors | Market share | 🟢 **Confirmed differentiator**: of 13 named competitors, only project44 markets anything resembling graph technology (a proprietary "logistics data graph," not a neutral cross-party network); none position as neutral infrastructure. Only Truckstop.com (via its RMIS acquisition) spans both fraud-vetting and load-matching — everyone else is single-focus. Full breakdown in §5 |
| Industry associations | Represent member interests | 🟢 ATA publicly backs anti-fraud legislation (SAFER in Transport Act); OOIDA filed a formal comment on FMCSA's broker-transparency rulemaking (49 CFR 371, primary source); TCA backs CORCA (cargo-theft legislation); CVSA is active on inspection data-interoperability but silent on duty-of-care/detention; NPTC's position is inaccessible (members-only). None have been contacted directly yet — this table reflects public positions, not outreach |
| Standards bodies | Interoperability | 🟢 ASTM F49 is the most concretely active body found: new goods-movement process codes, transport-unit-identifier standards, and a conformity-assessment guide, all in 2026 — high-value ally, confirmed no CAVRA linkage. NMFTA's 2026 focus is cybersecurity/cargo-crime, not duty-of-care specifically, but publishes the freight OpenAPIs (eBOL, pickup/visibility, freight charges) this programme's ontology should align to |
| Lawyers / transportation law firms | Liability clarity, precedent-setting | 🟢 Actively organizing post-*Montgomery* (multiple law-firm client alerts within days of the ruling — Hinshaw, DLA Piper, Crowell & Moring, Honigman). The CAVRA Standard is a **vendor-authored** attempt to define the evidentiary bar (see §1 conflict-of-interest note); a neutral alternative is a real differentiator |
| Law enforcement (FBI, DOJ, DHS) | Organized fraud/theft interdiction | 🔴 Unverified — no signal found on active interest, not researched this pass |

**Who pushes back, and why (unresolved — needs Review Agent + more Rabbit Agent evidence):**
- Brokers, if the duty-of-care standard the OKN embodies expands their liability beyond
  what they can control.
- Any platform with a proprietary carrier database, if a proposed neutral, interoperable
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

Full sourcing in [[03-research-evidence/evidence|03-research-evidence/evidence.md]]. Remaining gaps: PAPPG
page-limit/section requirements (needs direct check), current 2026 SBIR topic-area list
(only a stale 2023 version was found). The obsolete Proto-OKN `$80M/30-project` figure is
superseded by the verified inaugural-cohort figure above and must not be cited.

## 5. Technology / Competitive Landscape

Researched — see full table with sources in
[[03-research-evidence/evidence|03-research-evidence/evidence.md §G4]]. In the reviewed public
product materials as of 2026-08-18, no named competitor described the same proposed neutral,
cross-party evidence architecture. That is a scoped negative retrieval result, not evidence
about undisclosed internal systems or proof of a permanent market differentiator. project44
describes a proprietary logistics data graph; product terminology alone does not establish or
exclude the underlying architecture of any vendor.

Second finding: the landscape is split almost cleanly by problem area — most companies do
either fraud/identity verification (Highway, Carrier Assure, FreightValidate) **or**
visibility/detention (FourKites, Tive, Samsara, Motive) **or** load-matching (DAT, PTTR,
Amazon Relay). Within the reviewed public descriptions, Truckstop.com (via its 2021 RMIS
acquisition) spans fraud-vetting and load-matching. No reviewed public description was found
that spans the programme's identity, event, governance and orchestration layers; this does not
establish that no company has comparable private capabilities.

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
transition is a place where lag/dwell can be introduced, and where governance could reduce it.

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

The more rigorous thesis: build and evaluate a **federated, provenance-preserving
decision-support layer** that joins authoritative credential evidence and permissioned
facility-event records. Its first outcomes are verification accuracy, resolution time,
event completeness, dispute time, participation, and equity—not an unqualified
industry-wide “Trust Index.” The system may produce optional, explainable indicators,
but no score should control eligibility, pricing, contracting, or liability without
human review and a correction path.

This framing has technical precedent in peer-reviewed supply-chain knowledge-graph and
federated-learning work, plus NIST's traceability meta-framework, and a governance
precedent in federated mobility data spaces and shared legal-entity identity utilities.
Those precedents make the research question credible, not pre-solved. Full sourcing,
falsifiable hypotheses, pilot measures, and residual gaps are in
[[03-research-evidence/luna-wide-net-synthesis|03-research-evidence/luna-wide-net-synthesis.md]].

## 8. Open Research Questions

**Resolved this pass** (full detail in [[03-research-evidence/evidence|03-research-evidence/evidence.md]]):

1. ✅ FMCSA/Duffy activity — Motus registration system, primary-sourced timeline (§4).
2. ✅ The legal decision is *Montgomery v. Caribe Transport II* — a preemption ruling,
   not a duty-of-care definition (§1). Correction, not just confirmation.
3. ✅ CAVRA Standard is Cassandra Gaines' own framework; she also founded competitor
   Carrier Assure — it's vendor-authored, not neutral (§1, §5).
4. ✅ The dated public-materials review found no named competitor describing the same proposed
   neutral, cross-party architecture; no conclusion is drawn about private capabilities (§5).
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

## 9. Deliverables (per the agent roster's Publishing Agent, see [[05-agent-system/roster|05-agent-system/roster.md]])

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
| §1, §3 (fraud/detention figures), §7 | Promoted programme synthesis and cited evidence register |
| §2B, §6 | Promoted cross-actor orchestration model and domain vocabulary |
| §1, §3, §4, §5 (legal, regulatory, competitive — corrected/sourced) | [[03-research-evidence/evidence|03-research-evidence/evidence.md]], built from live web research per [[03-research-evidence/goals|03-research-evidence/goals.md]] |
| §8 research questions, agent pipeline design | Promoted research goals, operating model, and agent-system notes |
| Empty-mile/detention statistics | Cited public evidence and research register; verify page-level support before external reuse |

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
6. Verify any ATRI-derived figure against the cited public study record before external reuse.
