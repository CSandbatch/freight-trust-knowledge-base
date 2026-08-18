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
# Agent Roster — Freight Trust Research Programme

Five agents, chained into one pipeline. Three do research, one turns research into
deliverables, one turns research into pictures. Each agent has a single job, a defined
input, and a defined output artifact — no agent should silently absorb another's role.

```
                 ┌─────────────┐
                 │ Rabbit Agent │  breadth-first collection, no judgment
                 └──────┬──────┘
                        │ evidence graph (raw claims + sources)
                        ▼
                 ┌──────────────┐
                 │ Synthesis     │  turns chaos into a briefing
                 │ Agent         │
                 └──────┬────────┘
                        │ intelligence briefing (structured doc)
                        ▼
                 ┌──────────────┐
                 │ Review Agent  │  attacks the argument
                 └──────┬────────┘
                        │ annotated briefing + open questions
            ┌───────────┴────────────┐
            ▼                        ▼
   ┌─────────────────┐      ┌──────────────────┐
   │ Publishing Agent │      │ Visualization      │
   │                   │      │ Agent              │
   └─────────────────┘      └──────────────────┘
   SBIR sections,            stakeholder maps, timelines,
   briefing memos,           architecture diagrams,
   stakeholder one-pagers    process flows
```

## Coordination model

A Programme Orchestrator coordinates the five specialist agents. The roster is not a
one-way pipeline: the Orchestrator can fan out independent tasks, route review objections
back to the correct research branch, and stop after bounded retries. See
[[03-research-evidence/operating-model|03-research-evidence/operating-model.md]] for task packets, loops,
gates, and escalation rules.

The concise domain control-plane reference is [[05-agent-system/framework|framework.md]].
Repository-root `AGENTS.md` now controls execution and routes work to project personas in
`.codex/agents/`. The reusable project skill is
[[05-agent-system/skills/freight-trust-research/SKILL|`freight-trust-research`]], and the
connector/tool boundary is [[05-agent-system/mcp-capabilities|mcp-capabilities.md]].

## Shared contract

Every agent reads and writes into the same research memory rather than private scratch
state, so provenance survives the handoff:

- Active canonical notes and the evidence register — promoted findings with provenance and confidence
- `03-research-evidence/evidence.md` (or `.json` once volume justifies a real store) — the Rabbit
  Agent's running evidence graph: one entry per claim, schema below
- `03-research-evidence/briefing.md` — the Synthesis Agent's current draft, always superseded in
  place (git-style diffs, not forked copies)
- `03-research-evidence/review-notes.md` — the Review Agent's open objections, tagged resolved/open
- `01-client-briefs/` or `04-sbir/` — Publishing Agent output (SBIR drafts, memos, one-pagers)
- `07-visuals/` — Visualization Agent output (diagram source + rendered image)

Evidence schema (used by every agent that cites a claim):

```
{
  title, organization, date, url,
  stakeholder_category,   # regulator | carrier | broker | shipper | insurer | vendor | law firm | association
  claim,
  evidence,
  confidence,              # low | medium | high
  conflicts_of_interest,
  related_entities
}
```

Every delegated task also needs a task packet containing a task ID, parent task, owner,
objective, scope, required source class, output artifact, acceptance tests, maximum
attempts, and status. Review objections must include claim IDs, missing evidence, a
suggested query, and a return destination.

## Agents

0. **Programme Orchestrator** — decomposes goals, fans out independent tasks, assigns
   retries, owns gates, and escalates judgment calls. This is a coordinating role, not a
   license for every agent to rewrite every artifact.

1. `source_scout` — Rabbit-style discovery, breadth, no unsupported conclusions
2. `evidence_synthesizer` — briefing, structure, and named uncertainty
3. `red_team_reviewer` — independent adversarial stress test
4. `publisher` — accepted briefing → SBIR sections, memos, and stakeholder-facing copy
5. `visualization_engineer` — accepted evidence → maps, timelines, and diagrams

Specialized maintenance, graph, dataset, glossary, memory, and prose personas are listed
in root `AGENTS.md` and defined in `.codex/agents/`.

See [[05-agent-system/tools-and-skills|tools-and-skills.md]] for what each agent actually needs to do
its job — available now, worth adding, or a human/access gap no agent closes.

## Current cycle

Goals, source library, and phased plan for the active research pass live in
[[03-research-evidence/goals|03-research-evidence/goals.md]] and [[03-research-evidence/plan|03-research-evidence/plan.md]];
sourced findings accumulate in [[03-research-evidence/evidence|03-research-evidence/evidence.md]].

## Operating principle

Rabbit does not judge. Synthesis does not invent. Review does not soften. Publishing does
not add new claims. Visualization does not decorate — every diagram must trace back to an
evidence entry or a briefing section. If a diagram or a deliverable sentence has no
traceable source, that is a Review Agent finding, not a Publishing/Visualization Agent
judgment call.
