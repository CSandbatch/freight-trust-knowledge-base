"""Validate the Freight Trust canonical Markdown vault for CI and agent change gates."""

from __future__ import annotations

import pathlib
import posixpath
import re
import sys
from collections import deque

import yaml


ROOT = pathlib.Path("knowledge-base")
TYPES = {
    "home", "moc", "schema", "taxonomy", "policy", "experiment", "method",
    "dataset", "evidence", "source", "term", "brief", "draft", "strategy-note",
    "agent", "log", "archive", "claim", "decision", "gap", "drift", "meeting",
    "handoff", "task", "agent-run", "memory",
}
STATUSES = {
    "active", "draft", "planned", "candidate", "required", "stretch", "to-build",
    "partner-dependent", "current", "superseded", "frozen",
}
TYPE_FIELDS = {
    "moc": ("area",),
    "schema": ("owner", "version"), "taxonomy": ("owner", "version"),
    "policy": ("owner", "version"),
    "experiment": ("id", "phase", "owner", "primary_outcome"),
    "dataset": ("access", "licence", "verification"),
    "evidence": ("confidence_default",),
    "source": ("source_class", "accessed", "verification"),
    "term": ("aliases", "defined_by"), "brief": ("audience",),
    "draft": ("deliverable", "owner"), "agent": ("layer", "tools"),
    "archive": ("superseded_by", "frozen_on"),
    "claim": ("id", "proposition", "confidence", "sources"),
    "decision": ("id", "decision_date", "owner", "rationale"),
    "gap": ("id", "priority", "owner", "acceptance_criteria"),
    "drift": ("id", "severity", "finding", "owner"),
    "meeting": ("id", "meeting_date", "participants"),
    "handoff": ("id", "from", "to", "next_action"),
    "task": ("id", "owner", "objective", "acceptance_criteria"),
    "agent-run": ("id", "actor", "started", "outcome"),
    "memory": ("id", "memory_type", "memory_scope", "provenance", "review"),
}
CLAIM_BEARING = {"evidence", "source", "dataset", "brief", "draft", "term", "claim"}


def fail(issues: list[str], path: str, message: str) -> None:
    issues.append(f"{path}: {message}")


def main() -> int:
    if not ROOT.is_dir():
        print(f"Missing vault: {ROOT}", file=sys.stderr)
        return 2
    notes: dict[str, tuple[dict, str]] = {}
    files = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file()}
    issues: list[str] = []
    ids: dict[str, str] = {}
    frontmatter = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)
    for rel in sorted(p for p in files if p.endswith(".md")):
        text = (ROOT / rel).read_text(encoding="utf-8")
        match = frontmatter.match(text)
        if not match:
            fail(issues, rel, "frontmatter must start on line 1")
            continue
        try:
            metadata = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as exc:
            fail(issues, rel, f"invalid YAML: {exc}")
            continue
        note_type = metadata.get("type")
        if note_type not in TYPES:
            fail(issues, rel, f"invalid type {note_type!r}")
        if metadata.get("status") not in STATUSES:
            fail(issues, rel, f"invalid status {metadata.get('status')!r}")
        tags = metadata.get("tags")
        if not isinstance(tags, list) or not tags:
            fail(issues, rel, "tags must be a non-empty list")
        if note_type in CLAIM_BEARING and not metadata.get("updated"):
            fail(issues, rel, "claim-bearing note requires updated")
        for field in TYPE_FIELDS.get(note_type, ()):
            if not metadata.get(field):
                fail(issues, rel, f"{note_type} requires {field}")
        record_id = metadata.get("id")
        if record_id:
            if record_id in ids:
                fail(issues, rel, f"duplicate ID {record_id!r}; first in {ids[record_id]}")
            ids[record_id] = rel
        notes[rel] = (metadata, text)

    stems: dict[str, list[str]] = {}
    for path in files:
        stems.setdefault(pathlib.PurePosixPath(path).stem, []).append(path)
    graph = {path: set() for path in notes}
    for source, (_, text) in notes.items():
        for raw in re.findall(r"!?\[\[([^\]]+)\]\]", text):
            target = raw.split("|", 1)[0].split("#", 1)[0].strip()
            if not target or target in {"wikilink", "wikilinks"}:
                continue
            options: list[str] = []
            for candidate in (target, f"{target}.md"):
                for path in (
                    posixpath.normpath(posixpath.join(posixpath.dirname(source), candidate)),
                    posixpath.normpath(candidate),
                ):
                    if path in files:
                        options.append(path)
            if not options and "/" not in target:
                options = stems.get(pathlib.PurePosixPath(target).stem, [])
            options = list(dict.fromkeys(options))
            if len(options) != 1:
                fail(issues, source, f"{'ambiguous' if options else 'unresolved'} wikilink [[{target}]]")
            elif options[0].endswith(".md"):
                graph[source].add(options[0])

    start = "00-home/start-here.md"
    if start not in graph:
        fail(issues, start, "missing entry point")
    else:
        distance = {start: 0}
        queue: deque[str] = deque([start])
        while queue:
            current = queue.popleft()
            for linked in graph[current]:
                if linked not in distance:
                    distance[linked] = distance[current] + 1
                    queue.append(linked)
        for orphan in sorted(set(notes) - set(distance)):
            fail(issues, orphan, "unreachable from start-here")
        if distance and max(distance.values()) > 3:
            fail(issues, start, f"maximum navigation distance is {max(distance.values())}, expected <= 3")

    if issues:
        print("Knowledge-base validation failed:")
        print("\n".join(f"- {issue}" for issue in issues))
        return 1
    print(f"Knowledge-base validation passed: {len(notes)} Markdown notes, {len(ids)} atomic IDs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
