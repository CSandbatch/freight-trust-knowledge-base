"""Regression tests for the inclusive Freight Trust Knowledge Atlas compiler."""

from __future__ import annotations

import hashlib
import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from build_site import BuildError, build, normalise_path
from validate_site import validate


FRONTMATTER = """---
type: {kind}
status: {status}
updated: '2026-08-14'
tags:
- type/{kind}
- audience/{audience}
- lifecycle/{status}
---
"""


class KnowledgeAtlasTests(unittest.TestCase):
    def fixture(self, directory: pathlib.Path) -> tuple[pathlib.Path, pathlib.Path]:
        root = directory / "knowledge-base"
        (root / "00-home").mkdir(parents=True)
        (root / ".obsidian").mkdir()
        (root / "00-home" / "start-here.md").write_text(
            FRONTMATTER.format(kind="home", status="active", audience="internal")
            + """# Welcome

This is a complete public working record. [[draft#A heading|Open the draft]] and [[diagram.mmd]].

> [!IMPORTANT] Provenance first
> Use the raw download when auditing exact source bytes.

- [x] Published
- [ ] Not yet peer reviewed

```mermaid
flowchart LR
  A[Source] --> B[Atlas]
```

<script>alert('source html must not execute')</script>
""",
            encoding="utf-8",
        )
        (root / "draft.md").write_text(
            FRONTMATTER.format(kind="draft", status="draft", audience="internal")
            + """# Working draft

## A heading

Private working note text is intentionally still published with a draft badge.
""",
            encoding="utf-8",
        )
        (root / "diagram.mmd").write_text("flowchart TD\n  A[Evidence] --> B[Decision]\n", encoding="utf-8")
        (root / "cases.csv").write_text("case,status\nC1,pass\nC2,review\n", encoding="utf-8")
        (root / "ontology.yaml").write_text("entities:\n  - carrier\n", encoding="utf-8")
        (root / ".obsidian" / "graph.json").write_text('{"repulseStrength": 10}', encoding="utf-8")
        # This historic manifest is source material, not a publication allowlist.
        (root / "publication-manifest.json").write_text('{"notes": ["start-here.md"], "mode": "legacy"}', encoding="utf-8")
        return root, directory / "site"

    def test_every_fixture_artifact_has_page_raw_hash_and_search_graph_membership(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root, out = self.fixture(pathlib.Path(temporary))
            release = build(root, None, out, "https://example.test/freight-trust/", source_date_epoch=0)
            self.assertEqual(release["source_artifact_count"], 7)
            self.assertEqual(release["human_page_count"], 7)
            self.assertEqual(release["raw_artifact_count"], 7)
            self.assertEqual(validate(out, root), [])
            registry = json.loads((out / "data" / "artifact-registry.json").read_text(encoding="utf-8"))["artifacts"]
            self.assertEqual({item["source"] for item in registry}, {
                "00-home/start-here.md", "draft.md", "diagram.mmd", "cases.csv", "ontology.yaml", ".obsidian/graph.json", "publication-manifest.json",
            })
            for item in registry:
                self.assertTrue((out / item["page"]).is_file())
                raw = out / item["raw"]
                source = root / item["source"]
                self.assertEqual(raw.read_bytes(), source.read_bytes())
                self.assertEqual(item["sha256"], hashlib.sha256(source.read_bytes()).hexdigest())
                self.assertFalse(any(part.startswith(".") for part in pathlib.PurePosixPath(item["raw"]).parts))
            profile = next(item for item in registry if item["source"] == ".obsidian/graph.json")
            self.assertEqual(profile["raw"], "raw/vault-profile/graph.json")
            graph = json.loads((out / "data" / "graph.json").read_text(encoding="utf-8"))
            self.assertEqual(len(graph["nodes"]), 7)
            self.assertTrue(any(edge["target"] == "diagram.mmd" for edge in graph["edges"]))
            self.assertTrue(any(edge["anchor"] == "a-heading" for edge in graph["edges"]))

    def test_internal_draft_is_included_but_rendered_as_context_and_raw_html_is_inert(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root, out = self.fixture(pathlib.Path(temporary))
            build(root, None, out, "https://example.test/freight-trust/", source_date_epoch=0)
            draft = (out / "notes" / "draft" / "index.html").read_text(encoding="utf-8")
            home = (out / "notes" / "00-home" / "start-here" / "index.html").read_text(encoding="utf-8")
            self.assertIn("Private working note text", draft)
            self.assertIn("Working draft.", draft)
            self.assertIn('href="../../draft/#a-heading"', home)
            self.assertIn("Mermaid source fallback", home)
            self.assertIn("callout-important", home)
            self.assertIn("task-list-item", home)
            self.assertIn("&lt;script&gt;alert", home)
            self.assertNotIn("<script>alert", home)

    def test_build_is_deterministic_when_the_generation_time_is_explicit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root, first = self.fixture(pathlib.Path(temporary))
            second = pathlib.Path(temporary) / "site-two"
            build(root, None, first, "https://example.test/freight-trust/", source_date_epoch=0)
            build(root, None, second, "https://example.test/freight-trust/", source_date_epoch=0)
            first_files = {path.relative_to(first).as_posix(): path.read_bytes() for path in first.rglob("*") if path.is_file()}
            second_files = {path.relative_to(second).as_posix(): path.read_bytes() for path in second.rglob("*") if path.is_file()}
            self.assertEqual(first_files, second_files)

    def test_local_secret_and_path_traversal_are_never_silent_publication_inputs(self) -> None:
        self.assertRaises(BuildError, normalise_path, "../outside.md", "fixture source")
        with tempfile.TemporaryDirectory() as temporary:
            root, out = self.fixture(pathlib.Path(temporary))
            (root / ".env").write_text("TOKEN=do-not-publish", encoding="utf-8")
            with self.assertRaisesRegex(BuildError, "credential-like"):
                build(root, None, out, "https://example.test/freight-trust/", source_date_epoch=0)

    def test_validator_detects_tampered_raw_and_unexpected_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root, out = self.fixture(pathlib.Path(temporary))
            build(root, None, out, "https://example.test/freight-trust/", source_date_epoch=0)
            (out / "raw" / "draft.md").write_text("mutated", encoding="utf-8")
            (out / "surprise.txt").write_text("unexpected", encoding="utf-8")
            issues = validate(out, root)
            self.assertTrue(any("raw bytes differ" in issue for issue in issues))
            self.assertIn("unexpected generated output: surprise.txt", issues)


if __name__ == "__main__":
    unittest.main()
