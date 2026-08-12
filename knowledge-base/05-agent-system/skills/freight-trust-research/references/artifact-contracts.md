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
# Artifact Contracts

## Task packet

```yaml
task_id: Gxx-topic-01
parent_id: cycle-YYYY-MM-DD
owner: luna-domain
objective: One answerable research question.
required_source_class: primary | peer_reviewed | dataset | mixed
deliverable: Exact file and expected fields.
acceptance_tests:
  - Each proposition has source support.
  - Limits and conflicts are explicit.
max_attempts: 2
```

## Evidence entry

```yaml
claim_id: Gxx-Cyy
proposition: Narrow, testable statement.
source: Title, organization, publication date, URL.
source_class: primary | peer_reviewed | dataset | secondary | vendor
support: Brief paraphrase of what the source establishes.
limits: Scope, method, uncertainty, and conflicts.
confidence: high | medium | low
freshness_date: YYYY-MM-DD
```

## Review finding

```yaml
finding_id: R-Gxx-Cyy-01
severity: high | medium | low
failure_type: entailment | sufficiency | contradiction | freshness | equity | scope
required_action: Concrete re-search, rewrite, or human decision.
route_to: luna-domain | synthesis | publishing | visualization | human-owner
max_retries: 2
status: open | resolved
```
