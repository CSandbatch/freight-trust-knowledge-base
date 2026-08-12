---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-08
updated: 2026-08-08
review_by: 2027-08-08
tags:
- type/source
- domain/identity
- domain/standards
- confidence/primary
- audience/internal
- programme/e1
- lifecycle/active
---
# GLEIF — organizational identity separated from ownership relationships

## Citation

Global Legal Entity Identifier Foundation:

- *Level 1 Data: Who is Who*. <https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-1-data-who-is-who>
- *Level 2 Data: Who Owns Whom*. <https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-2-data-who-owns-whom>

Retrieved 2026-08-08.

## Why this is relevant

GLEIF is not a trucking authority and does not determine FMCSA identity. It is used only as a mature organizational-identity design analogue.

GLEIF explicitly separates:

- **Level 1** legal-entity reference data — the official name, registered address, jurisdiction/formational dates and other data answering “who is who”; and
- **Level 2** relationship data — direct and ultimate accounting parent relationships answering “who owns whom.”

This is a strong external sanity check on E1's architecture: an identity system should not collapse ownership relationships into entity identity.

## E1 consequence

The Freight Trust graph should represent the carrier legal person as a node and ownership/control/succession as separately typed relationships. That is consistent with both the U.S. motor-carrier statutory structure and a mature global organizational-identity system.

## Consumers

[[e1-carrier-identity-and-relationship-standard]] · [[e1-identity-ontology.yaml]]
