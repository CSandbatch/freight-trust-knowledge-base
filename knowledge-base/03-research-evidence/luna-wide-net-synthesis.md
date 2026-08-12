---
type: strategy-note
status: current
schema_version: 1.0.0
updated: '2026-08-01'
tags:
- type/strategy-note
- domain/freight
- domain/knowledge-engineering
- confidence/mixed
- audience/internal
- lifecycle/current
---
# Luna Wide-Net Synthesis — Evidence Expansion

**Orchestrator:** Terra

## Executive finding

The evidence supports a testable infrastructure question, not a promise that more shared
data automatically reduces fraud, detention, or empty miles. The defensible proposition
is that a federated, provenance-preserving freight trust layer may improve counterparty
verification and event visibility when it connects authoritative sources, minimizes
disclosure, and gives each participant a measurable benefit.

The system should be evaluated as a decision-support and data-governance intervention.

## Luna task results

| Task | Evidence supported | Limit |
|---|---|---|
| Operations | Detention is material, measurable, and safety-relevant enough to justify a pilot. | No proof that the proposed system reduces detention or empty miles at scale. |
| Identity | Existing public vetting has documented limits. | A new score must not decide eligibility or liability. |
| Data sharing | Governance, control, reciprocal value, and incentives matter. | “Neutral platform” alone is not a participation mechanism. |
| Technical | Knowledge graphs, provenance, and federation have credible precedents. | No production accuracy, fairness, or ROI evidence for this use case yet. |
| Equity | Small carriers have a concrete interest in transparency and a burden risk. | No quantified burden for this proposed system exists yet. |

## Quantitative anchors

- ATRI's 2023 detention analysis reports 39.3% of stops involved detention; for-hire
  trucking lost 135.9 million hours, $3.6B in direct expenses, and $11.5B in productivity
  losses. These are sector estimates rather than a federal census, but a credible pilot
  baseline. [ATRI study record](https://trid.trb.org/View/2427471).
- FMCSA treats detention measurement as an active research problem and distinguishes total
  dwell from delay attributable to loading/unloading. [FMCSA detention project](https://www.fmcsa.dot.gov/research-and-analysis/impact-driver-detention-time-safety-and-operations).
- BTS's Freight Mobility Initiative holds aggregated GPS-derived location/time data from
  roughly 350,000 unique truck tractors since October 2018. It demonstrates that
  large-scale freight measures are technically feasible and privacy-sensitive, not that
  its raw data is available for this programme. [BTS FMI](https://www.bts.gov/explore-topics-and-geography/topics/freight-transportation/trucking-movements-bts-freight-mobility).
- GAO documented historical limits in FMCSA's ability to identify freight carriers trying
  to evade detection through changed identities. [GAO-12-364](https://www.gao.gov/products/gao-12-364).

## Peer-reviewed and standards evidence

- Supply-chain knowledge graphs can represent and reason over multi-hop relationships;
  this is technical precedent, not proof of an operational outcome. [Brintrup et al.,
  2022](https://doi.org/10.1080/00207543.2022.2100841).
- A recent supply-chain KG framework shows how source-derived evidence can extend
  visibility beyond direct partners, but should not substitute for verified operational
  records. [AlMahri, Xu, and Brintrup, 2026](https://doi.org/10.1080/00207543.2025.2575841).
- Federated graph learning is a privacy-preserving technical option: it supports
  learning without pooling raw partner data, while leaving adoption and governance open.
  [Zhang et al., 2024](https://doi.org/10.1016/j.asoc.2024.112475).
- NIST's traceability meta-framework emphasizes trusted repositories, linked records,
  secure access, and event recording. [NIST IR 8536](https://csrc.nist.gov/pubs/ir/8536/ipd).

## Data-sharing conclusion

Data sharing requires a reciprocal, role-specific return. A peer-reviewed freight-service
platform study supports secure exchange of documents, transaction logs, and asset events;
a retail supply-chain study finds that clear incentives are needed because of privacy and
competitive concerns. [Freight platform study](https://link.springer.com/article/10.1007/s10257-022-00572-5), [retail study](https://doi.org/10.1108/IJOPM-07-2024-0560).

The European Mobility Data Space is a useful real-world model: a federated framework with
technical and governance dimensions rather than one central database. [European Commission](https://transport.ec.europa.eu/transport-themes/smart-mobility/creating-common-european-mobility-data-space_en).

Concrete pilot returns should be: faster verified onboarding, reduced duplicate
documentation, reciprocal facility-performance visibility, better insurance/broker
workflow, or contractual service-level benefits. The pilot must measure uptake and
retention by role and fleet size.

## Governance and equity

GLEIF shows the components of credible shared identity infrastructure: independent
governance, open standardized records, quality controls, and challenge/update mechanisms.
It is an analogue, not a freight solution. [GLEIF](https://www.gleif.org/en).

The programme should require: source provenance, access policies, participant correction
and appeal, no action solely on an automated indicator, no paywall for basic verification,
minimal new data entry, and false-positive remediation. Earlier FMCSA analysis estimated
that 99.1% of regulated carriers met applicable small-business standards, making a
small-entity impact assessment core design work. [GAO-16-401R](https://www.gao.gov/products/gao-16-401r).

## Falsifiable pilot hypotheses

| Hypothesis | Measure | Falsifier |
|---|---|---|
| Evidence graphs improve verification. | Resolution time; precision/recall against adjudicated cases; abstention rate. | No improvement over current workflow at matched error cost. |
| Provenanced events improve detention measurement. | Independent timestamp coverage; dispute time; agreement with ground truth. | Data is incomplete or biased enough not to improve agreement. |
| Federation is more acceptable than raw pooling. | Participation and retention by role; requested fields; rejection reasons. | No adoption or trust advantage. |
| Reciprocal value sustains participation. | Uptake under distinct benefit offers; net benefit by fleet segment. | Participation remains low after a concrete offer. |
| The system does not worsen small-carrier access. | Cost/time, false positives, appeals, and completion by fleet size. | Worse outcomes without mitigation. |

## Changes required to the programme

1. Reframe the Freight Trust Index as an explainable evidence graph with optional,
   challengeable indicators.
2. Separate work into entity/evidence resolution, facility-event provenance, and
   governance/incentive design.
3. Make federation and data minimization first-class hypotheses.
4. Replace industry-wide outcome promises with predeclared pilot measures and thresholds.
5. Treat the $7–16B annual fraud range as context until it passes a source-quality review.
6. Require legal/human review before any recommendation affecting eligibility, pricing,
   contracting, or liability.

## Residual gaps

No public evidence yet shows a federated U.S. freight trust graph reduces fraud or empty
miles; that is the proposed test. Direct small-carrier research, a properly adjudicated
benchmark, and legal expert validation remain required.

