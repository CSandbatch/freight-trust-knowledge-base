---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-20
updated: 2026-08-20
review_by: 2027-02-18
tags: [type/source, domain/federation, domain/software, domain/security, confidence/primary, audience/internal, programme/e3, lifecycle/active]
---
# NIST Policy Machine core and PDP software

## Citation and verification

NIST, `policy-machine-core` and `policy-machine-pdp`, official repositories inspected
2026-08-18: <https://github.com/usnistgov/policy-machine-core>,
<https://github.com/usnistgov/policy-machine-pdp>, and repository license
<https://github.com/usnistgov/policy-machine-core/blob/main/LICENSE.md>.

## Exact support

Official code/docs support an NGAC/PML implementation lane. The PDP documents `none` and JWT
authentication, including JWKS/issuer/audience configuration, and a sandbox that bypasses
administrative checks. The documented event path emits EPP events for Admin and Resource
operations; Query operations do not emit them.

Current inspected heads are Policy Machine core
`2df53ff1e473dc511c647be4f123cea1886d5c96` and PDP
`a10c01804b79f6c8e9f8f6aaf942223f47da795b`, both dated 2026-08-11; core identifies
`4.0.1-rc.1`. These are qualification candidates, not an accepted stable experiment runtime.

## Limits and E3 relevance

Official software documentation is authoritative only about this implementation. `none` auth
trusts headers and is not an evaluation security control; sandbox use invalidates an enforcement
claim. Engine events cannot prove all-request capture. E3 must pin versions, validate JWT and
subject binding, instrument a PEP, and reconcile an independent request ledger. Issuer/audience
checks are optional in the software configuration and therefore mandatory explicit E3 settings;
issuer-signed claims are not independent proof of organizational membership.

Consumers: [[dataset-nist-policy-machine-xacml-cases]] · [[method-hash-chained-audit-logging]] · [[experiment-e3-federated-access-and-policy-enforcement]]
