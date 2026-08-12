---
type: log
status: active
owner: memory-keeper
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/log
- domain/knowledge-engineering
- audience/internal
- lifecycle/active
---
# Decision Log

Durable choices and their reasoning. Append-only: a superseded decision is marked, never
deleted, because the reason a thing was decided is usually more valuable later than the
decision itself.

Entries are `DEC-###`. A decision that an agent is not permitted to make (see
[[methodology]] §7) arrives here as `status: open` and waits for a human.

## Format

`id · date · decision · rationale · consequences · status · owner`

## Entries

### `DEC-001` — Common Action is the client

**Date:** 2026-08-06 · **Status:** recorded · **Owner:** user

The work is performed for Common Action (common-action.org). Their site was retrieved and
recorded in [[client-common-action]] on the same date.

*Consequences:* the vault now has a named audience. `audience/client` in
[[tag-taxonomy]] resolves to Common Action. Their stated focus areas — Climate, Energy,
Agriculture, Supply Chain — and stated capabilities in knowledge engineering, graph
databases, and the semantic web are recorded as self-reported, not corroborated.

*Explicitly not decided:* that Common Action is the SBIR applicant entity. See `DEC-002`.

---

### `DEC-002` — SBIR applicant entity and route

**Date raised:** 2026-08-06 · **Status:** partially resolved 2026-08-06 · **Owner:** client + counsel

**Resolved:** the user has confirmed directly that **Common Action is the applicant
entity.** This is a direct instruction from the party commissioning the work, not a
retrieved source — recorded here as the authority for the fact, and propagated into
[[client-common-action]] and the SBIR placeholder register as "applicant: Common Action."

**Resolved 2026-08-08:** the commissioning team named **Ellie Young** as Principal Investigator.

**Still open:** legal form (nonprofit, for-profit, fiscally sponsored, or other), SBIR vs.
STTR route, and confirmation that Ellie Young will meet the applicable NSF employment/effort rule at award and throughout performance. NSF SBIR requires a qualifying small business concern and a PI
more than 50% employed by it — Common Action's site states no entity type, so eligibility
under that rule is not yet established even though the applicant's identity now is. Do not
infer legal form from the confirmed name; that is a separate fact requiring its own
source or its own direct confirmation.

*Blocks:* the legal-form, route, and PI employment/effort portions of the remaining `[PLACEHOLDER]` entries across the SBIR package. Applicant and PI identity are now unblocked.

---

### `DEC-003` — Is the reusable vault machinery in scope?

**Date raised:** 2026-08-06 · **Status:** open · **Owner:** client

This vault now contains two separable assets: the freight content, and the machinery that
builds and maintains it ([[kb-schema]], [[tag-taxonomy]], [[methodology]],
[[drift-control]], [[agents-and-loops]]). The machinery is domain-neutral and maps onto
Common Action's stated capabilities.

*If confirmed:* `GAP-015` opens cross-sector transfer notes, and the sector tags already
in the taxonomy start carrying notes.
*If declined:* the machinery stays as internal tooling and the sector tags stay empty —
harmless either way, which is why they were added before the decision.

---

### `DEC-004` — Is the website the authoritative description of the client?

**Date raised:** 2026-08-06 · **Status:** open · **Owner:** client

[[client-common-action]] is built entirely from common-action.org. If an internal
capability statement, incorporation record, or prior engagement brief exists, it
supersedes the site and the card should be rebuilt from it.

---

### `DEC-005` — Two character counts in the Pitch draft were recomputed

**Date:** 2026-08-06 · **Status:** recorded, needs confirmation · **Owner:** publishing

During the prose pass, Fields 1 and 4 of [[04-sbir/drafts/project-pitch-draft]] were
edited. The document states its own character counts against NSF limits, and those counts
were verified correct before editing. Leaving them would have made the document assert
something false about itself, so they were recomputed by the same method:

- Field 1: `3,304 / 3,500` → `3,262 / 3,500`
- Field 4: `1,135 / 1,750` → `1,130 / 1,750`

Fields 2 and 3 were not edited and their counts are unchanged.

*Rationale:* these are measurements of the vault's own prose, not external facts. The
no-invented-facts rule protects claims about the world; a self-measurement must track what
it measures. *Tracked as* `DRIFT-024` so a human confirms or reverts.

---

### `DEC-006` — Schema 1.0.0 adopted; the vault is not retro-migrated

**Date:** 2026-08-06 · **Status:** recorded · **Owner:** kb-schema-steward

[[kb-schema]] 1.0.0 codifies existing practice rather than imposing a new system, and
existing notes are **not** silently rewritten to conform. Divergences are recorded as
`DRIFT-025` and `GAP-011` and migrated deliberately.

