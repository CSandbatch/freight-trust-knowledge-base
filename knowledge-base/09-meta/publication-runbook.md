---
type: policy
status: active
owner: knowledge-architecture
version: 1.0.0
schema_version: 1.0.0
updated: '2026-08-13'
tags:
- type/policy
- domain/knowledge-engineering
- lifecycle/active
- audience/internal
---
# Public publication runbook

## Boundary

The public artifact is the **complete versioned vault**: every Git-tracked file beneath
`knowledge-base/` receives one stable reader or artifact page and one byte-identical raw
download. The compiler does not use an approval allowlist, a directory denylist, or
frontmatter values as publication gates.

`publication-manifest.json` now documents that inclusive policy and site metadata. It is
itself published as an artifact; it does not list approved notes. `audience`, `status`,
`type`, `confidence`, `verification`, `draft`, `archive`, and lifecycle values remain
important context in the reader, catalog, search, and graph. They never hide a tracked
vault artifact.

The boundary deliberately excludes only material that is not vault corpus: ignored or
untracked workstation state, `.env` files and credentials, and files outside
`knowledge-base/`. If a sensitive artifact must not be public, move or redact it in the
source repository before the release; do not attempt to bypass the corpus compiler with a
new allowlist rule.

## Add or change a public record

1. Add or update the source under `knowledge-base/` and keep its metadata truthful.
   `draft`, `candidate`, `planned`, `internal`, source-class, and verification markers are
   useful disclosures, not reasons to suppress the record.
2. Keep all internal `[[wikilinks]]` resolvable. A link may target a Markdown note,
   Mermaid file, YAML, CSV, JSON/Obsidian configuration, or another artifact. Heading
   anchors must identify an actual target heading.
3. Do not add secrets, private keys, or local environment state to the vault. The build
   deliberately fails on credential-like filenames rather than silently omitting them.
4. Stable portal routes derive from source paths. Keep paths deliberate; a rename changes
   a public route and should receive a redirect plan if it has already been shared. The
   `.obsidian/` vault-profile files are the one Pages compatibility exception: their
   source/provenance path remains `.obsidian/...`, while their byte-identical public raw
   downloads use `raw/vault-profile/...` because GitHub Pages cannot serve hidden URL
   segments.

## Pre-release check

Use the live HTTPS destination, including its final trailing slash:

```powershell
python scripts/validate_kb.py
python scripts/build_site.py --site-url https://public.example/
python scripts/validate_site.py
python -m unittest discover -s tests -p "test_*.py"
```

Review `_site/release.json` and `data/artifact-registry.json` before upload. They are
generated, not hand-authored, and record the source inventory, page/raw routes, hashes,
formats, graph counts, source revision, and working-tree state. A dirty working tree is a
release review signal, not a fact to edit out of the metadata.

GitHub Pages runs the public build and validator on `master`. Set the `PUBLIC_SITE_URL`
repository variable to an approved canonical URL when a custom domain is used; otherwise
the workflow uses GitHub's standard project URL. Do not deploy a manual artifact whose
release record or validation result has not been reviewed.

## Rollback and incident response

If an exposure is found, stop the release, move/redact the affected source through a
reviewed change, rebuild, validate, and redeploy the corrected artifact. Preserve a
properly controlled internal record outside the public vault if needed, and document the
incident through the normal release-audit and decision controls. Do not weaken raw-hash,
path-containment, link-resolution, or rendered-page safety checks.
