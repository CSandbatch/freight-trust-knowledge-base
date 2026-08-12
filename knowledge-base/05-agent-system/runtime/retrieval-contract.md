---
type: policy
status: active
owner: programme-orchestrator
version: 1.0.0
schema_version: 1.1.0
updated: '2026-08-12'
tags: [type/policy, domain/knowledge-engineering, domain/freight, lifecycle/active, audience/internal]
---
# Retrieval Contract

Resolve a request in this order: exact identifiers and paths; linked records and MOC
context; then semantic retrieval over a rebuildable index. Rerank by source class,
verification, freshness, and direct relationship to the question. Answers cite canonical
Markdown objects and identify uncertainty. Embeddings, graph stores, caches, and search
indexes are derived artifacts; deleting them must not lose knowledge.
