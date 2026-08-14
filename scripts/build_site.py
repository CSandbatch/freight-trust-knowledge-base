"""Compile the complete Freight Trust vault into a static public knowledge atlas.

The compiler deliberately discovers the *versioned* contents of ``knowledge-base``.
Frontmatter state (including ``audience/internal``, draft, archive, and confidence
markers) is preserved as reader context; it is never a publication gate.  The only
material outside the compiler boundary is local/ignored state and credentials.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import html
import json
import mimetypes
import os
import pathlib
import posixpath
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field
from typing import Any, Iterable
from urllib.parse import quote, urljoin

import yaml
from markdown_it import MarkdownIt


DEFAULT_ROOT = pathlib.Path("knowledge-base")
DEFAULT_OUT = pathlib.Path("_site")
STATIC_ROOT = pathlib.Path(__file__).resolve().parents[1] / "portal"
FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)
WIKILINK = re.compile(r"(?P<embed>!?)\[\[(?P<target>[^\]]+)\]\]")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
FENCED = re.compile(r"^\s*(`{3,}|~{3,})")
SECRETISH = re.compile(r"(?:^|[-_.])(secret|credential|password|private[-_]?key)(?:[-_.]|$)", re.I)
SAFE_RAW_SUFFIXES = {".md", ".mmd", ".csv", ".yaml", ".yml", ".json", ".txt", ".xml"}

COLLECTION_NAMES = {
    "00-home": "Orientation",
    "01-client-briefs": "Client briefs",
    "02-programme-strategy": "Programme strategy",
    "03-research-evidence": "Research & evidence",
    "04-sbir": "SBIR working set",
    "05-agent-system": "Agent system",
    "06-team-memory": "Team memory",
    "07-visuals": "Visuals & maps",
    "08-archive": "Archive & history",
    "09-meta": "Governance & controls",
    ".obsidian": "Obsidian vault profile",
    "(root)": "Vault release files",
}


class BuildError(ValueError):
    """The public corpus cannot be compiled faithfully or safely."""


@dataclass
class Heading:
    text: str
    anchor: str
    level: int


@dataclass
class Link:
    source: str
    target: str
    anchor: str | None
    label: str
    embed: bool = False


@dataclass
class Artifact:
    source: str
    kind: str
    title: str
    page: str
    url: str
    raw: str
    mime: str
    size: int
    sha256: str
    metadata: dict[str, Any] = field(default_factory=dict)
    body: str = ""
    headings: list[Heading] = field(default_factory=list)
    links: list[Link] = field(default_factory=list)
    incoming: list[str] = field(default_factory=list)
    outgoing: list[str] = field(default_factory=list)
    section: str = "(root)"
    tags: list[str] = field(default_factory=list)
    x: float = 0.0
    y: float = 0.0

    @property
    def is_note(self) -> bool:
        return self.kind == "note"

    @property
    def note_type(self) -> str:
        return str(self.metadata.get("type", self.kind))

    @property
    def status(self) -> str:
        return str(self.metadata.get("status", "unclassified"))

    @property
    def identifier(self) -> str:
        return self.source


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def jsonable(value: Any) -> Any:
    """Convert PyYAML's date-like values to deterministic JSON values."""
    if isinstance(value, (dt.datetime, dt.date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    return value


def normalise_path(value: str, label: str) -> str:
    candidate = posixpath.normpath(value.replace("\\", "/")).lstrip("/")
    if not value or candidate in {"", "."} or candidate.startswith("../") or ":" in candidate:
        raise BuildError(f"invalid {label}: {value!r}")
    return candidate


def safe_source_path(relative: str) -> None:
    name = pathlib.PurePosixPath(relative).name.lower()
    if name == ".env" or name.startswith(".env.") or name in {"id_rsa", "id_ed25519"}:
        raise BuildError(f"refusing credential-like vault file: {relative}")
    if pathlib.PurePosixPath(relative).suffix.lower() in {".pem", ".key", ".pfx", ".p12"}:
        raise BuildError(f"refusing credential-like vault file: {relative}")
    if SECRETISH.search(name):
        raise BuildError(f"refusing credential-like vault file: {relative}")


def discover_versioned_files(root: pathlib.Path) -> list[str]:
    """Return all tracked vault files, with a conservative non-git fixture fallback."""
    root = root.resolve()
    paths: list[str] = []
    try:
        repository = subprocess.check_output(
            ["git", "-C", str(root.parent), "rev-parse", "--show-toplevel"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        repo_path = pathlib.Path(repository).resolve()
        relative_root = root.relative_to(repo_path).as_posix()
        output = subprocess.check_output(
            ["git", "-C", str(repo_path), "ls-files", "-z", "--", relative_root],
            stderr=subprocess.DEVNULL,
        )
        for item in output.decode("utf-8").split("\0"):
            if not item:
                continue
            candidate = (repo_path / item).resolve()
            if candidate.is_file() and candidate.is_relative_to(root):
                paths.append(candidate.relative_to(root).as_posix())
    except (OSError, subprocess.CalledProcessError, ValueError):
        paths = [path.relative_to(root).as_posix() for path in root.rglob("*") if path.is_file()]
    if not paths:
        raise BuildError(f"no versioned vault files discovered under {root}")
    cleaned = sorted(dict.fromkeys(normalise_path(path, "vault source") for path in paths))
    for path in cleaned:
        safe_source_path(path)
    return cleaned


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[`*_~\[\]{}()<>]", "", value).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "section"


def route_slug(source: str) -> str:
    path = pathlib.PurePosixPath(source)
    stem = path.with_suffix("")
    return "/".join(slugify(part.lstrip(".")) for part in stem.parts)


def section_for(source: str) -> str:
    parts = pathlib.PurePosixPath(source).parts
    return parts[0] if len(parts) > 1 else "(root)"


def collection_slug(section: str) -> str:
    return slugify(section.lstrip("."))


def section_label(section: str) -> str:
    return COLLECTION_NAMES.get(section, section.replace("-", " ").title())


def page_href(from_page: str, destination: str) -> str:
    base = posixpath.dirname(from_page) or "."
    has_trailing_slash = destination.endswith("/")
    result = posixpath.relpath(destination, base)
    if result == ".":
        return "./"
    return result + ("/" if has_trailing_slash and not result.endswith("/") else "")


def canonical_url(site_url: str, route: str) -> str:
    return urljoin(site_url, quote(route))


def parse_frontmatter(text: str, source: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER.match(text)
    if not match:
        return {}, text
    try:
        metadata = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        raise BuildError(f"{source}: invalid YAML frontmatter: {exc}") from exc
    if not isinstance(metadata, dict):
        raise BuildError(f"{source}: frontmatter must be a mapping")
    return jsonable(metadata), text[match.end() :]


def plain_text(value: str) -> str:
    value = re.sub(r"!?(\[\[)(.*?)(\]\])", lambda item: item.group(2).split("|", 1)[-1], value)
    value = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"<[^>]+>", "", value)
    return html.unescape(re.sub(r"\s+", " ", value)).strip()


def extract_headings(body: str) -> list[Heading]:
    headings: list[Heading] = []
    used: Counter[str] = Counter()
    in_fence = False
    fence: str | None = None
    for line in body.replace("\r\n", "\n").split("\n"):
        marker = FENCED.match(line)
        if marker:
            token = marker.group(1)
            if not in_fence:
                in_fence, fence = True, token[0]
            elif fence == token[0]:
                in_fence, fence = False, None
            continue
        if in_fence:
            continue
        match = HEADING.match(line)
        if not match:
            continue
        text = plain_text(match.group(2))
        base = slugify(text)
        used[base] += 1
        anchor = base if used[base] == 1 else f"{base}-{used[base]}"
        headings.append(Heading(text=text, anchor=anchor, level=len(match.group(1))))
    return headings


def title_from_note(body: str, metadata: dict[str, Any], fallback: str) -> str:
    for heading in extract_headings(body):
        if heading.level == 1:
            return heading.text
    for key in ("title", "name", "id"):
        if metadata.get(key):
            return str(metadata[key])
    return fallback.replace("-", " ").replace("_", " ").title()


def kind_for(source: str) -> str:
    suffix = pathlib.PurePosixPath(source).suffix.lower()
    return {
        ".md": "note",
        ".mmd": "mermaid",
        ".csv": "csv",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".json": "json",
    }.get(suffix, "file")


def mime_for(source: str) -> str:
    return {
        ".md": "text/markdown; charset=utf-8",
        ".mmd": "text/vnd.mermaid; charset=utf-8",
        ".csv": "text/csv; charset=utf-8",
        ".yaml": "application/yaml; charset=utf-8",
        ".yml": "application/yaml; charset=utf-8",
        ".json": "application/json; charset=utf-8",
    }.get(pathlib.PurePosixPath(source).suffix.lower(), mimetypes.guess_type(source)[0] or "application/octet-stream")


def text_from_bytes(data: bytes, source: str) -> str:
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise BuildError(f"{source}: public vault artifacts must be UTF-8 text in this release") from exc


def create_artifacts(root: pathlib.Path, sources: Iterable[str]) -> list[Artifact]:
    artifacts: list[Artifact] = []
    used_routes: set[str] = set()
    for source in sources:
        data = (root / source).read_bytes()
        kind = kind_for(source)
        slug = route_slug(source)
        page = f"{'notes' if kind == 'note' else 'artifacts'}/{slug}/index.html"
        url = page.removesuffix("index.html")
        if page in used_routes:
            raise BuildError(f"duplicate portal route for {source}: {page}")
        used_routes.add(page)
        text = text_from_bytes(data, source)
        metadata: dict[str, Any] = {}
        body = text
        headings: list[Heading] = []
        if kind == "note":
            metadata, body = parse_frontmatter(text, source)
            headings = extract_headings(body)
            title = title_from_note(body, metadata, pathlib.PurePosixPath(source).stem)
        else:
            title = pathlib.PurePosixPath(source).name
            if kind == "json":
                try:
                    loaded = json.loads(text)
                    metadata = {"artifact_format": "json", "root_kind": type(loaded).__name__}
                except json.JSONDecodeError:
                    metadata = {"artifact_format": "json", "parse_status": "invalid"}
            elif kind == "yaml":
                try:
                    loaded = yaml.safe_load(text)
                    metadata = {"artifact_format": "yaml", "root_kind": type(loaded).__name__}
                except yaml.YAMLError:
                    metadata = {"artifact_format": "yaml", "parse_status": "invalid"}
        tags_value = metadata.get("tags", [])
        tags = [str(item) for item in tags_value] if isinstance(tags_value, list) else []
        artifacts.append(
            Artifact(
                source=source,
                kind=kind,
                title=title,
                page=page,
                url=url,
                raw=f"raw/{source}",
                mime=mime_for(source),
                size=len(data),
                sha256=sha256_bytes(data),
                metadata=metadata,
                body=body,
                headings=headings,
                section=section_for(source),
                tags=tags,
            )
        )
    return artifacts


def stem_lookup(artifacts: Iterable[Artifact]) -> dict[str, list[Artifact]]:
    lookup: dict[str, list[Artifact]] = defaultdict(list)
    for artifact in artifacts:
        lookup[pathlib.PurePosixPath(artifact.source).stem].append(artifact)
        lookup[pathlib.PurePosixPath(artifact.source).name].append(artifact)
    return lookup


def resolve_target(source: Artifact, raw_target: str, by_source: dict[str, Artifact], stems: dict[str, list[Artifact]]) -> tuple[Artifact, str | None]:
    target, _, fragment = raw_target.strip().partition("#")
    target = target.strip().strip("`")
    if not target:
        target = source.source
    target = target.replace("\\", "/")
    candidates: list[str] = []
    for candidate in (target, posixpath.normpath(posixpath.join(posixpath.dirname(source.source), target))):
        candidate = candidate.lstrip("/")
        candidates.append(candidate)
        if not pathlib.PurePosixPath(candidate).suffix:
            candidates.append(f"{candidate}.md")
    found: list[Artifact] = []
    for candidate in dict.fromkeys(candidates):
        if candidate in by_source:
            found.append(by_source[candidate])
    if not found and "/" not in target:
        found = stems.get(pathlib.PurePosixPath(target).name, [])
        if not found:
            found = stems.get(pathlib.PurePosixPath(target).stem, [])
    found = list({item.source: item for item in found}.values())
    if len(found) != 1:
        state = "ambiguous" if found else "unresolved"
        raise BuildError(f"{source.source}: {state} wikilink [[{raw_target}]]")
    artifact = found[0]
    if fragment:
        if not artifact.is_note:
            raise BuildError(f"{source.source}: heading link targets non-note artifact [[{raw_target}]]")
        wanted = slugify(plain_text(fragment))
        matches = [heading.anchor for heading in artifact.headings if heading.anchor == wanted or slugify(heading.text) == wanted]
        if not matches:
            raise BuildError(f"{source.source}: unresolved heading anchor [[{raw_target}]]")
        fragment = matches[0]
    return artifact, fragment or None


def resolve_links(artifacts: list[Artifact]) -> list[Link]:
    by_source = {artifact.source: artifact for artifact in artifacts}
    stems = stem_lookup(artifacts)
    all_links: list[Link] = []
    for artifact in artifacts:
        if not artifact.is_note:
            continue
        for match in WIKILINK.finditer(artifact.body):
            raw = match.group("target")
            target_part, divider, label = raw.partition("|")
            if target_part.split("#", 1)[0].strip().lower() in {"wikilink", "wikilinks"}:
                # The schema/agent documentation uses these literal tokens to describe
                # syntax. They are represented as code-like text, not graph targets.
                continue
            target, anchor = resolve_target(artifact, target_part, by_source, stems)
            label_text = label.strip() if divider else (target.title if target.is_note else pathlib.PurePosixPath(target.source).name)
            link = Link(
                source=artifact.source,
                target=target.source,
                anchor=anchor,
                label=label_text,
                embed=bool(match.group("embed")),
            )
            artifact.links.append(link)
            all_links.append(link)
    for artifact in artifacts:
        artifact.outgoing = sorted({link.target for link in artifact.links})
    incoming: dict[str, set[str]] = defaultdict(set)
    for link in all_links:
        incoming[link.target].add(link.source)
    for artifact in artifacts:
        artifact.incoming = sorted(incoming[artifact.source])
    return all_links


def graph_positions(artifacts: list[Artifact]) -> None:
    groups: dict[str, list[Artifact]] = defaultdict(list)
    for artifact in artifacts:
        groups[artifact.section].append(artifact)
    ordered = sorted(groups)
    # A fixed 4-column collection grid intentionally trades a "physics simulation" for
    # legible, repeatable geography. Large source libraries retain usable spacing and
    # never rearrange merely because a browser loaded the page.
    columns = 4
    for group_index, section in enumerate(ordered):
        members = sorted(groups[section], key=lambda item: item.source)
        grid_columns = max(2, int((len(members) * 1.25) ** 0.5 + 0.999))
        grid_rows = max(1, (len(members) + grid_columns - 1) // grid_columns)
        group_x = 125 + (group_index % columns) * 250
        group_y = 94 + (group_index // columns) * 168
        max_x = 214 / max(1, grid_columns - 1)
        max_y = 138 / max(1, grid_rows - 1)
        for index, artifact in enumerate(members):
            col, row = index % grid_columns, index // grid_columns
            seed = int(hashlib.sha256(artifact.source.encode("utf-8")).hexdigest()[:4], 16)
            jitter_x = ((seed % 9) - 4) * 0.58
            jitter_y = (((seed // 9) % 9) - 4) * 0.45
            artifact.x = round(group_x - 107 + col * max_x + jitter_x, 2)
            artifact.y = round(group_y - 69 + row * max_y + jitter_y, 2)


def article_excerpt(artifact: Artifact, limit: int = 260) -> str:
    if artifact.is_note:
        body = re.sub(r"```[\s\S]*?```", "", artifact.body)
        text = plain_text(body)
    else:
        text = plain_text(artifact.body)
    text = re.sub(r"\s+", " ", text).strip()
    return text[: limit - 1].rstrip() + "…" if len(text) > limit else text


def reading_minutes(artifact: Artifact) -> int:
    if not artifact.is_note:
        return 0
    return max(1, round(len(plain_text(artifact.body).split()) / 220))


def status_notice(artifact: Artifact) -> str:
    status = artifact.status
    if status == "draft" or artifact.note_type == "draft":
        return '<aside class="state-notice is-draft"><strong>Working draft.</strong> This record is fully public in the Atlas, but is not submission-ready or a downstream citation by default.</aside>'
    if status in {"superseded", "frozen"} or artifact.note_type == "archive" or artifact.section == "08-archive":
        return '<aside class="state-notice is-archive"><strong>Historical record.</strong> This material remains accessible for provenance; read its status and any supersession metadata before relying on it.</aside>'
    if status in {"planned", "candidate", "to-build", "partner-dependent", "stretch"}:
        return '<aside class="state-notice is-planned"><strong>Prospective material.</strong> This record describes a proposal, dependency, or planned activity—not a completed result.</aside>'
    return ""


def tag_badges(tags: Iterable[str], limit: int | None = None) -> str:
    values = list(tags)
    if limit is not None:
        values = values[:limit]
    return "".join(f'<span class="badge">{html.escape(tag)}</span>' for tag in values)


def metadata_badges(artifact: Artifact) -> str:
    badges = [f'<span class="badge badge-type">{html.escape(artifact.note_type)}</span>', f'<span class="badge badge-status">{html.escape(artifact.status)}</span>']
    confidence = next((tag.split("/", 1)[1] for tag in artifact.tags if tag.startswith("confidence/")), None)
    if confidence:
        badges.append(f'<span class="badge badge-confidence">confidence: {html.escape(confidence)}</span>')
    return "".join(badges)


def card_html(artifact: Artifact, page: str, compact: bool = False) -> str:
    href = page_href(page, artifact.url)
    context = f"{section_label(artifact.section)} · {artifact.kind}"
    return f'''<article class="artifact-card {'compact-card' if compact else ''}">
  <p class="eyebrow">{html.escape(context)}</p>
  <h3><a href="{html.escape(href, quote=True)}">{html.escape(artifact.title)}</a></h3>
  <div class="badge-row">{metadata_badges(artifact)}</div>
  <p>{html.escape(article_excerpt(artifact, 180 if compact else 260))}</p>
  <p class="card-meta">{html.escape(artifact.source)} · {artifact.size:,} bytes</p>
</article>'''


def render_markdown(artifact: Artifact, by_source: dict[str, Artifact]) -> str:
    """Render safe CommonMark/GFM/Obsidian content without executing source HTML."""
    placeholders: dict[str, str] = {}
    link_counter = 0

    def replace_wikilink(match: re.Match[str]) -> str:
        nonlocal link_counter
        raw = match.group("target")
        target_part, divider, label = raw.partition("|")
        if target_part.split("#", 1)[0].strip().lower() in {"wikilink", "wikilinks"}:
            return f"`[[{raw}]]`"
        # Resolve again for fragment; the corpus is small and this keeps the preprocessor
        # independent from regex order / duplicate link labels.
        resolved, anchor = resolve_target(artifact, target_part, by_source, stem_lookup(by_source.values()))
        display = label.strip() if divider else (resolved.title if resolved.is_note else pathlib.PurePosixPath(resolved.source).name)
        href = page_href(artifact.page, resolved.url)
        if anchor:
            href += f"#{quote(anchor)}"
        token = f"https://atlas.invalid/link/{link_counter}"
        markup = f'<a href="{html.escape(href, quote=True)}" class="wiki-link">{html.escape(display)}</a>'
        if match.group("embed"):
            markup = f'<span class="embedded-link">Embedded artifact · {markup}</span>'
        placeholders[token] = markup
        link_counter += 1
        return f"[{display}]({token})"

    source = WIKILINK.sub(replace_wikilink, artifact.body)
    renderer = MarkdownIt("commonmark", {"html": False, "linkify": True, "typographer": False}).enable("table").enable("strikethrough")
    heading_number = 0
    default_heading_open = renderer.renderer.rules.get("heading_open")

    def heading_open(tokens: list[Any], index: int, options: Any, env: Any) -> str:
        nonlocal heading_number
        token = tokens[index]
        heading = artifact.headings[heading_number] if heading_number < len(artifact.headings) else None
        heading_number += 1
        if heading:
            token.attrSet("id", heading.anchor)
            return f'<{token.tag} id="{html.escape(heading.anchor, quote=True)}"><a class="heading-anchor" href="#{html.escape(heading.anchor, quote=True)}" aria-label="Link to this section">#</a>'
        if default_heading_open:
            return default_heading_open(tokens, index, options, env)
        return f"<{token.tag}>"

    renderer.renderer.rules["heading_open"] = heading_open
    output = renderer.render(source)
    for token, markup in placeholders.items():
        output = output.replace(f'href="{token}"', f'href="{html.escape(markup.split(chr(34))[1], quote=True)}"')
        # Preserve generated text inside the regular Markdown anchor, then give it the
        # link treatment. A second pass is safer than allowing source HTML through.
    # Replace the entire token anchors so aliases cannot be reparsed as Markdown.
    for token, markup in placeholders.items():
        output = re.sub(rf'<a href="{re.escape(token)}">.*?</a>', markup, output, flags=re.S)
    output = re.sub(
        r'<a href="(https?://[^\"]+)"',
        r'<a href="\1" target="_blank" rel="noopener noreferrer external"',
        output,
    )
    def task_item(item: re.Match[str]) -> str:
        complete = item.group(1).lower() == "x"
        state = "complete" if complete else "incomplete"
        return f'<li class="task-list-item"><input type="checkbox" disabled aria-label="Task {state}"{" checked" if complete else ""}> '

    output = re.sub(r'<li>\s*\[([ xX])\]\s*', task_item, output)
    output = re.sub(r'<pre><code class="language-mermaid">([\s\S]*?)</code></pre>', lambda item: f'<figure class="diagram-fallback"><figcaption>Mermaid source fallback — rendered safely as code in this static release.</figcaption><pre><code class="language-mermaid">{item.group(1)}</code></pre></figure>', output)
    def callout(item: re.Match[str]) -> str:
        kind = item.group(1).lower()
        title = item.group(2).strip() or item.group(1).title()
        return f'<aside class="callout callout-{kind}" role="note"><p><strong>{html.escape(title)}</strong>{item.group(3)}</aside>'

    output = re.sub(
        r'<blockquote>\s*<p>\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*([^<\n]*)([\s\S]*?)</blockquote>',
        callout,
        output,
        flags=re.I,
    )
    return output


def provenance_panel(artifact: Artifact, page: str) -> str:
    raw_href = page_href(page, artifact.raw)
    graph_href = page_href(page, f"graph/index.html?focus={quote(artifact.source)}&mode=local&depth=1")
    fields: list[tuple[str, str]] = [
        ("Original path", artifact.source),
        ("Format", artifact.mime),
        ("Size", f"{artifact.size:,} bytes"),
        ("SHA-256", artifact.sha256),
        ("Release", "atlas release record"),
    ]
    for key, value in artifact.metadata.items():
        if key in {"tags", "type", "status"}:
            continue
        rendered = json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else str(value)
        fields.append((key.replace("_", " ").title(), rendered))
    definitions = "".join(f"<dt>{html.escape(label)}</dt><dd>{html.escape(value)}</dd>" for label, value in fields)
    return f'''<aside class="provenance-panel" aria-label="Artifact provenance">
  <p class="eyebrow">Source & provenance</p>
  <dl>{definitions}</dl>
  <p class="provenance-actions"><a class="button button-quiet" href="{html.escape(raw_href, quote=True)}" download>Download raw</a><a class="button button-quiet" href="{html.escape(graph_href, quote=True)}">Open in graph</a></p>
</aside>'''


def relationship_panel(artifact: Artifact, page: str, by_source: dict[str, Artifact]) -> str:
    def links(paths: list[str]) -> str:
        if not paths:
            return '<p class="muted">None recorded.</p>'
        return "<ul class=relationship-list>" + "".join(
            f'<li><a href="{html.escape(page_href(page, by_source[path].url), quote=True)}">{html.escape(by_source[path].title)}</a><small>{html.escape(by_source[path].source)}</small></li>'
            for path in paths
        ) + "</ul>"
    related_candidates = [
        other for other in by_source.values()
        if other.source != artifact.source and set(other.tags) & set(artifact.tags) and other.source not in artifact.outgoing and other.source not in artifact.incoming
    ]
    related_candidates.sort(key=lambda item: (-(len(set(item.tags) & set(artifact.tags))), item.title.lower()))
    related = related_candidates[:6]
    return f'''<section class="relationships" aria-label="Knowledge graph relationships">
  <div><p class="eyebrow">Outgoing links</p>{links(artifact.outgoing)}</div>
  <div><p class="eyebrow">Backlinks</p>{links(artifact.incoming)}</div>
  <div><p class="eyebrow">Related by shared tags</p>{"<ul class=relationship-list>" + "".join(f'<li><a href="{html.escape(page_href(page, item.url), quote=True)}">{html.escape(item.title)}</a></li>' for item in related) + "</ul>" if related else '<p class="muted">No shared-tag suggestions.</p>'}</div>
</section>'''


def toc_html(artifact: Artifact) -> str:
    entries = [heading for heading in artifact.headings if heading.level > 1]
    if not entries:
        return ""
    return '<nav class="table-of-contents" aria-label="On this page"><p class="eyebrow">On this page</p><ol>' + "".join(f'<li class="toc-level-{heading.level}"><a href="#{html.escape(heading.anchor, quote=True)}">{html.escape(heading.text)}</a></li>' for heading in entries) + "</ol></nav>"


def structured_preview(artifact: Artifact) -> str:
    source = artifact.body
    raw_href = page_href(artifact.page, artifact.raw)
    if artifact.kind == "mermaid":
        return f'''<section class="artifact-preview diagram-preview"><p class="eyebrow">Mermaid diagram</p><h2>Source-first diagram viewer</h2><p>This hosted release keeps Mermaid inert and readable; the exact source can be opened in Obsidian or rendered by a compatible Mermaid viewer.</p><pre><code class="language-mermaid">{html.escape(source)}</code></pre><p><a class="button" href="{html.escape(raw_href, quote=True)}" download>Download Mermaid source</a></p></section>'''
    if artifact.kind == "csv":
        try:
            rows = list(csv.reader(source.splitlines()))
        except csv.Error as exc:
            return f'<section class="artifact-preview"><p>CSV preview unavailable: {html.escape(str(exc))}</p></section>'
        if not rows:
            return '<section class="artifact-preview"><p>This CSV is empty.</p></section>'
        headers = rows[0]
        visible_rows = rows[1:101]
        header_html = "".join(f"<th scope=col>{html.escape(cell)}</th>" for cell in headers)
        body_html = "".join("<tr>" + "".join(f"<td>{html.escape(cell)}</td>" for cell in row) + "</tr>" for row in visible_rows)
        return f'''<section class="artifact-preview"><p class="eyebrow">CSV data preview</p><p>{len(rows) - 1:,} data rows; showing the first {len(visible_rows):,}. The raw file is the complete source.</p><div class="table-scroll"><table><thead><tr>{header_html}</tr></thead><tbody>{body_html}</tbody></table></div></section>'''
    if artifact.kind in {"yaml", "json"}:
        try:
            parsed = yaml.safe_load(source) if artifact.kind == "yaml" else json.loads(source)
            pretty = json.dumps(jsonable(parsed), ensure_ascii=False, indent=2, sort_keys=isinstance(parsed, dict))
            status = "Parsed structure"
        except (yaml.YAMLError, json.JSONDecodeError) as exc:
            pretty = source
            status = f"Source fallback — parser reported: {exc}"
        return f'''<section class="artifact-preview"><p class="eyebrow">{html.escape(artifact.kind.upper())} viewer</p><p>{html.escape(status)}</p><pre><code class="language-{html.escape(artifact.kind)}">{html.escape(pretty)}</code></pre></section>'''
    return f'<section class="artifact-preview"><p>Preview unavailable for this file type. The exact source remains available for download.</p></section>'


def shell_html(title: str, description: str, page: str, site_url: str, main: str, active: str = "") -> str:
    root_href = page_href(page, "index.html")
    nav = [
        ("Explore", "explore/index.html", "explore"),
        ("Graph", "graph/index.html", "graph"),
        ("Collections", "collections/index.html", "collections"),
        ("Experiments", "experiments/index.html", "experiments"),
        ("About", "about/index.html", "about"),
    ]
    navigation = "".join(f'<a class="nav-link {"is-active" if active == key else ""}" href="{html.escape(page_href(page, href), quote=True)}">{label}</a>' for label, href, key in nav)
    css_href = page_href(page, "assets/atlas.css")
    js_href = page_href(page, "assets/atlas.js")
    data_root = page_href(page, "index.html")
    command = f'''<dialog class="command-dialog" data-command-dialog aria-label="Search the knowledge atlas">
      <form method="dialog" class="dialog-top"><button class="icon-button" aria-label="Close search">×</button><label><span class="sr-only">Search the knowledge atlas</span><input data-command-input type="search" autocomplete="off" placeholder="Search titles, evidence, tags, source paths…"></label><kbd>Esc</kbd></form>
      <div class="command-filters" data-command-filters></div><p class="command-status" data-command-status>Type to search the full public corpus.</p><ol class="command-results" data-command-results></ol>
    </dialog>'''
    return f'''<!doctype html>
<html lang="en" data-theme="auto">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>{html.escape(title)} · Freight Trust Knowledge Atlas</title>
  <meta name="description" content="{html.escape(description, quote=True)}">
  <link rel="canonical" href="{html.escape(canonical_url(site_url, page.removesuffix('index.html')), quote=True)}">
  <meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title, quote=True)}"><meta property="og:description" content="{html.escape(description, quote=True)}"><meta property="og:url" content="{html.escape(canonical_url(site_url, page.removesuffix('index.html')), quote=True)}">
  <meta name="twitter:card" content="summary">
  <link rel="stylesheet" href="{html.escape(css_href, quote=True)}">
</head>
<body data-root="{html.escape(data_root, quote=True)}" data-search="{html.escape(page_href(page, 'data/search.json'), quote=True)}" data-catalog="{html.escape(page_href(page, 'data/catalog.json'), quote=True)}">
  <a class="skip-link" href="#main-content">Skip to content</a>
  <header class="site-header"><div class="site-header-inner">
    <a class="wordmark" href="{html.escape(root_href, quote=True)}"><span class="wordmark-mark" aria-hidden="true">FT</span><span><strong>Freight Trust</strong><small>Knowledge Atlas</small></span></a>
    <nav class="primary-nav" aria-label="Primary navigation">{navigation}</nav>
    <div class="header-actions"><button class="search-trigger" type="button" data-open-search><span aria-hidden="true">⌕</span> <span>Search</span><kbd>⌘K</kbd></button><button class="icon-button theme-toggle" type="button" data-theme-toggle aria-label="Switch color theme"><span aria-hidden="true">◐</span></button></div>
  </div></header>
  <main id="main-content">{main}</main>
  <footer class="site-footer"><div><strong>Freight Trust Knowledge Atlas</strong><p>A public working record. Status, confidence, provenance, and draft markers describe each artifact’s evidentiary position; they do not hide it.</p></div><div><a href="{html.escape(page_href(page, 'data/artifact-registry.json'), quote=True)}">Artifact registry</a><a href="{html.escape(page_href(page, 'data/graph.json'), quote=True)}">Graph data</a><a href="{html.escape(page_href(page, 'release.json'), quote=True)}">Release provenance</a></div></footer>
  {command}
  <script defer src="{html.escape(js_href, quote=True)}"></script>
</body></html>'''


def home_page(page: str, artifacts: list[Artifact], links: list[Link], site_url: str) -> str:
    notes = [artifact for artifact in artifacts if artifact.is_note]
    sections = sorted({artifact.section for artifact in artifacts})
    experiments = [artifact for artifact in artifacts if artifact.note_type == "experiment"]
    featured_sections = ["03-research-evidence", "04-sbir", "07-visuals", "09-meta"]
    clusters = "".join(
        f'<a class="pathway-card pathway-{index}" href="{html.escape(page_href(page, f"collections/{collection_slug(section)}/index.html"), quote=True)}"><span class="eyebrow">{index + 1:02d}</span><strong>{html.escape(section_label(section))}</strong><small>{sum(item.section == section for item in artifacts)} artifacts</small><span aria-hidden="true">↗</span></a>'
        for index, section in enumerate(featured_sections)
        if section in sections
    )
    latest = sorted([artifact for artifact in notes if artifact.metadata.get("updated")], key=lambda item: str(item.metadata.get("updated")), reverse=True)[:6]
    experiments_html = "".join(card_html(artifact, page, compact=True) for artifact in experiments[:5]) or '<p class="muted">Experiment records will appear here as they are added to the vault.</p>'
    main = f'''<section class="hero atlas-hero"><div class="hero-copy"><p class="eyebrow">Open research infrastructure · Release atlas</p><h1>Freight Trust<br><em>Knowledge Atlas</em></h1><p class="hero-dek">A navigable public record of the programme’s evidence, experiments, decision controls, working drafts, diagrams, and Obsidian knowledge graph.</p><div class="hero-actions"><a class="button" href="{html.escape(page_href(page, 'explore/index.html'), quote=True)}">Explore {len(artifacts):,} artifacts</a><a class="button button-quiet" href="{html.escape(page_href(page, 'graph/index.html'), quote=True)}">Enter the graph <span aria-hidden="true">↗</span></a></div><p class="hero-note">Everything versioned in the vault is accessible. “Draft,” “archive,” and “internal” labels remain evidence context—not access controls.</p></div><div class="instrument-panel" aria-label="Atlas summary"><div class="instrument-grid"><div><strong>{len(artifacts)}</strong><span>public artifacts</span></div><div><strong>{len(notes)}</strong><span>reading notes</span></div><div><strong>{len(links):,}</strong><span>resolved links</span></div><div><strong>{len(sections)}</strong><span>collections</span></div></div><div class="instrument-line"></div><p><span class="status-dot"></span> Static, source-derived, and release-provenanced</p><a href="{html.escape(page_href(page, 'about/index.html'), quote=True)}">How to read this atlas →</a></div></section>
<section class="section-shell"><div class="section-heading"><p class="eyebrow">Editorial pathways</p><h2>Start with a question, then follow the evidence.</h2><p>Use thematic collections for orientation, or trace authored relationships through the graph.</p></div><div class="pathway-grid">{clusters}</div></section>
<section class="section-shell split-feature"><div><p class="eyebrow">Evidence as a working system</p><h2>Experiments and evidence are first-class routes.</h2><p>Protocol, data, method, and source records remain adjacent so a visitor can inspect what a claim depends on rather than only its polished summary.</p><a class="text-link" href="{html.escape(page_href(page, 'experiments/index.html'), quote=True)}">Browse the experiment & evidence hub <span aria-hidden="true">→</span></a></div><div class="card-grid compact-grid">{experiments_html}</div></section>
<section class="section-shell latest-section"><div class="section-heading"><p class="eyebrow">Recent record updates</p><h2>Freshness belongs beside the material.</h2></div><div class="card-grid">{"".join(card_html(artifact, page, compact=True) for artifact in latest)}</div></section>
<section class="section-shell disclosure"><div><p class="eyebrow">Reading posture</p><h2>Transparent does not mean settled.</h2></div><p>The Atlas publishes working hypotheses, source records, draft SBIR material, archive documents, and governance controls together. Each page retains its status, confidence, owner, source path, checksum, and raw download so readers can judge it on its own terms.</p></section>'''
    return shell_html("Freight Trust Knowledge Atlas", "A public, source-derived research atlas for Freight Trust.", page, site_url, main, "")


def explore_page(page: str, artifacts: list[Artifact], site_url: str) -> str:
    static_cards = "".join(card_html(artifact, page, compact=True) for artifact in artifacts)
    main = f'''<section class="page-intro"><p class="eyebrow">Explore the complete vault</p><h1>Every artifact, one library.</h1><p>Search headings, body text, frontmatter, tags, IDs, and original paths. Facets and query state are shareable in the URL.</p></section>
<section class="explore-layout" data-explore><aside class="filter-panel" aria-label="Explore filters"><div class="filter-heading"><p class="eyebrow">Refine</p><button type="button" class="text-button" data-reset-filters>Reset</button></div><label>Search<input data-explore-search type="search" placeholder="Identity, source, E1, #tag…"></label><label>Collection<select data-filter="section"><option value="">All collections</option></select></label><label>Type<select data-filter="type"><option value="">All types</option></select></label><label>Status<select data-filter="status"><option value="">All states</option></select></label><label>Confidence<select data-filter="confidence"><option value="">Any confidence</option></select></label><label>Tag<select data-filter="tag"><option value="">All tags</option></select></label><p class="result-count" data-explore-count>Loading the catalog…</p></aside><div class="explore-results"><div class="result-toolbar"><p data-explore-summary>All public artifacts</p><button type="button" class="text-button" data-copy-explore>Copy this view</button></div><div class="card-grid" data-explore-results></div><noscript><p class="state-notice is-planned">JavaScript refines this library. The full static artifact list remains available below.</p><div class="card-grid">{static_cards}</div></noscript></div></section>'''
    return shell_html("Explore the Atlas", "Search and filter every public Freight Trust vault artifact.", page, site_url, main, "explore")


def collection_page(page: str, section: str, artifacts: list[Artifact], site_url: str) -> str:
    members = [artifact for artifact in artifacts if artifact.section == section]
    main = f'''<section class="page-intro"><p class="eyebrow">Collection · {html.escape(section)}</p><h1>{html.escape(section_label(section))}</h1><p>{len(members):,} source-derived artifacts from <code>{html.escape(section)}</code>.</p></section><section class="section-shell"><div class="collection-actions"><a class="button button-quiet" href="{html.escape(page_href(page, 'explore/index.html') + '?section=' + quote(section), quote=True)}">Filter in Explore</a><a class="button button-quiet" href="{html.escape(page_href(page, 'graph/index.html') + '?collection=' + quote(section), quote=True)}">View this cluster in Graph</a></div><div class="card-grid">{"".join(card_html(artifact, page) for artifact in members)}</div></section>'''
    return shell_html(section_label(section), f"Freight Trust Atlas collection: {section_label(section)}.", page, site_url, main, "collections")


def collections_index_page(page: str, artifacts: list[Artifact], site_url: str) -> str:
    sections = sorted({artifact.section for artifact in artifacts})
    cards = "".join(
        f'<a class="collection-card" href="{html.escape(page_href(page, f"collections/{collection_slug(section)}/index.html"), quote=True)}"><span class="collection-index">{index + 1:02d}</span><strong>{html.escape(section_label(section))}</strong><small>{section} · {sum(artifact.section == section for artifact in artifacts)} artifacts</small><span aria-hidden="true">→</span></a>'
        for index, section in enumerate(sections)
    )
    main = f'''<section class="page-intro"><p class="eyebrow">Curated by vault location</p><h1>Collections retain source provenance.</h1><p>Physical vault paths are stable citations. These collection views make them readable without hiding cross-cutting tags and graph relationships.</p></section><section class="collection-grid">{cards}</section>'''
    return shell_html("Collections", "Browse Freight Trust materials by their original vault collection.", page, site_url, main, "collections")


def experiments_page(page: str, artifacts: list[Artifact], site_url: str) -> str:
    experiments = [artifact for artifact in artifacts if artifact.note_type == "experiment"]
    evidence = [artifact for artifact in artifacts if artifact.note_type in {"evidence", "dataset", "source", "method"}]
    main = f'''<section class="page-intro"><p class="eyebrow">Programme instruments</p><h1>Experiments & evidence</h1><p>Follow the programme’s falsifiable hypotheses alongside the datasets, methods, source records, and controls that delimit them.</p></section><section class="section-shell"><div class="section-heading"><p class="eyebrow">E1–E5</p><h2>Experiment protocols</h2></div><div class="card-grid">{"".join(card_html(artifact, page) for artifact in experiments)}</div></section><section class="section-shell"><div class="section-heading"><p class="eyebrow">Evidence library</p><h2>Methods, datasets, and sources</h2><p>These records vary in source class, freshness, verification, and confidence. Their metadata stays visible in the reader.</p></div><div class="card-grid">{"".join(card_html(artifact, page, compact=True) for artifact in evidence[:30])}</div><p><a class="button button-quiet" href="{html.escape(page_href(page, 'explore/index.html') + '?section=03-research-evidence', quote=True)}">Open all research & evidence artifacts</a></p></section>'''
    return shell_html("Experiments & evidence", "A source-aware hub for Freight Trust experiments, methods, datasets, and evidence.", page, site_url, main, "experiments")


def about_page(page: str, artifacts: list[Artifact], links: list[Link], site_url: str) -> str:
    kinds = Counter(artifact.kind for artifact in artifacts)
    main = f'''<section class="page-intro about-intro"><p class="eyebrow">About this release</p><h1>A public Obsidian-style research portal.</h1><p>The Atlas is a static release compiler, not a separate editorial database. It derives readers, graph data, full-text search, and provenance directly from the tracked vault.</p></section><section class="section-shell prose-panel"><h2>What is included</h2><p>Every versioned file under <code>knowledge-base/</code> is published as both a human-readable portal page and an exact raw download. Local environment files, ignored workspace state, credentials, and anything outside that directory are never part of the corpus.</p><dl class="metric-list"><div><dt>{len(artifacts)}</dt><dd>versioned artifacts</dd></div><div><dt>{sum(1 for artifact in artifacts if artifact.is_note)}</dt><dd>Markdown readers</dd></div><div><dt>{len(links):,}</dt><dd>resolved authored links</dd></div><div><dt>{len(kinds)}</dt><dd>artifact formats</dd></div></dl><h2>How to interpret it</h2><p>Publication is not validation. Draft, planned, candidate, archival, confidence, verification, and audience markers are inherited from source frontmatter and rendered as context. Follow source citations and provenance rather than reading a presentation layer as a finding.</p><p><a class="button" href="{html.escape(page_href(page, 'release.json'), quote=True)}">Inspect release provenance</a> <a class="button button-quiet" href="{html.escape(page_href(page, 'llms.txt'), quote=True)}">Machine entrypoint</a></p></section>'''
    return shell_html("About the Atlas", "How the Freight Trust Knowledge Atlas is compiled and how to interpret its public working materials.", page, site_url, main, "about")


def note_page(page: str, artifact: Artifact, by_source: dict[str, Artifact], site_url: str) -> str:
    body = render_markdown(artifact, by_source)
    raw_href = page_href(page, artifact.raw)
    graph_href = page_href(page, f"graph/index.html?focus={quote(artifact.source)}&mode=local&depth=1")
    collection_href = page_href(page, f"collections/{collection_slug(artifact.section)}/index.html")
    main = f'''<article class="reader-layout"><div class="reader-main"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{html.escape(page_href(page, 'collections/index.html'), quote=True)}">Collections</a><span>/</span><a href="{html.escape(collection_href, quote=True)}">{html.escape(section_label(artifact.section))}</a><span>/</span><span>{html.escape(pathlib.PurePosixPath(artifact.source).name)}</span></nav><header class="reader-header"><p class="eyebrow">{html.escape(artifact.kind)} · {html.escape(artifact.source)}</p><h1>{html.escape(artifact.title)}</h1><div class="badge-row">{metadata_badges(artifact)}{tag_badges(artifact.tags, 8)}</div><p class="reader-dek">{html.escape(article_excerpt(artifact, 360))}</p><div class="reader-actions"><a class="button" href="{html.escape(raw_href, quote=True)}" download>Download raw</a><a class="button button-quiet" href="{html.escape(graph_href, quote=True)}">Open in graph</a><button class="button button-quiet" type="button" data-copy-link>Copy permalink</button></div></header>{status_notice(artifact)}<div class="reader-content">{body}</div>{relationship_panel(artifact, page, by_source)}</div><aside class="reader-side">{toc_html(artifact)}{provenance_panel(artifact, page)}</aside></article>'''
    return shell_html(artifact.title, article_excerpt(artifact), page, site_url, main)


def artifact_page(page: str, artifact: Artifact, by_source: dict[str, Artifact], site_url: str) -> str:
    raw_href = page_href(page, artifact.raw)
    graph_href = page_href(page, f"graph/index.html?focus={quote(artifact.source)}&mode=local&depth=1")
    collection_href = page_href(page, f"collections/{collection_slug(artifact.section)}/index.html")
    main = f'''<article class="reader-layout"><div class="reader-main"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="{html.escape(page_href(page, 'collections/index.html'), quote=True)}">Collections</a><span>/</span><a href="{html.escape(collection_href, quote=True)}">{html.escape(section_label(artifact.section))}</a><span>/</span><span>{html.escape(pathlib.PurePosixPath(artifact.source).name)}</span></nav><header class="reader-header"><p class="eyebrow">Artifact viewer · {html.escape(artifact.kind)}</p><h1>{html.escape(artifact.title)}</h1><div class="badge-row">{metadata_badges(artifact)}</div><p class="reader-dek">{html.escape(artifact.source)} · {artifact.size:,} bytes · {html.escape(artifact.mime)}</p><div class="reader-actions"><a class="button" href="{html.escape(raw_href, quote=True)}" download>Download raw</a><a class="button button-quiet" href="{html.escape(graph_href, quote=True)}">Open in graph</a><button class="button button-quiet" type="button" data-copy-link>Copy permalink</button></div></header>{structured_preview(artifact)}{relationship_panel(artifact, page, by_source)}</div><aside class="reader-side">{provenance_panel(artifact, page)}</aside></article>'''
    return shell_html(artifact.title, f"Artifact viewer for {artifact.source}.", page, site_url, main)


def graph_page(page: str, artifacts: list[Artifact], links: list[Link], site_url: str) -> str:
    rows = "".join(f'<li><a href="{html.escape(page_href(page, artifact.url), quote=True)}">{html.escape(artifact.title)}</a><small>{html.escape(artifact.note_type)} · {len(artifact.outgoing)} out · {len(artifact.incoming)} in</small></li>' for artifact in artifacts)
    graph_js = page_href(page, "assets/graph.js")
    main = f'''<section class="page-intro graph-intro"><p class="eyebrow">Obsidian-style relationship atlas</p><h1>Graph the working record.</h1><p>Positions are precomputed and stable. Start globally by collection, then focus a node to traverse authored links and artifacts at a depth of one to three.</p></section><section class="graph-layout" data-graph data-graph-url="{html.escape(page_href(page, 'data/graph.json'), quote=True)}"><aside class="graph-controls" aria-label="Graph controls"><label>Mode<select data-graph-mode><option value="global">Global atlas</option><option value="local">Local focus</option></select></label><label>Focus<input data-graph-search type="search" placeholder="Find an artifact"></label><label>Depth<select data-graph-depth><option value="1">1 hop</option><option value="2">2 hops</option><option value="3">3 hops</option></select></label><label>Collection<select data-graph-filter="collection"><option value="">All collections</option></select></label><label>Type<select data-graph-filter="type"><option value="">All types</option></select></label><label>Status<select data-graph-filter="status"><option value="">All states</option></select></label><label class="checkbox-label"><input data-graph-edges type="checkbox"> Show all relationship lines</label><button type="button" class="button button-quiet" data-graph-reset>Reset graph</button><p class="result-count" data-graph-count>Loading graph…</p></aside><div class="graph-stage"><div class="graph-legend" data-graph-legend></div><svg class="atlas-graph" data-graph-canvas viewBox="0 0 1000 700" role="img" aria-label="Freight Trust artifact relationship graph. Use the graph navigator list for a keyboard-accessible equivalent."></svg><section class="graph-inspector" data-graph-inspector aria-live="polite"><p class="eyebrow">Inspector</p><h2>Select an artifact</h2><p>Click a node or use the navigator below to inspect its authored links and backlinks.</p></section></div><section class="graph-navigator" aria-label="Accessible graph navigator"><p class="eyebrow">Graph navigator</p><p>This semantic list is equivalent to the visual graph and remains available without pointer interaction.</p><ul data-graph-list>{rows}</ul></section></section><noscript><section class="section-shell"><p class="state-notice is-planned">The interactive SVG graph requires JavaScript. The graph navigator above still exposes every artifact as a reading route.</p></section></noscript><script defer src="{html.escape(graph_js, quote=True)}"></script>'''
    return shell_html("Knowledge graph", "Explore the Freight Trust Obsidian-style artifact graph.", page, site_url, main, "graph")


def catalog_record(artifact: Artifact) -> dict[str, Any]:
    tags = artifact.tags
    return {
        "id": artifact.source,
        "source": artifact.source,
        "title": artifact.title,
        "kind": artifact.kind,
        "type": artifact.note_type,
        "status": artifact.status,
        "section": artifact.section,
        "collection": section_label(artifact.section),
        "url": artifact.url,
        "raw_url": artifact.raw,
        "excerpt": article_excerpt(artifact),
        "tags": tags,
        "domains": [tag.split("/", 1)[1] for tag in tags if tag.startswith("domain/")],
        "programmes": [tag.split("/", 1)[1] for tag in tags if tag.startswith("programme/")],
        "audiences": [tag.split("/", 1)[1] for tag in tags if tag.startswith("audience/")],
        "confidence": next((tag.split("/", 1)[1] for tag in tags if tag.startswith("confidence/")), None),
        "updated": str(artifact.metadata.get("updated", "")),
        "size": artifact.size,
        "sha256": artifact.sha256,
        "reading_minutes": reading_minutes(artifact),
        "outgoing": artifact.outgoing,
        "incoming": artifact.incoming,
        "degree": len(artifact.outgoing) + len(artifact.incoming),
    }


def registry_record(artifact: Artifact) -> dict[str, Any]:
    record = catalog_record(artifact)
    record.update({
        "page": artifact.page,
        "raw": artifact.raw,
        "mime": artifact.mime,
        "metadata": artifact.metadata,
        "headings": [{"text": heading.text, "anchor": heading.anchor, "level": heading.level} for heading in artifact.headings],
        "renderer": "markdown-it-safe" if artifact.is_note else f"{artifact.kind}-viewer",
    })
    return record


def search_record(artifact: Artifact) -> dict[str, Any]:
    searchable_metadata = json.dumps(artifact.metadata, ensure_ascii=False, sort_keys=True)
    return {
        "id": artifact.source,
        "title": artifact.title,
        "headings": " ".join(heading.text for heading in artifact.headings),
        "body": plain_text(artifact.body),
        "frontmatter": searchable_metadata,
        "tags": " ".join(artifact.tags),
        "path": artifact.source,
        "type": artifact.note_type,
        "status": artifact.status,
        "section": artifact.section,
    }


def graph_data(artifacts: list[Artifact], links: list[Link]) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "layout": "deterministic-section-grid-v1",
        "nodes": [
            {
                "id": artifact.source,
                "label": artifact.title,
                "source": artifact.source,
                "url": artifact.url,
                "raw_url": artifact.raw,
                "kind": artifact.kind,
                "type": artifact.note_type,
                "status": artifact.status,
                "section": artifact.section,
                "collection": section_label(artifact.section),
                "tags": artifact.tags,
                "degree": len(artifact.outgoing) + len(artifact.incoming),
                "x": artifact.x,
                "y": artifact.y,
            }
            for artifact in artifacts
        ],
        "edges": [
            {
                "id": f"{index}:{link.source}->{link.target}",
                "source": link.source,
                "target": link.target,
                "kind": "wikilink-embed" if link.embed else "wikilink",
                "anchor": link.anchor,
                "label": link.label,
            }
            for index, link in enumerate(links)
        ],
    }


def write_json(path: pathlib.Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")


def git_state(root: pathlib.Path) -> dict[str, Any]:
    def command(*args: str) -> str | None:
        try:
            return subprocess.check_output(args, text=True, stderr=subprocess.DEVNULL).strip()
        except (OSError, subprocess.CalledProcessError):
            return None
    repository = root.parent
    revision = command("git", "-C", str(repository), "rev-parse", "HEAD")
    dirty = command("git", "-C", str(repository), "status", "--porcelain")
    return {"source_revision": revision or "unavailable", "working_tree_clean": dirty == "" if dirty is not None else None}


def copy_static_assets(staging: pathlib.Path) -> list[str]:
    required = ["atlas.css", "atlas.js", "graph.js"]
    outputs: list[str] = []
    for name in required:
        source = STATIC_ROOT / name
        if not source.is_file():
            raise BuildError(f"missing portal static asset: {source}")
        destination = staging / "assets" / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        outputs.append(destination.relative_to(staging).as_posix())
    return outputs


def build(root: pathlib.Path = DEFAULT_ROOT, manifest_path: pathlib.Path | None = None, out: pathlib.Path = DEFAULT_OUT, site_url: str = "", source_date_epoch: int | None = None) -> dict[str, Any]:
    """Build a complete, staged public atlas and return its release record.

    ``manifest_path`` remains an accepted compatibility argument. Its file is published
    as a normal artifact but has no allowlist authority in the inclusive compiler.
    """
    if not re.fullmatch(r"https://[^\s]+/", site_url):
        raise BuildError("site URL must be an absolute HTTPS URL ending with '/'")
    root = root.resolve()
    if not root.is_dir():
        raise BuildError(f"knowledge-base root is missing: {root}")
    sources = discover_versioned_files(root)
    artifacts = create_artifacts(root, sources)
    by_source = {artifact.source: artifact for artifact in artifacts}
    links = resolve_links(artifacts)
    graph_positions(artifacts)
    out = out.resolve()
    if out in {root, root.parent}:
        raise BuildError("output directory is unsafe")
    staging = out.parent / f".{out.name}-atlas-staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    fixed = copy_static_assets(staging)
    (staging / ".nojekyll").write_text("\n", encoding="utf-8")
    # Exact raw routes are copied before page generation; their hashes are verified by
    # validate_site.py against the source inventory rather than trusted from metadata.
    for artifact in artifacts:
        destination = staging / artifact.raw
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / artifact.source, destination)
    # Human-readable pages.
    (staging / "index.html").write_text(home_page("index.html", artifacts, links, site_url), encoding="utf-8")
    explore_route = "explore/index.html"
    target = staging / explore_route
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(explore_page(explore_route, artifacts, site_url), encoding="utf-8")
    collection_index = "collections/index.html"
    target = staging / collection_index
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(collections_index_page(collection_index, artifacts, site_url), encoding="utf-8")
    for section in sorted({artifact.section for artifact in artifacts}):
        route = f"collections/{collection_slug(section)}/index.html"
        target = staging / route
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(collection_page(route, section, artifacts, site_url), encoding="utf-8")
    for route, page_html in (
        ("experiments/index.html", experiments_page("experiments/index.html", artifacts, site_url)),
        ("about/index.html", about_page("about/index.html", artifacts, links, site_url)),
        ("graph/index.html", graph_page("graph/index.html", artifacts, links, site_url)),
    ):
        target = staging / route
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page_html, encoding="utf-8")
    for artifact in artifacts:
        target = staging / artifact.page
        target.parent.mkdir(parents=True, exist_ok=True)
        content = note_page(artifact.page, artifact, by_source, site_url) if artifact.is_note else artifact_page(artifact.page, artifact, by_source, site_url)
        target.write_text(content, encoding="utf-8")
    catalog = [catalog_record(artifact) for artifact in artifacts]
    registry = [registry_record(artifact) for artifact in artifacts]
    write_json(staging / "data" / "catalog.json", {"schema_version": "1.0.0", "artifacts": catalog})
    write_json(staging / "data" / "search.json", {"schema_version": "1.0.0", "documents": [search_record(artifact) for artifact in artifacts]})
    write_json(staging / "data" / "graph.json", graph_data(artifacts, links))
    write_json(staging / "data" / "artifact-registry.json", {"schema_version": "1.0.0", "source_root": "knowledge-base", "artifacts": registry})
    inventory_hash = sha256_bytes("\n".join(f"{artifact.source}\0{artifact.sha256}" for artifact in artifacts).encode("utf-8"))
    generated_at = dt.datetime.fromtimestamp(source_date_epoch, tz=dt.timezone.utc) if source_date_epoch is not None else dt.datetime.now(tz=dt.timezone.utc)
    release = {
        "schema_version": "2.0.0",
        "build_profile": "inclusive-public-vault",
        "generated_at": generated_at.isoformat().replace("+00:00", "Z"),
        "site_url": site_url,
        "source_root": "knowledge-base",
        "source_artifact_count": len(artifacts),
        "human_page_count": len(artifacts),
        "raw_artifact_count": len(artifacts),
        "markdown_note_count": sum(artifact.is_note for artifact in artifacts),
        "graph_node_count": len(artifacts),
        "graph_edge_count": len(links),
        "source_inventory_sha256": inventory_hash,
        "artifacts": [{"source": artifact.source, "page": artifact.page, "url": artifact.url, "raw": artifact.raw, "sha256": artifact.sha256, "size": artifact.size, "mime": artifact.mime} for artifact in artifacts],
        "static_assets": fixed,
        **git_state(root),
    }
    write_json(staging / "release.json", release)
    all_human_routes = ["", "explore/", "graph/", "collections/", "experiments/", "about/"] + [f"collections/{collection_slug(section)}/" for section in sorted({artifact.section for artifact in artifacts})] + [artifact.url for artifact in artifacts]
    sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + "\n".join(f"  <url><loc>{html.escape(canonical_url(site_url, route))}</loc></url>" for route in all_human_routes) + "\n</urlset>\n"
    (staging / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (staging / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {canonical_url(site_url, 'sitemap.xml')}\n", encoding="utf-8")
    llms = f'''# Freight Trust Knowledge Atlas

Public, static, source-derived working corpus for the Freight Trust programme.

- Artifact registry: {canonical_url(site_url, 'data/artifact-registry.json')}
- Search index: {canonical_url(site_url, 'data/search.json')}
- Relationship graph: {canonical_url(site_url, 'data/graph.json')}
- Release provenance: {canonical_url(site_url, 'release.json')}
- Full library: {canonical_url(site_url, 'explore/')}

Interpret all status, confidence, draft, archive, source-class, and verification metadata as part of the record. Publication does not convert a proposal, source record, or draft into a demonstrated result.
'''
    (staging / "llms.txt").write_text(llms, encoding="utf-8")
    if out.exists():
        shutil.rmtree(out)
    staging.rename(out)
    print(f"Built Freight Trust Knowledge Atlas: {len(artifacts)} source artifacts, {len(links)} resolved wikilinks, {sum(item.is_note for item in artifacts)} Markdown readers.")
    return release


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=DEFAULT_ROOT)
    parser.add_argument("--manifest", type=pathlib.Path, help="Compatibility input; the manifest is published but is not an allowlist.")
    parser.add_argument("--out", type=pathlib.Path, default=DEFAULT_OUT)
    parser.add_argument("--site-url", default=os.environ.get("PUBLIC_SITE_URL", ""))
    parser.add_argument("--source-date-epoch", type=int)
    args = parser.parse_args()
    try:
        build(args.root, args.manifest, args.out, args.site_url, args.source_date_epoch)
    except BuildError as exc:
        print(f"Atlas build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
