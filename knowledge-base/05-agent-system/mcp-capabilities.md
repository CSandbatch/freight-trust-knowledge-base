---
type: strategy-note
status: active
schema_version: 1.0.0
tags:
- type/strategy-note
- domain/knowledge-engineering
- domain/freight
- lifecycle/active
---
# MCP and Tooling Capability Contract

This document is a project specification, not an installation record. It separates tools
available in the current workspace from capabilities that require a configured connector
or human access.

## Available now

| Capability | Use | Guardrail |
|---|---|---|
| Web research | Discovery and primary-source verification | Cite direct sources; record access date for unstable claims. |
| Local filesystem | Read/write project artifacts | Preserve raw originals; write derived material only to working folders. |
| Markdown + Mermaid | Briefs, evidence, task log, diagrams | Diagrams trace to accepted evidence. |

## Recommended MCP capabilities

| Connector/capability | Why | Required before production use |
|---|---|---|
| CourtListener/RECAP or legal-research MCP | Opinions, dockets, citation verification | Confirm coverage, terms, and authoritative source links. |
| Federal Register / regulations.gov | Rulemaking, notices, comments, deadlines | Capture document IDs and publication dates. |
| NSF awards + Research.gov | Funding precedent and solicitation checks | Recheck current solicitation and submission rules. |
| Document repository/Drive | Team source discovery and internal evidence | Permission-scoped read access and provenance labels. |
| Structured evidence store | Claim IDs, freshness, audit trail, review queues | Schema, access control, and export policy. |

## Tool-selection rules

Use a primary public source where one exists. Use a legal connector for court claims,
government registries for regulatory claims, and peer-reviewed indexes/publisher pages for
scientific claims. Do not use a general web result as a substitute for a required official
record. Do not grant an agent outbound communication, external writes, or broad account
access merely to research a claim.
