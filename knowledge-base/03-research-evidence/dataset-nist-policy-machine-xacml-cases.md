---
type: dataset
status: candidate
phase: phase-i
schema_version: 1.0.0
verification: confirmed
access: project-authored cases executed against a pinned open-source policy engine
licence: project-defined case-corpus licence; NIST Policy Machine uses the NIST Software Licensing Statement
updated: 2026-08-18
tags:
- type/dataset
- domain/federation
- confidence/dataset
- audience/internal
- lifecycle/candidate
- domain/freight
---
# Freight Policy Decision Cases

Synthetic access-control test cases for governed federation.

- Status boundary: the NIST Policy Machine is confirmed software; the freight case corpus
  is to be built. A test convention is not itself a dataset.
- Neutral format: policy version, request, expected domain decision, expected audit record,
  rule/authority citation, reviewer, and rationale.
- Engine-specific fixtures: encode NGAC/PML cases for a pinned NIST Policy Machine lane.
  If an XACML lane is selected, encode actual XACML policies and requests and run them on a
  pinned XACML PDP. Do not call NGAC results XACML conformance.
- Use: test purpose limitation, denied access, audit capture, and correction propagation.
- Limitation: structural policy tests do not prove policy completeness, legal sufficiency,
  social legitimacy, privacy, or real-world partner participation.
- Sources: [[source-nist-access-control-guidance]], [[source-oasis-xacml-3-0]],
  [[source-nist-policy-machine]].
- Linked experiment: [[experiment-e3-federated-access-and-policy-enforcement]]
- Linked methods: [[method-policy-conformance-testing]], [[method-hash-chained-audit-logging]].
