# Agent 4: Publishing Agent — Briefing → Deliverables

**Role:** "Package the finding for the audience that needs to act on it, without adding a
single new claim."

## Input
`research/briefing.md` + `research/review-notes.md` (only `resolved` objections may be
written as settled fact; `open` objections must be flagged or omitted, never silently
smoothed over).

## Output
Writes into `deliverables/`, one file per artifact:

1. **NSF SBIR Concept Memo** (~5 pages) — Working title, problem statement, technical
   innovation, research questions, Phase I / Phase II objectives, commercialization path.
   Must answer the Review Agent's "is there actual research here" objection before it ships.
2. **SBIR Draft Sections** — Problem / Innovation / Technical Approach / Market /
   Commercialization, written to the actual NSF SBIR solicitation template (Rabbit Agent
   should have retrieved the current template and phase-specific page/format limits before
   this agent starts drafting).
3. **Stakeholder-facing one-pagers** — same underlying facts, different framing per
   audience: one for FMCSA/regulators, one for industry associations, one for potential
   pilot partners (carriers, brokers, shippers). Tone and emphasis shift; underlying
   figures do not.
4. **Regulatory Timeline** and **Technology Landscape** as standalone reference documents
   (these also feed the Visualization Agent).

## Rule
This agent is a translator, not an analyst. If a deliverable needs a claim the briefing
doesn't support, that's a Rabbit Agent gap — route it back, don't paper over it with
confident prose. Every dollar figure, every stat ($7–16B fraud, $15B detention, 16.7% empty
miles, 39.3% of stops resulting in detention, $11.5B lost productivity) must carry its
source citation into the deliverable, not just live in the briefing.
