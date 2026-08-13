"""Build the manifest-authorized public Markdown reader.

This script intentionally has no "include everything" mode. A note reaches the public
artifact only when it is named in ``knowledge-base/publication-manifest.json`` and passes
the publication policy below.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import pathlib
import posixpath
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from urllib.parse import urljoin


DEFAULT_ROOT = pathlib.Path("knowledge-base")
DEFAULT_MANIFEST = DEFAULT_ROOT / "publication-manifest.json"
DEFAULT_OUT = pathlib.Path("_site")
PROHIBITED_PREFIXES = (
    "03-research-evidence/",
    "04-sbir/",
    "05-agent-system/",
    "06-team-memory/",
    "08-archive/",
    "09-meta/",
)
FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)
WIKILINK = re.compile(r"!?(\[\[([^\]]+)\]\])")


class PublicationError(ValueError):
    """A source note is not safe to include in the public artifact."""


@dataclass(frozen=True)
class ManifestNote:
    source: str
    slug: str

    @property
    def url(self) -> str:
        return f"notes/{self.slug}.html"


@dataclass(frozen=True)
class PublicNote:
    manifest: ManifestNote
    metadata: dict[str, object]
    title: str
    body: str


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    """Parse the deliberately small YAML subset used by vault frontmatter."""
    match = FRONTMATTER.match(text)
    if not match:
        return {}, text
    metadata: dict[str, object] = {}
    list_key: str | None = None
    for line in match.group(1).splitlines():
        if line.startswith("- ") and list_key:
            value = metadata[list_key]
            assert isinstance(value, list)
            value.append(line[2:].strip().strip("\"'"))
            continue
        list_key = None
        key, separator, value = line.partition(":")
        if not separator:
            continue
        key, value = key.strip(), value.strip()
        if value:
            metadata[key] = value.strip("\"'")
        else:
            metadata[key] = []
            list_key = key
    return metadata, text[match.end():]


def normalise_relative(value: str, label: str) -> str:
    value = value.replace("\\", "/")
    candidate = posixpath.normpath(value).lstrip("/")
    if not value or candidate in {".", ""} or candidate.startswith("../") or ":" in candidate:
        raise PublicationError(f"invalid {label}: {value!r}")
    return candidate


def load_manifest(path: pathlib.Path) -> tuple[dict[str, object], list[ManifestNote], dict[str, str]]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PublicationError(f"publication manifest is missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PublicationError(f"publication manifest is invalid JSON: {exc}") from exc
    if raw.get("schema_version") != "1.0.0" or not isinstance(raw.get("site"), dict):
        raise PublicationError("publication manifest requires schema_version 1.0.0 and site metadata")
    notes: list[ManifestNote] = []
    for item in raw.get("notes", []):
        if not isinstance(item, dict) or not isinstance(item.get("source"), str) or not isinstance(item.get("slug"), str):
            raise PublicationError("each publication manifest note requires string source and slug")
        source = normalise_relative(item["source"], "note source")
        slug = normalise_relative(item["slug"], "note slug")
        if not re.fullmatch(r"[a-z0-9][a-z0-9/-]*", slug):
            raise PublicationError(f"note slug is not URL-safe: {slug!r}")
        notes.append(ManifestNote(source, slug))
    if not notes or len({note.source for note in notes}) != len(notes) or len({note.slug for note in notes}) != len(notes):
        raise PublicationError("publication manifest needs non-empty, unique note sources and slugs")
    assets: dict[str, str] = {}
    for item in raw.get("assets", []):
        if not isinstance(item, dict) or not isinstance(item.get("source"), str) or not isinstance(item.get("url"), str):
            raise PublicationError("each approved asset requires string source and url")
        source = normalise_relative(item["source"], "asset source")
        url = normalise_relative(item["url"], "asset url")
        if source in assets or url in assets.values():
            raise PublicationError("approved asset sources and URLs must be unique")
        assets[source] = url
    return raw, notes, assets


def source_path(root: pathlib.Path, relative: str) -> pathlib.Path:
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise PublicationError(f"source escapes knowledge-base: {relative}") from exc
    return candidate


def title_from_body(body: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", body, flags=re.M)
    return match.group(1).strip() if match else fallback


def is_public_metadata(metadata: dict[str, object], source: str) -> None:
    tags = metadata.get("tags")
    if not isinstance(tags, list) or "audience/public" not in tags:
        raise PublicationError(f"{source}: manifest note must carry audience/public")
    if "audience/internal" in tags:
        raise PublicationError(f"{source}: internal notes cannot be published")
    if metadata.get("status") == "draft" or metadata.get("type") in {"draft", "archive"}:
        raise PublicationError(f"{source}: draft or archive material cannot be published")


def resolve_wikilink(source: str, target: str, source_to_note: dict[str, ManifestNote], root: pathlib.Path) -> str | None:
    target = target.split("#", 1)[0].strip().strip("`")
    if not target:
        return None
    candidates = [target, target.removesuffix(".md") + ".md"]
    relative = posixpath.normpath(posixpath.join(posixpath.dirname(source), target))
    candidates.extend([relative, relative.removesuffix(".md") + ".md"])
    for candidate in dict.fromkeys(candidates):
        candidate = candidate.lstrip("/")
        if candidate in source_to_note:
            return source_to_note[candidate].url
        if candidate.endswith(".md") and source_path(root, candidate).is_file():
            raise PublicationError(f"{source}: links to unpublished note [[{target}]]")
    raise PublicationError(f"{source}: unresolved wikilink [[{target}]]")


def relative_from_note(url: str) -> str:
    return "../" + url


def inline_markdown(value: str, source: str, source_to_note: dict[str, ManifestNote], root: pathlib.Path, assets: dict[str, str]) -> str:
    """Render a deliberately safe, common subset of Markdown without raw HTML."""
    if "![[" in value:
        raise PublicationError(f"{source}: Obsidian embeds are not publishable; use an approved Markdown image asset")
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", value):
        destination = target.strip()
        if not destination.startswith(("https://", "http://", "mailto:", "#")):
            raise PublicationError(f"{source}: local Markdown link is not an approved public URL: {destination}")
    tokens: dict[str, str] = {}

    def token(markup: str) -> str:
        key = f"\x00TOKEN{len(tokens)}\x00"
        tokens[key] = markup
        return key

    def image(match: re.Match[str]) -> str:
        alt, asset = match.group(1), normalise_relative(match.group(2).strip(), "image asset")
        if asset not in assets:
            raise PublicationError(f"{source}: image asset is not approved: {asset}")
        return token(f'<img src="{html.escape("../" + assets[asset], quote=True)}" alt="{html.escape(alt, quote=True)}">')

    value = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", image, value)

    def wiki(match: re.Match[str]) -> str:
        raw = match.group(2)
        target, separator, label = raw.partition("|")
        destination = resolve_wikilink(source, target, source_to_note, root)
        text = label.strip() if separator else pathlib.PurePosixPath(target.split("#", 1)[0]).stem
        return token(f'<a href="{html.escape(relative_from_note(destination), quote=True)}">{html.escape(text)}</a>')

    value = WIKILINK.sub(wiki, value)
    value = html.escape(value, quote=False)

    def external_link(match: re.Match[str]) -> str:
        label, href = match.group(1), html.unescape(match.group(2))
        return token(f'<a href="{html.escape(href, quote=True)}" target="_blank" rel="noopener noreferrer">{label}</a>')

    value = re.sub(r"\[([^\]]+)\]\((https?://[^\s)]+)\)", external_link, value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\*\*(.+?)\*\*|__(.+?)__", lambda m: f"<strong>{m.group(1) or m.group(2)}</strong>", value)
    value = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)|(?<!_)_([^_\n]+)_(?!_)", lambda m: f"<em>{m.group(1) or m.group(2)}</em>", value)
    for key, markup in tokens.items():
        value = value.replace(key, markup)
    return value


def render_markdown(body: str, source: str, source_to_note: dict[str, ManifestNote], root: pathlib.Path, assets: dict[str, str]) -> str:
    lines = body.replace("\r\n", "\n").split("\n")
    output: list[str] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{inline_markdown(' '.join(part.strip() for part in paragraph), source, source_to_note, root, assets)}</p>")
            paragraph.clear()

    def table_cells(value: str) -> list[str]:
        value = value.strip()
        if value.startswith("|"):
            value = value[1:]
        if value.endswith("|"):
            value = value[:-1]
        return [cell.strip() for cell in value.split("|")]

    def is_table_separator(value: str) -> bool:
        cells = table_cells(value)
        return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)

    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            flush_paragraph()
            index += 1
            continue
        if line.startswith("```"):
            flush_paragraph()
            language = line[3:].strip()
            index += 1
            code: list[str] = []
            while index < len(lines) and not lines[index].startswith("```"):
                code.append(lines[index])
                index += 1
            if index == len(lines):
                raise PublicationError(f"{source}: unclosed fenced code block")
            css = f' class="language-{html.escape(language, quote=True)}"' if language else ""
            output.append(f"<pre><code{css}>{html.escape(chr(10).join(code))}</code></pre>")
            index += 1
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if heading:
            flush_paragraph()
            level = len(heading.group(1))
            text = inline_markdown(heading.group(2), source, source_to_note, root, assets)
            anchor = re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", heading.group(2)).lower()).strip("-")
            output.append(f"<h{level} id=\"{html.escape(anchor, quote=True)}\">{text}</h{level}>")
            index += 1
            continue
        if "|" in line and index + 1 < len(lines) and is_table_separator(lines[index + 1]):
            flush_paragraph()
            headers = table_cells(line)
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                cells = table_cells(lines[index])
                if len(cells) != len(headers):
                    raise PublicationError(f"{source}: table row has a different number of cells than its header")
                rows.append(cells)
                index += 1
            header_html = "".join(f"<th scope=\"col\">{inline_markdown(cell, source, source_to_note, root, assets)}</th>" for cell in headers)
            row_html = "".join("<tr>" + "".join(f"<td>{inline_markdown(cell, source, source_to_note, root, assets)}</td>" for cell in row) + "</tr>" for row in rows)
            output.append(f"<table><thead><tr>{header_html}</tr></thead><tbody>{row_html}</tbody></table>")
            continue
        if re.match(r"^ {0,3}([-*_])(?: *\1){2,}\s*$", line):
            flush_paragraph()
            output.append("<hr>")
            index += 1
            continue
        if line.startswith("> "):
            flush_paragraph()
            quote: list[str] = []
            while index < len(lines) and lines[index].startswith("> "):
                quote.append(lines[index][2:])
                index += 1
            output.append(f"<blockquote><p>{inline_markdown(' '.join(quote), source, source_to_note, root, assets)}</p></blockquote>")
            continue
        list_match = re.match(r"^\s*([-+*])\s+(.+)$", line)
        ordered_match = re.match(r"^\s*(\d+)\.\s+(.+)$", line)
        if list_match or ordered_match:
            flush_paragraph()
            ordered = bool(ordered_match)
            entries: list[str] = []
            while index < len(lines):
                current = re.match(r"^\s*\d+\.\s+(.+)$", lines[index]) if ordered else re.match(r"^\s*[-+*]\s+(.+)$", lines[index])
                if not current:
                    break
                entries.append(f"<li>{inline_markdown(current.group(1), source, source_to_note, root, assets)}</li>")
                index += 1
            tag = "ol" if ordered else "ul"
            output.append(f"<{tag}>{''.join(entries)}</{tag}>")
            continue
        paragraph.append(line)
        index += 1
    flush_paragraph()
    return "\n".join(output)


def page_html(title: str, description: str, canonical: str, body: str, navigation: str, home_href: str, language: str) -> str:
    return f"""<!doctype html>
