---
type: taxonomy
status: active
owner: glossary-builder
version: 1.1.0
schema_version: 1.0.0
updated: 2026-08-18
tags:
- type/taxonomy
- domain/knowledge-engineering
- confidence/mixed
- audience/internal
- lifecycle/active
---
# Glossary

Controlled vocabulary for the Freight Trust programme. Every definition is drawn from a
cited source or explicitly marked as coined in this vault. Terms defined from general
knowledge without a citation do not belong here — where that is currently the case, the
entry says so.

The **Not to be confused with** lines do most of the work here. The programme's precision
rests on a small number of distinctions, and each one is a place where a claim gets
overstated once the distinction slips.

Maintained by `glossary-builder`. Seeded 2026-08-06; `GAP-007` tracks completion. Updated
2026-08-07: resolved the three previously-unsourced terms (Evidence graph, Trust layer,
Neutral infrastructure) with coined-here definitions, added Backhaul, Deadhead, Aim, and
MCS-150, and logged one term-collision finding (Neutral infrastructure) for human review.

## Core architecture and positioning

### Evidence graph

**Definition.** A graph-structured evidence record connecting a carrier or broker entity to
authoritative identity, registration, insurance, safety, and relationship data, in which
every relationship retains its source, timestamp, confidence, access policy, and correction
path. The output is meant to be an explainable evidence trail for a human reviewer, not an
opaque decision engine.
**Source.** `coined-here`. First given operational content — not just named — in
[[preliminary-freight-trust-brief]] (08-archive): "Build an evidence graph that connects a
carrier or broker to authoritative identity, registration, insurance, safety, and
relationship records. Every relationship must retain its source, timestamp, confidence,
access policy, and correction path." Carried forward as the construct under direct test in
[[experiment-e1-entity-resolution-and-identity-assurance]] and named as the architecture's
substrate in [[experiment-e5-orchestration-value]].
**Aliases.** Carrier evidence graph; shared evidence graph; evidence layer.
**Not to be confused with.** A generic knowledge graph, or a risk-scoring/eligibility
engine — E1 states plainly that it resolves identity claims and explains the evidence used;
producing a risk score is explicitly not under test (see **Entity resolution**). Also
distinct from **Trust layer**: the evidence graph is the identity/evidence data structure;
the trust layer is the larger governed architecture (identity, provenance, policy, and
participation together) built around it. E5 states the relationship directly: "the evidence
graph is the substrate, and cross-actor orchestration is the first high-value use case."
**Used in.** [[preliminary-freight-trust-brief]], [[freight-trust-client-master-brief]],
[[client-facing-freight-trust-programme]],
[[experiment-e1-entity-resolution-and-identity-assurance]],
[[experiment-e5-orchestration-value]], [[roster]]

### Trust layer

**Definition.** The federated architecture that links authoritative identity/credential
evidence and permissioned facility-event records across participants without requiring raw
data to be pooled centrally. Source systems remain authoritative; the trust layer
establishes what evidence exists, where it came from, and how it may be used.
**Source.** `coined-here`. First given operational content in
[[preliminary-freight-trust-brief]] (08-archive), which proposes testing "whether a
**federated freight trust layer** can make \[freight] decisions more explainable, timely,
and fair," and states the governing principle: "source systems remain authoritative, while
the trust layer links evidence, permissions, and provenance." Carried into
[[freight-trust-client-master-brief]]'s "Proposed system" section in near-identical
language, and tested piecewise across the experiment suite — E1 through E5.
**Aliases.** Freight trust layer; freight-trust infrastructure; freight-trust layer.
**Not to be confused with.** The **Evidence graph** (the data structure the trust layer
exposes), or a **Federation** that is merely distributed rather than governed (see
**Federation**, below). E1 is explicit that it tests only "whether the proposed identity
substrate is technically credible enough for the rest of the trust layer to rely on," not
whether the trust layer as a whole works — that broader claim is reserved for
[[experiment-e5-orchestration-value]], which is deliberately sequenced later and "should not
be used to validate the trust layer until identity, provenance, policy, and participation
are sufficiently credible."
**Used in.** [[preliminary-freight-trust-brief]], [[freight-trust-client-master-brief]],
[[client-landscape-and-sbir-readiness-brief]], [[luna-wide-net-synthesis]],
[[datasets-and-experiments-moc]], E1, E3, E5, [[data-management-plan-draft]],
[[commercialization-plan-draft]]

