# Freight Trust Knowledge Base

Public, read-only research knowledge base for the Common Action Freight Trust and NSF SBIR programme. It contains working material and is not a submission-ready proposal or a source of legal, regulatory, or operational advice.

## Open the vault

Open `knowledge-base/` as an Obsidian vault, then begin with
[`00-home/start-here.md`](knowledge-base/00-home/start-here.md). The vault's own
[`README.md`](knowledge-base/README.md) is the canonical release overview.

## Working rules

- Treat `knowledge-base/` as the sole tracked source of truth.
- Follow the metadata, source, link, and archive controls in `knowledge-base/09-meta/`.
- Use the root [AGENTS.md](AGENTS.md) as the orchestration contract. Callable project
  personas live in [`.codex/agents/`](.codex/agents/), outside the public vault.
- Keep credentials and local session state out of Git. `.env` and Obsidian workspace files
  are intentionally ignored.

## Canonical-state workflow

`master` is the canonical remote state. Research and maintenance work starts from it,
uses an `agent/<area>/<run-id>` branch, runs `python scripts/validate_kb.py`, and is
submitted as a pull request. Portable Git and retrieval contracts remain documented in
[`knowledge-base/05-agent-system/runtime/`](knowledge-base/05-agent-system/runtime/), while
the executable persona factory lives at [`.codex/agents/`](.codex/agents/).
Operational work records are stored as atomic objects in
[`knowledge-base/06-team-memory/`](knowledge-base/06-team-memory/).

## Local AWS and OpenRouter runtime

Create a repository-local environment and install the deterministic site dependencies:

```powershell
python -m venv .venv  # bootstrap exception; use the venv interpreter afterward
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env  # only when .env does not already exist
```

After `.venv` exists, use `.\.venv\Scripts\python.exe` for every repository Python
command. The root `AGENTS.md` makes this mandatory for the orchestrator and all personas.

Populate `.env` with either an AWS profile or an SDK credential pair, an AWS region, a
dedicated `OPENROUTER_API_KEY`, and an explicit `OPENROUTER_MODEL`. Do not store AWS
console usernames, passwords, or sign-in URLs in application environment files. For
deployed AWS workloads, prefer an attached IAM role or workload identity over static keys.

Run the secret-safe configuration audit from the local interpreter. Add `--live` to make
read-only AWS STS and OpenRouter key-metadata requests:

```powershell
.\.venv\Scripts\python.exe scripts\check_runtime.py
.\.venv\Scripts\python.exe scripts\check_runtime.py --live
```

The checker never prints credential values, account IDs, ARNs, or OpenRouter key metadata.

The public vault now carries the experiment implementation boundary and proposed MCP profile:
[`E1-E5 Build Readiness and Run Contract`](knowledge-base/03-research-evidence/e1-e5-build-readiness-and-run-contract.md)
and [`Experiment MCP and Tooling Setup`](knowledge-base/05-agent-system/experiment-mcp-and-tooling-setup.md).

## Public browser and agent access

Build the complete public Knowledge Atlas locally with
`python scripts/build_site.py --site-url https://example.test/freight-trust/`, then serve the
generated directory with `python -m http.server 4173 --directory _site` and open
`http://127.0.0.1:4173/`. The static portal includes the editorial Atlas home, full-text
Explore library, Obsidian-style global/local graph, collection and experiment hubs, a
reader for every Markdown note, artifact viewers, and byte-identical raw downloads.

The compiler discovers every **Git-versioned** file under `knowledge-base/`; draft,
archive, audience, confidence, and verification values are rendered as context rather than
publication exclusions. `.env` files, credentials, ignored local state, and non-vault files
are not source material. Run `python scripts/validate_site.py --check-deterministic` after
each build. The generated `release.json`, `data/artifact-registry.json`, and
`data/graph.json` record the exact source-to-output release.

The value passed to `--site-url` must be the eventual HTTPS public URL, including its
trailing slash, because canonical and social metadata use it. GitHub Pages uses the
`PUBLIC_SITE_URL` repository variable when set, otherwise its standard project URL. See
[`knowledge-base/09-meta/publication-runbook.md`](knowledge-base/09-meta/publication-runbook.md)
for the full corpus/release contract.

Agents can use the read-only gateway on a workstation or server with
`python scripts/kb_gateway.py --port 8787`. Its OpenAPI document is available at
`http://127.0.0.1:8787/openapi.json`; supported read endpoints are health, status, search,
read, and related. It binds only to loopback and has no write endpoint. A remote
write-capable MCP service remains intentionally separate, because it must authenticate and
submit pull requests rather than mutate canonical state.

The repository contains research, draft SBIR material, and unresolved commercial and legal
questions. Treat it as a transparent working record, not a public claim set or a
submission-ready proposal.
