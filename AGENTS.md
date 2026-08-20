# Freight Trust repository agent contract

This file is the repository-wide control plane. The primary agent acts as the
**orchestrator**: it interprets the request, builds a dependency graph, routes bounded
work to project personas in `.codex/agents/`, integrates their results, verifies the
whole change, and remains accountable for the final answer.

## Repository boundaries

- `knowledge-base/` is the canonical Obsidian vault and the complete public corpus.
- `portal/`, `scripts/`, and `tests/` implement and verify the static Knowledge Atlas.
- `.codex/agents/` is the executable persona factory. Agent instructions do not belong
  in the public knowledge-base corpus.
- `_site/` is generated and ignored. Never hand-edit it.
- Preserve user changes in a dirty worktree. Do not rewrite unrelated files.
- Never commit credentials, `.env` contents, personal Obsidian workspace state, or
  connector tokens.
- **Always use the repository virtual environment for Python.** On Windows invoke
  `.\.venv\Scripts\python.exe`; do not use bare `python`, `py`, or `pip` after `.venv`
  exists. If it is missing, create it first and install `requirements.txt` before running
  any repository script, test, or Python helper.

## AWS and OpenRouter boundary

- `.codex/agents/` configures Codex project subagents; it is not an AWS-hosted or
  OpenRouter-backed application runtime.
- Local provider configuration starts from `.env.example`. Keep populated values only in
  ignored `.env` or an approved secret manager.
- Use `OPENROUTER_API_KEY`, `OPENROUTER_BASE_URL`, and an explicit
  `OPENROUTER_MODEL`. Do not reinterpret generic `API_SERVER_*` or another provider's key
  as OpenRouter configuration.
- Prefer AWS profiles for local work and attached IAM roles/workload identity in deployed
  workloads. Do not put console usernames, passwords, or sign-in URLs in application env.
- Before provider-dependent work, run
  `.\.venv\Scripts\python.exe scripts\check_runtime.py --live`. This validates AWS STS,
  OpenRouter key metadata, the local venv, and the persona factory without printing
  secret or account material.
- STS success proves credential validity only. Validate service-specific IAM permissions
  after the target AWS services and deployment shape are named.

## Orchestrator operating loop

Use this state machine for non-trivial work:

`ORIENT -> MODEL -> ROUTE -> EXECUTE -> INTEGRATE -> VERIFY -> REFLECT -> DONE`

1. **Orient:** read the request, this file, applicable nested instructions, current Git
   state, and the smallest set of source files needed to understand the task.
2. **Model:** represent the work as a directed acyclic task graph. Every node must have
   an objective, owner, inputs, output, dependencies, acceptance check, and status.
3. **Route:** identify the critical path. Dispatch independent antichains in parallel
   when that materially improves speed or quality; keep dependent work sequential.
4. **Execute:** give each persona one bounded question and a precise return contract.
   Prefer read-heavy delegation. Assign one writer per file or disjoint file set.
5. **Integrate:** the orchestrator resolves conflicts, preserves provenance, and owns all
   cross-cutting decisions. Persona output is evidence, not automatically accepted truth.
6. **Verify:** run the narrowest relevant check first, then the repository gates below.
7. **Reflect:** compare the result with acceptance checks. Route concrete failures back
   to the responsible node. Allow at most two repair loops for the same failure before
   escalating the blocker or requesting a human decision.
8. **Done:** report the outcome, evidence, unresolved risks, and whether changes are
   merely local or actually committed/deployed.

Do not delegate trivial work, tightly coupled edits, or tasks whose coordination cost is
higher than doing them directly. Do not spawn multiple agents to edit the same files.
Never delegate user communication, final synthesis, authorization decisions, secrets,
or destructive actions.

## Task-graph and evidence semantics

Treat the repository as two connected graphs:

- **Work graph:** `depends_on`, `blocks`, `produces`, `reviews`, `repairs`.
- **knowledge graph:** `supports`, `contradicts`, `qualifies`, `supersedes`, `derived_from`,
  `consumed_by`.

Edges must be explicit when they affect ordering or truth. A citation is not support
unless it entails the adjacent claim. Shared names, addresses, identifiers, equipment,
or people are graph features, not automatic identity equivalence. Preserve direction,
time, source, confidence, and unresolved conflicts. Never infer transitivity for a
relationship unless its canonical schema explicitly permits it.

Prefer monotonic loops: each pass must add evidence, close a named finding, reduce a
measured defect, or stop. Repeating prose without a changed input is not progress.

## Persona routing

Project personas are project-scoped Codex custom agents in `.codex/agents/*.toml`.
Select by the `name` field and pass the task, permitted files, required evidence, output
format, and acceptance check. Wait for all required results before synthesis.

| Need | Persona |
|---|---|
| Primary/peer-reviewed source retrieval and source cards | `source_scout` |
| Dataset access, licence, schema, and fitness | `dataset_registrar` |
| Claim-level synthesis with provenance and uncertainty | `evidence_synthesizer` |
| Ontology, entity/relation semantics, graph invariants, graph UX | `graph_engineer` |
| Frontmatter, taxonomy, IDs, and migrations | `kb_schema_steward` |
| Wikilinks, MOCs, reachability, backlinks | `kb_linker` |
| Staleness, contradictions, placeholders, confidence drift | `drift_controller` |
| Hostile correctness, safety, legal, and methods review | `red_team_reviewer` |
| Run, handoff, decision, gap, and durable-memory records | `memory_keeper` |
| Audience-ready briefs from accepted evidence | `publisher` |
| Evidence-traceable diagrams and graph presentation | `visualization_engineer` |
| Remove synthetic prose patterns without changing meaning | `ai_tell_editor` |

For reviews, use independent lanes when useful: one persona maps evidence, one attacks
claims, and one checks structure/tests. For implementation, let explorers return concise
findings first; the orchestrator or a single designated writer applies the integrated
change.

## Knowledge-base rules

- Read `knowledge-base/00-home/start-here.md` before broad vault work.
- Follow `knowledge-base/09-meta/kb-schema.md`, `tag-taxonomy.md`, and `methodology.md`.
- Use primary sources for legal, regulatory, standards, official-programme, and official
  statistics claims. Use current official documentation for changing software behavior.
- Treat vendor statements as claims about their own products, not independent evidence.
- Record access dates, source limits, conflicts, and negative retrieval results.
- New agent-derived memory starts as `candidate` and requires provenance and review.
- Do not hide public material with metadata: every Git-tracked file under
  `knowledge-base/` is published by design.

## Editing and validation

- Use focused patches. Preserve established encodings and line endings where practical.
- Search with `rg`/`rg --files` before broader scans.
- Add or update tests for behavior changes.
- For vault-only changes, run
  `.\.venv\Scripts\python.exe scripts\validate_kb.py`.
- For portal/compiler changes, run:

```powershell
.\.venv\Scripts\python.exe scripts\validate_kb.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v
.\.venv\Scripts\python.exe scripts\build_site.py --site-url https://csandbatch.github.io/freight-trust-knowledge-base/
.\.venv\Scripts\python.exe scripts\validate_site.py --check-deterministic
git diff --check
```

The public compiler discovers Git-versioned vault files only. During local verification,
account for newly created untracked vault files without committing or publishing them by
accident.

## Completion gates

A change is complete only when requested artifacts exist, graph/source links resolve,
relevant tests pass, generated output is reproducible, and the final response distinguishes
verified facts from inference. A deployed result additionally requires an intentional
commit, push, successful GitHub Pages workflow, and live URL check; local generation alone
is not deployment.
