# Freight Trust Infrastructure

## A research and pilot programme for verifiable freight decisions

**Prepared for:** Prospective partners, funders, and industry stakeholders  
**Status:** Preliminary programme brief — evidence-led, pilot-ready, and subject to legal and stakeholder validation

## Executive summary

For the landscape, stakeholder-pushback, and SBIR-readiness view requested by the client,
read this document alongside [the Landscape and SBIR Readiness Brief](CLIENT_LANDSCAPE_AND_SBIR_READINESS_BRIEF.md). It is the primary entry point for external conversations; this document remains the full programme and pilot overview.

Freight decisions depend on information that is fragmented across carriers, brokers,
shippers, facilities, insurers, regulators, and technology platforms. As a result,
counterparty verification, operating-event records, and accountability often rely on
incomplete or inconsistent evidence.

This programme will evaluate a **federated freight trust infrastructure**: a shared layer
that links authoritative identity and credential evidence with permissioned operating-event
records. It is designed to improve the quality, speed, and explainability of freight
decisions without requiring participants to surrender raw data into a single central
database.

The programme does not presume that a new platform will automatically reduce fraud,
detention, or empty miles. Instead, it will test the enabling conditions: reliable entity
resolution, traceable facility events, workable data-sharing incentives, fair access for
small carriers, and a governed path from evidence to human decision.

## Why this matters

### Detention and operating visibility

