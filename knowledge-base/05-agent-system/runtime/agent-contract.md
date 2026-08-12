---
type: policy
status: active
owner: programme-orchestrator
version: 1.0.0
schema_version: 1.1.0
updated: '2026-08-12'
tags: [type/policy, domain/knowledge-engineering, domain/freight, lifecycle/active, audience/internal]
---
# Agent Change Contract

Agents may read protected `master` and derived retrieval results. A proposed canonical
write follows: create `agent/<area>/<run-id>`, make a bounded change, run repository
validation, create a pull request, and wait for the required review before merge.

Every change links its task or agent-run record and preserves source provenance. Agents
never modify secrets, branch protection, CODEOWNERS, release gates, or frozen archive
content without an authorized human instruction. A blocked or contradictory result is a
recorded finding, not an invitation to guess.
