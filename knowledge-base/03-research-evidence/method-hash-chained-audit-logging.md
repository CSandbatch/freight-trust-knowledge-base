---
type: method
status: candidate
schema_version: 1.0.0
tags:
- type/method
- lifecycle/candidate
- domain/freight
---
# Hash-Chained Audit Logging

Records each access request, purpose, decision, requester, and timestamp in an append-only chain so later alteration is detectable.

- Use: test audit capture and tamper evidence in E3.
- Strength: creates a verifiable access history without centralizing raw partner data.
- Limitation: tamper evidence does not guarantee the underlying request or source data was truthful.
- Linked dataset: [[dataset-nist-policy-machine-xacml-cases]].
- Linked experiment: [[experiment-e3-federated-access-and-policy-enforcement]].
