---
type: strategy-note
status: active
schema_version: 1.0.0
updated: '2026-08-08'
tags:
- type/strategy-note
- domain/freight
- domain/knowledge-engineering
- audience/internal
- lifecycle/active
---
# Research Goals

Formalized from `02-programme-strategy/research-programme.md` §8. Each goal has a success criterion (what
"done" looks like — a fact with a primary source, not a plausible narrative) and an
owning agent. Tier 1 blocks everything downstream; Tiers 2–3 can run in parallel once
Tier 1 is underway.

## Tier 1 — Load-bearing facts (everything else cites these)

**G1. Pin the SCOTUS broker-duty-of-care decision.**
Success: case name, citation, docket number, decision date, holding, and — critically —
what the Court explicitly declined to define. Every claim in the programme about
"post-SCOTUS liability" currently has no citation behind it.
Owner: Rabbit Agent → Synthesis Agent.

**G2. Pin the FMCSA / Sean Duffy fraud initiative.**
Success: primary-source document (press release, Federal Register notice, DOT.gov
announcement, or speech transcript), dated, with the specific actions named — not a
secondhand trade-press characterization.
Owner: Rabbit Agent.

**G3. Retrieve the current NSF SBIR/STTR solicitation.**
Success: the actual current solicitation document (topic areas, Phase I page limits,
required sections, review criteria, submission deadlines). Blocks all Publishing Agent
SBIR deliverables — nothing should be drafted against a remembered/assumed template.
Owner: Rabbit Agent → Publishing Agent.

## Tier 2 — Competitive and standards landscape

**G4. Classify the twelve named competitors** (project44, FourKites, Highway, Carrier
Assure, RMJ, FreightValidate, Tive, Samsara, Motive, DAT, Truckstop, PTTR Load Board) plus
Amazon Relay by: closed proprietary database vs. any knowledge-graph/interoperability
architecture; fraud detection vs. detention/visibility vs. routing/matching focus.
Success: one evidence entry per company minimum, citing product docs/site, not inference
from company name.
Owner: Rabbit Agent → Synthesis Agent (feeds Visualization Agent's competitive map).

**G5. Determine the status of the CAVRA Standard.**
Success: what CAVRA actually specifies (data fields, evidentiary bar), current adoption,
and whether ASTM F49 incorporation ever happened. Determines whether this programme
should fold CAVRA in, coordinate, or compete against it.
Owner: Rabbit Agent.

**G6. Map industry associations and standards bodies to actual positions**, not assumed
interest — ATA, NPTC, OOIDA, NASTC, TCA, NAIT, CVSA, Food Shippers of America, National
Retail Federation, National Grocers Association, ASTM F49, NMFTA.
Success: for each, a public statement, published position paper, or a first-degree
contact — not inclusion-by-plausibility.
Owner: Rabbit Agent → Synthesis Agent (feeds stakeholder matrix).

## Tier 3 — Adoption economics and equity

**G7. Test the data-sharing incentive assumption.**
The entire OKN model assumes brokers/carriers will voluntarily share data with a neutral
third party. Success: find at least one analogous precedent (another industry's neutral
data trust, e.g. banking KYC utilities, airline on-time reporting compliance) and what
made participation happen — mandate, liability shield, or market pressure — since no
direct evidence exists yet for freight specifically.
Owner: Rabbit Agent → Review Agent (this is the Review Agent's sharpest standing
objection).

**G8. Assess small-carrier compliance-cost equity risk.**
Success: identify who speaks for small/owner-operator carriers (OOIDA is the obvious
first stop) and what they've said, if anything, about verification/compliance burden
scaling with fleet size.
Owner: Rabbit Agent.

**G9. Confirm status of the four exploratory interviews** referenced in the OKN pilot
concept note (carrier/shipper veteran, startup-carrier executive, Fortune 500 safety
leader, TMS software expert).
Success: this is not web-researchable — it requires asking the user/team directly whether
these interviews happened and what came out of them.
Owner: User/team (flag as a direct question, not a Rabbit Agent task).

## Tier 4 — Research validity, pilot design, and governance

**G10. Replace broad outcome assertions with falsifiable pilot hypotheses.**
Success: define baseline, intervention, comparison, success threshold, and failure
condition for entity verification, facility-event provenance, adoption, and small-carrier
equity. Do not claim fraud, detention, or empty-mile reduction without a measured pilot.
Owner: Terra (orchestrator) → Synthesis Agent → Review Agent.

**G11. Define the minimum trusted-data architecture.**
Success: document the authoritative source, provenance record, access policy, correction
path, and retention rule for every proposed claim type. The architecture must be federated
by default; raw partner-data pooling needs a specific justification.
Owner: Luna technical subagents → Synthesis Agent.

**G12. Test the participation mechanism.**
Success: specify at least three concrete reciprocal benefits and a pilot method to measure
uptake and retention by stakeholder and fleet size.
Owner: Luna adoption subagent → Review Agent.

**G13. Define redress and non-discrimination requirements.**
Success: a written policy for automated-indicator abstention, human review, participant
correction/challenge, false-positive remediation, and no-paywall basic verification.
Owner: Terra → legal/human review.

**G14. Build the freight evidence benchmark.**
Success: an adjudicated sample of identity and facility-event cases with provenance labels,
against which precision, recall, calibration, abstention, and dispute-resolution metrics
can be measured.
Owner: Luna technical and operations subagents.
Status (2026-08-01): dataset/tooling scan complete, benchmark not yet built. See
[[dataset-scan-entity-resolution]] (identity/Aim 1 — real seed source confirmed: FMCSA
Company Census File, no agreement required; no labeled chameleon-carrier dataset exists
anywhere) and [[dataset-scan-event-provenance-and-federation]] (facility-events/Aim 2 —
no freight-specific event benchmark exists anywhere, confirmed; buildable via OpenEPCIS
generator + process-mining anomaly-injection methodology — and Aim 3 policy enforcement —
resolved to a concrete, no-cost build path via NIST's open-source Policy Machine + OASIS
XACML conformance-test format). Actual benchmark construction, adjudication protocol, and
numeric targets remain open Phase I work, not resolved by this scan.

## Non-goals (explicitly out of scope for this pass)

- Actually drafting SBIR prose (Publishing Agent's job, blocked on G3).
- Building any OKN software/ontology artifacts (this is intelligence-gathering, not
  engineering, at this stage).
- Contacting stakeholders directly (G6/G9 flag *who* to contact; outreach itself is a
  team decision, not an agent action).
