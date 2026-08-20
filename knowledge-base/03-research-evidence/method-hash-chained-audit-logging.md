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
- Strength: under a declared trust model, a hash chain makes modification of an earlier block
  detectable because the following digest changes.
- Capture boundary: instrument the policy-enforcement point before and after the PDP and
  reconcile it against an independently generated request ledger. The selected Policy Machine
  emits EPP events only for Admin and Resource operations; engine events alone cannot prove
  capture of queries, authentication failures, malformed requests, timeouts, or other errors.
- Control boundary: test event selection, content/minimization, authoritative time, protection,
  nonrepudiation, retention, generation, truncation/rollback, key protection, and independent
  anchoring separately. Hash chaining alone supplies none of those properties.
- Privacy: log the minimum decision basis. Attribute values, identities, timing, and denial
  patterns can create personal or commercial leakage; protect detailed records and publish
  only approved summaries.
- Limitation: tamper evidence does not authenticate the requester, guarantee source truth,
  prevent a controller from truncating or rebuilding an unanchored chain, or provide
  confidentiality, availability, or nonrepudiation.
- Sources: [[source-nist-audit-and-privacy-controls]], [[source-nist-policy-machine]].
- Linked dataset: [[dataset-nist-policy-machine-xacml-cases]].
- Linked experiment: [[experiment-e3-federated-access-and-policy-enforcement]].
