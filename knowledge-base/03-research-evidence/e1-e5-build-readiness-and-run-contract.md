---
type: strategy-note
status: active
owner: research-orchestrator-plus-experiment-owners
schema_version: 1.1.0
updated: '2026-08-20'
tags:
- type/strategy-note
- domain/freight
- domain/data-science
- domain/knowledge-engineering
- lifecycle/active
- confidence/mixed
- audience/internal
---
# E1-E5 Build Readiness and Run Contract

This note translates the source-grounded experiment protocols into implementation work. It
defines what engineers may build now, what constitutes a valid dry run, and which approvals
remain mandatory before a pilot, confirmatory run, participant study, or external claim.

## Readiness states

| State | Meaning | Evidence required |
|---|---|---|
| Protocol-ready | Scientific question, conditions, outcomes, claim limits and gates are specified | Reviewed experiment note and linked source/dataset/method cards |
| Build-ready | A bounded implementation packet names inputs, outputs, fixtures, interfaces, owner and acceptance tests | This contract plus the experiment build-start section |
| Dry-run-ready | Code runs on public or synthetic fixtures and emits a complete run packet | Passing fixture, schema, determinism, failure-path and provenance tests |
| Pilot-ready | Required human, rights, privacy, authority and numeric development gates are closed | Signed gate record and immutable pilot manifest |
| Confirmatory-ready | Protocol, data, baseline and custody locks are complete; held-out data remains unopened | Approved preregistration and one-shot access record |
| Finding-ready | A completed run survived independent review and its reproducibility package exists | Accepted run record, review, limitations and claim-level evidence |

`Build-ready` never means data-authorized, pilot-ready, effective, or safe to deploy.

## Shared implementation boundary

Create implementation code outside the public vault under a future `experiments/` package. The
recommended first layout is:

```text
experiments/
  common/       schemas, hashing, manifests, logging, seed and environment capture
  e1/           identity loaders, candidates, resolvers, reconciliation and metrics
  e2/           event profiles, generators, injectors, reconstruction and privacy metrics
  e3/           policy corpus, adapters, PEP/PDP harness, oracle and audit reconciliation
  e4/           blank instruments, assignment simulation and disclosure-control checks
  e5/           scenario model, simulator, HOS checks, solvers and feasibility verification
  fixtures/     public or synthetic test inputs only
  tests/        unit, contract, adversarial and deterministic replay tests
```

Raw or pseudonymized partner, participant, adjudication, credential and restricted records stay
outside Git. Run outputs default to an ignored local path or an access-controlled versioned
object store. Only schemas, synthetic fixtures, redacted examples and independently reviewed
aggregate findings may enter this repository.

## Common run manifest

Every executable entry point accepts an immutable configuration and emits one machine-readable
manifest containing at least:

- `run_id`, `attempt_id`, experiment, condition, phase and outcome;
- protocol, code commit, schema, dataset and configuration versions and content hashes;
- source/rights manifest, sensitivity class, approved processing boundary and retention rule;
- feature, evidence and knowledge cutoffs plus train/development/test split identifiers;
- dependency lock, container digest, runtime, hardware, region and random seeds;
- input count, exclusion/missing/error denominators and failure taxonomy codes;
- output, log, metric and review-artifact hashes;
- operator, reviewer, gate approvals, deviations, start/end times and cost record; and
- a claim ceiling chosen from the result ladder in [[integrated-e1-e5-research-programme]].

Retries create new attempts. They never overwrite an earlier packet. A failed or null attempt is
a result and remains auditable.

## Build-start packets

