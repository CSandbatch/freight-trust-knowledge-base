---
type: strategy-note
status: active
owner: research-orchestrator-plus-platform-owner
schema_version: 1.1.0
updated: '2026-08-20'
review_by: '2026-11-20'
tags:
- type/strategy-note
- domain/knowledge-engineering
- domain/data-science
- domain/freight
- lifecycle/active
- confidence/mixed
- audience/internal
---
# Experiment MCP and Tooling Setup

This is the recommended agent-access layer for building E1-E5. It is deliberately smaller than
the runtime itself. Local libraries, CLIs and AWS jobs perform experiments; MCP supplies current
documentation, repository/CI context, browser verification and narrowly controlled operational
actions.

## Recommended MCP profile

| Server | Initial mode | Purpose | Boundary |
|---|---|---|---|
| OpenAI Developer Docs | Read-only, enabled | Current Codex, MCP and OpenAI API documentation | Documentation only; it does not call the API |
| GitHub official MCP | Read-only toolsets first | Repository, PR and Actions inspection | Enable write tools only for an authorized publish task; use least-privilege OAuth/PAT |
| AWS Knowledge/Documentation | Read-only, enabled | Current AWS docs, APIs and architecture guidance | Documentation is not evidence of account permission or deployed state |
| AWS managed MCP or selected AWS Labs servers | Disabled until an AWS work packet names services/IAM/budget | Auditable resource inspection and, later, bounded operations | Separate read and write profiles; require approval for mutation; CloudTrail is supplementary, not the experiment run ledger |
| Playwright MCP | Isolated, local/site hosts allowlisted | Live Knowledge Atlas and future experiment-console checks | Browser content is untrusted; no partner credentials or unrestricted browsing |
| Freight Trust run MCP (future project server) | Local STDIO, read-only initially | Validate manifests, inspect run packets, resolve public source IDs and compare schemas | Must never return secrets/raw restricted rows or launch a final run without a signed gate token |

