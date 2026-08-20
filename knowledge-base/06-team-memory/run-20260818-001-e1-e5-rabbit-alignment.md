---
type: agent-run
status: current
id: run-20260818-001
actor: research-orchestrator-with-rabbit-source-lanes
started: 2026-08-18
outcome: completed
owner: research-orchestrator
schema_version: 1.1.0
updated: '2026-08-18'
tags:
- type/agent-run
- domain/knowledge-engineering
- domain/freight
- lifecycle/current
- audience/internal
---
# Agent Run - E1-E5 Rabbit alignment

## Objective

Re-research all five experiment protocols, anchor the programme on E1, reconcile their
interfaces and claim boundaries, and update the public vault without representing proposed
methods as completed experiments.

## Inputs and retrieval scope

The run reviewed E1-E5, their dataset and method cards, programme and SBIR consumers, source
navigation, decision and gap records, and the AWS execution plan. Three bounded source lanes
covered E1, E2-E3, and E4-E5. Retrieval prioritized controlling law and regulation, official
standards and programme documentation, official statistics, peer-reviewed methods research,
and primary software documentation. Each new source card records what the source supports and
what it does not establish.

## Actions and artifacts

- Reframed [[03-research-evidence/experiment-e1-entity-resolution-and-identity-assurance]]
  around the legal-person benchmark, hierarchical safety/yield test, explicit action harms,
  weighted estimands, and a frozen black-box LLM challenger.
- Corrected the E2 anomaly/provenance and E3 authenticated policy-enforcement boundaries,
  including GS1 semantics, missing-event observability, separate NGAC/XACML lanes, and
  independently reconciled audit evidence.
- Bounded E4 as consent-sensitive feasibility research by default and E5 as a synthetic
  orchestration test whose operational claims depend on upstream evidence.
- Added primary and peer-reviewed source cards and updated the programme, proposal, data
  management, source, experiment, and navigation notes that consume those claims.
- Added [[03-research-evidence/integrated-e1-e5-research-programme]],
  [[03-research-evidence/e1-experiment-brief-and-readiness-map]], and
  [[09-meta/gaps/gap-019-e1-e5-programme-readiness]].

## Outcome, blockers, and next route

The protocols are now source-refreshed and use one versioned dependency/interface model. They
remain **unrun**. Numeric gates, E1 benchmark construction and semantic freeze, E2 adjudication,
E3 policy authority and authenticated implementation, E4 institutional determination and
partner access, and E5 solver/runtime choices remain human or implementation gates. No source
retrieval in this run authorizes restricted-data egress, partner commitments, legal conclusions,
or opening any held-out test set.

Acceptance evidence recorded after integration and independent hostile review:

- `validate_kb.py`: passed, 214 Markdown notes and 16 atomic IDs.
- six public-site unit tests: passed.
- full site build: 230 source artifacts, 1,974 resolved wikilinks and 214 Markdown readers.
- deterministic site validation: passed exhaustive inventory, raw-hash, link, graph-parity and
  rendered-page-safety checks.
- `git diff --check`: passed; line-ending normalization warnings only.
- hostile review: Critical/Major partner-authorization, semantic-collapse, synthetic-evidence,
  consent, audit and deployment-language findings corrected before final validation.

Related task: [[task-20260818-e1-e5-rabbit-program-alignment]].
