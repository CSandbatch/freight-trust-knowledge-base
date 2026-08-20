---
type: experiment
id: E5
status: stretch
phase: phase-ii-or-late-phase-i
owner: operations-research-lead-plus-domain-panel
schema_version: 1.0.0
updated: 2026-08-20
primary_outcome: service-and-empty-mile-improvement-without-risk-shifting
tags:
- type/experiment
- lifecycle/stretch
- domain/freight
- domain/orchestration
---
# E5 — Orchestration Value

Protocol standard: [[experiment-protocol-standard]].

## Thesis

When dwell, service windows, HOS constraints, and cross-actor evidence are modeled
together, governed cross-actor planning can improve a bounded backhaul or dwell-sensitive
workflow over local optimization. The benefit is only credible if safety, service, margin,
and distributional effects are reported together; a reduction in empty miles that shifts
delay or risk to another actor is not a success.

This experiment is deliberately later than E1-E4. It should not be used to validate the
trust layer until identity, provenance, policy, and participation are sufficiently credible.

## How E5 tests the Freight Trust thesis

E5 is the application-level test of the programme's two-part thesis: the evidence graph is
the substrate, and cross-actor orchestration is the first high-value use case. It must show
that trusted, governed cross-party evidence changes a decision that local actors cannot
optimize well in isolation.

| Thesis layer | What E5 contributes |
|---|---|
| Local optimization creates network waste | Compares local planning with shared planning under identical demand and constraints. |
| Empty miles are upstream of dwell and timing | Varies dwell, service windows, and HOS slack to test whether a nominal match is feasible. |
| Governance matters as much as algorithms | Limits the governed planner to permitted, provenance-tagged, freshness-aware evidence. |
| Uncertainty should change decisions | Tests abstention, safe fallback, and recourse when events are stale or contradictory. |
| Efficiency cannot be purchased with hidden harm | Reports safety, service, margin, delay, and actor-level distributional outcomes together. |

E5 must not retroactively define the value of the entire project. If it fails, identity,
provenance, governance, or participation may still be valuable. If it succeeds only under
P2's perfect-information oracle, it supports the importance of information but not product
feasibility. The strongest result is a P3/P4 improvement that survives uncertainty, partial
participation, and competing interests.

### How the methods connect to the thesis

- **Synthetic orchestration simulation** isolates the value of coordination before a live
  network is available.
- **Travel-time and dwell calibration** prevents unrealistic timing from making the planner
  appear better than it is.
- **Constraint modeling** ties the experiment to HOS, time windows, capacity, equipment,
  queues, and legal sequencing.
- **Ablations** identify whether gains come from evidence federation, provenance,
  uncertainty handling, or a better optimizer.
- **Pareto and distributional analysis** tests whether one actor's benefit is another
  actor's hidden cost or risk.

### How the factors map to decisions

P0 represents fragmented/local decisions, P1 a simple feasible comparator, and P2 an upper-bound
oracle. P3 tests governed point-estimate planning and P4 tests uncertainty-aware governance.
Stress and reporting behavior are crossed modifiers, not alternative planning policies.

## Provenance

### Where E5 came from

E5 has a different provenance from E1–E4. Those four are answers to open findings; E5 is a
**deliberately deferred** application claim. Its most important design decision — that it
happens later — comes from a recommendation to *stop* leading with it.

