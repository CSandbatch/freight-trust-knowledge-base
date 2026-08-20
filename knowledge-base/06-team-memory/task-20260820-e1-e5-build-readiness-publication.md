---
type: task
status: current
id: task-20260820-e1-e5-build-readiness-publication
owner: research-orchestrator
objective: Bring E1-E5 documentation to source-current build-start readiness, define the recommended MCP and runtime tool boundary, and publish the verified repository state to the live Knowledge Atlas.
acceptance_criteria: Every experiment has a bounded first implementation slice and executable artifact contract; unresolved scientific, rights, human-subjects, security, and holdout gates remain explicit; MCP recommendations preserve the runtime and custody boundaries; vault, tests, deterministic build, push, Pages workflow, and live checks pass.
schema_version: 1.1.0
updated: '2026-08-20'
tags:
- type/task
- domain/knowledge-engineering
- domain/freight
- domain/reproducibility
- lifecycle/current
- audience/internal
---
# Task - E1-E5 Build Readiness Publication

## Work graph

| Node | Owner | Inputs | Produces | Depends on | Acceptance | Status |
|---|---|---|---|---|---|---|
| Source and protocol audit | source research lanes | E1-E5 protocols, datasets, methods, source cards | bounded corrections and retrieval limits | none | claims map to current primary or peer-reviewed evidence | complete |
| Build contract integration | research orchestrator | audit findings and programme dependency graph | shared run contract plus E1-E5 build slices | source and protocol audit | each slice names artifacts, fixtures, gates, and prohibited claims | complete |
| Tooling boundary | research orchestrator | repository runtime policy and official MCP documentation | MCP and runtime-tool recommendation | build contract integration | no MCP path bypasses custody, authorization, or immutable run capture | complete |
| Independent review | red-team reviewer | integrated documentation diff | severity-ranked findings and repairs | build contract integration | no open critical or major documentation defect | complete |
| Publication | research orchestrator | reviewed Git index | commit, push, Pages run, live verification | independent review | all repository gates and the live URL pass | complete |

## Scope boundary

This task authorizes documentation, schemas/contracts, public or synthetic fixture planning,
repository validation, and publication. It does not authorize partner contact, restricted-data
retrieval, human-subject recruitment, held-out opening, production AWS mutation, or a scientific
experiment run.

## Related

[[03-research-evidence/e1-e5-build-readiness-and-run-contract]] -
[[05-agent-system/experiment-mcp-and-tooling-setup]] -
[[09-meta/gaps/gap-019-e1-e5-programme-readiness]] -
[[run-20260820-001-e1-e5-build-readiness-publication]]