### Neutral infrastructure

**Definition.** The claim that a "neutral" label is not itself a safeguard — neutrality has
to be made operational through governance: independent stewardship and transparent funding,
role-based access plus purpose limitation plus data minimization, source provenance plus
correction/appeal rights, published data-quality and error-remediation rules, human review
and meaningful abstention, and no paywall for basic small-carrier verification access.
**Source.** `coined-here`. Stated in [[preliminary-freight-trust-brief]] (08-archive) under
"Governance principles": "A 'neutral' label is not a safeguard; the system behind it needs
operational ones," with the GLEIF challenge-mechanism analogue and the listed minimum
safeguards. Restated as a directly tested thesis component in
[[experiment-e3-federated-access-and-policy-enforcement]]: "Neutral infrastructure must be
governed."
**Aliases.** Neutral utility; "neutral, federated, challengeable infrastructure" (the
positioning phrase in [[improvement-suggestions]] item 7).
**Not to be confused with.** A separate, uncollapsed usage in [[research-programme]], where
"neutral infrastructure" describes how *competitors* position themselves in the market
("none position as neutral infrastructure") rather than the governed-safeguards property E3
tests for internally. The two uses are not necessarily in tension — a positioning claim
could be true and the underlying governance could still be untested — but they are doing
different work in different documents and have not been reconciled in one place. **See
Collisions in this glossary's maintenance report; not resolved here.**
**Used in.** [[preliminary-freight-trust-brief]],
[[experiment-e3-federated-access-and-policy-enforcement]], [[research-programme]],
[[experiment-e4-participation-and-small-carrier-equity]], [[goals]]

## Identity and entity resolution

### Chameleon carrier

**Definition.** A motor carrier that (1) submitted registration information matching a
previously registered carrier, and (2) where that previous carrier had a motive for
evading detection, such as a history of safety violations.
**Source.** GAO-12-364, *Motor Carrier Safety: New Applicant Reviews Should Expand to
Identify Freight Carriers Evading Detection* (March 2012). `primary`, retrieved and
confirmed.
**Aliases.** Reincarnated carrier; chameleon attributes (GAO's own phrasing for the
matching criteria).
**Not to be confused with.** A carrier that merely re-registered, changed name, or changed
ownership. GAO's second prong is a *motive*. Because motive is not a field in any dataset,
no synthetic pipeline can manufacture the pattern and no labeled dataset exists.
**Used in.** [[experiment-e1-entity-resolution-and-identity-assurance]],
[[dataset-scan-entity-resolution]], [[dataset-e1-adjudicated-carrier-identity-cases]]

### Entity resolution

**Definition.** Deciding whether two or more records refer to the same real-world entity.
**Source.** Standard term of art in the record-linkage literature; the vault's operative
references are Papadakis et al. on blocking and nearest-neighbour search
(arXiv:2202.12521) and the Fellegi–Sunter probabilistic linkage tradition named in the
Project Description. `peer_reviewed`.
**Aliases.** Record linkage, deduplication, entity matching.
**Not to be confused with.** Risk scoring. E1 resolves identity claims and explains the
evidence; it does not rate a carrier.
**Used in.** [[experiment-e1-entity-resolution-and-identity-assurance]], the `method-*`
cards

### Blocking

**Definition.** Reducing the candidate comparison space so that only plausibly matching
record pairs are scored, rather than every pair.
**Source.** Papadakis et al., arXiv:2202.12521. `peer_reviewed`.
**Not to be confused with.** Matching itself. **Blocking recall** — whether the true match
was generated as a candidate at all — is a separate metric from final match recall. A
method that never generates the true candidate cannot recover it downstream, and reporting
only end-to-end recall hides that failure.
**Used in.** [[experiment-e1-entity-resolution-and-identity-assurance]]