| Origin | What it contributed to E5 | Status |
|---|---|---|
| [[improvement-suggestions]] item 1 — "Narrow the first buyer and workflow… keep network-wide orchestration as the later application" | The `status: stretch`, `phase: phase-ii-or-late-phase-i` framing. Orchestration was the programme's most attractive story and the least evidenced; the fix was to demote it in sequence without discarding it | Adopted |
| [[review-notes]] R-WN-01 — "Outcome overreach" (severity: high) | The finding that available sources establish a material operational problem and technical plausibility, **not** that a freight trust graph causes industry-wide reduction in fraud, detention, or empty miles. Empty-mile reduction is the specific claim E5 is allowed to test at bounded scale and forbidden to assert at industry scale | Resolved in programme section 7A; still enforced in publishing |
| [[goals]] G10 — "Replace broad outcome assertions with falsifiable pilot hypotheses" | The requirement for a baseline, intervention, comparison, success threshold, and failure condition — which for orchestration means P0/P1 as baselines and a predeclared primary objective | Open |
| [[04-sbir/drafts/phase-1-project-description-draft]] Sections 6, 10 | The explicit statement that this is not a claim that empty miles are reduced at industry scale, and that expansion beyond the single bounded workflow is a Phase II candidate contingent on Phase I results | Draft |
| [[dataset-scan-event-provenance-and-federation]] | The dwell and travel-time inputs, and the confirmation that no real multi-actor freight planning dataset is accessible | Current |

### Provenance of each input

E5 consumes the outputs of the earlier experiments more than it consumes external data.
That is the point: it is the test of whether the trust layer produces decision value, so
its inputs must be the trust layer's own artifacts.

| Input | Origin | Access | Verification status | What it can support | What it cannot support |
|---|---|---|---|---|---|
| [[dataset-openepcis-generated-event-logs]] | The E2 generator (OpenEPCIS, Apache 2.0, GS1 EPCIS 2.0/CBV 2.0) | Open, local generation | **Primary** for the tooling | Schema-valid synthetic events and controlled missing, delayed, duplicated, contradictory, and tampered cases | Real facility behavior or empirical dwell distributions. Dwell remains an authored prior until permissioned facility data supports calibration |
| [[dataset-bts-truck-travel-time-data]] | BTS–ATRI Freight Mobility Initiative, county-to-county truck travel times from a panel of ~350,000 unique tractors, 2018–2024 | Free, data.bts.gov Socrata portal | **Primary/secondary mix** — BTS is a federal statistical agency; the underlying ATRI panel terms are not stated on the BTS page | Travel-time calibration so route timing is not invented | Appointment, dock, chassis, or labor constraints. These are the constraints that most affect whether a backhaul match is feasible, and none of them are in this data |
| [[dataset-permissioned-terminal-facility-event-feed]] | A pilot partner, if secured | Registration, contract, or partner permission | **Partner-dependent**, not a dependency | Optional external-validity inputs | Anything, absent an agreement |
| Synthetic demand, truck availability, HOS limits, service windows, equipment constraints, load attributes, actor objectives, data freshness | Authored by the project | Project-defined | **To-build** | A controlled factorial in which coordination value can be isolated | External validity. Synthetic demand and behavior may be unrealistic, and the design says so first rather than last |

### Provenance of each method

| Method | Intellectual origin | What E5 borrows | What must be built | Known limitation |
|---|---|---|---|---|
| [[method-synthetic-orchestration-simulation]] | [[source-solomon-sintef-vrptw-benchmark]], [[source-ismael-2024-empty-freight-trips]], [[source-fmcsa-hours-of-service]], [[source-stochastic-and-strategic-collaborative-vrp]], and [[source-multiobjective-and-equitable-vrp]] | Exact-convention benchmark validation before freight scenarios; regulatory HOS checks; explicit uncertainty, strategic-reporting, and actor-distribution models | The governance constraints, authored scenario priors, adversary bounds, actor deterioration gates, and whole scenario factorial | Modeling precedents do not validate Freight Trust assumptions, U.S. freight parameters, or operational benefits |
| [[method-travel-time-calibration]] | Shared with E2; BTS/ATRI-derived travel times | Realistic timing distributions | Facility-side service-time distributions | Aggregate travel time is not facility ground truth |

### Provenance of the individual design choices

