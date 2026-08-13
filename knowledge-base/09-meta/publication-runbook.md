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

The public artifact is built only from the exact note and asset entries in
`publication-manifest.json`. It does not discover notes by directory, tag, search index,
or link traversal. A manifest entry is refused unless its frontmatter contains
`audience/public`, and it is refused when it is internal, draft, archive, or in a protected
working area. Protected areas include research evidence, SBIR, the agent system, team
memory, archive, and meta/control records.

The current allowlist is deliberately small: the public overview and the two existing
client notes that were already tagged `audience/public`. Adding an item is an external
publication decision, not a formatting change. Preserve internal notes in place; never
copy them into a public directory merely to make the build pass.

## Add or change a public note

1. Obtain the accountable content owner's approval and make sure the note is truly
   suitable for external reading. Check source freshness, evidence limits, privacy,
   contractual rights, and the absence of draft/review content.
2. Add `audience/public` to the source note only after that approval. Do not remove
   `audience/internal` to bypass the gate.
3. Add its exact source path and a stable lowercase URL slug to
   `publication-manifest.json`. Slugs are public URLs: changing one requires an approved
   redirect plan before release.
4. Resolve every wiki link to another manifest entry, remove it, or obtain approval for
   the target. The build fails on links to unpublished or missing notes.
5. For an image or other local asset, add one exact source-to-output mapping under
   `assets` in the manifest. The build rejects every local image not on that list.

## Pre-release check

Use the live HTTPS destination, including its final trailing slash:

```powershell
python scripts/validate_kb.py
python scripts/build_site.py --site-url https://public.example/
python scripts/validate_site.py
python -m unittest discover -s tests -p "test_*.py"
```

Review `_site/release.json` before upload. It is generated, not hand-authored, and records
the build timestamp, source revision, working-tree cleanliness, manifest checksum, exact
published source paths, URLs, and content checksums. A dirty working tree is a release
review signal, not a fact to edit out of the metadata.

GitHub Pages runs the public build and validator on `master`. Set the `PUBLIC_SITE_URL`
repository variable to an approved canonical URL when a custom domain is used; otherwise
the workflow uses GitHub's standard project URL. Do not deploy a manual artifact whose
release record or validation result has not been reviewed.

## Rollback and incident response

If a policy failure or exposure is found, stop the release, remove the affected note or
asset from the manifest in a reviewed change, rebuild, validate, and redeploy the corrected
artifact. Preserve the internal source record and document the incident through the normal
release-audit and decision controls. A public build failure is expected protection, not a
reason to broaden the allowlist or weaken a path check.
