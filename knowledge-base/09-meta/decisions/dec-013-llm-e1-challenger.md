---
type: decision
status: active
id: DEC-013
decision_date: 2026-08-18
owner: research-orchestrator
rationale: Evaluate a constrained LLM resolver prospectively without weakening E1 gold semantics or the one-shot confirmatory gate.
schema_version: 1.1.0
updated: '2026-08-18'
tags:
- type/decision
- domain/freight
- domain/identity
- domain/data-science
- programme/e1
- lifecycle/active
- audience/internal
---
# DEC-013 — Add a constrained LLM challenger to E1

## Decision

Add a named, preregistered LLM-assisted entity-resolution challenger to [[experiment-e1-entity-resolution-and-identity-assurance]] before protocol and test freeze.

The LLM is a resolver/reranker over frozen candidates and permitted evidence. It is not a
source, adjudicator, gold-label generator, autonomous graph writer, legal decision-maker, or
regulatory reincarnation detector. [[e1-carrier-identity-and-relationship-standard]] remains
controlling.

Exactly one non-manual candidate reaches the confirmatory holdout as `C*`. The LLM becomes
eligible only through the frozen development promotion and tie-break rule. Adding or changing a
model, prompt, provider, evidence schema, calibration method, or search budget after test access
creates a new method version and cannot redefine the confirmatory winner.

## Rationale

Recent primary research makes generative LLM entity matching a credible candidate under limited
labels, heterogeneous records, and unseen entities. That evidence does not establish freight
legal-person performance, cluster coherence, calibrated abstention, or safety at E1's false-merge
ceiling. Testing the method against the adjudicated benchmark is therefore useful; assuming it
works is not.

The decision preserves deterministic and Fellegi–Sunter baselines, graph ablations, independent
gold adjudication, time-forward leakage controls, representative versus challenge cohorts,
cluster reconciliation, and the precision-first decision gate.

## Consequences

- Add and maintain [[method-llm-assisted-entity-resolution]].
- Freeze an exact model/checkpoint, provider, prompt, schema, serialization, parameters,
  candidate generator, calibration method, cost budget, and retry policy.
- Prohibit `openrouter/auto`, web access, arbitrary provider fallback, verbal confidence as a
  calibrated probability, and unsupported evidence citations in evaluation.
- Keep restricted packets outside the public vault and require data-egress approval before any
  hosted inference.
- Record null, unstable, unsafe, or uneconomic performance as valid Phase I evidence.

## Related

[[e1-benchmark-sampling-and-split-plan]] · [[e1-statistical-analysis-and-preregistration-plan]] ·
[[e1-reporting-and-reproducibility-checklist]] · [[aws-experiment-execution-and-findings-plan]] ·
[[09-meta/gaps/gap-018-e1-llm-readiness]]