### Calibration

**Definition.** The property that a model's stated confidence matches its observed
accuracy — among cases assigned 80% confidence, about 80% are correct.
**Source.** Standard in the uncertainty-quantification literature. The Project Description
names Bayesian calibration and conformal-prediction-style abstention sets as *candidate*
methods to be evaluated. `peer_reviewed`. Evaluated via reliability diagrams, expected
calibration error, Brier score, and coverage-risk curves.
**Not to be confused with.** Accuracy. A model can be accurate and badly calibrated, or
well calibrated and weak. Calibration connects a score to a review policy; without it,
abstention has no threshold to work from.
**Used in.** [[experiment-e1-entity-resolution-and-identity-assurance]]

### Abstention

**Definition.** The system declining to decide a case and routing it to human review,
rather than returning a low-confidence answer.
**Source.** Coined-here usage, grounded in the required action of R-WN-03
([[review-notes]]) and goal G13.
**Not to be confused with.** Denial. An abstention says "not enough evidence"; a denial
says "no". Conflating them turns missing data into an adverse finding — the exact failure
mode the programme is designed to avoid.
**Used in.** E1 (condition C4), E3 (decision vocabulary), [[goals]] G13

## Events and provenance

### Provenance

**Definition.** The record of where a claim came from — source, time of observation,
derivation chain, corrections, and reviewers — retained alongside the claim rather than
discarded once the claim is stored.
**Source.** NIST IR 8536's traceability meta-framework, cited in Project Description §2:
traceability requires trusted repositories, linked records, secure access, and event
recording, not a graph database alone. `primary`.
**Not to be confused with.** A timestamp. A timestamp says when; provenance says who
asserted it, on what basis, and what happened to it since.
**Used in.** [[experiment-e2-facility-event-provenance-and-dwell-reconstruction]], G11

### Dwell

**Definition.** The elapsed time a truck spends at a facility, decomposed into distinct
intervals: appointment-to-arrival, arrival-to-gate, gate-to-dock, dock-to-release, and
release-to-departure.
**Source.** Interval decomposition is specified in
[[experiment-e2-facility-event-provenance-and-dwell-reconstruction]]; ATRI's 2025
Operational Costs update reports roughly 1.5–2 hours average dwell per stop, with
secondary sources disagreeing between ~1h38m and ~1h49m — the discrepancy is unresolved.
`primary` for the measure, `secondary` and contested for the figure.
**Not to be confused with.** **Detention** — see next entry. This is the single most
important distinction in Aim 2.
**Used in.** E2, E5, [[evidence]]

### Detention

**Definition.** Dwell beyond an agreed threshold, for which a carrier may be owed
compensation. The threshold, appointment context, carrier/facility rule, and exception
policy must be explicit for the term to mean anything.
**Source.** FMCSA treats detention measurement — separating it from ordinary dwell — as an
active, unresolved research question (Project Description §1(b)). `primary` for the
unresolved status.
**Not to be confused with.** Dwell. Detention is never inferred from a long dwell interval
alone. The widely repeated $15.1B/year figure ($11.5B lost productivity plus $3.6B added
expense) is flagged `[UNVERIFIED]` in this vault and barred from load-bearing use.
**Used in.** E2, [[evidence]], [[sbir-evidence-refresh]]

### EPCIS

**Definition.** The GS1 standard for supply-chain event visibility data, structuring what
happened, when, where, and in what business context.
**Source.** GS1 EPCIS / CBV 2.0. `primary`; royalty-free per GS1. Reference implementation
for generation: the OpenEPCIS Test Data Generator, Apache 2.0.
**Not to be confused with.** A facility-appointment schema. EPCIS is retail and
product-tracking oriented; the freight profile adds `source_id`, `observed_at`,
`valid_time`, `clock_quality`, `actor`, `confidence`, `correction_state`, and
`access_purpose`.
**Used in.** E2, E5, [[dataset-openepcis-generated-event-logs]]

