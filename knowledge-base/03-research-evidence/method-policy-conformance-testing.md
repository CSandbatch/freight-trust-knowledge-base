---
type: method
status: candidate
schema_version: 1.0.0
tags:
- type/method
- lifecycle/candidate
- domain/freight
- domain/federation
---
# Policy Conformance Testing

Represents each access-control test as a policy, request, expected decision, and audit expectation, then executes the suite against the policy engine.

- Use: test permitted and disallowed partner, field, and purpose combinations in E3.
- Strength: repeatable structural test with explicit expected outcomes.
- Limitation: passing synthetic tests does not prove policy completeness in live operations.
- Linked dataset: [[dataset-nist-policy-machine-xacml-cases]].
- Linked experiment: [[experiment-e3-federated-access-and-policy-enforcement]].
