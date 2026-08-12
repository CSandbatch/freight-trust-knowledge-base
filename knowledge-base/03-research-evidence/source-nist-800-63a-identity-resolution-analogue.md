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
# NIST SP 800-63A implementation resource — identity resolution as a context-bounded evidence problem

## Citation

National Institute of Standards and Technology, SP 800-63A implementation resource, *Identity Resolution and Evidence Collection*.

<https://pages.nist.gov/800-63-3-Implementation-Resources/63A/resolution/>

Retrieved 2026-08-08.

## Scope caveat

This NIST material concerns **individual identity proofing**, not organizational/carrier identity. It is therefore a methodological analogue only and cannot override FMCSA or state corporate authority.

## Useful principles

NIST frames identity resolution as resolving an applicant to one unique entity in a defined **population and context**, using the minimum necessary attributes. It distinguishes self-asserted information from evidence traceable to issuing sources, and states that conflicts among attributes can require additional information/evidence rather than a forced resolution.

## E1 consequence

- E1 must state the population and context of each identity claim.
- Observation claims must retain provenance to the issuing/authoritative source.
- Conflicting evidence should trigger `UNRESOLVED` or additional evidence collection, not automatic majority voting across fields.
- Collect only fields necessary for the scientific task; high-risk PII such as SSNs/EINs should not be added merely because historical GAO screening used them.

## Consumers

[[e1-carrier-identity-and-relationship-standard]] · [[e1-adjudication-decision-tree]]