### Tamper evidence

**Definition.** The property that later alteration of a record is detectable, typically
via an append-only or hash-chained log.
**Source.** Standard construction; applied in
[[method-hash-chained-audit-logging]]. `peer_reviewed`.
**Not to be confused with.** Proof that the original record was true. Hash chaining
detects alteration; it says nothing about whether the underlying assertion was accurate.
Losing this distinction is how a provenance system gets oversold.
**Used in.** E3

## Operations and orchestration

### Backhaul

**Definition.** The return leg of a round trip; in trucking specifically, freight secured
to cover what would otherwise be an empty return run. It typically pays a lower rate than
the outbound ("headhaul") leg.
**Source.** DAT, *Trucking Industry Glossary*: "Backhaul: The return trip, which usually
pays a lower rate than the headhaul." `vendor` — industry-standard usage, not a regulatory
or peer-reviewed definition; no primary government source was found defining the term.
**Aliases.** Backhaul load; backhaul match.
**Not to be confused with.** **Deadhead** (below). A backhaul is a load type — freight
carried on the return leg; deadhead is the distance/cost metric for running that same leg
empty. Securing a backhaul is what avoids deadheading a given leg; the two terms describe
opposite outcomes of the same trip segment, not the same thing.
**Used in.** [[preliminary-freight-trust-brief]], [[research-programme]],
[[experiment-e5-orchestration-value]], [[method-synthetic-orchestration-simulation]]

### Deadhead

**Definition.** Driving with an empty trailer — miles run without a load, typically between
a drop-off and the next pickup. Since carriers are generally paid only for loaded miles,
deadhead miles are a cost (fuel, hours, equipment wear) without offsetting revenue.
**Source.** DAT, *Trucking Industry Glossary*: "Deadhead: Driving with an empty trailer.
Since most trucks are paid by the mile only when they're loaded, deadhead often means
moving the truck for no pay." `vendor`. ATRI's *Analysis of the Operational Costs of
Trucking* tracks "percent deadhead" / empty miles as a standard annual industry metric,
consistent with how this vault already treats ATRI-sourced operational figures (see
**Dwell**, **Detention**). `secondary`.
**Aliases.** Deadhead miles; empty miles — used interchangeably in this vault, e.g. E5's
"empty/deadhead miles" primary outcome.
**Not to be confused with.** **Backhaul** (above). Also not to be confused with **Dwell** —
deadhead is time/distance spent moving without a load; dwell is time spent stationary at a
facility. E5 tracks them as separate outcomes: empty/deadhead miles as a primary outcome,
dwell as a secondary one.
**Used in.** [[experiment-e5-orchestration-value]], [[03-research-evidence/evidence]]

## Governance and federation

### Federation

**Definition.** An architecture in which participants retain their raw data and a decision
uses permitted summaries or derived evidence, rather than pooling raw data centrally.
**Source.** Coined-here usage within the programme; goal G11 requires federated-by-default
with raw pooling needing specific justification.
**Not to be confused with.** Distribution. Data being spread across systems does not make
a federation governed. E3 exists because a graph can connect records while still
permitting overbroad access, silent overwrites, and opaque secondary use.
**Used in.** E3, [[goals]] G11

### ABAC / NGAC / XACML

**Definition.** Attribute-Based Access Control decides access from attributes of
requester, resource, action, and context rather than role alone. **NGAC** (Next Generation
Access Control) is an ANSI/INCITS standard with a NIST reference implementation, the
Policy Machine. **XACML** is the OASIS policy language whose conformance-test format uses
`(policy, request, expected decision)` triples.
**Source.** NIST SP 800-162 (ABAC guide), SP 800-178 (XACML vs. NGAC comparison), SP
800-192 (verification and test methods). `primary`.
**Not to be confused with.** RBAC, role-based access control — which E3 tests as condition
C1 rather than assuming inadequate. The vault does **not** pre-select NGAC or XACML as the
policy model; it uses NGAC's engine and XACML's test convention while the model choice
stays an evaluated outcome.
**Used in.** E3, [[dataset-nist-policy-machine-xacml-cases]]