| Design choice | Why it is there, and whose finding forced it |
|---|---|
| P2 is an explicit oracle *diagnostic*, never a deployable claim | The single most common way an orchestration result misleads: full-information performance presented as achievable. If gains appear only under P2, the honest reading is that information matters, not that this product works. Failure mode F06 (oracle information unavailable in deployment) |
| Ablations that remove cross-actor evidence, provenance, uncertainty, governance constraints, and dwell modeling one at a time | The question E5 has to answer is *what caused the gain*. Without ablations, a better solver would be indistinguishable from a working trust layer — which would make the result useless as evidence for the architecture. Failure mode F13 (solver artifact) |
| Actor objectives kept separate before any composite, with Pareto frontiers and shadow prices reported | A composite objective with weights chosen after seeing results can manufacture any conclusion. Failure mode F12 (objective-weight manipulation) |
| H5 and the distributional analysis: no stakeholder subgroup may bear a material unpriced shift in delay, margin, or risk | The substantive claim, not a fairness footnote. A reduction in empty miles that relocates delay or risk to a facility, a driver, or a small carrier is cost transfer described as efficiency. R-WN-05's segment discipline extended to the operational setting |
| Guardrails that forbid rewarding unserved demand, hidden lateness, unrecorded waiting, or any HOS/safety violation | The optimizer will find whatever the metric permits. These are the four ways an empty-mile improvement can be produced by not doing the work |
| Common random numbers across conditions; seeds preserved and scenarios replayable | Simulation noise across conditions is otherwise indistinguishable from effect. Also the reproducibility requirement in [[experiment-protocol-standard]] |
| Sensitivity analysis over objective weights, solver time limits, demand forecasts, dwell parameters, HOS slack, and data freshness | A result that disappears after a small plausible parameter change is a fragile hypothesis, and Phase II money should not be committed to one |
| Explicit prohibition on E5 retroactively defining the project's value | Stated in the thesis section because the temptation is real: orchestration is the most exciting result available, and letting it become the verdict on identity, provenance, governance, and participation would invert the dependency structure |

## What E5 adds

### To the proposal

- It is the Phase II trajectory made concrete. Section 10 needs a defensible answer to
  "what does this become," and a bounded, preregistered orchestration study with declared
  ablations is a better answer than a market projection.
- It is where the programme's second thesis half — the evidence graph is the substrate,
  cross-actor orchestration is the first high-value use case — is tested. R-WN-01 makes
  asserting it unavailable.
- Its ablation design is itself a proposal asset: it demonstrates that the team knows
  which parts of its own architecture might turn out not to matter.

### To the benchmark artifact

A formal scenario and constraint specification, a validated simulator with a benchmark
report, a scenario generator with preserved seeds, and condition/ablation/sensitivity/
Pareto results. The scenario matrix — demand density and volatility, dwell shape, time
window tightness, HOS slack, travel uncertainty, evidence freshness, participation level,
facility disruption, strategic behavior — is the reusable contribution, because it names
the axes on which any cross-actor freight planning claim should be stress-tested.

### To the evidence chain

E5 licenses claims that, in a bounded simulated workflow, governed cross-actor planning
does or does not improve a declared objective at equal safety and service; which
constraints drive the result; and who bears the cost. It licenses **nothing** about
industry-scale empty-mile reduction — the exact claim R-WN-01 removed from the programme's
vocabulary.

### To risk retirement

It addresses the largest commercial unknown — whether the trust layer produces decision value
beyond compliance and dispute avoidance. A Phase I specification and CPU feasibility smoke test
can inform the Phase II ask; only an executed late-Phase-I experiment can retire the operational
hypothesis before Phase II capital is committed. The strategic-reporting axis also tests a
governance risk the technical experiments cannot reach: what the planner does when a participant
withholds, delays, or misreports within modeled bounds.

### What E5 deliberately does not add

Not a production planning product, not a claim about real network behavior, and not a
verdict on E1–E4. If E5 fails, identity, provenance, governance, and participation may
still be valuable independently — stated in the experiment's own thesis section so the
failure mode cannot be reinterpreted later.

## Why we are using E5

### The counterfactual

Without E5, the programme's Phase II story rests on an untested inference: that better
shared evidence must produce better cross-actor decisions. That inference is plausible and
unproven, and it is the one a Phase II reviewer will interrogate hardest. E5's absence
would also leave the distributional question unasked — whether coordination benefits are
real or relocated. That question is most likely to determine whether the system is adopted
by the actors who would bear its costs.

