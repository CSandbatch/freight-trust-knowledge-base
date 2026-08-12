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
- domain/regulatory
- confidence/primary
- audience/internal
- programme/e1
- lifecycle/active
---
# 49 CFR identity vocabulary — person, motor carrier, operating authority, and affiliates

## Citations

- 49 CFR § 390.5, *Definitions*. <https://www.law.cornell.edu/cfr/text/49/390.5>
- 49 CFR § 385.1003, *Definitions*. <https://www.law.cornell.edu/cfr/text/49/385.1003>

Retrieved 2026-08-08. Cornell LII renders the current eCFR text; controlling regulatory citations are the CFR sections themselves.

## What the definitions establish

Section 390.5 defines **person** broadly to include individuals, partnerships, associations, corporations, business trusts, and other organized groups. It defines for-hire and private motor carriers in terms of a person performing transportation.

Critically, the § 390.5 regulatory term **motor carrier** can, for purposes of the relevant subchapter, include the carrier's agents, officers, representatives, and certain employees. That makes “motor carrier” too broad to serve as E1's ontological equivalence class without qualification.

The section separately defines **operating authority** as registration under the specified statutes/regulations.

Section 385.1003 defines “reincarnated or affiliated motor carriers” for that subpart in terms of common ownership, management, control, or familial relationship. The scope is subpart-specific and must not be generalized into a universal legal definition of identity.

## E1 consequence

Use `LegalPerson` / `FMCSARegisteredPerson` as the core entity class, with a time-bounded `CarrierRole`. Do not use the broad regulatory phrase “motor carrier” as though it uniquely identified a legal entity in every context. Keep operating authority and affiliate relations as separate objects/edges.

## Consumers

[[e1-carrier-identity-and-relationship-standard]] · [[e1-identity-ontology.yaml]]
