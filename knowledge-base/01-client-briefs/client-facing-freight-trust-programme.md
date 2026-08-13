---
type: brief
status: current
audience:
- website
- prospective-partner
- industry-stakeholder
schema_version: 1.0.0
updated: 2026-08-01
tags:
- type/brief
- domain/freight
- domain/identity
- domain/provenance
- domain/federation
- confidence/secondary
- audience/public
- lifecycle/current
tier: intermediate-web-copy
---
# Freight Trust Infrastructure

## Building better evidence for freight decisions

Freight decisions rely on information spread across carriers, brokers, shippers,
facilities, insurers, regulators, and technology platforms. When that information is
fragmented or difficult to challenge, verification slows down, operating events become
disputed, and responsibility is harder to establish.

We are developing a **federated freight-trust infrastructure**: a shared evidence layer
that links authoritative identity and credential records with permissioned operating
events, while participants keep control of their raw commercial data.

### What it does

- More explainable carrier and counterparty verification.
- Traceable appointment, arrival, dock, loading, and departure events.
- Better evidence for detention and service disputes.
- Correction, appeal, and human review when records are incomplete or wrong.
- A future path toward cross-actor coordination and backhaul planning.

The programme is intentionally evidence-led. It does not assume that a new platform will
automatically reduce fraud, detention, or empty miles. Those are outcomes to measure.

## Why now

ATRI estimated that 39.3% of stops involved detention in 2023, representing 135.9 million
lost hours and $11.5 billion in productivity losses. [ATRI study record](https://trid.trb.org/View/2427471)
FMCSA is modernizing carrier registration and anti-fraud capabilities through its
[Motus registration system](https://www.fmcsa.dot.gov/regulations/federal-register-documents/2026-08334).
The Supreme Court's [*Montgomery v. Caribe* decision](https://www.law.cornell.edu/supremecourt/text/24-1238)
also made broker negligent-selection claims more consequential without defining a universal
standard of reasonable care.

These developments point to a practical need: better evidence, clearer provenance, and
governed workflows that support human decisions without pretending to be a legal standard.

## How the programme works

1. Build a carrier evidence graph from authoritative records.
2. Model facility events with source, timestamp, confidence, and correction metadata.
3. Test federated access, purpose limits, and auditability.
4. Measure participation and burden across large and small carriers.
5. Expand toward coordination only if the evidence and governance tests pass.

The first pilot should be deliberately narrow: one carrier cohort, one broker or shipper
cohort, and one or two facilities. The initial workflow should be carrier onboarding or a
facility-event dispute, not a promise to optimize the entire freight network at once.

## Built for trust

The system is designed around source authority, data minimization, role-based access,
purpose limitation, correction and appeal, meaningful abstention, and human review. Basic
verification should remain accessible to small carriers without creating a new paywall or
manual-entry burden.

A dedicated benchmark and experiments plan covers identity resolution, event provenance,
policy enforcement, participation, and later orchestration.

## Scope of the claim

The goal is to establish whether a neutral, federated evidence layer can produce measurable
improvements for real participants while preserving privacy, contestability, and fair
access. That is a deliberately smaller claim than transforming freight. If the evidence
supports it, the programme can move from verification and dispute evidence toward broader
coordination.
