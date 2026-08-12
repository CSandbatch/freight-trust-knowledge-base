---
type: dataset
status: candidate
phase: phase-i
schema_version: 1.0.0
verification: confirmed
access: bulk download, CSV/JSON/XML via Socrata; no login, no API key, no agreement
licence: metadata licence field reads "unknown"; presumed public domain under 17 U.S.C. §105 but not stated — confirm, do not assume
updated: 2026-08-04
tags:
- type/dataset
- domain/identity
- domain/freight
- confidence/dataset
- audience/internal
- lifecycle/candidate
---
# FMCSA Company Census File

Real identity and registration seed records for carrier entity resolution.

- Access: public/open seed source.
- Fields: carrier identifiers, legal names, addresses, status, and temporal changes as available.
- Use: normalize entities and create time-aware identity cases.
- Limitation: it carries no labeled fraud or chameleon-carrier outcomes; expert adjudication is required.
- Linked experiment: [[experiment-e1-entity-resolution-and-identity-assurance]]
- Linked methods: [[method-deterministic-entity-matching]], [[method-probabilistic-entity-resolution]], [[method-graph-assisted-entity-resolution]].