| Experiment | First build slice allowed now | Fixture acceptance | Gate that still blocks a real run |
|---|---|---|---|
| E1 | Parse the RC1 ontology and public source schemas; implement deterministic `C1` and probabilistic `C2`; add candidate/cluster reconciliation and metric interfaces; reserve adapters for `C3`/`C6` | The 70-case edge suite passes; permutations are stable; unsupported evidence IDs fail closed; every merge/split/abstention is traceable | Human semantic freeze; institutional/sponsor determination before reviewer recruitment or behavior observation; reviewer pilot; source rights; benchmark/split construction; numeric lock; `C6` also closes GAP-018 |
| E2 | Pin the EPCIS/CBV profile; wrap a pinned OpenEPCIS generator; create separate canonical, observability and source traces; implement anomaly operators and interval metrics | Schema-valid seeded traces replay byte-for-byte; hidden truth is inaccessible to the system under test; each anomaly family and missingness state has a hand-checked case | Freight threat-operator review and numeric/privacy gates; institutional/sponsor determination before reviewer recruitment or behavior observation; partner authorization only for the optional real-data lane |
| E3 | Define the neutral domain-decision schema; build one declared pinned NGAC/PML or XACML native lane behind the PEP harness; add JWT/JWKS fixtures, independent request ledger, audit reconciliation and policy mutation tests; keep a later second lane separate | Every allow/deny/redact/abstain/error path in the selected lane is authenticated and reconciled; its native obligations are enforced; severity-one false allows, bypasses and missing audit entries fail the suite | Authority-approved policy oracle, pinned engine/adapter and identity configuration, numeric coverage/privacy gates; adapter parity only if both native lanes enter scope |
| E4 | Build blank instrument schemas, synthetic recruitment/assignment and spillover simulations, burden-event logging, export/suppression checks and a participant-facing correction-flow prototype | No real participant rows; cluster/exposure calculations reproduce; unsafe exports and small cells are blocked; consent/comprehension fields are complete | Institutional determination, approved instruments/private store, partners, budget and recruitment authorization |
| E5 | Formalize scenario/constraint schemas; implement hand-checkable state transitions, HOS conformance, local/time-window baselines and a pinned solver adapter; validate benchmark conventions | Hand-worked cases and pinned Solomon/SINTEF instances pass independent feasibility checks; equal seeds/realizations are enforced; infeasible plans cannot score | Full Phase I scope decision or Phase II authorization; frozen objectives/gates and accepted upstream evidence for any non-synthetic claim |

## Shared first-sprint acceptance

1. Each experiment has a CLI entry point with `validate`, `dry-run` and `inspect` behavior.
2. Every dry run uses only committed synthetic/public fixtures and emits the common manifest.
3. Schemas reject unknown fields where silent expansion could change an estimand or policy.
4. Tests cover success, abstention/unresolved, malformed input, missing source, timeout, partial
   output, retry, correction and deliberate protocol-version mismatch.
5. Identical code, inputs, seed and configuration reproduce output hashes or record the precise
   nondeterministic boundary.
6. Logs and metrics contain no credentials, raw restricted values or participant identifiers.
7. The run packet identifies the controlling experiment note and unresolved gate records.
8. CI executes fixture tests without cloud credentials; provider/AWS smoke tests are separate and
   opt-in.

## Tool selection guardrails

Prefer established engines for domain logic and wrap them behind versioned adapters. Candidate
tools are Splink for a Fellegi-Sunter E1 baseline, pinned OpenEPCIS generator/validation tooling
for E2, separate NIST Policy Machine and OASIS XACML implementations for E3, an institutionally
approved survey platform for E4, and OR-Tools plus independently checked Solomon/SINTEF fixtures
for E5. A tool is not accepted because it is popular: record version, licence, maintenance state,
input/output semantics, deterministic controls, security posture and replacement path.

Use [[05-agent-system/experiment-mcp-and-tooling-setup]] for agent/tool access. MCP is an
operator interface, not the experimental treatment, gold oracle, evidence source, or audit system
of record.

## Start order

E1, E2 and E3 non-participant fixture implementations may start in parallel. E1/E2 reviewer
recruitment or behavior observation and all E4 participant activity wait for the responsible
institution or sponsor's documented determination. E4 may build only non-participant
infrastructure before that gate. E5 may build simulator and solver qualification
mechanics using labeled synthetic priors. Close `DG-P0` before any data-backed pilot, and open a
confirmatory holdout only after `G0-G3` under [[experiment-protocol-standard]].

## Related

[[integrated-e1-e5-research-programme]] - [[aws-experiment-execution-and-findings-plan]] -
[[09-meta/gaps/gap-018-e1-llm-readiness]] - [[09-meta/gaps/gap-019-e1-e5-programme-readiness]]
