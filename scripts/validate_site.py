"""Validate the generated public artifact for leaks and broken local references."""

from __future__ import annotations

import argparse
import html.parser
import json
import pathlib
import posixpath
import sys
from urllib.parse import unquote, urlparse

from build_site import DEFAULT_MANIFEST, DEFAULT_OUT, PROHIBITED_PREFIXES, PublicationError, load_manifest


class LinkCollector(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.urls.append(value)


def validate(site: pathlib.Path, manifest_path: pathlib.Path) -> list[str]:
    issues: list[str] = []
    try:
        _manifest, notes, assets = load_manifest(manifest_path)
    except PublicationError as exc:
        return [str(exc)]
    required = ["index.html", "robots.txt", "sitemap.xml", "release.json", *(note.url for note in notes), *assets.values()]
    for relative in required:
        if not (site / relative).is_file():
            issues.append(f"missing generated file: {relative}")
    release_path = site / "release.json"
    if release_path.is_file():
        try:
            release = json.loads(release_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append(f"invalid release metadata: {exc}")
            release = {}
        if release.get("build_profile") != "public-manifest-only":
            issues.append("release metadata does not identify the public-manifest-only profile")
        if release.get("published_count") != len(notes):
            issues.append("release metadata has an incorrect published note count")
        expected_urls = [note.url for note in notes]
        if [item.get("url") for item in release.get("published_notes", [])] != expected_urls:
            issues.append("release metadata does not exactly match the publication manifest")
        if not str(release.get("site_url", "")).startswith("https://"):
            issues.append("release metadata has no HTTPS site URL")
    sitemap = (site / "sitemap.xml")
    if sitemap.is_file():
        text = sitemap.read_text(encoding="utf-8")
        for note in notes:
            if note.url not in text:
                issues.append(f"sitemap omits {note.url}")
    for page in [site / "index.html", *(site / note.url for note in notes)]:
        if not page.is_file():
            continue
        text = page.read_text(encoding="utf-8")
        for prohibited in PROHIBITED_PREFIXES:
            if prohibited in text:
                issues.append(f"{page.relative_to(site)} exposes prohibited path {prohibited}")
        if "<link rel=\"canonical\"" not in text or "og:url" not in text:
            issues.append(f"{page.relative_to(site)} is missing canonical or social metadata")
        collector = LinkCollector()
        collector.feed(text)
        for target in collector.urls:
            parsed = urlparse(target)
            if parsed.scheme or parsed.netloc or target.startswith("#"):
                continue
            if target.startswith("/"):
                candidate = site / unquote(target.lstrip("/"))
            else:
                candidate = page.parent / unquote(parsed.path)
            candidate = candidate.resolve()
            try:
                candidate.relative_to(site.resolve())
            except ValueError:
                issues.append(f"{page.relative_to(site)} links outside site: {target}")
                continue
            if parsed.path and not candidate.is_file():
                issues.append(f"{page.relative_to(site)} has broken local link or asset: {target}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=pathlib.Path, default=DEFAULT_OUT)
    parser.add_argument("--manifest", type=pathlib.Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()
    issues = validate(args.site, args.manifest)
    if issues:
        print("Public site validation failed:")
        print("\n".join(f"- {issue}" for issue in issues))
        return 1
    print("Public site validation passed: manifest-only output has no broken local links or prohibited source paths.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
