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
# IETF RFC 8785 - JSON Canonicalization Scheme

## Citation

IETF RFC 8785, *JSON Canonicalization Scheme (JCS)*, June 2020:
<https://www.rfc-editor.org/rfc/rfc8785.html>.

## Supported proposition

Defines deterministic JSON serialization suitable for producing stable bytes before hashing E3
audit entries.

## Limits

Canonicalization alone does not provide capture completeness, authentication, confidentiality,
truth, append-only storage or protection against controller-led truncation/rebuilding.

Consumers: [[method-hash-chained-audit-logging]] -
[[experiment-e3-federated-access-and-policy-enforcement]]
