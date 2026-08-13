---
type: brief
status: current
audience:
- client
- prospective-partner
- funder
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/brief
- domain/freight
- domain/identity
- domain/provenance
- domain/federation
- domain/adoption
- domain/orchestration
- domain/equity
- confidence/mixed
- audience/client
- audience/public
- lifecycle/current
tier: exhaustive
---
# Freight Trust Infrastructure

## Exhaustive programme brief

### Executive position

Freight decisions depend on fragmented information about counterpart identity,
credentials, operating events, and responsibility. This programme will test a federated
freight-trust layer that links authoritative evidence and permissioned events without
requiring participants to pool raw commercial data.

The first value proposition is narrower than a universal logistics platform: more
explainable counterparty verification, better facility-event records, and faster dispute
resolution. Fraud reduction, detention reduction, empty-mile reduction, and network-wide
orchestration are hypotheses to test, not promises to make in advance.

## Why now

ATRI estimated that 39.3% of stops involved detention in 2023, representing 135.9 million
lost hours, $3.6 billion in direct expenses, and $11.5 billion in productivity losses for
for-hire trucking. These are industry estimates, not a federal census, but they establish
a material measurement and coordination problem. [ATRI study record](https://trid.trb.org/View/2427471)

FMCSA continues to study detention measurement and carrier identity assurance. Its Motus
registration system demonstrates that identity and anti-fraud infrastructure is a current
public priority, not that a private system should replace official records. [FMCSA Motus notice](https://www.fmcsa.dot.gov/regulations/federal-register-documents/2026-08334)

In *Montgomery v. Caribe Transport II, LLC*, the Supreme Court held that the FAAAA does
not categorically preempt state-law negligent-selection claims against brokers. The ruling
cleared a preemption barrier but did not define a universal reasonable-care standard. The
programme supports evidence and workflow; it is not a legal safe harbor or legal
standard. [Opinion](https://www.law.cornell.edu/supremecourt/text/24-1238)

## Proposed system

1. **Carrier evidence graph:** connects identity, registration, insurance, safety, and
   relationship evidence with source, date, confidence, access, and correction metadata.
2. **Facility-event provenance:** records appointment, arrival, gate, dock, loading,
   departure, and delivery events while preserving uncertainty and source lineage.
3. **Governance and participation:** controls access, purpose, retention, correction,
   appeal, redress, and reciprocal benefits.
4. **Later orchestration:** tests whether governed evidence can support backhaul planning
   or dwell-sensitive coordination without shifting cost or risk to another actor.

The architecture is federated by default: source systems remain authoritative, raw data
stays with its owner where possible, and the shared layer exposes only permitted evidence
and derived records.

## Stakeholders and pushback

| Stakeholder | Value | Concern | Response |
|---|---|---|---|
| FMCSA / DOT | Traceable evidence aligned to public records | Implied delegated authority | Complement official systems |
| Brokers | Faster, defensible due diligence | Expanded liability or data duties | Evidence trails and human review |
| Legitimate carriers | Fairer identity and market access | False positives and opaque scoring | Abstention, correction, and appeal |
| Small carriers | Basic verification and lower friction | Cost, manual entry, exclusion | Fleet-size metrics and no paywall |
| Shippers / facilities | Reliability and event visibility | Commercial disclosure | Permissioned events and purpose limits |
| Insurers | Better-supported risk evidence | Data quality and claims implications | Provenance and auditability |
| Existing platforms | Interoperable evidence rails | Data-moat erosion | Open interfaces and complementarity |
| Associations / standards bodies | Reusable terminology | Premature standards claims | Align with ASTM F49 and NMFTA |
| Transportation lawyers | Better factual records | Overstated duty-of-care claims | Legal review and non-reliance language |

The strongest unresolved assumption is participation. No public evidence proves that
carriers, brokers, and facilities will voluntarily share commercially sensitive data with
a neutral third party. Participation has to be an experiment with concrete reciprocal
benefits, not a premise.

## Competitive and technical position

The market includes carrier verification, visibility, telematics, load matching, and
freight-data platforms. The identity prior-art boundary is broader than SCAC Verified alone. **FMCSA URSA** previously implemented automated risk-based chameleon/reincarnation screening and its lineage includes a prior SBIR Phase I; **FMCSA Motus** now separates individual identity proofing from company/business verification in the registration lifecycle; and **NMFTA SCAC Verified** adds natural-person identity verification at SCAC issuance/renewal for non-Class-8 carriers. The programme therefore does not claim novelty in automated chameleon screening, point-in-time identity verification, or registration-stage business verification. The proposed distinction is a neutral, federated, explainable evidence/provenance layer that resolves legal-person identity under incomplete/conflicting anchors while separately preserving registrant continuity, ownership/succession/operational relationships, regulatory dispositions, and later operational events — with calibrated uncertainty and contestability.
It should complement existing systems, not require their replacement.

Knowledge-graph research supports representing multi-party supply-chain relationships;
federated-learning research supports privacy-preserving analysis; NIST traceability work
supports combining linked records, trusted repositories, secure access, and event recording.
These sources back the technical direction but do not prove freight-pilot outcomes.
[Knowledge graphs](https://doi.org/10.1080/00207543.2022.2100841), [federated learning](https://doi.org/10.1016/j.asoc.2024.112475), [NIST traceability](https://csrc.nist.gov/pubs/ir/8536/ipd)

## Dataset and experiment backbone

The evaluation sequence is:

- **E1:** entity resolution and identity assurance against deterministic, probabilistic,
  and graph-assisted baselines.
- **E2:** facility-event provenance and dwell reconstruction using synthetic event traces,
  controlled anomalies, and optional permissioned validation.
- **E3:** federated access and policy enforcement using policy/request/expected-decision
  tests and tamper-evident audit logging.
- **E4:** participation and small-carrier equity using staged reciprocal offers.
- **E5:** later orchestration simulation comparing local and governed planning.

Every experiment has a baseline, metrics, controls, and go/no-go criteria. The benchmark
is itself a Phase I deliverable: an adjudicated identity/event evaluation asset remains
valuable even if a product hypothesis fails.

## Governance and redress

The trust layer must include independent stewardship, transparent funding, data
minimization, role- and purpose-based access, source provenance, retention limits,
correction and appeal rights, meaningful abstention, and human review for consequential
decisions. A participant challenge must be able to correct, annotate, or preserve a
disagreement rather than silently overwrite history.

Basic verification access should not become a pay-to-participate barrier for small carriers.
Outcomes must be reported by stakeholder role and fleet-size band.

## Recommended pilot

1. Recruit one carrier cohort, one broker or shipper cohort, and one or two facilities.
2. Select one bounded workflow: carrier onboarding or a facility-event dispute.
3. Agree on minimum fields, source authority, permissions, retention, and correction.
4. Build and adjudicate identity and event cases before model development.
5. Run E1-E4; defer E5 until feasibility and participation are demonstrated.
6. Expand only if evidence quality, adoption, safety, and equity thresholds are met.

## NSF SBIR/STTR framing

**Working title:** *Federated Evidence Graphs for Explainable Freight Identity and Facility-Event Verification*.

**Research question:** Can a federated evidence graph improve verification accuracy,
resolution time, and facility-event completeness compared with fragmented workflows while
preserving source control, correction, and fair access?

**Intellectual Merit:** evidence lineage, confidence and abstention, entity/event graph
reasoning, policy-based federation, and contestable records in freight.

**Broader Impacts:** lower administrative friction, fairer small-carrier access, reusable
interoperability patterns, and better evidence for freight safety and disputes.

**Commercial potential:** a bounded verification and event-evidence service that works with
existing platforms and creates a measured path toward coordination.

SBIR readiness depends on the current solicitation, applicant eligibility, PI, data rights,
pilot partners, and numeric Phase I thresholds being confirmed before submission.

## Decisions required

- Choose the first buyer and workflow.
- Confirm Common Action's legal form and SBIR/STTR route; Ellie Young is now the confirmed PI, with employment/effort eligibility still to document.
- Secure one real partner and one permissioned event source.
- Approve benchmark label and adjudication protocol.
- Set subgroup and correction-latency thresholds.
- Decide whether orchestration remains a Phase II application.

## Boundaries

This is not legal advice, a compliance certification, a universal risk score, or a claim
that a trust graph will automatically reduce fraud, detention, or empty miles. The project
exists to test those outcomes under governed conditions and report failure as carefully as
success.
