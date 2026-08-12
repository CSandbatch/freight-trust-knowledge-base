---
type: policy
status: active
owner: kb-schema-steward
version: 1.0.0
schema_version: 1.0.0
updated: 2026-08-06
tags:
- type/policy
- domain/knowledge-engineering
- audience/internal
- lifecycle/active
---
# Methodology — how a claim enters and stays in this vault

The rule set every agent and every human contributor works under. It extends
[[source-policy]] (which governs source classes) with the full lifecycle: acquisition,
admission, representation, maintenance, and retirement.

A reader should be able to tell, for any sentence in this vault, where it came from and
how much weight it carries. The rules below exist to protect that property, not to grow
the vault.

## 1. Acquisition

**Source classes and what each may support.** Primary sources for legal, regulatory,
standards, public-programme, and official-statistics claims. Peer-reviewed work for
technical feasibility, measurement design, and organizational mechanisms. Vendor pages
only as statements of that vendor's own product — never as independent market validation.

**Retrieval is recorded, not assumed.** Every source card records `accessed`,
`verification`, and — on failure — the failure mode. The vault already carries FMCSA pages
that returned HTTP 403, catalog pages that would not render past a JS shell, and
commercial products whose licence terms could not be read. Those records are the product,
not a backlog.

**Search exhaustion is reportable.** When a search establishes that something does not
exist, the negative finding is written down with its scope: what was searched, where, and
on what date. "No labeled chameleon-carrier dataset is published anywhere found in this
scan" is a stronger statement than silence, and it is what let the SBIR draft argue the
benchmark is first-of-kind. Confirmed absence and failure to find are different claims and
are never collapsed.

## 2. Admission

A claim may enter the vault when it has: a proposition narrow enough to be falsified, a
source with class and date, a statement of what the source actually establishes, and a
statement of limits. That is the evidence-entry contract in [[artifact-contracts]].

**Quantitative claims** additionally state population, period, and method, and whether the
figure is an estimate, a survey, an administrative record, or a modeled result. Figures
from different populations or years are never combined without showing the conversion.

**What is refused admission:**

- A number without a traceable source. It becomes `[PLACEHOLDER]` with a named owner.
- A figure whose provenance is contested, unless it is admitted *as contested* with the
  contest documented. The detention-cost family ($15.1B / $11.5B / $3.6B) is the standing
  example: retained, flagged `[UNVERIFIED]`, and explicitly barred from load-bearing use.
- A borrowed benchmark number from an adjacent domain presented as a target for this one.
  Methodology transfers between domains; performance figures do not.
- Anything about a person, company, or partner not stated by a retrievable source.

## 3. Representation

**One claim, one home.** A claim lives in [[evidence]] (or a dataset/source card) and is
cited elsewhere by link. Restating a claim in a second note is how two versions of it
start to drift — [[drift-control]] catches several instances of exactly this.

**Confidence travels with the claim.** When a claim is cited into a brief or a draft, its
confidence marker travels with it. A `secondary` claim never becomes a fact by being
quoted in a reviewer-facing document.

**Uncertainty is represented, not resolved.** Where reviewers or sources disagree, the
disagreement is the record. Adjudication panels preserve an unresolved label; source
conflicts are kept as conflicts. Forcing a binary manufactures certainty the sources do
not contain.

**Structure over prose.** If something is a set of typed facts — a dataset's access terms,
an experiment's conditions, a policy's attributes — it is a table with fixed columns, not
a paragraph. Prose is for reasoning; tables are for facts.

## 4. Maintenance

**Freshness has an expiry.** Time-sensitive claims — solicitations, statutes, market
figures, live URLs — carry `review_by`. Loop L2 in [[agents-and-loops]] re-verifies them.
Anything past its date is tagged `action/stale` and may not be cited into a reviewer-facing
document until re-checked.

**History is preserved, never overwritten.** A superseded claim is marked `superseded` and
retains its dated original. This is the same discipline the programme demands of its own
proposed system: corrections propagate, the prior assertion stays visible.

**Contradiction is a first-class defect.** When two notes assert the same thing
differently — a different milestone month, a different connective, a hedge in one place and
none in another — that is a `DRIFT-###` issue with a severity, not a cosmetic inconsistency.

## 5. Retirement

Superseded material moves to `08-archive/` with `superseded_by` and `frozen_on`. Frozen
notes are never updated toward current facts; their value is showing what was believed
when. Deleting is reserved for genuine duplicates and is recorded in [[decision-log]].

## 6. Reproducibility

Any result the vault reports must ship with enough to regenerate it: protocol version,
data manifest, code and dependency versions, random seeds, configuration, raw and derived
outputs, reviewer identity, and a log of deviations. The full contract is in
[[experiment-protocol-standard]]. The vault-level obligation is narrower: **no result is
citable unless its reproducibility package exists.**

## 7. What agents may and may not do

Agents may: search, retrieve, extract, structure, link, tag, validate, detect
contradiction, draft prose, and propose.

Agents may not: invent a fact, fill a placeholder, upgrade a confidence marker, delete a
caveat, resolve a contradiction between two sources by choosing one, decide anything in
[[decision-log]], or edit `08-archive/`.

When an agent hits the boundary, it files — a `GAP-###`, a `DRIFT-###`, or a decision
request — and stops. A stopped agent with a filed issue is a success.

## Related

[[kb-schema]] · [[tag-taxonomy]] · [[agents-and-loops]] · [[drift-control]] · [[source-policy]] · [[artifact-contracts]]
