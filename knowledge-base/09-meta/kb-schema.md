---
type: schema
status: active
owner: kb-schema-steward
version: 1.1.0
schema_version: 1.1.0
updated: 2026-08-08
tags:
- type/schema
- domain/knowledge-engineering
- audience/internal
- lifecycle/active
---
# Knowledge Base Schema

The contract every note in this vault is validated against. Version 1.0.0 codifies what
the vault already does, then tightens it. Where existing notes diverge, the divergence is
recorded in [[drift-control]] as a migration item. Correcting it silently would let the
schema rewrite the vault's history.

Owner: `kb-schema-steward`. Changes to this file require a decision-log entry in
[[decision-log]] and a version bump.

## Versioning

`MAJOR.MINOR.PATCH`. MAJOR breaks existing frontmatter (requires migration). MINOR adds
an optional field or a new note type. PATCH clarifies wording without changing validity.
Every note may carry `schema_version`; absence means "pre-1.0, unmigrated". Team release 0.9 completed the active-vault migration on 2026-08-08. Schema 1.1.0 adds operational-memory objects and an atomic-record convention without changing the validity of 1.0.0 notes.

## Note types

`type` is required on every note and is a closed vocabulary. Adding a type is a MINOR
version bump.

| `type` | What it holds | Required fields beyond the universal set | Naming |
|---|---|---|---|
| `home` | Vault entry point | — | `start-here.md` |
| `moc` | Map of content for one folder or theme | `area` | `*-moc.md` |
| `schema` / `taxonomy` / `policy` | The control layer in `09-meta/` | `owner`, `version` | descriptive |
| `experiment` | A protocol under the experiment standard | `id` (E#), `phase`, `owner`, `primary_outcome` | `experiment-e#-*.md` |
| `method` | A technique used by one or more experiments | `status` from the method ladder | `method-*.md` |
| `dataset` | One data source, real or to-build | `access`, `licence`, `verification` | `dataset-*.md` |
| `evidence` | Claim-level register or a source scan | `confidence_default` | `evidence.md`, `dataset-scan-*.md` |
| `source` | One external document, cited and retrievable | `source_class`, `accessed`, `verification` | `source-*.md` |
| `term` | One glossary entry | `aliases`, `defined_by` | inside [[glossary]] or `term-*.md` |
| `brief` | Client- or reviewer-facing narrative | `audience` | descriptive |
| `draft` | A deliverable in progress (SBIR sections) | `deliverable`, `owner` | `*-draft.md` |
| `strategy-note` | Programme reasoning, not evidence | — | descriptive |
| `agent` | An agent role definition | `layer`, `tools` | `##-*-agent.md` |
| `log` | Append-only record | — | `*-log.md`, `run-log.md` |
| `archive` | Frozen superseded material | `superseded_by`, `frozen_on` | in `08-archive/` |
| `claim` | Atomic, sourced proposition | `id`, `proposition`, `confidence`, `sources` | `claim-ft-######.md` |
| `decision` | One durable institutional decision | `id`, `decision_date`, `owner`, `rationale` | `dec-###.md` |
| `gap` | One independently actionable unknown | `id`, `priority`, `owner`, `acceptance_criteria` | `gap-###.md` |
| `drift` | One contradiction, staleness, or integrity finding | `id`, `severity`, `finding`, `owner` | `drift-###.md` |
| `meeting` | Dated meeting record | `id`, `meeting_date`, `participants` | `meeting-YYYYMMDD-*.md` |
| `handoff` | Explicit transfer between actors | `id`, `from`, `to`, `next_action` | `handoff-YYYYMMDD-*.md` |
| `task` | Bounded work packet | `id`, `owner`, `objective`, `acceptance_criteria` | `task-*.md` |
| `agent-run` | One reproducible agent execution | `id`, `actor`, `started`, `outcome` | `run-YYYYMMDD-*.md` |
| `memory` | Candidate or accepted operational memory | `id`, `memory_type`, `memory_scope`, `provenance`, `review` | `mem-ft-######.md` |

## Universal frontmatter

Required on every note:

```yaml
type: <from the table above>
status: <from the status ladder below>
tags: [<layered tags per tag-taxonomy>]
```

Required on everything that makes a factual claim (`evidence`, `source`, `dataset`,
`brief`, `draft`, `term`):

```yaml
updated: YYYY-MM-DD        # last substantive edit, not last touch
```

Optional but strongly preferred:

```yaml
schema_version: 1.0.0
owner: <role or agent that maintains it>
supersedes / superseded_by: <wikilink>
review_by: YYYY-MM-DD      # forces a freshness recheck; see drift-control L2
```

## Atomic records and operational memory

Atomic records avoid multi-writer conflicts in shared registers. New decisions, gaps,
drift findings, claims, tasks, handoffs, meetings, agent runs, and memories are one file
per immutable ID. Human-facing MOCs may summarize them, but are indexes rather than the
authoritative record. Historic aggregate registers remain authoritative for their existing
IDs until they are deliberately migrated; never duplicate or renumber their contents.

Operational records live under `06-team-memory/`; institutional decisions, gaps, and
drift findings live under their respective `09-meta/` subdirectories. Agent-authored
memory starts `status: candidate`. Only an authorized reviewer may promote it to `active`.
The following fields are required for every `memory` note:

```yaml
id: mem-ft-######
memory_type: semantic | episodic | procedural
memory_scope: shared | private
provenance:
  actor: <human or agent role>
  run: <agent-run ID or null>
  method: <how the memory was created>
review:
  status: pending | accepted | rejected
  reviewer: <role or null>
write_policy: patch | append-only
```

IDs are immutable and unique within their namespace. `status` remains the maturity axis;
confidence remains a separate evidence axis. Derived indexes, graph stores, and semantic
embeddings are rebuildable from the protected Git branch and are never canonical memory.

## Status ladder

One vocabulary, read the same way everywhere. `status` describes the *note's* maturity,
never the confidence of its contents — confidence is a separate axis (below).

| `status` | Means |
|---|---|
| `active` | Current and maintained |
| `draft` | Being written; not citable downstream |
| `planned` | Specified but not executed (experiments) |
| `candidate` | Proposed for use, not yet selected (methods, datasets) |
| `required` | Non-optional component |
| `stretch` | Deferred beyond current phase |
| `to-build` | Does not exist yet; this note is its specification |
| `partner-dependent` | Blocked on an external agreement |
| `current` | A dated scan or snapshot, valid as of `updated` |
| `superseded` | Replaced; must carry `superseded_by` |
| `frozen` | Archived deliberately; never update toward current facts |

## The confidence axis

Confidence attaches to *claims*, not notes, and uses the ladder already in force across
[[evidence]] and the dataset scans. It is never merged into `status`.

| Marker | Means | Citable as |
|---|---|---|
| `primary` | Official document, statute, standards body, or the issuing agency's own data | Fact |
| `peer_reviewed` | Published research | Fact, with method stated |
| `dataset` | A retrievable data product | Fact about the data, not the world |
| `secondary` | Trade press, aggregator, third-party summary | Attributed claim only |
| `vendor` | A vendor describing its own product | The vendor's assertion, never market validation |
| `unverified` | Single weak source, or retrieval failed | Context only; never load-bearing |
| `synthetic` | Generated by this project | Feasibility only; never external validity |

Retrieval status is recorded separately from confidence, because "we could not fetch it"
and "the source is weak" are different failures:

```yaml
verification: confirmed | snippet-only | retrieval-failed | not-attempted
accessed: YYYY-MM-DD
```

`retrieval-failed` must record the failure mode (`HTTP 403`, `JS shell`, `paywalled`,
`agreement-gated`). The vault already carries several. They are honest records of what
could not be fetched, and must not be cleaned away as TODOs.

## Identifier namespaces

The vault has three overlapping `G` namespaces, which [[drift-control]] tracks as a known
defect (DRIFT-003). Until it is resolved, always qualify on first use in a note.

| Prefix | Space | Defined in |
|---|---|---|
| `G1`–`G14` | Research goals | [[goals]] |
| `G0`–`G5` (quality gates) | Protocol gates: protocol lock, data lock, baseline lock, blind eval, review, publication | [[experiment-protocol-standard]] |
| `G0`–`G5` (decision gates) | Programme gates: protocol freeze, identity, event, federation, participation, application value | [[datasets-and-experiments-moc]] |
| `E1`–`E5` | Experiments | the `experiment-*` notes |
| `C0`–`C5` | Conditions within one experiment | each experiment note |
| `H1`–`H5` | Hypotheses within one experiment | each experiment note |
| `F01`–`F15` | Failure taxonomy | [[experiment-protocol-standard]] |
| `R-WN-##` | Wide-net review findings | [[review-notes]] |
| `R-G##-C##-##` | Per-claim review findings | [[artifact-contracts]] |
| `DRIFT-###` | Drift issues | [[drift-control]] |
| `GAP-###` | Build-out backlog | [[gap-register]] |
| `DEC-###` | Decisions | [[decision-log]] |

Identifiers are immutable once published. Retire, never renumber.

## Naming and location

- Files: lowercase kebab-case, no spaces, no ampersands. Extension `.md`. Root-level `README.md` and `CHANGELOG.md` are conventional distribution-file exceptions.
- Folders: `##-kebab-name`. A note lives in exactly one folder; cross-cutting membership
  is expressed with tags and MOC links, never with copies.
- `SKILL.md` keeps its uppercase name — it is the Claude Skill filename convention.
- One concept per note. If a note needs two `type` values, it is two notes.

## Link contract

- Internal references use `[[wikilinks]]`, never bare paths.
- A link target must resolve. `kb-linker` fails the build on a dead link.
- Ambiguous basenames take the folder-qualified form: `[[04-sbir/drafts/project-pitch-draft]]`.
- Every note is reachable from [[start-here]] within three hops. Orphans are a
  `kb-linker` finding.
- Every claim-bearing note links to its evidence source; every evidence entry links back
  to at least one consumer. Both directions are checked.

## Validation

`kb-schema-steward` runs the checks; `drift-controller` files what fails.

1. Frontmatter parses; `type` and `status` are in vocabulary.
2. Required fields present for the declared `type`.
3. `updated` is not in the future and not older than `review_by`.
4. Confidence markers come from the ladder; no bare "verified".
5. Filenames and folders match convention.
6. All wikilinks resolve; no orphans beyond three hops.
7. Identifiers are unique within their namespace and never reused.
8. No claim-bearing note cites a `status: draft` note as support.

## Related

[[tag-taxonomy]] · [[methodology]] · [[drift-control]] · [[gap-register]] · [[meta-moc]]
