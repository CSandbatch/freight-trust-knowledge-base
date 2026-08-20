---
type: memory
status: candidate
id: mem-ft-000001
memory_type: semantic
memory_scope: shared
owner: memory-keeper
provenance:
  actor: user-supplied transcript
  run: null
  method: parsed and mapped against canonical E1 records
review:
  status: pending
  reviewer: null
write_policy: patch
schema_version: 1.1.0
updated: '2026-08-18'
tags:
- type/memory
- domain/knowledge-engineering
- domain/identity
- domain/regulatory
- programme/e1
- lifecycle/candidate
- audience/internal
---
# Memory — MEM-FT-000001: E1 carrier-identity design transcript

## Memory

A user-supplied design transcript dated **Saturday, August 8 at 11:35 AM** set out the
reasoning that led to the E1 carrier-identity definition work. The year is not present in
the transcript; **2026 is inferred** from the referenced vault state and adjacent dated
artifacts. The transcript was received for ingestion on 2026-08-18.

The design contribution was to reject a binary “same carrier” label and model several
different questions explicitly: legal-person identity, FMCSA registration continuity,
identifier assignment and claimed use, operating authority, trade identity, corporate and
operational relationships, and regulatory reincarnation or affiliation dispositions. It
also called for temporal assertions, source-aware evidence, an unresolved state, blinded
adjudication, adversarial review, and a pathological edge-case suite.

The transcript is **design-history provenance, not legal or factual authority**. It does
not replace the primary and methodological sources in the E1 claims ledger. Its proposed
agent roles, staffing assignments, prompts, labels, thresholds, and artifact names are
historical recommendations unless separately adopted in a canonical record.

## Source fingerprint

- Intake file: `pasted-text.txt` (external Codex attachment; intentionally not copied into
  the distributed vault)
- SHA-256: `6225D8FC01621EFF75BAD8AF191EBED5ADF4C3F90C9BA01EF2A2EF453F62F18F`
- Transcript timestamp as written: `Sat, Aug 8 at 11:35 AM`
- Ingestion date: `2026-08-18`
- Preservation rule: retain the fingerprint and this normalized mapping; do not treat the
  conversational prose as a citable authority.

## Parsed contribution and disposition

| Transcript proposal | Canonical disposition |
|---|---|
| Reject one binary “same carrier” target | Adopted and sourced in [[../03-research-evidence/e1-carrier-identity-and-relationship-standard]] and [[../03-research-evidence/e1-identity-definition-research-report]]. |
| Separate observations, persons, registrations, identifiers, authority, names, and relationships | Adopted and further normalized in [[../03-research-evidence/e1-identity-ontology.yaml]]. The current ontology controls when its vocabulary differs from the transcript. |
| Distinguish claimed USDOT use from authoritative assignment | Adopted in the standard, ontology, and [[../03-research-evidence/e1-identity-claims-ledger]]. |
| Make assertions temporal and source-aware | Adopted in the standard and ontology. |
| Separate identity resolution from relationship resolution | Adopted and expanded into Task A legal-person identity, Task B FMCSA registrant continuity, and Task C typed relationships. |
| Keep motive and safety history out of identity truth | Adopted as a benchmark safety rule; regulatory motive/disposition remains a separate layer. |
| Rank evidence, record conflicts, and allow `UNRESOLVED` | Adopted and sourced in the standard, decision tree, and claims ledger. |
| Use independent research and hostile evaluation loops | Executed in [[../03-research-evidence/e1-definition-freeze-review]] and subsequent conformance and academic-design reviews. |
| Test adversarial and pathological cases | Expanded into the 70-case [[../03-research-evidence/e1-edge-case-suite.csv]]. |
| Do not freeze with Critical findings open | Adopted as review governance; the initial findings and dispositions are recorded in the freeze review. |
| Assign named agents and reuse the sample prompts | Retained only as design history. The current agent roster and governance records control execution. |

## Canonical precedence and sourcing decision

The current E1 artifacts supersede the transcript where they differ. In particular, the
canonical model separates final FMCSA dispositions from review candidates, avoids treating
shared operational features as proof of legal identity, and uses a three-task benchmark
rather than the transcript's earlier two-task framing.

No new external source card was created during ingestion. Every material legal,
regulatory, identity, and evaluation proposition retained from the transcript is already
supported by the 16-source map and 64-claim ledger in the canonical research package. The
transcript itself supports only the historical fact that these ideas were proposed in the
design process.

## Evidence and linked objects

- [[../03-research-evidence/e1-identity-definition-research-report]] — authoritative
  research execution and source map.
- [[../03-research-evidence/e1-identity-claims-ledger]] — claim-level authority and
  confidence.
- [[../03-research-evidence/e1-carrier-identity-and-relationship-standard]] — controlling
  operational definition.
- [[../03-research-evidence/e1-identity-ontology.yaml]] — controlling machine-readable
  vocabulary.
- [[../03-research-evidence/e1-adjudication-decision-tree]] — adjudication procedure.
- [[../03-research-evidence/e1-definition-freeze-review]] — hostile review and finding
  dispositions.
- [[../03-research-evidence/e1-edge-case-suite.csv]] — adversarial case coverage.

## Review disposition

**Pending memory-keeper review.** Accept as design-history provenance if the fingerprint,
date inference, and canonical mappings are confirmed. Acceptance must not promote the
transcript into a legal source or reopen settled vocabulary without a new evidence-backed
decision.
