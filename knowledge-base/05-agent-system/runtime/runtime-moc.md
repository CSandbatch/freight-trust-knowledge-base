---
type: moc
area: agent-runtime
status: active
owner: programme-orchestrator
schema_version: 1.1.0
updated: '2026-08-12'
tags: [type/moc, domain/knowledge-engineering, domain/freight, lifecycle/active, audience/internal]
---
# Portable Agent Runtime

Tracked, platform-neutral operating specifications for Freight Trust agents. Adapters may
materialize these instructions into Claude, Codex, Cursor, or a remote MCP gateway, but
the files here are canonical. Local credentials, connector configuration, and generated
adapter files are not versioned.

## Runtime contracts

- [[agent-contract]] — branch, PR, provenance, and permission rules.
- [[retrieval-contract]] — exact → graph → semantic retrieval order.
- [[mcp-interface]] — planned headless read/write interface.

## Roles

- [[agents/source-scout]] · [[agents/dataset-registrar]] · [[agents/evidence-registrar]]
- [[agents/kb-schema-steward]] · [[agents/kb-linker]] · [[agents/drift-controller]]
- [[agents/red-team-reviewer]] · [[agents/memory-keeper]] · [[agents/publishing-agent]]
