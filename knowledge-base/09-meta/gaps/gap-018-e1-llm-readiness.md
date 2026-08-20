---
type: gap
status: active
id: GAP-018
priority: high
owner: e1-technical-lead-plus-data-governance
acceptance_criteria: Frozen LLM method, approved evidence-egress class, implemented resolver and reconciliation pipeline, development promotion rule, reproducibility manifest, and adversarial tests pass before final-test access.
schema_version: 1.1.0
updated: '2026-08-18'
tags:
- type/gap
- domain/freight
- domain/identity
- domain/data-science
- programme/e1
- lifecycle/active
- action/verify
- audience/internal
---
# GAP-018 — E1 LLM challenger is specified but not experiment-ready

## Gap

[[dec-013-llm-e1-challenger]] authorizes a prospective LLM challenger, but no executable matcher,
frozen model/checkpoint, provider approval, prompt/schema, candidate interface, calibration layer,
cluster reconciliation, cost envelope, or adversarial test harness exists.

Unknown pretrained knowledge may also expose post-feature-cutoff carrier facts even when web
access is disabled. Hosted processing can create a separate data-egress risk for enriched public
records, state filings, human-actor fields, restricted sources, and adjudication annotations.

## Required closure evidence

1. Select no more than a small preregistered model family and record exact immutable identifiers.
2. Freeze L0-L7 ablations, prompt/serialization hashes, structured output schema, parameters,
   retry/failure policy, candidate cap, token/cost budget, and development tie-break.
3. Implement evidence-ID grounding, schema rejection, `UNRESOLVED`/`ABSTAIN`, and deterministic
   symmetry/transitivity/conflict reconciliation.
4. Pass masked-name, chronology-canary, post-cutoff, weak-field collision, record-order,
   repetition, prompt-variation, unsupported-citation, and prompt-injection tests.
5. Obtain data-owner/legal/security approval for every field sent to a hosted provider, or run
   the applicable checkpoint inside the approved AWS boundary.
6. Demonstrate local/AWS or hosted-run manifests that preserve model, provider, prompt, inputs,
   raw output, parsed decision, latency, tokens, charge, retry history, and hashes.
7. Complete the development promotion decision before the confirmatory test is opened.

## Dependencies

This gap depends on the human semantic freeze and benchmark pilot in historic `GAP-003` and the
pilot-derived numeric locks in historic `GAP-010`. It blocks LLM eligibility for `C*`, not the C1
or C2 baseline build.

## Related

[[experiment-e1-entity-resolution-and-identity-assurance]] ·
[[method-llm-assisted-entity-resolution]] · [[aws-experiment-execution-and-findings-plan]] ·
[[09-meta/decisions/dec-013-llm-e1-challenger]]
