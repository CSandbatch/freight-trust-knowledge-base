"""Check the generated static site index for deployment regressions."""

from __future__ import annotations

import json
import pathlib
import sys


def main() -> int:
    index = pathlib.Path("_site/notes.json")
    if not index.is_file():
        print("Missing _site/notes.json; run scripts/build_site.py first.", file=sys.stderr)
        return 1
    notes = json.loads(index.read_text(encoding="utf-8"))
    required = {"path", "title", "text", "section", "type", "status", "tags", "links", "degree"}
    paths = {note.get("path") for note in notes}
    issues = []
    if not notes:
        issues.append("document index is empty")
    for note in notes:
        missing = required - note.keys()
        if missing:
            issues.append(f"{note.get('path', '<unknown>')}: missing {sorted(missing)}")
        for link in note.get("links", []):
            if link not in paths:
                issues.append(f"{note['path']}: generated link is missing target {link}")
    if issues:
        print("Static site validation failed:")
        print("\n".join(f"- {issue}" for issue in issues))
        return 1
    print(f"Static site validation passed: {len(notes)} documents, {sum(len(note['links']) for note in notes)} links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
