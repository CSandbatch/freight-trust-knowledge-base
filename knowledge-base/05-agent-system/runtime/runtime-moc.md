---
type: moc
area: agent-runtime
status: active
owner: programme-orchestrator
schema_version: 1.1.0
updated: '2026-08-18'
tags: [type/moc, domain/knowledge-engineering, domain/freight, lifecycle/active, audience/internal]
---
# Portable Agent Runtime

Tracked, platform-neutral operating contracts for Freight Trust agents. The executable
Codex orchestration policy and persona factory are repository infrastructure in root
`AGENTS.md` and `.codex/agents/`, outside the public vault. Local credentials and
connector configuration are never versioned.

## Runtime contracts

- [[agent-contract]] — branch, PR, provenance, and permission rules.
- [[retrieval-contract]] — exact → graph → semantic retrieval order.
- [[mcp-interface]] — planned headless read/write interface.

## Roles

The current project-scoped roles are the TOML definitions in root `.codex/agents/`.
`AGENTS.md` contains the routing table and bounded-loop policy. These runtime definitions
are intentionally excluded from the public corpus boundary.
