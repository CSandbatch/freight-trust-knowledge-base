---
type: strategy-note
status: planned
owner: programme-orchestrator
schema_version: 1.1.0
updated: '2026-08-12'
tags: [type/strategy-note, domain/knowledge-engineering, domain/freight, lifecycle/planned, audience/internal]
---
# Headless Freight Trust MCP Interface

The production gateway is Git-aware and authenticated. Read operations expose
`kb.search`, `kb.read`, `kb.related`, `kb.claims`, `kb.sources`, `kb.decisions`, and
`kb.status` against protected canonical state. Write operations expose
`kb.create_candidate`, `kb.patch_candidate`, and `kb.submit_change`; each creates a
branch and pull request rather than writing to `master`. Hosting, identity provider,
authorization model, and secrets management remain deployment decisions.
