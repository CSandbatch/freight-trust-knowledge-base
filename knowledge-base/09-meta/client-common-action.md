---
type: brief
status: active
owner: commercial-lead
audience: internal
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/brief
- domain/knowledge-engineering
- confidence/vendor
- audience/internal
- action/open-decision
- lifecycle/active
---
# Client — Common Action

The organization this work is performed for. Everything below is drawn from
common-action.org, retrieved 2026-08-08. That makes it **self-reported**: it is the
organization describing itself, which under [[kb-schema]]'s ladder is `vendor`-class for
any claim about capability or standing. It is `primary` only for what the organization
states about its own intent.

Nothing here has been corroborated against a third-party register, filing, or directory.
Do not upgrade any of it without a separate source.

## What the site states

| Field | Stated | Confidence |
|---|---|---|
| Name | Common Action | primary (self) |
| Mission | "Moving the world from chaos to comprehension" | primary (self) |
| Purpose | Reduce knowledge-worker friction in climate action through information and communication infrastructure | primary (self) |
| Focus areas | Climate, Energy, Agriculture, Supply Chain | primary (self) |
| Stated capabilities | Knowledge engineering, business intelligence, graph database, semantic web, data science, spatiotemporal analysis, physical modeling, GIS, NLP | vendor |
| Problems addressed | Resource discovery, message management, project structure, team collaboration, oversight of knowledge work | vendor |
| Positioning | Supports climate action and the open-science transition | primary (self) |
| Contact | ellie [at] common-action.org | primary (self) |
| Legal form / entity type | **Not stated** | — |
| Location | **Not stated** | — |
| Founding date | **Not stated** | — |
| Team beyond the contact | **Not stated on the public site** | — |
| Principal Investigator | **Ellie Young — confirmed directly by the commissioning team on 2026-08-08; not a claim derived from the public site** | direct team confirmation |
| Partners / affiliations | **Not stated** | — |

## Why the unstated fields outweigh the stated ones

Three of the unstated fields are load-bearing for the SBIR track, and none can be filled
by inference.

1. **Entity type is unstated.** NSF SBIR requires the applicant to be a small business
   concern meeting specific ownership and size rules, and the PI must be more than 50%
   employed by that business at award and throughout performance
   ([[nsf-sbir-sttr-process-and-readiness-guide]]). An organization positioned around
   open science and climate action may be a nonprofit, a for-profit, a fiscally sponsored
   project, or something else. Each answer changes the route — or forecloses it. This is
   now the sharper question, since the applicant's identity is confirmed but its form
   is not.
2. **Common Action is the applicant entity — confirmed 2026-08-06.** The user
   commissioning this work stated this directly. It is recorded here as fact on that
   authority (`DEC-002` in [[decision-log]]), not inferred or retrieved from the site.
   What remains open is *how* Common Action submits: directly, through a subsidiary, or
   via STTR with a research-institution partner — that still depends on the legal-form
   answer in point 1.
3. **The PI identity is now resolved: Ellie Young.** This was confirmed directly by the commissioning team on 2026-08-08. The public site identifies `ellie [at] common-action.org`, which is consistent with that instruction but does not itself establish the full name, PI role, employment percentage, or SBIR eligibility. Those employment/effort facts remain open.

Until legal form, route, and PI employment/effort eligibility resolve, the remaining `[PLACEHOLDER]` personnel and eligibility entries across
[[04-sbir/drafts/phase-1-project-description-draft]] and
[[04-sbir/drafts/phase-1-budget-and-justification-draft]] remain only where facts are still genuinely unknown. Ellie Young is now named as PI, and Russell Berry is named internally as Research & Knowledge Architecture Lead; effort, compensation, and formal employment classification remain open. These are not oversights; they are the honest state.

## Fit between the client and this vault

Common Action's stated focus areas include Supply Chain, and its stated capabilities are
knowledge engineering, graph databases, and the semantic web. The Freight Trust programme
is a supply-chain knowledge-graph problem. That alignment is the strategic reason this
vault is worth building properly rather than as a one-off proposal folder:

- The **freight content** serves the SBIR application.
- The **vault machinery** — [[kb-schema]], [[tag-taxonomy]], [[methodology]],
  [[drift-control]], the agent layers in [[agents-and-loops]] — is a reusable instance of
  the client's own product thesis. It transfers to Climate, Energy, and Agriculture
  without carrying freight facts along. The sector tags exist in the taxonomy on that
  basis, before any note needs them.

That framing is a working hypothesis about strategic fit, not a claim the client has
endorsed. It needs confirmation (`DEC-003`).

## Open decisions this note raises

| ID | Decision | Owner |
|---|---|---|
| `DEC-002` | What is Common Action's legal form, and which route (SBIR/STTR) follows from it? Applicant identity itself is resolved. | Client + counsel |
| `DEC-003` | Is the reusable-vault-machinery framing something the client wants pursued, or is freight the only deliverable? | Client |
| `DEC-004` | Is the site the authoritative description, or is there an internal capability statement that supersedes it? | Client |

## Verification queue

- Corroborate entity type against a state registry or IRS record before any eligibility
  claim is written. `action/needs-verification`.
- Re-fetch common-action.org before external publication; a site is a mutable source and
  this snapshot is dated.

## Related

[[decision-log]] · [[meta-moc]] · [[04-sbir/sbir-moc]] · [[00-home/client-request-and-outcomes]]
