---
type: method
status: stretch
schema_version: 1.0.0
updated: 2026-08-18
tags:
- type/method
- lifecycle/stretch
- domain/freight
- domain/orchestration
---
# Synthetic Orchestration Simulation

Specifies a simulator intended to model loads, trucks, a declared and conformance-tested HOS state, authored or permissioned-calibrated
dwell, service windows, and separate actor objectives. Planning policies are crossed with common
stress and reporting-behavior axes rather than mixing policies and scenarios into one treatment.

- Use: evaluate the later E5 backhaul or dwell-sensitive workflow.
- Strength: permits controlled comparison before partner-scale deployment.
- Limitation: simulated incentives and constraints must be validated against real operations.
- Policy axis: local, simple feasible, oracle diagnostic, governed point-estimate, and governed
  uncertainty-aware. The latter uses declared distributions/intervals, abstention, recourse, and
  safe fallback; the oracle never supports a deployable claim.
- Validation: pin benchmark inputs/checksums, objective and precision convention, solver/runtime,
  hardware, seeds, time limits, status, and gaps; independently check every route's feasibility.
- HOS: implement applicable driving, duty-window, break, cycle, and exception state from
  [[source-fmcsa-hours-of-service]]. Synthetic tightening is labeled non-legal stress.
- Equity: predeclare actor/fleet strata, workload resource, deterioration statistic, and veto or
  non-inferiority rule. Pareto membership alone is not a fairness conclusion.
- Uncertainty/reporting: declare sources and ranges; separate missing, withheld, delayed, biased,
  and false reports; bound actor knowledge, action set, budget, and objective.
- Linked datasets: [[dataset-openepcis-generated-event-logs]], [[dataset-bts-truck-travel-time-data]], [[dataset-permissioned-terminal-facility-event-feed]].
- Linked experiment: [[experiment-e5-orchestration-value]].
- Sources: [[source-solomon-sintef-vrptw-benchmark]],
  [[source-ismael-2024-empty-freight-trips]], [[source-fmcsa-hours-of-service]],
  [[source-stochastic-and-strategic-collaborative-vrp]], and
  [[source-multiobjective-and-equitable-vrp]].
