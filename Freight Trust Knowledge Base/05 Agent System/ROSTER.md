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

The five specialist agents are coordinated by a Programme Orchestrator. The roster is
not a one-way pipeline: the Orchestrator can fan out independent tasks, route review
objections back to the correct research branch, and stop after bounded retries. See
[research/OPERATING_MODEL.md](../research/OPERATING_MODEL.md) for task packets, loops,
gates, and escalation rules.

The concise control-plane reference is [FRAMEWORK.md](FRAMEWORK.md). The reusable
project skill is [`freight-trust-research`](skills/freight-trust-research/SKILL.md), and
the connector/tool boundary is [MCP_CAPABILITIES.md](MCP_CAPABILITIES.md).

## Shared contract

Every agent reads and writes into the same research memory rather than private scratch
state, so provenance survives the handoff:

- `raw/` — source-of-truth documents (converted from originals, never edited in place)
- `research/evidence.md` (or `.json` once volume justifies a real store) — the Rabbit
  Agent's running evidence graph: one entry per claim, schema below
- `research/briefing.md` — the Synthesis Agent's current draft, always superseded in
  place (git-style diffs, not forked copies)
- `research/review-notes.md` — the Review Agent's open objections, tagged resolved/open
- `deliverables/` — Publishing Agent output (SBIR drafts, memos, one-pagers)
- `visuals/` — Visualization Agent output (diagram source + rendered image)

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

1. [Rabbit Agent](01-rabbit-agent.md) — discovery, breadth, no conclusions
2. [Synthesis Agent](02-synthesis-agent.md) — briefing, structure, named uncertainty
3. [Review Agent](03-review-agent.md) — adversarial stress test
4. [Publishing Agent](04-publishing-agent.md) — briefing → SBIR sections, memos, stakeholder-facing copy
5. [Visualization Agent](05-visualization-agent.md) — briefing → stakeholder maps, timelines, diagrams

See [TOOLS_AND_SKILLS.md](TOOLS_AND_SKILLS.md) for what each agent actually needs to do
its job — available now, worth adding, or a human/access gap no agent closes.

## Current cycle

Goals, source library, and phased plan for the active research pass live in
[research/GOALS.md](../research/GOALS.md) and [research/PLAN.md](../research/PLAN.md);
sourced findings accumulate in [research/evidence.md](../research/evidence.md).

## Operating principle

Rabbit does not judge. Synthesis does not invent. Review does not soften. Publishing does
not add new claims. Visualization does not decorate — every diagram must trace back to an
evidence entry or a briefing section. If a diagram or a deliverable sentence has no
traceable source, that is a Review Agent finding, not a Publishing/Visualization Agent
judgment call.
