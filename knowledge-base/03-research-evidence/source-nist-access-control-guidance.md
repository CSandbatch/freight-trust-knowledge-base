---
type: source
status: active
schema_version: 1.0.0
source_class: primary
verification: confirmed
accessed: 2026-08-18
updated: 2026-08-18
review_by: 2027-08-18
tags: [type/source, domain/federation, domain/security, confidence/primary, audience/internal, programme/e3, lifecycle/active]
---
# NIST ABAC definition, comparison, verification, and testing guidance

## Citation and verification

NIST SP 800-162 Rev. 1, *Guide to Attribute Based Access Control*,
<https://csrc.nist.gov/pubs/sp/800/162/upd2/final>; SP 800-178, *A Comparison of
Attribute Based Access Control Standards*, <https://csrc.nist.gov/pubs/sp/800/178/final>;
SP 800-192, *Verification and Test Methods for Access Control Policies/Models*,
<https://csrc.nist.gov/pubs/sp/800/192/final>. Final publication pages inspected 2026-08-18.

## Exact support

Supports typed subject/object/action/environment attributes, comparison of XACML and NGAC,
and systematic policy-model verification/test design including conflicts and combinatorial
coverage concerns.

## Limits and E3 relevance

The publications do not supply freight policy, legal authority, a complete oracle, an
implementation, or pass thresholds. Comparison does not make XACML and NGAC interchangeable.
E3 needs separate engine-native lanes or an explicitly verified translation and must report gaps.

Consumers: [[method-policy-conformance-testing]] · [[dataset-nist-policy-machine-xacml-cases]] · [[experiment-e3-federated-access-and-policy-enforcement]]