<html lang=\"{html.escape(language, quote=True)}\">
<head>
  <meta charset=\"utf-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
  <title>{html.escape(title)}</title>
  <meta name=\"description\" content=\"{html.escape(description, quote=True)}\">
  <link rel=\"canonical\" href=\"{html.escape(canonical, quote=True)}\">
  <meta property=\"og:type\" content=\"website\">
  <meta property=\"og:title\" content=\"{html.escape(title, quote=True)}\">
  <meta property=\"og:description\" content=\"{html.escape(description, quote=True)}\">
  <meta property=\"og:url\" content=\"{html.escape(canonical, quote=True)}\">
  <meta name=\"twitter:card\" content=\"summary\">
  <style>body{{max-width:72ch;margin:0 auto;padding:1.5rem;font:1rem/1.6 system-ui,sans-serif;color:#17212b}}a{{color:#075d93}}header{{border-bottom:1px solid #ccd6dd;margin-bottom:2rem}}nav ul{{display:flex;gap:1rem;flex-wrap:wrap;padding:0;list-style:none}}img{{max-width:100%;height:auto}}pre{{overflow:auto;padding:1rem;background:#f3f6f8}}code{{font-family:ui-monospace,monospace}}blockquote{{border-left:4px solid #9ab4c4;margin-left:0;padding-left:1rem;color:#344c5b}}.skip{{position:absolute;left:-999px}}.skip:focus{{left:1rem;top:1rem;background:white;padding:.5rem}}</style>
</head>
<body>
  <a class=\"skip\" href=\"#content\">Skip to content</a>
  <header><p><a href=\"{html.escape(home_href, quote=True)}\">Freight Trust public materials</a></p><nav aria-label=\"Published materials\">{navigation}</nav></header>
  <main id=\"content\">{body}</main>
</body>
</html>"""


def git_build_state() -> dict[str, object]:
    def command(*args: str) -> str | None:
        try:
            return subprocess.check_output(args, text=True, stderr=subprocess.DEVNULL).strip()
        except (OSError, subprocess.CalledProcessError):
            return None
    revision = command("git", "rev-parse", "HEAD")
    dirty = command("git", "status", "--porcelain")
    return {"source_revision": revision or "unavailable", "working_tree_clean": dirty == "" if dirty is not None else None}


def build(root: pathlib.Path, manifest_path: pathlib.Path, out: pathlib.Path, site_url: str, source_date_epoch: int | None = None) -> None:
    if not re.fullmatch(r"https://[^\s]+/", site_url):
        raise PublicationError("site URL must be an absolute HTTPS URL ending with '/'")
    manifest, manifest_notes, assets = load_manifest(manifest_path)
    root = root.resolve()
    source_to_note = {note.source: note for note in manifest_notes}
    notes: list[PublicNote] = []
    for item in manifest_notes:
        if item.source.startswith(PROHIBITED_PREFIXES):
            raise PublicationError(f"{item.source}: prohibited source area cannot be published")
        path = source_path(root, item.source)
        if not path.is_file():
            raise PublicationError(f"{item.source}: manifest source does not exist")
        metadata, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        is_public_metadata(metadata, item.source)
        notes.append(PublicNote(item, metadata, title_from_body(body, pathlib.PurePosixPath(item.source).stem), body))
    for asset in assets:
        if not source_path(root, asset).is_file():
            raise PublicationError(f"{asset}: approved asset does not exist")
    # Render before replacing the old output, so a policy failure never leaves a partial site.
    rendered = {note.manifest.source: render_markdown(note.body, note.manifest.source, source_to_note, root, assets) for note in notes}
    out = out.resolve()
    if out in {root, root.parent}:
        raise PublicationError("output directory is unsafe")
    staging = out.parent / f".{out.name}-public-staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    def navigation_for(page_url: str) -> str:
        page_dir = posixpath.dirname(page_url)
        links = []
        for note in notes:
            href = posixpath.relpath(note.manifest.url, page_dir or ".")
            links.append(f'<li><a href="{html.escape(href, quote=True)}">{html.escape(note.title)}</a></li>')
        return "<ul>" + "".join(links) + "</ul>"

    index_cards = "".join(f'<li><a href="{html.escape(note.manifest.url, quote=True)}">{html.escape(note.title)}</a></li>' for note in notes)
    site = manifest["site"]
    assert isinstance(site, dict)
    site_title = str(site.get("title", "Public knowledge base"))
    description = str(site.get("description", "Published materials."))
    language = str(site.get("language", "en"))
    index_body = f"<h1>{html.escape(site_title)}</h1><p>{html.escape(description)}</p><h2>Published materials</h2><ul>{index_cards}</ul>"
    (staging / "index.html").write_text(page_html(site_title, description, urljoin(site_url, "index.html"), index_body, navigation_for("index.html"), "index.html", language), encoding="utf-8")
    for note in notes:
        page = staging / note.manifest.url
        page.parent.mkdir(parents=True, exist_ok=True)
        canonical = urljoin(site_url, note.manifest.url)
        home_href = posixpath.relpath("index.html", posixpath.dirname(note.manifest.url))
        page.write_text(page_html(note.title, description, canonical, rendered[note.manifest.source], navigation_for(note.manifest.url), home_href, language), encoding="utf-8")
    for asset, destination in assets.items():
        target = staging / destination
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source_path(root, asset), target)
    sitemap_urls = ["index.html", *(note.manifest.url for note in notes)]
    sitemap = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n" + "\n".join(f"  <url><loc>{html.escape(urljoin(site_url, url))}</loc></url>" for url in sitemap_urls) + "\n</urlset>\n"
    (staging / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    (staging / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {urljoin(site_url, 'sitemap.xml')}\n", encoding="utf-8")
    timestamp = dt.datetime.fromtimestamp(source_date_epoch, tz=dt.timezone.utc) if source_date_epoch is not None else dt.datetime.now(tz=dt.timezone.utc)
    release = {
        "schema_version": "1.0.0",
        "build_profile": "public-manifest-only",
        "generated_at": timestamp.isoformat().replace("+00:00", "Z"),
        "site_url": site_url,
        "manifest_sha256": sha256_bytes(manifest_path.read_bytes()),
        "published_count": len(notes),
        "published_notes": [{"source": note.manifest.source, "url": note.manifest.url, "content_sha256": sha256_bytes(note.body.encode("utf-8"))} for note in notes],
        "approved_asset_count": len(assets),
        **git_build_state(),
    }
    (staging / "release.json").write_text(json.dumps(release, indent=2) + "\n", encoding="utf-8")
    if out.exists():
        shutil.rmtree(out)
    staging.rename(out)
    print(f"Built public site: {len(notes)} approved notes, {len(assets)} approved assets.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=DEFAULT_ROOT)
    parser.add_argument("--manifest", type=pathlib.Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--out", type=pathlib.Path, default=DEFAULT_OUT)
    parser.add_argument("--site-url", default=os.environ.get("PUBLIC_SITE_URL", ""))
    parser.add_argument("--source-date-epoch", type=int)
    args = parser.parse_args()
    try:
        build(args.root, args.manifest, args.out, args.site_url, args.source_date_epoch)
    except PublicationError as exc:
        print(f"Public build refused: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
