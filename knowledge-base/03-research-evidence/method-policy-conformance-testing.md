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

Represents each access-control test as a versioned policy, request, expected domain decision,
expected audit record, authority citation, and rationale, then executes engine-specific fixtures
through a tested decision adapter.

- Use: test permitted and disallowed partner, field, and purpose combinations in E3.
- Strength: repeatable structural test with explicit expected outcomes.
- Model boundary: NGAC/PML fixtures run on the NIST Policy Machine. XACML policies and
  requests run on an XACML PDP. A neutral project tuple can generate both lanes only after
  explicit semantic mapping; one lane does not certify the other.
- Decision mapping: map engine-native results to `permit`, `deny`,
  `permit-with-redaction`, `require-review`, and `abstain` explicitly. For XACML, redaction
  is a Permit plus a tested obligation enforced by the PEP; Indeterminate and NotApplicable
  require a predeclared fail-closed/review rule.
- Coverage: exhaust high-severity rule families; use risk-based covering arrays for the
  remaining attribute combinations; add boundaries, conflicts, malformed requests, and
  single-rule mutation tests. Report uncovered combinations.
- Oracle authority: every expected result records policy owner, authority or contract source,
  effective date, jurisdiction, version, reviewer, and uncertainty. Unresolved rules are routed
  to review and excluded from pass-rate denominators.
- Limitation: passing synthetic tests does not prove policy completeness, legality, or
  legitimacy in live operations.
- Sources: [[source-nist-access-control-guidance]], [[source-oasis-xacml-3-0]].
- Linked dataset: [[dataset-nist-policy-machine-xacml-cases]].
- Linked experiment: [[experiment-e3-federated-access-and-policy-enforcement]].