### Purpose limitation

**Definition.** The rule that access granted for one stated purpose may not be reused for
another, enforced as an explicit decision input rather than a policy statement.
**Source.** Encoded as E3 hypothesis H3. `coined-here` in this application; the concept is
standard in data-protection practice.
**Not to be confused with.** Access control generally. The specific test is that a request
cannot gain access by changing only its stated purpose.
**Used in.** E3

### Contestability / redress

**Definition.** The ability of a participant to challenge a record about them and have the
correction propagate to derived views, while the prior assertion remains visible as
superseded.
**Source.** Goal G13; required action of R-WN-03. Framing precedents: the FCRA dispute
window (15 U.S.C. §1681i — the commonly cited 30-day figure is `unverified` in this vault
and must be confirmed against the statute before citation) and GLEIF's challenge mechanism.
**Not to be confused with.** Algorithmic recourse, which explains or reverses a *model's*
decision. Redress here corrects a *factual record* and propagates the correction. Different
problem, different literature.
**Used in.** E3, E4, [[goals]] G13

## Programme and evidence terms

### Confirmed absence

**Definition.** A finding that something does not exist, established by a documented
search with stated scope, sources, and date.
**Source.** `coined-here`; the discipline is specified in [[methodology]] §1.
**Not to be confused with.** Not found. Confirmed absence is a claim about the world and
supports arguments (it is what lets the proposal call the benchmark first-of-kind); not
found is a claim about the search. Collapsing them either overstates or wastes the finding.
**Used in.** Both dataset scans, [[goals]] G14

### Load-bearing

**Definition.** A claim that a conclusion actually rests on, as opposed to context.
**Source.** `coined-here`, used throughout the review notes.
**Not to be confused with.** Merely present. The $7–16B/year fraud range is retained as
context and explicitly barred from load-bearing use (R-WN-06).
**Used in.** [[review-notes]], [[methodology]], the SBIR drafts

### Beachhead

**Definition.** The single bounded workflow the Phase I pilot is scoped to — carrier
onboarding and identity verification, as a working default pending client confirmation.
**Source.** Project Description §1, §6; improvement item 1. `coined-here`.
**Not to be confused with.** The full application. Disputed facility events are Aim 2's
research validation context, explicitly *not* a second Phase I beachhead.
**Used in.** [[04-sbir/drafts/phase-1-project-description-draft]], E4

### Aim (Aim 1 / Aim 2 / Aim 3)

**Definition.** The three funded Phase I research work packages named in the NSF project
description: Aim 1 (calibrated entity resolution), Aim 2 (event provenance and
verification), Aim 3 (governed federation and contestability). Each carries its own thesis,
method, milestone, and failure condition in the proposal.
**Source.** `coined-here` in this vault's usage, following the standard NSF/NIH proposal
convention of numbered "Specific Aims." [[04-sbir/drafts/phase-1-project-description-draft]]
§§3-5 defines the three Aims and their failure conditions;
[[04-sbir/drafts/phase-1-budget-and-justification-draft]] confirms the mapping: "Aim 1
(entity-resolution benchmarking and calibration), Aim 2 (event-provenance and
tamper-resistance prototyping), Aim 3 (governed federation/policy-enforcement
prototyping)."
**Aliases.** Research Aim 1 / 2 / 3.
**Not to be confused with.** The vault's **Experiment** numbering (E1-E5, defined in
`03-research-evidence/`) or its **Goal** numbering (G1-G14, in [[goals]]). Aim 1
corresponds most closely to E1, Aim 2 to E2, and Aim 3 to E3, but the mapping is not exact:
E4 (participation and small-carrier equity) and E5 (orchestration value, `status: stretch`)
belong to the vault's broader experiment framework without being funded Phase I Aims in
their own right. Also distinct from **Beachhead** (above) — the Aims are the three parallel
research work packages; the beachhead is the single bounded pilot workflow they integrate
to serve. See `DRIFT-003` for the related G0-G5 namespace collision this numbering sits
next to.
**Used in.** [[04-sbir/drafts/phase-1-project-description-draft]],
[[04-sbir/drafts/phase-1-budget-and-justification-draft]],
[[nsf-sbir-sttr-process-and-readiness-guide]], [[data-management-plan-draft]],
[[commercialization-plan-draft]], [[experiment-e3-federated-access-and-policy-enforcement]],
visuals in `07-visuals/`

