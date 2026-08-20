---
type: strategy-note
status: active
owner: programme-orchestrator
schema_version: 1.0.0
updated: '2026-08-18'
tags:
- type/strategy-note
- domain/knowledge-engineering
- domain/freight
- lifecycle/active
- audience/internal
---
# Guiding Routes for Freight Trust Work

Use this note for the domain route before changing a vault artifact. Repository-root
`AGENTS.md` is the executable orchestration contract; it maps these responsibilities to
project personas in `.codex/agents/`. This guide records required inputs, output location,
and acceptance gates for the public research programme.

## Start route

1. Read [[00-home/start-here]], [[09-meta/kb-schema]], and [[09-meta/tag-taxonomy]].
2. Classify the request as source intake, dataset intake, claim synthesis, quality review,
   publishing, visualization, maintenance, or external delivery.
3. Create a task packet with objective, scope, owner, output, source standard, acceptance
   tests, and at most two retries.
4. Route only accepted evidence into client briefs, SBIR drafts, or visuals.

## Route table

| Request | Primary role | Required output and gate |
|---|---|---|
| Find or recheck an external source | Source scout / Rabbit | Source card with retrieval status; evidence verifier confirms fit. |
| Add or change a dataset | Dataset registrar | Dataset card with access, licence, verification, and consumer links. |
| Turn sources into claims or evidence records | Evidence registrar / Synthesis | Evidence entries with confidence and provenance; Review accepts. |
| Resolve terminology or ontology drift | Glossary builder | Glossary addition or collision report; schema steward validates. |
| Check structure, tags, links, or MOC membership | Schema steward + KB linker | Clean validation report; no unapproved schema/taxonomy changes. |
| Challenge a factual or proposal claim | Red-team reviewer | Severity-rated finding routed to the evidence owner or human decision-maker. |
| Rewrite accepted material for an audience | Publishing / AI-tell editor | Draft preserves facts, citations, hedges, IDs, and link anchors. |
| Build a decision, process, or architecture visual | Visualization agent | Mermaid source linked to accepted evidence or a reviewed brief. |
| Record session state, decisions, gaps, or drift | Memory keeper / drift controller | Append-only log or explicit register update; never silently close human-owned items. |

## Hard gates

- A source that was not retrieved is never treated as confirmed evidence.
- A review finding returns to the evidence or human-owner route; the reviewer does not self-close it.
- Draft, client, SBIR, and visual outputs cannot introduce facts absent from accepted evidence.
- Frozen material under [[08-archive/archive-moc]] is reference-only.
- Any current solicitation, law, price, policy, or live service claim requires a freshness check.

## Handoffs and escalation

Rabbit discovers; Synthesis organizes; Review challenges; Publishing and Visualization
translate accepted material. Terra owns decomposition, dependency order, retry limits, and
escalation. Escalate to a human owner when evidence conflicts, a legal/commercial judgement
is required, an external action is requested, or two bounded attempts fail.

## Exit checks

Before closing work, run the applicable schema/link validation, update the relevant MOC and
registers, and record material decisions or unresolved blockers in [[09-meta/decision-log]],
[[09-meta/gap-register]], or [[03-research-evidence/run-log]].

## Related

[[framework]] · [[roster]] · [[tools-and-skills]] · [[09-meta/agents-and-loops]]
