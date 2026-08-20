"""Validate source-to-portal completeness, link integrity, and rendered-page safety."""

from __future__ import annotations

import argparse
import hashlib
import html.parser
import json
import pathlib
import posixpath
import tempfile
from collections import defaultdict
from urllib.parse import unquote, urlparse

from build_site import (
    DEFAULT_OUT,
    DEFAULT_ROOT,
    BuildError,
    collection_slug,
    create_artifacts,
    discover_versioned_files,
    resolve_links,
)


class PageCollector(html.parser.HTMLParser):
    """Collect navigational targets and reject executable content in rendered pages."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.issues: list[str] = []
        self._script_has_src = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(str(attributes["id"]))
        for key, value in attrs:
            if key.lower().startswith("on"):
                self.issues.append(f"unsafe event handler attribute {key}")
            if key.lower() in {"href", "src"} and value:
                self.targets.append((key.lower(), value))
                if value.strip().lower().startswith(("javascript:", "data:text/html", "vbscript:")):
                    self.issues.append(f"unsafe URL scheme in {key}")
        if tag.lower() == "script":
            self._script_has_src = bool(attributes.get("src"))
            if not self._script_has_src:
                self.issues.append("inline script tag is not permitted")

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script":
            self._script_has_src = False

    def handle_data(self, data: str) -> None:
        if self._script_has_src and data.strip():
            self.issues.append("external script tag unexpectedly has inline content")


def load_json(path: pathlib.Path, label: str, issues: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        issues.append(f"missing {label}: {path.name}")
    except json.JSONDecodeError as exc:
        issues.append(f"invalid {label}: {exc}")
    return {}


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def target_file(site: pathlib.Path, page: pathlib.Path, value: str) -> tuple[pathlib.Path | None, str | None, str | None]:
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc or value.startswith("mailto:"):
        return None, None, None
    path = unquote(parsed.path)
    fragment = unquote(parsed.fragment) or None
    if not path:
        return page, fragment, None
    candidate = site / path.lstrip("/") if path.startswith("/") else page.parent / path
    candidate = candidate.resolve()
    try:
        candidate.relative_to(site.resolve())
    except ValueError:
        return None, fragment, "link resolves outside generated site"
    if candidate.is_dir():
        candidate = candidate / "index.html"
    elif not candidate.is_file() and (candidate / "index.html").is_file():
        candidate = candidate / "index.html"
    return candidate, fragment, None


def expected_output_files(release: dict[str, object], catalog: list[dict[str, object]]) -> set[str]:
    artifacts = release.get("artifacts", [])
    expected = {
        ".nojekyll", "index.html", "explore/index.html", "graph/index.html", "collections/index.html",
        "experiments/index.html", "knowledge/index.html", "about/index.html", "robots.txt", "sitemap.xml", "llms.txt", "release.json",
        "data/catalog.json", "data/search.json", "data/graph.json", "data/artifact-registry.json",
        "assets/atlas.css", "assets/atlas.js", "assets/graph.js", "assets/favicon.svg",
        "assets/freight-terminal-hero.png",
    }
    for item in artifacts if isinstance(artifacts, list) else []:
        if isinstance(item, dict):
            expected.update({str(item.get("page", "")), str(item.get("raw", ""))})
    for section in {str(item.get("section", "")) for item in catalog if isinstance(item, dict)}:
        if section:
            expected.add(f"collections/{collection_slug(section)}/index.html")
    for item in catalog:
        if not isinstance(item, dict) or item.get("type") != "experiment":
            continue
        source_name = pathlib.PurePosixPath(str(item.get("source", ""))).name.lower()
        for experiment_id in ("e1", "e2", "e3", "e4", "e5"):
            if source_name.startswith(f"experiment-{experiment_id}-"):
                expected.add(f"experiments/{experiment_id}/index.html")
    expected.discard("")
    return expected


def validate(site: pathlib.Path = DEFAULT_OUT, root: pathlib.Path = DEFAULT_ROOT) -> list[str]:
    site, root = site.resolve(), root.resolve()
    issues: list[str] = []
    release = load_json(site / "release.json", "release metadata", issues)
    registry_payload = load_json(site / "data" / "artifact-registry.json", "artifact registry", issues)
    catalog_payload = load_json(site / "data" / "catalog.json", "catalog", issues)
    search_payload = load_json(site / "data" / "search.json", "search index", issues)
    graph_payload = load_json(site / "data" / "graph.json", "graph", issues)
    if not isinstance(release, dict) or not isinstance(registry_payload, dict) or not isinstance(catalog_payload, dict) or not isinstance(search_payload, dict) or not isinstance(graph_payload, dict):
        return issues or ["generated JSON payloads have invalid root shapes"]
    registry = registry_payload.get("artifacts", [])
    catalog = catalog_payload.get("artifacts", [])
    documents = search_payload.get("documents", [])
    nodes = graph_payload.get("nodes", [])
    edges = graph_payload.get("edges", [])
    if not all(isinstance(value, list) for value in (registry, catalog, documents, nodes, edges)):
        return [*issues, "one or more generated data arrays are invalid"]
    try:
        sources = discover_versioned_files(root)
    except BuildError as exc:
        return [*issues, str(exc)]
    source_set = set(sources)
    release_artifacts = release.get("artifacts", [])
    if release.get("build_profile") != "inclusive-public-vault":
        issues.append("release metadata does not identify inclusive-public-vault")
    for key in ("source_artifact_count", "human_page_count", "raw_artifact_count", "graph_node_count"):
        if release.get(key) != len(sources):
            issues.append(f"release {key} does not equal discovered source count {len(sources)}")
    if not isinstance(release_artifacts, list):
        issues.append("release artifacts is not a list")
        release_artifacts = []
    release_by_source = {item.get("source"): item for item in release_artifacts if isinstance(item, dict)}
    registry_by_source = {item.get("source"): item for item in registry if isinstance(item, dict)}
    catalog_by_source = {item.get("source"): item for item in catalog if isinstance(item, dict)}
    node_by_source = {item.get("source"): item for item in nodes if isinstance(item, dict)}
    search_sources = {item.get("id") for item in documents if isinstance(item, dict)}
    for label, values in (
        ("release", set(release_by_source)),
        ("artifact registry", set(registry_by_source)),
        ("catalog", set(catalog_by_source)),
        ("graph nodes", set(node_by_source)),
        ("search index", search_sources),
    ):
        if values != source_set:
            missing, unexpected = source_set - values, values - source_set
            if missing:
                issues.append(f"{label} omits source artifacts: {sorted(missing)[:5]}")
            if unexpected:
                issues.append(f"{label} has non-source artifacts: {sorted(unexpected)[:5]}")
    for source in sources:
        source_file = root / source
        expected_hash = sha256(source_file)
        for label, record in (("release", release_by_source.get(source)), ("registry", registry_by_source.get(source))):
            if not isinstance(record, dict):
                continue
            if record.get("sha256") != expected_hash:
                issues.append(f"{label} hash mismatch for {source}")
        record = release_by_source.get(source)
        if not isinstance(record, dict):
            continue
        raw = str(record.get("raw", ""))
        page = str(record.get("page", ""))
        if not raw or posixpath.normpath(raw).startswith("../") or not raw.startswith("raw/"):
            issues.append(f"unsafe or missing raw route for {source}")
            continue
        if any(part.startswith(".") for part in pathlib.PurePosixPath(raw).parts):
            issues.append(f"Pages-incompatible hidden raw route for {source}: {raw}")
        for label, sibling, field in (
            ("artifact registry", registry_by_source.get(source), "raw"),
            ("catalog", catalog_by_source.get(source), "raw_url"),
            ("graph node", node_by_source.get(source), "raw_url"),
        ):
            if not isinstance(sibling, dict) or sibling.get(field) != raw:
                issues.append(f"{label} raw route does not match release metadata for {source}")
        raw_file = site / raw
        if not raw_file.is_file():
            issues.append(f"missing raw file for {source}")
        elif raw_file.read_bytes() != source_file.read_bytes():
            issues.append(f"raw bytes differ from source for {source}")
        if not page or not (site / page).is_file():
            issues.append(f"missing reader/preview page for {source}")
    expected = expected_output_files(release, catalog)
    actual = {path.relative_to(site).as_posix() for path in site.rglob("*") if path.is_file()}
    for missing in sorted(expected - actual):
        issues.append(f"missing generated output: {missing}")
    for unexpected in sorted(actual - expected):
        issues.append(f"unexpected generated output: {unexpected}")
    if release.get("graph_edge_count") != len(edges):
        issues.append("release graph edge count does not equal graph data")
    node_ids = {item.get("id") for item in nodes if isinstance(item, dict)}
    edge_pairs: dict[str, set[str]] = defaultdict(set)
    reverse_pairs: dict[str, set[str]] = defaultdict(set)
    for edge in edges:
        if not isinstance(edge, dict) or edge.get("kind") not in {"wikilink", "wikilink-embed"}:
            issues.append("graph contains an invalid edge record")
            continue
        source, target = edge.get("source"), edge.get("target")
        if source not in node_ids or target not in node_ids:
            issues.append(f"graph edge has missing endpoint: {source!r} -> {target!r}")
            continue
        edge_pairs[str(source)].add(str(target))
        reverse_pairs[str(target)].add(str(source))
        anchor = edge.get("anchor")
        if anchor:
            target_page = release_by_source.get(target, {}).get("page") if isinstance(release_by_source.get(target), dict) else None
            if target_page and (site / str(target_page)).is_file():
                content = (site / str(target_page)).read_text(encoding="utf-8")
                if f'id="{anchor}"' not in content:
                    issues.append(f"graph heading edge anchor is absent: {source} -> {target}#{anchor}")
    for item in catalog:
        if not isinstance(item, dict):
            continue
        source = str(item.get("source", ""))
        if set(item.get("outgoing", [])) != edge_pairs.get(source, set()):
            issues.append(f"catalog outgoing graph parity failure for {source}")
        if set(item.get("incoming", [])) != reverse_pairs.get(source, set()):
            issues.append(f"catalog incoming graph parity failure for {source}")
    try:
        expected_artifacts = create_artifacts(root, sources)
        expected_links = resolve_links(expected_artifacts)
        actual_edges = {(str(edge.get("source")), str(edge.get("target")), edge.get("anchor"), str(edge.get("kind"))) for edge in edges if isinstance(edge, dict)}
        expected_edges = {(link.source, link.target, link.anchor, "wikilink-embed" if link.embed else "wikilink") for link in expected_links}
        if actual_edges != expected_edges:
            issues.append("graph edge inventory does not exactly match resolved source wikilinks")
    except BuildError as exc:
        issues.append(f"source graph could not be recomputed: {exc}")
    sitemap = (site / "sitemap.xml").read_text(encoding="utf-8") if (site / "sitemap.xml").is_file() else ""
    for item in release_artifacts:
        if isinstance(item, dict) and str(item.get("url", "")) not in sitemap:
            issues.append(f"sitemap omits human artifact route {item.get('source')}")
    page_cache: dict[pathlib.Path, PageCollector] = {}
    for page in sorted(site.rglob("*.html")):
        text = page.read_text(encoding="utf-8")
        collector = PageCollector()
        collector.feed(text)
        page_cache[page] = collector
        if '<link rel="canonical"' not in text or 'og:url' not in text:
            issues.append(f"{page.relative_to(site)} lacks canonical or social metadata")
        for issue in collector.issues:
            issues.append(f"{page.relative_to(site)}: {issue}")
        for attribute, value in collector.targets:
            target, fragment, error = target_file(site, page, value)
            if error:
                issues.append(f"{page.relative_to(site)}: {error}: {value}")
                continue
            if target is None:
                continue
            if not target.is_file():
                issues.append(f"{page.relative_to(site)} has broken local {attribute}: {value}")
                continue
            if fragment:
                target_collector = page_cache.get(target)
                if target_collector is None:
                    target_collector = PageCollector()
                    target_collector.feed(target.read_text(encoding="utf-8"))
                    page_cache[target] = target_collector
                if fragment not in target_collector.ids:
                    issues.append(f"{page.relative_to(site)} has broken heading anchor: {value}")
    return issues


def deterministic_check(root: pathlib.Path, site_url: str) -> list[str]:
    """Build twice with an explicit epoch and compare every byte of generated output."""
    from build_site import build

    with tempfile.TemporaryDirectory(prefix="freight-trust-atlas-") as temporary:
        base = pathlib.Path(temporary)
        first, second = base / "first", base / "second"
        build(root, None, first, site_url, source_date_epoch=0)
        build(root, None, second, site_url, source_date_epoch=0)
        first_files = {path.relative_to(first).as_posix(): path.read_bytes() for path in first.rglob("*") if path.is_file()}
        second_files = {path.relative_to(second).as_posix(): path.read_bytes() for path in second.rglob("*") if path.is_file()}
        if first_files.keys() != second_files.keys():
            return ["deterministic build file inventory differs"]
        return [f"deterministic build differs: {path}" for path in first_files if first_files[path] != second_files[path]]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=pathlib.Path, default=DEFAULT_OUT)
    parser.add_argument("--root", type=pathlib.Path, default=DEFAULT_ROOT)
    parser.add_argument("--check-deterministic", action="store_true")
    parser.add_argument("--site-url", default="https://ci.invalid/freight-trust/")
    args = parser.parse_args()
    issues = validate(args.site, args.root)
    if args.check_deterministic:
        issues.extend(deterministic_check(args.root, args.site_url))
    if issues:
        print("Knowledge Atlas validation failed:")
        print("\n".join(f"- {issue}" for issue in issues))
        return 1
    print("Knowledge Atlas validation passed: exhaustive inventory, raw hashes, links, graph parity, and rendered-page safety verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
