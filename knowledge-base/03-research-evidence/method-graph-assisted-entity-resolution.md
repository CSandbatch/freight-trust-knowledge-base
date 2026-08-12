---
type: method
status: candidate
schema_version: 1.0.0
updated: 2026-08-08
tags:
- type/method
- lifecycle/candidate
- domain/freight
- domain/identity
- programme/e1
---
# Graph-Assisted Entity Resolution

Uses typed, time-bounded relationships among legal persons, registrations, identifiers, names,
addresses, owners, managers, insurers, vehicles, transactions, and other permitted evidence to
test whether relational context improves E1 resolution beyond row-level matching.

The graph is specifically prohibited from collapsing **relationship** into **identity**. Two
carriers may share owners, addresses, managers, equipment, insurance, or operational continuity
while remaining distinct legal persons.

## E1 constraints

- Node and edge semantics follow [[e1-identity-ontology.yaml]].
- Legal-person identity, FMCSA registrant continuity, operating authority, corporate succession,
  affiliation, substantial continuity, and regulatory disposition are separate objects/predicates.
- Relationship edges are time-bounded and source-attributed.
- Edges created after the feature cutoff are masked from the model even if later used to settle
  retrospective gold truth.
- Safety/enforcement/motive information is excluded from Task A graph features.
- No single weak edge (shared address/name/phone/owner/equipment/etc.) is dispositive.
- Graph leakage tests must detect whether a test entity is indirectly connected to training
  labels or future evidence.

## Evaluation

Primary evaluation is end-to-end with the graph method's frozen production candidate generator. A secondary **common-candidate-set** analysis gives C1-C3 the same broad candidate union to isolate the incremental value of relational/temporal reasoning.

Graph embeddings, degree/frequency statistics, high-degree suppression thresholds and any learned edge representations are fit on train/development/pre-cutoff structure only. Test/future graph structure cannot leak into learned representations.


Compare against deterministic and non-graph probabilistic conditions at matched precision,
coverage, and review burden. Report gains/losses by relationship type, fleet-size band, graph
degree, missingness, record age, and source combination. Explicitly audit false merges caused by
high-degree addresses, service providers, registered agents, common insurers, and family-owned
operations.

- Strength: can expose multi-hop conflicts and temporal continuity that field-by-field matching
  misses while preserving explainable evidence paths.
- Limitation: graph structure can amplify source bias, high-degree weak links, and label leakage;
  relationship inference must remain challengeable and provenance-bearing.
- Linked dataset: [[dataset-fmca-company-census-file]], [[dataset-fmca-registration-insurance-safety-records]], [[dataset-e1-adjudicated-carrier-identity-cases]].
- Linked experiment: [[experiment-e1-entity-resolution-and-identity-assurance]].
