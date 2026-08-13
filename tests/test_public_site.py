"""Fixtures for the fail-closed public publisher."""

from __future__ import annotations

import json
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from build_site import PublicationError, build
from validate_site import validate


PUBLIC_FRONTMATTER = """---
type: brief
status: current
updated: '2026-08-13'
tags:
- type/brief
- audience/public
---
"""


class PublicPublisherTests(unittest.TestCase):
    def write_fixture(self, directory: pathlib.Path, body: str) -> tuple[pathlib.Path, pathlib.Path, pathlib.Path]:
        root = directory / "knowledge-base"
        (root / "public-assets").mkdir(parents=True)
        (root / "public-note.md").write_text(PUBLIC_FRONTMATTER + body, encoding="utf-8")
        (root / "internal.md").write_text("---\ntype: brief\nstatus: current\ntags:\n- audience/internal\n---\n# Internal\nSECRET INTERNAL TEXT", encoding="utf-8")
        (root / "public-assets" / "mark.svg").write_text("<svg xmlns='http://www.w3.org/2000/svg'></svg>", encoding="utf-8")
        manifest = {
            "schema_version": "1.0.0",
            "site": {"title": "Fixture", "description": "Fixture description", "language": "en"},
            "notes": [{"source": "public-note.md", "slug": "fixture"}],
            "assets": [{"source": "public-assets/mark.svg", "url": "assets/mark.svg"}],
        }
        manifest_path = root / "publication-manifest.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        return root, manifest_path, directory / "site"

    def test_build_filters_internal_content_and_renders_common_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root, manifest, out = self.write_fixture(pathlib.Path(temporary), """# Public fixture

## A heading

Text with **strong**, *emphasis*, `code`, and an [external link](https://example.com/).

- one
- two

| Column | Value |
| --- | --- |
| A | B |

![Approved mark](public-assets/mark.svg)
""")
            build(root, manifest, out, "https://example.test/kb/", source_date_epoch=0)
            page = (out / "notes" / "fixture.html").read_text(encoding="utf-8")
            self.assertIn("<h2", page)
            self.assertIn("<strong>strong</strong>", page)
            self.assertIn("<table><thead>", page)
            self.assertIn('rel="noopener noreferrer"', page)
            self.assertIn('<img src="../assets/mark.svg"', page)
            self.assertNotIn("SECRET INTERNAL TEXT", page)
            self.assertEqual(validate(out, manifest), [])

    def test_build_refuses_link_to_unpublished_note(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root, manifest, out = self.write_fixture(pathlib.Path(temporary), "# Public fixture\n\n[[internal]]\n")
            with self.assertRaisesRegex(PublicationError, "unpublished note"):
                build(root, manifest, out, "https://example.test/kb/", source_date_epoch=0)

    def test_build_refuses_unapproved_local_asset(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root, manifest, out = self.write_fixture(pathlib.Path(temporary), "# Public fixture\n\n![No approval](internal.png)\n")
            with self.assertRaisesRegex(PublicationError, "not approved"):
                build(root, manifest, out, "https://example.test/kb/", source_date_epoch=0)


if __name__ == "__main__":
    unittest.main()
