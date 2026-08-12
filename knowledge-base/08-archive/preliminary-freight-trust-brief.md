---
type: archive
status: superseded
schema_version: 1.0.0
superseded_by: '[[01-client-briefs/freight-trust-client-master-brief]]'
frozen_on: 2026-08-01
tags:
- type/archive
- domain/freight
- lifecycle/superseded
---
# Preliminary Brief: Freight Trust Infrastructure

**Status:** Research concept for validation, not a product or legal standard.

## The opportunity

For a client-oriented landscape, stakeholder, regulatory, and SBIR view, see
[[01-client-briefs/client-landscape-and-sbir-readiness-brief|01-client-briefs/client-landscape-and-sbir-readiness-brief.md]].

Freight logistics depends on decisions made across organizations that do not share a
common, trusted view of counterparties or operating events. A broker may need to verify a
carrier; a carrier may need to establish a facility delay; an insurer may need an auditable
record; and a shipper may need to understand whether a delay is isolated or systemic.
Today, the relevant facts are fragmented across registrations, insurance records, broker
workflows, telematics, facility systems, and private platforms.

The proposed research programme asks whether a **federated freight trust layer** can make
those decisions more explainable, timely, and fair. It would link authoritative evidence
and permissioned operating events without assuming that all parties must pool their raw
data in one database.

The near-term purpose is to test whether evidence provenance, entity resolution, and shared
event semantics improve verification and operational visibility — not to create a universal
carrier score or prescribe a legal duty of care.

## Why now

Driver detention is economically significant and poorly measured. ATRI's 2023
analysis estimates that 39.3% of stops involved detention, representing 135.9 million
lost hours, $3.6 billion in direct costs, and $11.5 billion in productivity losses for
for-hire trucking. These are industry estimates rather than a federal census, but they
make a strong case for better measurement. [ATRI study record](https://trid.trb.org/View/2427471)

FMCSA continues to study how detention can be measured and separated from ordinary dwell
time. Its research agenda recognizes the lack of consistent, usable evidence about the
source and operational effect of delays. [FMCSA](https://www.fmcsa.dot.gov/research-and-analysis/impact-driver-detention-time-safety-and-operations)

There is also a demonstrated identity-resolution gap. GAO found that FMCSA's historical
vetting work did not determine whether all new freight applicants were attempting to evade
detection through changed identities, in part because comprehensive investigation is
resource-intensive. [GAO-12-364](https://www.gao.gov/products/gao-12-364)

## What is being proposed

The programme has three connected work packages.

### 1. Carrier evidence and entity resolution

Build an evidence graph that connects a carrier or broker to authoritative identity,
registration, insurance, safety, and relationship records. Every relationship must retain
its source, timestamp, confidence, access policy, and correction path.

The output is an explainable evidence trail for a reviewer—not an opaque decision engine.
Automated indicators may prioritize cases for review, but they must be able to abstain and
must not become the sole basis for eligibility, pricing, contracting, or liability.

### 2. Facility-event provenance

Define a shared event model for appointments, arrival, gate, dock, loading/unloading, and
departure. The research question is whether permissioned, independently timestamped event
records improve detention measurement, dispute resolution, and facility-performance
visibility.

This does not assume that every operating system or GPS signal is publicly shared. A pilot
can start with a small number of partners and a limited event vocabulary.

### 3. Governance and participation

Treat participation as a design problem. Parties will not reliably share commercially
sensitive data merely because collective efficiency is attractive. The programme should
test reciprocal benefits such as faster verified onboarding, less duplicate documentation,
reciprocal facility-performance visibility, or service-level commitments.

The proposed architecture is federated and minimum-disclosure by default: source systems
remain authoritative, while the trust layer links evidence, permissions, and provenance.

## Why this is technically credible

Peer-reviewed supply-chain research supports knowledge graphs as a way to model complex,
multi-hop relationships and reason over risk evidence. It does not prove the proposed
freight intervention will work, but it establishes a credible technical basis. [Brintrup
et al., 2022](https://doi.org/10.1080/00207543.2022.2100841)

Recent work also shows that supply-chain graphs can extend visibility beyond direct
partners and that federated graph learning can preserve raw-data boundaries while enabling
collaborative analysis. [AlMahri, Xu, and Brintrup, 2026](https://doi.org/10.1080/00207543.2025.2575841), [Zhang et al., 2024](https://doi.org/10.1016/j.asoc.2024.112475)

NIST's traceability framework reinforces the broader architecture: effective traceability
requires trusted repositories, linked records, secure access, and event recording, which a
graph database alone does not deliver. [NIST IR 8536](https://csrc.nist.gov/pubs/ir/8536/ipd)

## What success would look like

The programme should judge success against predeclared measures, not a broad promise of
industry transformation.

| Hypothesis | Proposed measure |
|---|---|
| Evidence graphs improve verification work | Resolution time, precision/recall against adjudicated cases, and abstention rate |
| Provenanced events improve detention measurement | Timestamp coverage, agreement with ground truth, and dispute-resolution time |
| Federation improves acceptability | Participation and retention by role, data fields requested, and rejection reasons |
| Reciprocal value sustains participation | Uptake under different benefit offers and net value by fleet-size segment |
| The design does not disadvantage small carriers | Onboarding completion, time/cost burden, false positives, and appeal outcomes by fleet size |

Fraud, detention, and empty-mile reduction should be treated as downstream pilot outcomes.
They should not be claimed until a study has a baseline, comparison condition, and a
credible causal design.

## Governance principles

A “neutral” label is not a safeguard; the system behind it needs operational ones. The
Global Legal Entity Identifier System provides a useful analogue: standardized open entity
data, quality controls, and a challenge/update mechanism under independent governance. It
is not a freight solution, but it illustrates the elements needed for a trusted utility.
[GLEIF](https://www.gleif.org/en)

Minimum safeguards should include:

- independent governance and transparent funding;
- role-based access, purpose limitation, and data minimization;
- source provenance, correction rights, and participant challenge/appeal;
- published data-quality and error-remediation rules;
- human review and meaningful abstention for automated indicators; and
- no paywall for basic verification access needed by small carriers.

## What remains uncertain

There is no public proof that a federated U.S. freight trust graph reduces fraud or empty
miles. That is the core research question, not a settled conclusion. The programme also
needs direct research with small carriers, an adjudicated evaluation dataset, and legal
expert review before linking the work to any duty-of-care or liability framing.

The often-cited $7–16 billion annual fraud-cost range should remain context only until its
methodology and source quality are independently verified. The research case remains strong
without relying on it: detention, identity verification, auditability, and fragmented data
are independently documentable problems.

## Recommended next 90 days

1. Convene a small pilot group: one carrier cohort, one broker/shipper cohort, and one or
   two facilities.
2. Agree on a minimum event vocabulary, authoritative sources, permissions, and correction
   rules.
3. Assemble an adjudicated sample of identity and event cases before model development.
4. Run a limited federation experiment with predeclared success and equity measures.
5. Conduct a legal and small-carrier review before any external claim about standard of
   care, risk scoring, or consequential decisions.

## Further project material

This brief is derived from the programme's [[03-research-evidence/luna-wide-net-synthesis|wide-net evidence synthesis]], [[03-research-evidence/goals|research goals]], and [[03-research-evidence/review-notes|review notes]]. The underlying agent and evidence workflow is documented in [[05-agent-system/framework|the project framework]].