### Alternatives considered and rejected

| Alternative | Why rejected |
|---|---|
| Lead with orchestration as the Phase I headline | Improvement item 1. It was the least evidenced claim in the strongest position, and it depends on identity, provenance, governance, and participation all being credible first |
| Claim value from the P2 oracle policy | Explicitly forbidden in the decision rules. Oracle information is unavailable to real participants; a P2-only result supports the importance of information, not the feasibility of the product |
| Run a live multi-actor pilot instead of a simulation | No such network exists to run it on, and no partner is secured. Simulation isolates coordination value before a live network is available — that is its entire justification |
| Use a single composite objective for simplicity | It would let weight selection determine the finding. Actor objectives stay separate, and trade-offs are reported as frontiers |
| Skip the strategic-reporting axis | A federated system that assumes universal cooperation because it is called federated has assumed away its hardest operating condition. The reporting axis exists so the simulator cannot make that assumption silently |
| Compare only on empty miles | Empty-mile reduction can be bought with service degradation, safety exceptions, or unserved demand. The comparison is made at equal feasibility and safety, or it is not made |

### Cost, dependency, and sequencing

E5 is the most expensive to build and the most dependent. Simulator mechanics can begin with
authored synthetic priors. E2's synthetic output can test sensitivity mechanics but cannot
empirically calibrate dwell or facility behavior; that claim requires permissioned observations
with documented truth fitness and rights. A governance-specific claim needs E3's constraints on what evidence the
planner may use, and an adoption-realistic claim needs E4's measured participation distributions.
Before those outputs exist, E5 must use labeled sensitivity ranges rather than imply observation. That
dependency chain is why it carries `status: stretch` and `phase: phase-ii-or-late-phase-i`,
and why [[datasets-and-experiments-moc]] still lists "whether E5 belongs in Phase I or is
reserved for Phase II" as an open decision. The defensible default is that E5 is scoped and
specified during Phase I and executed when the application-value decision gate `DG-E5` is
reached — the specification itself
is a deliverable, and it is what makes the Phase II ask concrete.

## Research questions

1. Does governed cross-actor planning reduce empty miles or missed appointments in a bounded scenario?
2. Which constraints drive the result: dwell, service windows, HOS, demand density, or data freshness?
3. Does imperfect evidence cause the planner to overcommit or should it abstain?
4. Who receives the benefit and who bears delay, cost, or risk?
5. Is the result robust to travel-time uncertainty, demand shocks, and strategic behavior?

## Hypotheses and nulls

| ID | Hypothesis | Null / failure interpretation |
|---|---|---|
| H1 | Governed planning improves one preregistered primary outcome (empty miles or total cost, not selected after results) against P0/P1 while satisfying hard safety and service non-inferiority gates. | The tested cross-actor information/policy provides no improvement under those gates. |
| H2 | Modeling dwell explicitly improves backhaul feasibility more than matching on route proximity alone. | Explicit dwell modeling provides no improvement in the tested synthetic scenarios. |
| H3 | Provenance/confidence-aware planning outperforms planning that treats all data as certain. | Uncertainty handling adds no value or is too conservative. |
| H4 | Benefits persist across demand and travel-time scenarios. | Result depends on one favorable synthetic case. |
| H5 | No stakeholder subgroup bears a material unpriced shift in delay, margin, or risk. | Optimization is merely cost transfer. |

## Experimental factors

| Policy | Description |
|---|---|
| P0 | Local baseline: each actor optimizes its own route or dispatch objective with no shared coordination. |
| P1 | Simple time-window- and HOS-feasible planner without the trust-layer capabilities. |
| P2 | Centralized oracle: full information and no governance friction; upper-bound diagnostic, not deployable claim. |
| P3 | Governed point-estimate planner: uses only permitted, provenance-tagged evidence and fixed predeclared acceptance rules. |
| P4 | Governed uncertainty-aware planner: uses predeclared predictive distributions or intervals, robust or chance-constrained decisions, abstention, clarification/recourse, and safe fallback. |

