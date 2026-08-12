"""Read-only HTTP gateway for agents over the canonical Freight Trust vault.

Run: python scripts/kb_gateway.py --port 8787
Endpoints: /health, /status, /search?q=, /read?path=, /related?path=, /openapi.json
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse


ROOT = pathlib.Path("knowledge-base").resolve()


def notes() -> dict[str, str]:
    return {p.relative_to(ROOT).as_posix(): p.read_text(encoding="utf-8") for p in ROOT.rglob("*.md")}


def safe_path(value: str) -> pathlib.Path | None:
    candidate = (ROOT / value).resolve()
    return candidate if candidate.is_file() and candidate.is_relative_to(ROOT) else None


class Gateway(BaseHTTPRequestHandler):
    def send_json(self, payload: object, status: int = 200) -> None:
        encoded = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(status); self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "http://127.0.0.1")
        self.send_header("Content-Length", str(len(encoded))); self.end_headers(); self.wfile.write(encoded)

    def do_GET(self) -> None:  # noqa: N802
        request = urlparse(self.path); query = parse_qs(request.query); vault = notes()
        if request.path == "/health": return self.send_json({"ok": True, "root": str(ROOT)})
        if request.path == "/status": return self.send_json({"notes": len(vault), "canonical_root": "knowledge-base", "write_policy": "pull-request-only"})
        if request.path == "/openapi.json": return self.send_json(OPENAPI)
        if request.path == "/read":
            path = query.get("path", [""])[0]; file = safe_path(path)
            return self.send_json({"path": path, "content": file.read_text(encoding="utf-8")}) if file else self.send_json({"error": "unknown path"}, 404)
        if request.path == "/search":
            terms = query.get("q", [""])[0].lower().split(); result = []
            for path, text in vault.items():
                title = re.search(r"^#\s+(.+)$", text, re.M); haystack = f"{path}\n{text}".lower()
                score = sum(haystack.count(term) for term in terms)
                if score: result.append({"path": path, "title": title.group(1) if title else path, "score": score})
            return self.send_json(sorted(result, key=lambda item: item["score"], reverse=True)[:50])
        if request.path == "/related":
            path = query.get("path", [""])[0]
            if path not in vault: return self.send_json({"error": "unknown path"}, 404)
            stem = pathlib.PurePosixPath(path).stem; related = []
            for other, text in vault.items():
                if other != path and (f"[[{stem}" in text or f"[[{path.removesuffix('.md')}" in text): related.append(other)
            return self.send_json({"path": path, "related": related})
        self.send_json({"error": "not found"}, 404)

    def log_message(self, format: str, *args: object) -> None: pass


OPENAPI = {"openapi": "3.0.3", "info": {"title": "Freight Trust KB Gateway", "version": "0.1.0"}, "paths": {"/health": {"get": {}}, "/status": {"get": {}}, "/search": {"get": {"parameters": [{"name": "q", "in": "query", "required": True}]}}, "/read": {"get": {"parameters": [{"name": "path", "in": "query", "required": True}]}}, "/related": {"get": {"parameters": [{"name": "path", "in": "query", "required": True}]}}}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(); parser.add_argument("--port", type=int, default=8787); args = parser.parse_args()
    print(f"Freight Trust KB Gateway: http://127.0.0.1:{args.port}")
    ThreadingHTTPServer(("127.0.0.1", args.port), Gateway).serve_forever()
