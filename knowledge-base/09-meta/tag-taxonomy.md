---
type: taxonomy
status: active
owner: kb-schema-steward
version: 1.0.0
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/taxonomy
- domain/knowledge-engineering
- audience/internal
- lifecycle/active
---
# Tag Taxonomy

Seven independent layers. A tag from one layer never implies a tag from another, so they
compose: `type/experiment` + `domain/identity` + `confidence/synthetic` +
`action/needs-source` describes a note precisely, and each facet can be queried alone.

Namespaced with `/` so Obsidian nests them and so a bare word like `identity` can never
collide with a heading. Owner: `kb-schema-steward`. Adding a tag inside an existing layer
is routine; adding a *layer* is a schema MINOR bump.

## Layer 1 — `type/` (what kind of note)

Mirrors the `type` frontmatter field exactly. Duplicated as a tag so the graph view and
tag pane both work.

`type/home` `type/moc` `type/schema` `type/taxonomy` `type/policy` `type/experiment`
`type/method` `type/dataset` `type/evidence` `type/source` `type/term` `type/brief`
`type/draft` `type/strategy-note` `type/agent` `type/log` `type/archive`

## Layer 2 — `domain/` (what it is about)

The subject matter. A note may carry several.

**Programme domains:** `domain/identity` (entity resolution, carrier identity),
`domain/provenance` (event records, traceability), `domain/federation` (cross-party access
and federation), `domain/governance` (institutional controls and stewardship),
`domain/adoption` (participation, incentives), `domain/orchestration` (planning, routing),
`domain/equity` (small-carrier burden, distributional effects), `domain/privacy`
(re-identification, disclosure), `domain/legal` (liability, antitrust, statutory analogues),
`domain/regulatory` (agency rules, programmes, enforcement context), `domain/standards`
(standards bodies, identifiers, interoperability), `domain/data-access` (licensing,
permissions, retrieval posture), and `domain/procurement` (buyer/procurement constraints).

**Sector domains:** `domain/freight`, `domain/supply-chain`, `domain/climate`,
`domain/energy`, `domain/agriculture`.

The four sector tags beyond freight exist because [[client-common-action]] names Climate,
Energy, Agriculture and Supply Chain as its focus areas. They are the hooks by which this
vault's methods become reusable outside freight. Most notes will not carry them yet. That
is expected and should not be filed as a gap.

**Craft domains:** `domain/knowledge-engineering`, `domain/semantic-web`,
`domain/graph-database`, `domain/data-science`, `domain/gis`, `domain/nlp`. Also from the
client's stated capabilities. They tag the notes documenting *how the vault itself is
built* — the transferable asset.

## Layer 3 — `lifecycle/` (maturity)

Mirrors `status`. `lifecycle/active` `lifecycle/draft` `lifecycle/planned`
`lifecycle/candidate` `lifecycle/required` `lifecycle/stretch` `lifecycle/to-build`
`lifecycle/partner-dependent` `lifecycle/current` `lifecycle/superseded`
`lifecycle/frozen`

## Layer 4 — `confidence/` (how much weight the content bears)

Applied at note level to signal the *weakest* claim inside, so a reader scanning tags is
never over-promised. Claim-level confidence still lives in the evidence entry.

`confidence/primary` `confidence/peer-reviewed` `confidence/dataset`
`confidence/secondary` `confidence/vendor` `confidence/unverified` `confidence/synthetic`
`confidence/mixed`

## Layer 5 — `programme/` (where it sits in the work)

The cross-reference layer. It turns "show me everything bearing on G14" into a one-click
query instead of a grep.

- Goals: `programme/g1` … `programme/g14`
- Experiments: `programme/e1` … `programme/e5`
- Aims: `programme/aim-1` `programme/aim-2` `programme/aim-3`
- Findings: `programme/r-wn-01` … `programme/r-wn-06`
- Gates: `programme/gate-protocol-freeze` `programme/gate-identity` `programme/gate-event`
  `programme/gate-federation` `programme/gate-participation` `programme/gate-application`
- Phase: `programme/phase-i` `programme/phase-ii` `programme/pre-submission`

## Layer 6 — `audience/` (who it is written for)

Register differs by audience and the de-slop pass treats them differently.

`audience/internal` — working notes, logs, scans.
`audience/client` — Common Action-facing narrative.
`audience/reviewer` — NSF reviewer-facing prose; strictest evidentiary standard.
`audience/participant` — carrier/broker-facing consent and comprehension material.
`audience/public` — anything intended for external publication.

## Layer 7 — `action/` (what it needs from a human)

The work queue, expressed as tags so it can be swept without a separate tracker.

`action/blocker` — blocks submission or a downstream gate.
`action/open-decision` — needs a human choice; belongs in [[decision-log]].
`action/needs-source` — asserts something without a citation.
`action/needs-verification` — has a citation that failed retrieval or is snippet-only.
`action/needs-adjudication` — needs the expert panel, not an agent.
`action/stale` — past its `review_by` date.
`action/migrate` — does not yet satisfy [[kb-schema]] 1.0.0.
`action/none` — explicitly swept and clean.

## Rules

1. Every note carries at least `type/`, `domain/`, and `lifecycle/`.
2. Claim-bearing notes additionally carry `confidence/` and `audience/`.
3. `action/` tags are transient. Clearing one is an edit to the note, and
   `drift-controller` reports any `action/` tag older than 30 days as itself stale.
4. Never invent a tag inline. Add it here first, or it will not survive the next sweep.
5. Tags never replace links. A tag says what a note is; a link says what it depends on.

## Query recipes

| Question | Query |
|---|---|
| What blocks submission? | `tag:#action/blocker` |
| What rests on unverified sources? | `tag:#confidence/unverified OR tag:#action/needs-verification` |
| Everything bearing on the benchmark goal | `tag:#programme/g14` |
| Reviewer-facing prose due a de-slop pass | `tag:#audience/reviewer -tag:#action/none` |
| Transferable method notes for other sectors | `tag:#domain/knowledge-engineering` |
| Notes that never got migrated | `tag:#action/migrate` |

## Related

[[kb-schema]] · [[drift-control]] · [[gap-register]] · [[meta-moc]]
