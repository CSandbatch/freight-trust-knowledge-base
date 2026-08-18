---
type: moc
area: team-memory
status: active
owner: memory-keeper
schema_version: 1.1.0
updated: '2026-08-18'
tags:
- type/moc
- domain/knowledge-engineering
- domain/freight
- lifecycle/active
- audience/internal
---
# Team Memory MOC

Operational and episodic memory for the Freight Trust team. This folder records what
happened, who owns the next action, and what an agent or collaborator can safely resume.
It complements durable evidence in `03-research-evidence/`, procedures in
`05-agent-system/`, and institutional decisions in `09-meta/`.

## Memory objects

- [[mem-ft-000001-e1-carrier-identity-design-transcript]] — candidate design-history
  provenance for the E1 carrier-identity definition work.
- [[templates/agent-run-template]] — reproducible execution record.
- [[templates/handoff-template]] — transfer of an incomplete or reviewed work item.
- [[templates/meeting-template]] — meeting record with decisions and actions.
- [[templates/task-template]] — bounded task packet.
- [[templates/memory-template]] — candidate or accepted shared memory.

## Operating rules

1. Write one object per run, task, handoff, meeting, or memory; do not append to a shared
   prose log for new work.
2. Agent-derived memory begins `candidate` with provenance and review state.
3. Link a record to its source, experiment, decision, and predecessor where applicable.
4. Promote only reviewed records. Derived retrieval indexes are disposable and rebuilt from Git.

## Related

[[05-agent-system/guiding-routes]] · [[09-meta/kb-schema]] · [[09-meta/decision-log]] · [[03-research-evidence/run-log]]