## Regulatory and data acronyms

| Term | Expansion | Note | Source class |
|---|---|---|---|
| FMCSA | Federal Motor Carrier Safety Administration | Registration and safety authority; publisher of most Aim 1 seed data | `primary` |
| MCMIS | Motor Carrier Management Information System | The FMCSA system behind the Company Census File and crash/inspection catalogs | `primary` |
| USDOT number | The carrier identifier issued by FMCSA | Not permanent per organization — the assumption of permanence is what E1 tests | `primary` |
| SAFER | Safety and Fitness Electronic Records | One-carrier-per-query public lookup; not a bulk source | `primary` |
| L&I | Licensing & Insurance | FMCSA dataset described as a daily *difference* feed — a change log, which is what makes registration churn observable | `secondary` — page not directly retrieved |
| ELD | Electronic Logging Device | FMCSA publishes the data-transfer *format*; no public bulk dataset of actual records exists | `primary` for the spec |
| HOS | Hours of Service | Driver working-time limits; a hard constraint in E5 | `primary` |
| ATRI | American Transportation Research Institute | Source of the operational-cost figures and the GPS panel behind the BTS travel-time product | `primary` |
| BTS | Bureau of Transportation Statistics | Publisher of the free county-to-county truck travel times | `primary` |
| TABA | Technical and Business Assistance | NSF-funded assistance, ≤$6,500 inside the Phase I budget | `primary` |
| OOIDA | Owner-Operator Independent Drivers Association | Primary organization representing small-carrier interests in this vault's evidence base | `primary` |
| GLEIF | Global Legal Entity Identifier Foundation | Cross-industry analogue for governed identity with a challenge mechanism | `primary` |
| MCS-150 | Motor Carrier Identification Report | FMCSA's carrier registration/biennial-update form; the vault pursued historical semi-annual snapshots (2000-2019) via FOIA to test reincorporation tracking — the request was "fully granted" but released only a scanned image and correspondence, not usable bulk data ([[dataset-scan-entity-resolution]]) | `primary` for the form itself; `secondary` for the FOIA-outcome description |

## Terms admitted without a source

None currently. Evidence graph, Trust layer, and Neutral infrastructure — previously listed
here as `action/needs-source` — now carry `coined-here` definitions anchored to
[[preliminary-freight-trust-brief]] under **Core architecture and positioning**, above.
`GAP-007` should be updated to reflect this closure; that update is outside this file's
scope.

## Candidates considered and not admitted

Used in enough places to be tempting, but judged below the bar (either plain compositional
English a reader would not stumble on, or too thin a footprint to warrant a full entry).
Recorded so a future pass does not re-litigate them from zero.

- **Small-carrier equity** — used in 9+ notes (E1, E4, [[goals]], [[review-notes]],
  [[improvement-suggestions]], [[research-programme]], [[evidence]],
  [[method-staged-participation-and-equity-evaluation]]). The vault does give it an
  operational meaning narrower than the phrase alone suggests — R-WN-05 requires it be a
  predeclared fleet-size subgroup estimand, not an asserted fairness conclusion — but the
  phrase itself is transparent compositional English. Borderline; revisit if a future note
  uses "equity" in a way that conflicts with this operational sense.
