---
type: moc
area: operating-system
status: active
schema_version: 1.0.0
tags:
- type/moc
- domain/knowledge-engineering
- lifecycle/active
---
# Agent System

## Control plane

- [[framework]] — Terra orchestration, Luna synthesis, Rabbit discovery, loops, and stop conditions.
- [[guiding-routes]] — request-to-role routing, acceptance gates, handoffs, and exit checks.
- [[roster]] — roles and handoffs.
- [[mcp-capabilities]] — tool and connector boundaries.
- [[tools-and-skills]] — current tool/skill roster.

## Role notes

- [[01-rabbit-agent]] — wide-net discovery.
- [[02-synthesis-agent]] — evidence synthesis.
- [[03-review-agent]] — challenge and quality control.
- [[04-publishing-agent]] — human-readable output.
- [[05-visualization-agent]] — diagrams and visual brief support.

## Reusable research skill

- [[05-agent-system/skills/freight-trust-research/SKILL]]
- [[05-agent-system/skills/freight-trust-research/references/artifact-contracts]]
- [[05-agent-system/skills/freight-trust-research/references/source-policy]]

## Operating loop

```mermaid
flowchart LR
  T[Terra: frame and delegate] --> R[Rabbit: discover]
  R --> L[Luna: synthesize]
  L --> V[Review: challenge]
  V --> P[Publish: decide / brief]
  P --> T
```
