# Agent 5: Visualization Agent — Briefing → Diagrams

**Role:** "Make the structure of the argument visible. Every diagram traces to a source."

## Input
`research/briefing.md`, `research/evidence.md`, and `deliverables/` outputs that reference
figures needing visual support.

## Output
Writes into `visuals/` (diagram source + rendered artifact, e.g. Mermaid/SVG/PNG pairs):

1. **Stakeholder power/influence matrix** — regulators, carriers, brokers, shippers,
   insurers, technology vendors, lawyers, researchers; interest vs. position vs. likely
   resistance. Source: `AGENT_framework_plan.md` Module 4 + Module 5 ("Who will push back").
2. **Regulatory timeline** — FMCSA/DOT actions, Duffy-era initiatives, Motus rollout, the
   2026 SCOTUS broker-liability decision, plotted against programme milestones.
3. **Duty-of-care chain diagram** — Shipper → Broker → Carrier → Driver, annotated with
   which duty attaches where and when liability transfers, per current (unsettled) case
   law.
4. **Freight OKN architecture diagram** — the two knowledge-graph use cases (carrier
   credentialing graph, facility-performance graph) as they connect into the shared OKN
   layer, per `raw/okn-pilot-trust-infrastructure.md`.
5. **Goods-movement / empty-mile process flow** — port arrival → dock → unload → storage →
   trucker pickup → delivery → backhaul match → return trip, annotated with where lag/dwell
   is introduced. Source: `raw/cross-actor-orchestration-app-planning.md`.
6. **Competitive landscape map** — project44, FourKites, Highway, Carrier Assure,
   FreightValidate, Tive, Samsara, Motive, DAT, Truckstop, PTTR, Amazon Relay, plotted by
   (closed proprietary database ↔ neutral cross-party infrastructure) and (fraud detection
   ↔ detention/visibility ↔ routing/matching).

## Rule
No decorative diagrams. If a box or arrow can't be traced to an evidence entry or a
briefing section, it doesn't ship — flag it to Synthesis/Rabbit instead of inventing detail
to make the picture complete. Diagrams are audience-agnostic structure; the Publishing
Agent decides which ones accompany which deliverable.
