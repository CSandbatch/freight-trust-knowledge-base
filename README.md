# Freight Trust Knowledge Base

Public, read-only research knowledge base for the Common Action Freight Trust and NSF SBIR programme. It contains working material and is not a submission-ready proposal or a source of legal, regulatory, or operational advice.

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

## Public browser and agent access

Build the manifest-authorized public browser locally with
`python scripts/build_site.py --site-url https://example.test/freight-trust/`, then serve the
generated directory with `python -m http.server 4173 --directory _site` and open
`http://127.0.0.1:4173/`. The public GitHub Pages deployment uses the same artifact. It
contains only exact entries from `knowledge-base/publication-manifest.json`; no directory,
tag, or search rule can publish an unlisted note. Run `python scripts/validate_site.py`
after each build. The release record in `_site/release.json` records the manifest hash,
source revision, working-tree state, and published content hashes.

The value passed to `--site-url` must be the eventual HTTPS public URL, including its
trailing slash, because canonical and social metadata use it. GitHub Pages uses the
`PUBLIC_SITE_URL` repository variable when set, otherwise its standard project URL. See
[`knowledge-base/09-meta/publication-runbook.md`](knowledge-base/09-meta/publication-runbook.md)
before approving new public material.

Agents can use the read-only gateway on a workstation or server with
`python scripts/kb_gateway.py --port 8787`. Its OpenAPI document is available at
`http://127.0.0.1:8787/openapi.json`; supported read endpoints are health, status, search,
read, and related. It binds only to loopback and has no write endpoint. A remote
write-capable MCP service remains intentionally separate, because it must authenticate and
submit pull requests rather than mutate canonical state.

The repository contains research, draft SBIR material, and unresolved commercial and legal
questions. Treat it as a transparent working record, not a public claim set or a
submission-ready proposal.
