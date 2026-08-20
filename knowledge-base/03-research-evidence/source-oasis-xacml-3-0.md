---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-20
updated: 2026-08-20
review_by: 2027-08-18
tags: [type/source, domain/federation, domain/standards, confidence/primary, audience/internal, programme/e3, lifecycle/active]
---
# OASIS XACML 3.0 standard and conformance-test boundary

## Citation and verification

OASIS, *eXtensible Access Control Markup Language (XACML) Version 3.0*, approved
2013-01-22, <https://www.oasis-open.org/standard/xacmlv3-0/> and
<https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-en.html>. OASIS committee test
notice: <https://www.oasis-open.org/committees/xacml/ConformanceTests/ConformanceTests.html>.
Inspected 2026-08-18.

## Exact support

Defines XACML request/policy/response semantics and native decisions Permit, Deny,
Indeterminate, and NotApplicable, plus obligations/advice handled through an enforcement path.
The current complete Errata 01 artifact is dated 2017-07-12.

## Limits and E3 relevance

The cited committee-test page is for XACML 1.1 and explicitly is not a full conformance test. It
is not a 3.0 corpus and cannot support certification. XACML cases
do not execute natively on the NIST Policy Machine. `permit-with-redaction`, `require-review`,
and `abstain` are project outcomes requiring an explicit mapping; redaction requires a tested
Permit obligation and PEP enforcement.

Consumers: [[method-policy-conformance-testing]] · [[dataset-nist-policy-machine-xacml-cases]] · [[experiment-e3-federated-access-and-policy-enforcement]]
