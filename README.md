# Freight Trust Knowledge Base

Private, internal Obsidian knowledge base for the Common Action Freight Trust and NSF SBIR programme.

## Open the vault

Open `knowledge-base/` as an Obsidian vault, then begin with
[`00-home/start-here.md`](knowledge-base/00-home/start-here.md). The vault's own
[`README.md`](knowledge-base/README.md) is the canonical release overview.

## Working rules

- Treat `knowledge-base/` as the sole tracked source of truth.
- Follow the metadata, source, link, and archive controls in `knowledge-base/09-meta/`.
- Use the agent system's [routing guide](knowledge-base/05-agent-system/guiding-routes.md)
  before delegating work.
- Keep credentials and local session state out of Git. `.env` and Obsidian workspace files
  are intentionally ignored.

## Canonical-state workflow

`master` is the canonical remote state. Research and maintenance work starts from it,
uses an `agent/<area>/<run-id>` branch, runs `python scripts/validate_kb.py`, and is
submitted as a pull request. The portable agent contract and retrieval order live in
[`knowledge-base/05-agent-system/runtime/`](knowledge-base/05-agent-system/runtime/).
Operational work records are stored as atomic objects in
[`knowledge-base/06-team-memory/`](knowledge-base/06-team-memory/).

## Browser and agent access

Build the read-only browser locally with `python scripts/build_site.py`; open
`_site/index.html` to search and read the vault. A GitHub Actions workflow builds the
same artifact after each `master` update. GitHub Pages deployment is intentionally gated
behind the repository variable `ENABLE_GITHUB_PAGES=true`: the current private-repository
plan does not permit Pages, and this vault must not be made public to work around that.

Agents can use the read-only gateway on a workstation or server with
`python scripts/kb_gateway.py --port 8787`. Its OpenAPI document is available at
`http://127.0.0.1:8787/openapi.json`; supported read endpoints are health, status, search,
read, and related. It binds only to loopback and has no write endpoint. A remote
write-capable MCP service remains intentionally separate, because it must authenticate and
submit pull requests rather than mutate canonical state.

The repository is private because the vault contains internal research, draft SBIR material,
and unresolved commercial and legal questions. It is not a public claim set or a submission-ready proposal.