Cross every deployable policy with the same two modifier axes rather than treating modifiers as
competing policies:

- **Stress axis:** demand, appointment, port/dock, weather, stale-event, travel, dwell, and
  explicitly non-legal synthetic-tightening scenarios.
- **Reporting axis:** truthful, missing/withheld, delayed, and bounded biased/misreported data.

## Unit of analysis and estimand

- Primary unit: simulated planning episode under a fixed seed and scenario.
- Secondary units: load assignment, truck route, facility visit, actor, and constraint violation.
- Primary estimand: difference between P3/P4 and P0/P1 in empty miles and service outcomes at
  equal safety and feasibility.
- Secondary estimands: cost, margin, dwell, missed appointments, on-time delivery, rejected
  HOS-infeasible alternatives, risk exceptions, fairness/distributional effects, and data-value
  sensitivity. Accepted-route HOS violations are a stop condition, not a tradeable outcome.

## Inputs and datasets

- [[dataset-openepcis-generated-event-logs]] — schema-valid synthetic events and anomaly cases;
  it does not provide empirical dwell distributions.
- [[dataset-bts-truck-travel-time-data]] — travel-time calibration.
- [[dataset-permissioned-terminal-facility-event-feed]] — optional external-validity inputs.
- Synthetic demand, truck availability, HOS limits, service windows, equipment constraints,
  load attributes, actor objectives, and data freshness/confidence.

## Methods

- [[method-synthetic-orchestration-simulation]]
- [[method-travel-time-calibration]]

The problem is a constrained vehicle-routing/assignment simulation with time windows,
uncertain travel and service times, and multi-actor objectives. Use exact-convention benchmark
validation before freight-specific scenarios; see [[source-solomon-sintef-vrptw-benchmark]] and
the bounded simulation precedent in [[source-ismael-2024-empty-freight-trips]].

## Protocol

1. Define one bounded workflow, actor objectives, hard constraints, and permitted evidence.
2. Validate the simulator against simple hand-checkable cases and known routing benchmarks.
3. Calibrate travel time from eligible public observations. Treat dwell as an authored,
   provenance-labeled prior until permissioned facility observations support calibration; never
   use the outcome as a calibration input.
4. Generate a scenario factorial: demand density, dwell variance, service-window tightness,
   HOS slack, data freshness, and disruption rate.
5. Run P0-P4 on identical seeds, scenario inputs, and realized uncertainty.
6. Cross the policies with every predeclared stress and reporting-behavior cell.
7. Record every assignment, rejected load, constraint violation, delay, and actor outcome.
8. Perform sensitivity analysis on objective weights; do not hide trade-offs in one composite score.
9. Report whether a result is caused by better information, better optimization, or an
   unrealistic oracle assumption.

## Variables

**Scenario factors:** demand density, spatial dispersion, dwell mean/variance, time-window
tightness, HOS slack, travel-time uncertainty, data freshness, disruption rate, and actor mix.

**Treatment:** planning policy P0-P4, crossed with separate stress and reporting axes.

**Primary outcomes:** the preregistered empty/deadhead-mile or total-cost contrast, feasible loads
assigned, missed appointments and on-time delivery, subject to zero accepted-route HOS/safety
violations and a frozen service non-inferiority rule.

**Secondary outcomes:** dwell, total miles, fuel proxy, operating cost, margin, load rejection,
constraint shadow prices, data freshness value, and actor-level distributional effects.

**Guardrails:** no route can violate hard HOS or safety constraints; no metric may reward
unserved demand or hidden delay; all actor outcomes must be reported.

## Analysis plan

- Use common random numbers across conditions to reduce simulation noise.
- Run multiple independent seeds and report confidence intervals or quantile intervals.
- Use factorial or fractional-factorial analysis to identify interaction effects.
- Compare P3/P4 with P0/P1 at equal feasibility and safety, not on miles alone.
- Treat P2 as an oracle ceiling; do not compare it as a deployable product.
- Report Pareto frontiers across empty miles, service, margin, safety, and equity; do not
  select weights after seeing results.
