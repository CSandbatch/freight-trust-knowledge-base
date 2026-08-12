---
type: method
area: experiments
status: active
schema_version: 1.0.0
tags:
- type/method
- lifecycle/active
- domain/freight
- domain/standards
---
# Experiment Protocol Standard

Every Freight Trust experiment must be specified before data or results are inspected.
The protocol must distinguish a technical feasibility result, a causal effect estimate,
an external-validity result, and a governance judgment.

## Required protocol fields

1. Thesis and decision the experiment informs.
2. Research questions, hypotheses, nulls, and estimands.
3. Unit of analysis and assignment unit.
4. Dataset version, access rights, schema, label policy, and split strategy.
5. Conditions, baselines, controls, and ablations.
6. Primary, secondary, safety, equity, and privacy outcomes.
7. Sampling, replication, random seeds, and minimum detectable effect or precision target.
8. Analysis model, uncertainty intervals, missing-data treatment, and subgroup plan.
9. Stopping rules, go/no-go rules, and escalation conditions.
10. Threats to validity, misuse conditions, and participant protections.
11. Reproducibility package and audit trail.

## Shared quality gates

- **G0 — protocol lock:** schema, labels, conditions, outcomes, and decision rules are frozen.
- **G1 — data lock:** access, provenance, license, retention, and split manifests are recorded.
- **G2 — baseline lock:** simple baselines run before any proposed method is tuned.
- **G3 — blind evaluation:** labels, injected anomalies, or treatment outcomes are hidden as appropriate.
- **G4 — review:** an independent reviewer inspects leakage, oracle assumptions, and failure cases.
- **G5 — publication:** results include limitations, unresolved cases, subgroup outcomes, and reproducibility artifacts.

## Shared result categories

- **Feasible:** the method can be built and evaluated under stated conditions.
- **Effective in benchmark:** it outperforms the declared baseline on the declared benchmark.
- **Operationally useful:** it changes a real workflow outcome under realistic constraints.
- **Generalizable:** it survives held-out entities, times, partners, or scenarios.
- **Safe to advance:** it passes privacy, equity, policy, and misuse guardrails.

No experiment may silently upgrade “feasible” to “effective,” or “effective in synthetic
data” to “operationally useful.” NIST’s AI RMF emphasizes validity, accuracy, robustness,
reliability, and context-specific risk measurement as distinct trustworthiness concerns:
[NIST AI RMF](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10).

## Reproducibility package

Each run should preserve:

- protocol version and commit/hash;
- data-manifest and schema versions;
- code and dependency lockfile;
- random seeds and hardware/runtime details;
- model/solver configuration;
- raw, derived, and redacted outputs;
- reviewer identity and decision record; and
- a run log describing deviations from protocol.

## Common failure taxonomy

`F01` label ambiguity; `F02` source leakage; `F03` train/test/entity contamination;
`F04` baseline mis-specification; `F05` missingness treated as negative evidence;
`F06` oracle information unavailable in deployment; `F07` subgroup degradation;
`F08` privacy leakage; `F09` policy incompleteness; `F10` unmeasured burden;
`F11` spillover/interference; `F12` objective-weight manipulation; `F13` solver artifact;
`F14` external-validity failure; `F15` unreported null or failed run.