- **Reciprocal benefit / reciprocal value** — used in 10+ notes as the term for a concrete
  incentive offered in exchange for data participation (G12, E4's H1-H3). Compositional and
  self-explanatory in context; not admitted.
- **Operating authority**, **MC number** — FMCSA-specific terms appearing in
  [[experiment-e1-entity-resolution-and-identity-assurance]] and
  [[dataset-scan-entity-resolution]], but only in passing (inline in field lists and a
  borrowed-methodology table), never as a concept the vault argues about the way it argues
  about dwell/detention or abstention/denial. Not admitted; flag if a note starts treating
  either as a load-bearing distinct construct.
- **C0-C5 / H1-H5 condition and hypothesis notation** — used across all five experiment
  files, but each file defines its own conditions and hypotheses locally in a table
  immediately next to first use, the way a table's column headers are defined by the table.
  Structural, not vocabulary; not admitted. (Distinct from the G0-G5 namespace collision in
  `DRIFT-003`, which is a genuine ambiguity because that notation is reused across three
  *different* meanings without a local table to disambiguate it.)

## Related

[[meta-moc]] · [[kb-schema]] · [[tag-taxonomy]] · [[gap-register]]

## E1 identity terms

### Legal person
**Definition.** The legally cognizable individual, corporation, partnership, LLC, or other
organized person to which E1 assigns source observations. This is the primary Task A identity
object; a DBA, owner, address, vehicle set, regulatory role, or account is not the legal person.
**Sources:** [[source-us-code-motor-carrier-registration-relationship-disclosure]],
[[source-fmcsa-usdot-and-operating-authority-identity-guidance]],
[[source-ecfr-390-5-and-385-1003-identity-definitions]].

### FMCSA registrant continuity
**Definition.** A separate E1 construct recording whether FMCSA treats registration continuity as
persisting across records or a form-of-business change. It is kept separate from state-law legal-
person identity because FMCSA publishes a narrow sole-proprietor continuity exception.
**Source:** [[source-fmcsa-usdot-and-operating-authority-identity-guidance]].

### Claimed USDOT versus authoritative USDOT assignment
**Definition.** `claimed_usdot` records what an observation/document/actor asserts;
`authoritative_usdot_assignment` records the person to which FMCSA assigns the number. The first
does not prove the second. This distinction is required to represent impersonation or misuse.
**Source:** [[source-fmcsa-usdot-and-operating-authority-identity-guidance]].

### Substantial continuity
**Definition.** A §386.73 relationship concept under which FMCSA may determine that one entity is
merely a continuation of another after considering a totality of factors. E1 represents supported
operational continuity as a relationship between distinct legal-person nodes; it does not turn
that relationship into identity equivalence.
**Source:** [[source-ecfr-386-73-reincarnated-carrier-standard]].

### Reincarnation / reincarnated carrier
**Definition.** In E1, a regulatory disposition layer, not a synonym for “same carrier.” A
`REINCARNATION_CONFIRMED` label requires authoritative agency/judicial support and procedural
status; similarity, shared ownership, or substantial continuity alone can support review or
relationship evidence but not an authoritative conclusion.
**Sources:** [[source-ecfr-386-73-reincarnated-carrier-standard]],
[[source-federal-register-2012-reincarnated-carrier-rule-preamble]],
[[source-gao-12-364-chameleon-carrier-matching]].

### Operating authority
**Definition.** FMCSA authorization for specified for-hire interstate operations. It is not a
legal-person identity key and can, in some legitimate corporate transactions, be transferred to a
different entity.
**Source:** [[source-fmcsa-usdot-and-operating-authority-identity-guidance]].

### Identity anchor leakage
**Definition.** Benchmark leakage that occurs when an authoritative identifier used to establish
gold identity (for example an FMCSA USDOT assignment) is also exposed unchanged to the model,
reducing evaluation to identifier lookup. E1 treats anchor-visible results as controls and uses
masked/missing/corrupted/conflict regimes for headline resolution evidence.
**See:** [[e1-carrier-identity-and-relationship-standard]], [[e1-definition-freeze-review]].