- Predeclare the actor/fleet strata, workload resource, actor-level deterioration statistic,
  non-inferiority or veto rule, and treatment of priced versus unpriced transfers. Pareto status
  alone is not an equity finding, and no numeric threshold may be selected after results.
- Predeclare every uncertainty distribution or interval, source, scenario range, and adversary
  capability. Separate missing, withheld, delayed, biased, and false reports; do not infer their
  real-world prevalence from simulated frequency.
- Conduct ablations: remove event provenance, remove uncertainty, remove cross-actor data,
  and remove governance constraints to identify the source of any gain.

## Initial decision rules

- No Phase II orchestration claim unless P3/P4 beats P0/P1 on the predeclared primary objective
  without worsening safety or service beyond guardrails.
- No scale recommendation if benefits occur only under P2 oracle information.
- No success claim if one actor’s gains are explained by another actor’s unpriced losses.
- Synthetic E5 results never authorize deployment. Passing demand, dwell, travel-time and stale-
  data stress tests gates only a later permissioned external evaluation.
- No fairness claim unless every predeclared actor/fleet deterioration gate is evaluated; synthetic
  labels support sensitivity analysis, not a real-world equity conclusion.
- No calibrated-realism claim until the relevant authored priors are replaced or bounded by
  permissioned observations with documented rights and fitness.

## Threats to validity

- Synthetic demand and behavior may be unrealistic.
- Objective weights can manufacture a preferred result.
- The oracle condition can make federation look weaker than it is or stronger than deployability permits.
- Solver quality can be confused with architecture value.
- Strategic behavior and data withholding are hard to model credibly.
- Empty-mile reduction may trade off against service, safety, or carrier economics.

## Extended operational specification

### Scenario and state model

Each simulation state must identify current time, truck location, load status, HOS clocks,
equipment, facility queue, appointment window, road condition, data freshness, actor
ownership, and available alternatives. A location and a time window do not make a load
“available”: equipment, legal hours, service duration, queue uncertainty, and feasible next
destination must also be satisfied.

### Objective model

Keep actor objectives separate before creating any composite objective. At minimum model:

- carrier operating cost, revenue, margin, and empty miles;
- driver hours, HOS slack, and safety exceptions;
- broker/shipper service level and assignment reliability;
- facility queue, dwell, appointment adherence, and labor constraints;
- risk exceptions, data uncertainty, and correction burden; and
- distributional outcomes by actor and fleet-size band.

The weights and actor-deterioration gates must be declared before results. Report Pareto
frontiers and shadow prices so a decision-maker can see what each improvement costs elsewhere.
The frontier is descriptive; it does not choose a normative fairness threshold.

### Scenario matrix

Run at least these factors independently and in interaction:

| Factor | Suggested levels |
|---|---|
| Demand density | sparse, normal, dense |
| Demand volatility | stable, seasonal, shock |
| Dwell | low variance, heavy tail, facility-specific |
| Time windows | loose, normal, tight |
| HOS slack | regulation-conformant ample, typical, constrained; any synthetic tightening is explicitly non-legal |
| Travel uncertainty | low, calibrated, disruption-heavy |
| Evidence freshness | current, delayed, stale |
| Participation | full, partial, asymmetric |
| Facility disruption | none, appointment miss, port/dock delay |
| Strategic behavior | truthful, withholding, delayed, misreported |

Use common random numbers across conditions. Preserve scenario seeds and make each scenario
replayable. Validate the state transitions with hand-worked cases before optimization.

### Baselines and ablations

Required baselines are local greedy dispatch, proximity-only backhaul matching, and a simple
time-window- and HOS-feasible planner. P2 is an oracle diagnostic, not a deployable baseline. Ablate
one capability at a time: remove cross-actor evidence, remove provenance, remove uncertainty,
remove governance constraints, and remove dwell modeling. This identifies whether gains come
from the trust layer or from giving the solver more information.

