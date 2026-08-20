---
type: moc
area: decisions
status: active
owner: memory-keeper
schema_version: 1.1.0
updated: '2026-08-18'
tags: [type/moc, domain/knowledge-engineering, domain/freight, lifecycle/active, audience/internal]
---
# Atomic Decisions MOC

New decisions use one `dec-###.md` file per immutable ID. The historic [[decision-log]]
remains the source for `DEC-001` through `DEC-012` until each record is individually
migrated and linked here; no historic content is duplicated or renumbered.

## Active decisions

- [[dec-013-llm-e1-challenger]] — adds a constrained, preregistered LLM resolver challenger
  without changing E1 gold semantics or the one-shot confirmatory gate.
