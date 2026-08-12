---
type: strategy-note
status: active
schema_version: 1.0.0
tags:
- type/strategy-note
- domain/knowledge-engineering
- domain/freight
- lifecycle/active
name: freight-trust-research
description: Run evidence-grounded research, synthesis, and pilot design for freight trust, carrier identity, detention, facility-event provenance, data sharing, and freight interoperability. Use when expanding or reviewing this project's research claims, evidence library, goals, technical architecture, stakeholder analysis, or human-readable briefs.
---
# Freight Trust Research

Use this project-local skill to run a Terra-orchestrated research cycle with bounded Luna
subtasks. Maintain claim-level provenance; distinguish evidence from inference; and treat
fraud, detention, and empty-mile reduction as pilot outcomes unless directly measured.

## Workflow

1. Read `03-research-evidence/goals.md`, `03-research-evidence/evidence.md`, `03-research-evidence/review-notes.md`, and the
   relevant section of `02-programme-strategy/research-programme.md`.
2. Have Terra create task packets in `03-research-evidence/run-log.md`. Split Luna tasks only where
   source class, expertise, or failure mode differs.
3. Prioritize sources in this order: primary government/standards/court records;
   peer-reviewed research; authoritative datasets; reputable trade reporting; vendor
   claims. Label the source class and conflict of interest.
4. Add or amend evidence at claim level. Record source, date, URL, exact supported
   proposition, limits, confidence, and freshness date. Do not let a citation support a
   broader claim than it states.
5. Run the review gate: coverage, entailment, sufficiency, contradiction, freshness,
   adoption/equity impact, and consequential-use risk.
6. Synthesize only accepted evidence. Route new factual claims back to Luna; cap a section
   at two revision loops before escalating a decision to the human owner.

## Required research posture

- Design a federated, minimum-disclosure architecture unless raw-data pooling has a stated
  justification.
- Treat automated indicators as review-prioritization aids. Require abstention, human
  review, correction, and appeal for consequential use.
- Segment adoption and burden measures by stakeholder role and fleet size.
- State the counterfactual, metric, threshold, and falsifier for every pilot hypothesis.

## Resources

Use [[05-agent-system/skills/freight-trust-research/references/artifact-contracts|references/artifact-contracts.md]] for task packets,
evidence entries, and review findings. Use [[05-agent-system/skills/freight-trust-research/references/source-policy|references/source-policy.md]]
for source-quality and freshness rules.