### Feasibility and safety checks

Every proposed route must pass hard constraints for service windows, capacity, equipment, legal
travel, appointment order, and the applicable property-carrying HOS clocks and exceptions in
[[source-fmcsa-hours-of-service]]. The conformance layer must represent driving, on-duty,
off-duty/break, duty-window, cycle, and explicitly invoked exception state. Synthetic tightening
is a stress assumption, not a statement of law. Log infeasible alternatives and the first binding
constraint. Never award an objective improvement for unserved loads, hidden lateness,
unrecorded waiting, or safety violations.

### Solver qualification

Before freight scenarios, pin benchmark-instance files and checksums, solver and dependency
versions, hardware, objective convention, distance precision, time limit, random seed, solver
status, and reported gap. Match the hierarchical fleet-count/distance convention when comparing
with SINTEF. Independently verify depot return, capacity, service, and time-window feasibility;
separate solver correctness from solution quality. A mismatch in convention is not evidence of
inferior or superior optimization.

### Statistical design

Use enough independent seeds to estimate the uncertainty of episode-level outcomes; the number
is determined by the desired interval width, not by the number of routes within one seed.
Report means, medians, tails, and probability of improvement. Use factorial effects for
scenario factors and interactions. If episodes share generated networks or demand, cluster
uncertainty at the scenario/network level.

### Sensitivity and robustness

Vary objective weights, solver time limits, demand forecasts, dwell parameters, HOS slack,
and data freshness. A result that disappears after a small plausible parameter change is a
fragile hypothesis. Compare point-estimate and uncertainty-aware planners under identical
realizations; do not let one policy receive better forecasts. Report coverage or calibration of
predictive intervals where observations exist and label authored ranges as sensitivity inputs.

### Strategic behavior

Model missing, withholding, delayed, biased, and false reporting separately as bounded behavior,
not as an assumed malicious optimum. Freeze the actor's information, action set, budget, and
objective before runs. Test whether the planner detects the condition, abstains, requests
clarification, falls back to a safe local policy, or reallocates work. Record which actor bears the
consequence. The simulator should not silently assume universal cooperation because the system
is called federated; simulated behavior does not estimate its real-world prevalence.

### Exit and escalation

Stop if any condition violates hard HOS/safety constraints, produces unbounded service
degradation, or relies on oracle information unavailable to participants. Escalate if the
result is highly weight-sensitive, if the solver fails to find comparable feasible solutions,
or if improvements are explained by shifting cost or risk to a less powerful actor.

## Build-start specification

Start with a declared operating population and HOS scope, formal scenario/state/constraint
schemas, deterministic generator, hand-worked route cases, explicit P0/P1 algorithms and tie-
breaks, a pinned solver adapter, independent feasibility checker and mock P3/P4 policy/evidence
fixtures. Pin Solomon/SINTEF instances and checksums; they qualify VRPTW conventions and solution
feasibility only, not HOS, governance, uncertainty, actor economics or Freight Trust value. Use
the common packet in [[e1-e5-build-readiness-and-run-contract]].

The base HOS state machine must test 11/14-hour clocks, cumulative eight-hour break and 60/70-hour
cycles for the declared property-carrying population. Add sleeper-berth, restart, adverse-driving
or short-haul vectors only when those exceptions are explicitly in scope. Build acceptance also
requires one frozen primary contrast/outcome, service bounds, actor-deterioration rules, identical
information/seeds/realizations, deterministic smoke replay and zero accepted-route hard-constraint
violations. Findings remain synthetic build-feasibility evidence.

## Required outputs

1. Formal scenario and constraint specification.
2. Simulator validation and benchmark report.
3. Scenario generator and random seeds.
4. Policy, stress, reporting, ablation, sensitivity, and Pareto-frontier results.
5. Actor-level distributional and safety report.
6. Decision memo on whether orchestration belongs in Phase II.