Driver detention is a material operational problem. ATRI's 2023 analysis estimated that
39.3% of stops involved detention, with 135.9 million lost hours, $3.6 billion in direct
expenses, and $11.5 billion in productivity losses for for-hire trucking. These are
industry estimates rather than a federal census, but they establish a strong reason to
improve how delays are measured and resolved. [ATRI study record](https://trid.trb.org/View/2427471)

FMCSA continues to examine how detention can be consistently measured and distinguished
from ordinary dwell time. [FMCSA detention research](https://www.fmcsa.dot.gov/research-and-analysis/impact-driver-detention-time-safety-and-operations)

### Identity and verification

Carrier and counterparty verification remains difficult when entities, registrations,
relationships, and historical signals are distributed across systems. GAO documented the
resource constraints and coverage limits in historical efforts to identify freight carriers
that may evade detection through changed identities. [GAO-12-364](https://www.gao.gov/products/gao-12-364)

### An opportunity for trusted interoperability

Large-scale freight measurement is technically feasible: BTS's Freight Mobility Initiative
uses aggregated, anonymized GPS-derived data from roughly 350,000 unique truck tractors.
The data are controlled, which is itself instructive—the opportunity is not indiscriminate
data pooling, but governed, privacy-conscious interoperability. [BTS Freight Mobility Initiative](https://www.bts.gov/explore-topics-and-geography/topics/freight-transportation/trucking-movements-bts-freight-mobility)

## The proposed solution

The programme will design and test a trust layer with three integrated capabilities.

| Capability | What it does | Value to participants |
|---|---|---|
| Carrier evidence graph | Connects authoritative identity, registration, insurance, safety, and relationship evidence with provenance. | Faster, more explainable verification and a defensible due-diligence record. |
| Facility-event provenance | Captures permissioned milestones such as appointment, arrival, gate, dock, loading/unloading, and departure. | Better delay measurement, faster dispute resolution, and facility-performance visibility. |
| Governance and participation layer | Applies access controls, correction rights, data-quality rules, and reciprocal-value mechanisms. | Trustworthy participation without unnecessary exposure of commercial data. |

The design is **federated by default**. Participants retain control of their source data;
the shared layer records what evidence exists, where it came from, who may use it, and how
it can be corrected or challenged.

## What the programme will prove—or disprove

The programme is built around measurable hypotheses.

| Research question | How it will be tested |
|---|---|
| Can an evidence graph improve verification work? | Compare resolution time, precision/recall against adjudicated cases, and abstention rate with the current workflow. |
| Can provenance improve detention measurement? | Measure independent timestamp coverage, agreement with a ground-truth sample, and dispute-resolution time. |
| Will federation improve participation? | Compare adoption, retention, requested data fields, and stated objections across stakeholder roles. |
| What makes sharing worthwhile? | Test concrete offers such as faster onboarding, reduced duplicate documentation, facility visibility, and service-level benefits. |
| Can the system protect small-carrier access? | Segment onboarding, burden, false-positive, and appeal outcomes by fleet size. |

Downstream outcomes—reduced fraud, detention, and empty miles—will be measured only where
a pilot design supports a credible comparison. They will not be assumed in advance.

## Programme goals and deliverables

The work is organized into four client-relevant workstreams.

### Workstream 1: Legal, regulatory, and funding readiness

| Goal | Client outcome |
|---|---|
| G1 — Legal decision analysis | An accurate, source-backed explanation of applicable broker-liability and duty-of-care context, including what remains undefined. |
| G2 — FMCSA/DOT fraud initiative | A verified regulatory timeline and implications for identity, registration, and fraud-prevention infrastructure. |
| G3 — NSF SBIR/STTR requirements | A current funding-readiness brief: solicitation fit, submission gates, timeline, and required proposal structure. |

### Workstream 2: Market, standards, and stakeholder alignment

| Goal | Client outcome |
|---|---|
| G4 — Competitive landscape | A sourced map of existing verification, visibility, matching, and graph/interoperability capabilities. |
| G5 — CAVRA assessment | A neutral assessment of the framework’s scope, adoption, relationship to formal standards, and potential conflicts of interest. |
| G6 — Association and standards-body mapping | An evidence-backed stakeholder map covering industry associations, ASTM, NMFTA, and relevant public positions. |

### Workstream 3: Adoption, equity, and partner discovery

| Goal | Client outcome |
|---|---|
| G7 — Data-sharing incentives | A participation model grounded in real incentives, governance, and comparable data-sharing precedents. |
| G8 — Small-carrier equity | A documented view of compliance and access risks, with safeguards tailored to owner-operators and small fleets. |
| G9 — Exploratory interviews | A structured interview synthesis from the team’s existing conversations, or a clear plan to fill that gap. |

### Workstream 4: Pilot, governance, and technical validity

| Goal | Client outcome |
|---|---|
| G10 — Falsifiable pilot design | Baselines, comparison conditions, thresholds, and failure conditions for every material claim. |
| G11 — Minimum trusted-data architecture | A source/provenance/access/correction blueprint for each claim type and event record. |
| G12 — Participation testing | Concrete reciprocal benefits and a method for measuring uptake and retention by role and fleet size. |
| G13 — Redress and non-discrimination | Policies for abstention, human review, challenge, correction, false-positive remediation, and basic-access fairness. |
| G14 — Freight evidence benchmark | An adjudicated dataset and measurement protocol for identity and facility-event performance. |

## Technical rationale

Peer-reviewed research supports the use of knowledge graphs to represent complex,
multi-party supply-chain relationships and reason over linked evidence. This supports the
technical direction, but does not substitute for pilot evidence in freight operations.
[Brintrup et al., 2022](https://doi.org/10.1080/00207543.2022.2100841)

Research also supports privacy-preserving approaches such as federated graph learning,
where analysis can be coordinated without pooling raw partner data. [Zhang et al., 2024](https://doi.org/10.1016/j.asoc.2024.112475)

NIST's traceability meta-framework further emphasizes that useful traceability combines
linked records with trusted repositories, secure access, and event recording. [NIST IR 8536](https://csrc.nist.gov/pubs/ir/8536/ipd)

## Governance principles

A credible trust utility needs more than neutral branding. The programme will design for:

- independent governance and a transparent funding model;
- role-based access, purpose limitation, and data minimization;
- source provenance and data-quality standards;
- participant correction, challenge, and appeal rights;
- human review for consequential decisions;
- meaningful abstention when evidence is insufficient; and
- basic verification access that does not create a pay-to-participate barrier for small carriers.

The Global Legal Entity Identifier System is a useful governance analogue: it combines
standardized reference data, quality controls, and a challenge process under independent
stewardship. It is not a freight product, but it illustrates the qualities a trusted shared
utility needs. [GLEIF](https://www.gleif.org/en)

## Pilot approach

The recommended first pilot is deliberately narrow.

1. Recruit one carrier cohort, one broker or shipper cohort, and one or two facilities.
2. Agree on a minimum event vocabulary and the authoritative source for each record.
3. Establish permissions, retention rules, correction paths, and participant support.
4. Assemble adjudicated identity and facility-event examples before introducing models.
5. Run a limited federation experiment and report results by stakeholder role and fleet size.
6. Review legal, equity, and security findings before expanding the scope.

## What stakeholders can expect

By the end of the research and pilot-design phase, partners should have:

- a validated problem statement and source library;
- a clear view of legal, regulatory, funding, market, and standards context;
- a practical minimum architecture and governance model;
- a partner-value proposition rather than an assumption of voluntary data sharing;
- a fair-access and redress framework; and
- a decision-ready pilot plan with measurable success and failure conditions.

## Current boundaries and open questions

This is not yet a production platform, a legal standard, or a claim that a score can make
consequential decisions. It is a research programme to determine whether governed,
federated evidence infrastructure can deliver measurable value.

The following questions remain active and should be resolved with partners and subject
matter experts:

- Which data elements can be shared with clear reciprocal value and acceptable risk?
- Which organization or governance structure can credibly steward a neutral utility?
- What is the smallest viable pilot that produces an adjudicated evidence benchmark?
- How should the programme avoid increasing burden or false positives for small carriers?
- What legal review is required before any external duty-of-care or liability framing?

## Source note

This brief draws on the programme’s research library, including government sources, peer-
reviewed research, standards-related material, and quantified industry research. Current
evidence, uncertainties, and limitations are maintained in the underlying research record;
claims that remain unverified are not represented here as established facts.