Codex supports local STDIO and streamable HTTP servers, project-scoped `.codex/config.toml`,
environment-variable forwarding, per-server/per-tool allowlists and approval modes. The official
documentation recommends putting cross-tool constraints in the server `instructions` field and
keeping its first 512 characters self-contained. See [Codex MCP documentation](https://learn.chatgpt.com/docs/extend/mcp?surface=cli).

OpenAI also hosts a public, read-only documentation server at
`https://developers.openai.com/mcp`; it searches official OpenAI developer documentation and does
not call the OpenAI API. See [OpenAI Docs MCP](https://learn.chatgpt.com/learn/docs-mcp).

## Project configuration example

Treat this as a reviewed template, not a credential file. Exact server versions and tool names
must be pinned during implementation.

```toml
[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"
required = false
default_tools_approval_mode = "approve"

[mcp_servers.githubReadOnly]
# Server-side headers limit toolsets and remove write tools.
url = "https://api.githubcopilot.com/mcp/"
http_headers = { "X-MCP-Toolsets" = "repos,pull_requests,actions", "X-MCP-Readonly" = "true" }
auth = "oauth"
required = false
default_tools_approval_mode = "approve"

[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@PINNED_VERSION", "--headless", "--isolated"]
required = false
default_tools_approval_mode = "prompt"

# Add one current AWS documentation/knowledge server after platform review.
# Keep AWS mutation servers disabled until the work packet names an IAM role,
# services, region, resource tags, spend ceiling, teardown and approval owner.
# A GitHub write-capable publish profile is likewise stored separately and is not
# present in this default project configuration.
```

The official GitHub MCP server supports repository and Actions inspection, toolset selection,
server-enforced read-only mode and a separate lockdown mode. Approval mode controls prompting; it
does not turn a write-capable server into a read-only server. The official Playwright MCP server supports isolated
browser profiles and warns that it is not a security boundary. AWS Labs now recommends the AWS
managed MCP/Agent Toolkit direction for secure auditable AWS operations and individual servers
instead of the deprecated Core proxy. Sources: [GitHub MCP](https://github.com/github/github-mcp-server),
[Playwright MCP](https://github.com/microsoft/playwright-mcp), and
[AWS MCP servers](https://github.com/awslabs/mcp).

## Future Freight Trust run server

Start with these read-only tools:

- `list_protocols()` and `get_protocol_version(experiment)`;
- `validate_registered_manifest(artifact_id)` for a manifest already registered beneath a
  configured public/development artifact root;
- `resolve_public_source(source_id)` with source-card and retrieval metadata;
- `inspect_run(run_id)` returning hashes, state, gates and redacted summaries;
- `compare_interface_versions(producer, consumer)`; and
- `verify_artifact_hash(run_id, artifact_id)`.

Only after threat review add `launch_dry_run`. Do not expose `launch_pilot`, `open_holdout`, raw
row retrieval, arbitrary shell, generic AWS execution, unrestricted SQL or secret-reading tools.
Final-test opening remains a human authorization recorded outside the MCP conversation.

The server must never accept a caller-supplied filesystem path. Registration resolves canonical
paths beneath explicit allowlisted public/development roots, rejects symlinks and junctions that
escape those roots, limits size and permitted extensions, parses against the declared schema
before returning a bounded result, and emits non-reflective errors that do not echo file content.
Acceptance tests cover traversal, symlink/junction escape, oversized and wrong-type files,
malformed manifests, unknown IDs, and a secret-canary file outside every allowed root.

## Runtime tools by experiment

| Experiment | Candidate implementation tools | Required wrapper checks |
|---|---|---|
| E1 | Python, DuckDB/Parquet, Splink, graph library, scikit-learn calibration/metrics; optional pinned hosted or open-weight LLM adapter | Entity/time split isolation, evidence-ID validation, cluster consistency, calibrated abstention, model/provider manifest |
| E2 | Pinned OpenEPCIS generator and schema validator, Python event pipeline, process/event metrics | EPCIS/CBV profile validation, canonical/observability/source separation, seeded injection, privacy release tests |
| E3 | NIST Policy Machine implementation lane, separate XACML 3.0 engine lane, JWT/JWKS test issuer, append-only request ledger | Neutral decision algebra, adapter parity, PEP enforcement, mutation tests, independent audit reconciliation |
| E4 | Institutionally approved survey system, private encrypted store, statistical package, disclosure-control/export checker | No public row data, assignment/exposure accounting, consent version, withdrawal/correction flow, small-cell review |
| E5 | Python, OR-Tools or another pinned solver, simulation library, DuckDB/Parquet | Hand-worked feasibility oracle, HOS state machine, benchmark convention/checksum, common random numbers, independent route checker |

Centralize environment locks, JSON Schema/Pydantic contracts, structured logging, content hashing,
seed handling and run-packet validation in one shared package. Keep experiment estimators and
domain semantics in their owning modules.

## AWS execution profile

Use local/CI fixture runs first. For cloud runs, prefer short-lived IAM roles, KMS-encrypted and
versioned S3, immutable container digests in ECR, AWS Batch or Step Functions only where the job
graph needs them, CloudWatch metrics/logs, CloudTrail for account activity, Secrets Manager for
provider secrets, and explicit cost tags/budgets. Run
`.\.venv\Scripts\python.exe scripts\check_runtime.py --live` before provider-dependent work,
then test service-specific permissions separately. STS success alone is not authorization.

## Approval policy

- Documentation/search tools: auto or approve when read-only.
- Repository and CI reads: approve; repository writes: prompt on every write-capable tool.
- Browser: prompt, isolated profile, explicit hosts.
- AWS reads: prompt under a named read role; AWS writes: disabled until a reviewed work packet.
- Partner/private data: no general MCP access.
- Hosted inference: only approved fields, exact model/provider route and a complete request manifest.

## Related

[[03-research-evidence/e1-e5-build-readiness-and-run-contract]] -
[[03-research-evidence/aws-experiment-execution-and-findings-plan]] - [[mcp-capabilities]] -
[[runtime/mcp-interface]]
