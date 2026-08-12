---
type: strategy-note
status: active
schema_version: 1.0.0
tags:
- type/strategy-note
- domain/knowledge-engineering
- domain/freight
- lifecycle/active
---
# Tools & Skills Roster

What each agent in [[05-agent-system/roster|roster.md]] actually needs to do its job — split into what's
already available in this environment, what would need to be added, and what no agent can
substitute for (human access/skill gaps). Written after the first live research pass
(Phase 1 of [[03-research-evidence/plan|03-research-evidence/plan.md]]), so this reflects real friction, not
guesswork.

## Orchestration layer (new)

The programme now needs a lightweight Orchestrator role and an evidence-verification
gate. These do not require a new external service yet: the current Codex session or a
human operator can maintain [[03-research-evidence/run-log|`03-research-evidence/run-log.md`]], create task
packets, route objections, and enforce retry limits. A structured JSON store or workflow
runner becomes worthwhile only when the number of concurrent tasks makes Markdown
tracking unreliable.

Recommended future capabilities: stable claim IDs, source retrieval snapshots,
citation-entailment checks, per-task retry budgets, and a machine-readable execution
trace. NIST's evaluation-probe work is a useful reference for the audit-trail shape.

The current capability contract is [[05-agent-system/mcp-capabilities|mcp-capabilities.md]]. The
project-local reusable workflow is
[[05-agent-system/skills/freight-trust-research/SKILL|`freight-trust-research`]].

## Rabbit Agent

**Available now:**
- `WebSearch` / `WebFetch` — general web research, the workhorse for most of Tier 1–2.
- Google Drive search (`mcp__claude_ai_Google_Drive__*`) — the team's notes reference
  emails, decks, and conversations with Matt/Bola/Evan that may live in Drive rather than
  this local folder. Worth a pass to check for source material this programme doesn't
  have yet, before assuming the active evidence register is complete.
- PDF/DOCX-to-markdown extraction is an intake step, not an active-vault dependency —
  reusable for any future document intake.

**Would help, not available:**
- **Case law search** — CourtListener/RECAP (free, covers federal courts including
  circuit courts of appeals — more useful here than paid Westlaw/Lexis for a first pass)
  for pinning G1 precisely. Web search can usually find case *commentary*; it's weaker at
  finding the actual opinion PDF and docket.
- **Federal Register / regulations.gov API** — better than web search for G2 (FMCSA
  notices) and tracking any open rulemaking dockets and comment periods relevant to
  broker liability or carrier verification.
- **NSF award search** (`award.nsf.gov`) — for identifying the ~30 existing Proto-OKN
  awardees by name, to benchmark this concept against funded precedent rather than
  describing the program only in the abstract.
- **Company intelligence** (Crunchbase/PitchBook-class data) — for G4, to get funding
  stage, actual customer base, and product depth on the 13 competitors beyond what their
  marketing sites say. Not available in this environment; web search is a workable
  substitute but weaker on funding/traction specifics.

## Synthesis Agent

**Available now:** long-context reading and structured writing — no special tooling
needed beyond what's already in use for `02-programme-strategy/research-programme.md`.

**Skill, not tool:** light ontology/domain-modeling discipline for §6/§7 (the
vocabulary and technical-architecture sections) — keep it a sketch, not a formal
RDF/OWL schema, until Phase 6 actually requires one.

## Review Agent

**Available now:** the four adversarial personas are prompt-driven, not tool-driven —
already spec'd in [[05-agent-system/03-review-agent|03-review-agent.md]].

**Would help:** the ability to re-run a targeted `WebSearch` mid-review to check whether a
Synthesis Agent claim is actually supported, rather than only reviewing the prose as
given. Worth explicitly allowing Review Agent to kick a claim back to Rabbit with a
specific query attached instead of only flagging it as unsupported.

## Publishing Agent

**Available now:** markdown drafting.

**Would help, not available yet:**
- The **actual current NSF SBIR/STTR solicitation document** (G3) — this agent should not
  start drafting section-by-section content until that's retrieved; drafting against a
  remembered/assumed template is exactly the failure mode this whole programme is trying
  to avoid.
- **Document formatting for submission** — NSF SBIR proposals go through Research.gov as
  PDF, with specific formatting rules (margins, font size, page limits per section). A
  markdown → PDF pipeline (e.g. via a local pandoc install, which isn't currently
  installed in this environment) will be needed once drafting actually starts.

**Skill, not tool:** grant-writing craft — specifically, writing to NSF's actual review
criteria (Intellectual Merit / Broader Impacts, plus SBIR-specific commercial-potential
criteria) rather than general persuasive writing. This is a real skill gap worth having a
human with prior NSF SBIR experience review before submission, not just an agent output.

## Visualization Agent

**Available now:**
- Mermaid diagrams (already used for the pipeline diagram in `05-agent-system/roster.md`) — sufficient
  for the duty-of-care chain, OKN architecture, and process-flow diagrams in
  `03-research-evidence/plan.md` Phase 7.
- The `dataviz` skill available in this environment — load it before building any actual
  charts (e.g. a bar comparison of the $7–16B fraud / $15B detention / $11.5B lost-
  productivity figures), rather than freehanding chart colors/layout.
- `Artifact` publishing — for turning a finished stakeholder map or regulatory timeline
  into a shareable, presentable page rather than a static markdown table, when it's time
  to actually show these to teammates or external contacts.

**Would help, not available:** real geographic mapping (port locations, freight lane
flows) would benefit from actual geodata (e.g. port coordinates, lane volume data) that
hasn't been collected — the empty-mile process-flow diagram should stay a stylized
flowchart, not a literal map, until/unless that data gets pulled in.

## Human / team skill gaps — no agent substitutes for these

1. **Direct outreach** — contacting the ASTM F49 committee chair, industry associations,
   or the four exploratory interview candidates (G9) requires a person with existing
   relationships, not a research agent. This is explicitly out of agent scope per
   `03-research-evidence/goals.md`.
2. **Legal sanity-check** — the Review Agent's "transportation lawyer" persona is a
   simulation. Before the duty-of-care characterization goes into an SBIR narrative or
   anything external-facing, it needs an actual lawyer's read, especially once G1 is
   pinned down and the real holding (which may be narrower than the team's current
   framing) is known.
3. **NSF pre-submission conversation** — standard SBIR practice is a conversation with an
   NSF program director before submitting, to sanity-check topic fit. This is a
   relationship/access item, not a research task.
4. **Grant-writing review** — someone who has actually written or reviewed a funded NSF
   SBIR should sanity-check Publishing Agent drafts before submission; the Review Agent's
   "NSF reviewer" persona narrows the gap but doesn't close it.