*Rationale:* a bulk frontmatter rewrite across ~70 notes is exactly the kind of operation
that corrupted prose during the folder reorganization (`DRIFT-007`). Migration happens
per-note, on a pass that a human can review.

---

### `DEC-007` — Control layer lives in `09-meta/`

**Date:** 2026-08-06 · **Status:** recorded · **Owner:** kb-schema-steward

The schema, taxonomy, methodology, registers, glossary, and agent architecture live in a
new numbered folder rather than a dotfolder or the existing `05-agent-system/`.

*Rationale:* it follows the vault's `##-name` convention, stays visible in Obsidian, and
keeps a clean split — `05-agent-system/` documents the *research* agents that investigate
freight; `09-meta/` documents the *knowledge-base* agents that maintain the vault.

---

### `DEC-008` — `French Trans.md` left in place

**Date:** 2026-08-06 · **Status:** recorded · **Owner:** user

A French poem translation in the vault root is not programme content and violates the
naming convention. It was **not** deleted or moved — it may be deliberate. Flagged as
`DRIFT-023` for the user to dispose of.

*Rationale:* deleting a user's file because it does not match a schema the assistant just
wrote is not a decision an agent gets to make.

---

### `DEC-009` — The dataset index is typed `moc`, not `dataset`

**Date:** 2026-08-06 · **Status:** recorded · **Owner:** kb-schema-steward

[[dataset-index]] was initially typed `dataset`, which failed [[kb-schema]]'s own
requirement that a `dataset` note carry `access`, `licence`, and `verification` fields. It
is an index *of* datasets, not a dataset card.

*Options considered:* add an `index` type to the schema (a MINOR version bump), or use the
existing `moc` type with `area: datasets`. Chose `moc` — the vocabulary already had a fit,
and adding a type to accommodate one note is how a closed vocabulary stops being closed.

*Also fixed in the same pass:* `kb-schema` and `tag-taxonomy` carried `meta/schema` and
`meta/taxonomy` tags from a layer that does not exist in [[tag-taxonomy]], and both were
missing the mandatory `domain/` tag. [[glossary]] declared `type: taxonomy` while tagging
`type/term`. All four were self-inflicted violations of the schema those same files
define, caught by the prose-editing pass rather than by validation — which is itself a
finding: no validator has been run yet (`GAP-011`).


---

### `DEC-010` — Team-release personnel roles

**Date:** 2026-08-08 · **Status:** recorded · **Owner:** commissioning team

For the team-distribution release, **Ellie Young** is the named Principal Investigator.
**Russell Berry** is named **Research & Knowledge Architecture Lead**, reflecting the work
already performed across the programme: ontology/evidence architecture, source and
provenance governance, benchmark and experiment specification support, technical synthesis,
and SBIR narrative architecture.

This is a programme-role designation for the working package. It does **not** invent a
salary, effort percentage, employee/consultant classification, or corporate title. Those
remain budget/eligibility facts to be supplied by Common Action before submission.

---

### `DEC-011` — E1 identity target is layered; RC1 advances to human freeze review

**Date:** 2026-08-08 · **Status:** recorded / approval pending · **Owner:** Ellie Young + E1 protocol owner

A source-grounded Research Agent pass and independent hostile Eval Agent pass reject the loose
“same carrier” binary as the scientific target. E1 now treats **legal-person identity** as Task A
and separately represents FMCSA registrant/identifier continuity, operating authority, typed
corporate/ownership/continuity relationships, and regulatory reincarnation/affiliate dispositions.

The resulting package is [[e1-carrier-identity-and-relationship-standard]] `1.0.0-rc1`,
[[e1-identity-ontology.yaml]], [[e1-adjudication-decision-tree]],
[[e1-identity-claims-ledger]], [[e1-edge-case-suite.csv]],
[[e1-definition-freeze-review]], [[e1-adjudicator-governance-and-training]],
[[e1-state-corporate-source-access-memo]], and [[e1-definition-conformance-report]]. The hostile review found eight Critical and eleven Major defects
in the prior loose formulation; RC1 closes those design findings in the synthetic suite.

**Not yet approved/frozen:** PI scientific sign-off, freight/FMCSA-domain walk-through of all 60
cases, counsel/domain review of reincarnation/affiliation language and sensitive evidence, first
state/jurisdiction source-access memo, adjudicator COI/training/pilot double-label run. No model or
benchmark builder may silently change the target while these gates are being completed.

**Novelty consequence:** GAO/ARCHI/URSA, Motus, and SCAC Verified establish substantial prior art
for carrier screening and identity verification. E1 novelty is therefore framed around an
evaluated, provenance-bearing, time-aware, contestable identity/relationship benchmark and
resolution workflow — not “first automated chameleon detector.”

## Related

[[meta-moc]] · [[gap-register]] · [[drift-control]] · [[client-common-action]] · [[run-log]]
