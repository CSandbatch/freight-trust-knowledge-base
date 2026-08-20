---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-20
updated: 2026-08-20
review_by: 2027-08-20
tags: [type/source, domain/federation, domain/security, domain/standards, confidence/primary, audience/internal, programme/e3, lifecycle/active]
---
# IETF RFC 8725 - JWT Best Current Practices

## Citation

IETF BCP 225 / RFC 8725, *JSON Web Token Best Current Practices*, February 2020:
<https://www.rfc-editor.org/rfc/rfc8725.html>.

## Supported proposition

Supports explicit algorithm verification, issuer/subject and audience validation, separation of
token types and defensive handling of claims and key/URL references. E3 uses these requirements to
test its JWT/JWKS fixture and reject permissive defaults.

## Limits

The BCP does not define Freight Trust roles, organizational membership, authorization policy,
token issuance operations or the NIST Policy Machine adapter.

Consumers: [[experiment-e3-federated-access-and-policy-enforcement]]
