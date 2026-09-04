"""Serve the static Atlas and a narrow, read-only Hermes chat gateway.

The browser never receives an OpenRouter or Hermes credential and cannot select a
model or tools.  Knowledge retrieval happens here; the public Hermes instance has
all toolsets disabled so an anonymous prompt cannot reach a shell or write files.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import pathlib
import re
import secrets
import shutil
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import defaultdict, deque
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlsplit


ROOT = pathlib.Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
SEARCH_INDEX = SITE / "data" / "search.json"
HERMES_CONFIG = ROOT / "config" / "hermes-replit.yaml"
MODEL = "z-ai/glm-5.3-flash"
MAX_BODY = 2_000_000
MAX_MESSAGES = 20
MAX_MESSAGE_CHARS = 8_000
MAX_TOTAL_CHARS = 40_000
MAX_CONTEXT_CHARS = 14_000
RATE_WINDOW_SECONDS = 60
RATE_LIMIT = 20
SYSTEM_PROMPT = """You are the BellHill Freight Trust Knowledge Agent, powered only by
z-ai/glm-5.3-flash through the NousResearch Hermes Agent framework. Answer from the
retrieved public knowledge-base context below. Cite supporting notes using the supplied
Markdown links. If the context does not support an answer, say so plainly. Distinguish
verified evidence from BellHill analysis, hypotheses, drafts, and unresolved facts. Never
claim partnership, endorsement, data access, legal eligibility, or experimental results
unless the supplied context explicitly establishes it. The corpus is a working research
record, not legal, regulatory, financial, or operational advice."""


def _words(value: str) -> set[str]:
    return {word for word in re.findall(r"[a-z0-9][a-z0-9_-]{1,}", value.lower()) if len(word) > 2}


def retrieve(query: str, index_path: pathlib.Path = SEARCH_INDEX, limit: int = 5) -> tuple[str, list[dict[str, str]]]:
    """Return bounded excerpts and source metadata from the generated public index."""
    try:
        payload = json.loads(index_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return "No knowledge-base excerpts were available for this request.", []
    documents = payload.get("documents", payload if isinstance(payload, list) else [])
    if not isinstance(documents, list):
        return "No knowledge-base excerpts were available for this request.", []
    terms = _words(query)
    phrase = query.strip().lower()
    ranked: list[tuple[int, dict[str, object]]] = []
    for document in documents:
        if not isinstance(document, dict):
            continue
        title = str(document.get("title", ""))
        headings = str(document.get("headings", ""))
        body = str(document.get("body", ""))
        haystack = f"{title} {headings} {body}".lower()
        score = sum(7 for term in terms if term in title.lower())
        score += sum(3 for term in terms if term in headings.lower())
        score += sum(1 for term in terms if term in haystack)
        if phrase and len(phrase) > 6 and phrase in haystack:
            score += 12
        if score:
            ranked.append((score, document))
    ranked.sort(key=lambda item: (-item[0], str(item[1].get("title", ""))))
    excerpts: list[str] = []
    sources: list[dict[str, str]] = []
    used = 0
    for _, document in ranked[:limit]:
        title = str(document.get("title", "Untitled note"))
        url = str(document.get("url") or document.get("path") or "")
        if url and not url.startswith(("http://", "https://", "/")):
            url = "/" + url.lstrip("./")
        body = re.sub(r"\s+", " ", str(document.get("body", ""))).strip()
        excerpt = body[: min(2_800, MAX_CONTEXT_CHARS - used)]
        if not excerpt:
            continue
        status = str(document.get("status", "unclassified"))
        block = f"SOURCE: {title}\nLINK: {url}\nSTATUS: {status}\nEXCERPT: {excerpt}"
        excerpts.append(block)
        sources.append({"title": title, "url": url, "status": status})
        used += len(block)
        if used >= MAX_CONTEXT_CHARS:
            break
    if not excerpts:
        return "No directly relevant excerpt was located in the public knowledge base.", []
    return "\n\n---\n\n".join(excerpts), sources


def _image_part(part: object) -> dict[str, object] | None:
    if not isinstance(part, dict) or part.get("type") != "image_url":
        return None
    image = part.get("image_url")
    url = image.get("url") if isinstance(image, dict) else None
    if not isinstance(url, str) or not re.fullmatch(r"data:image/(?:png|jpeg|webp);base64,[A-Za-z0-9+/=]+", url):
        return None
    if len(url) > 1_500_000:
        return None
    try:
        base64.b64decode(url.split(",", 1)[1], validate=True)
    except (ValueError, base64.binascii.Error):
        return None
    return {"type": "image_url", "image_url": {"url": url}}


def sanitize_messages(value: object) -> tuple[list[dict[str, object]], str]:
    if not isinstance(value, list) or not value or len(value) > MAX_MESSAGES:
        raise ValueError(f"messages must contain 1-{MAX_MESSAGES} items")
    clean: list[dict[str, object]] = []
    total = 0
    latest_user = ""
    for item in value:
        if not isinstance(item, dict) or item.get("role") not in {"user", "assistant"}:
            raise ValueError("only user and assistant messages are accepted")
        role = str(item["role"])
        content = item.get("content")
        if isinstance(content, str):
            text = content.strip()
            if not text or len(text) > MAX_MESSAGE_CHARS:
                raise ValueError("message text is empty or too long")
            safe_content: object = text
        elif isinstance(content, list):
            safe_parts: list[dict[str, object]] = []
            text_parts: list[str] = []
            for part in content:
                if isinstance(part, dict) and part.get("type") == "text" and isinstance(part.get("text"), str):
                    text = str(part["text"]).strip()
                    if text:
                        text_parts.append(text)
                        safe_parts.append({"type": "text", "text": text})
                else:
                    image = _image_part(part)
                    if image:
                        safe_parts.append(image)
            if not safe_parts or sum(len(text) for text in text_parts) > MAX_MESSAGE_CHARS:
                raise ValueError("multimodal message is invalid or too long")
            safe_content = safe_parts
            text = " ".join(text_parts)
        else:
            raise ValueError("message content must be text or supported multimodal content")
        total += len(text)
        if total > MAX_TOTAL_CHARS:
            raise ValueError("conversation is too long")
        if role == "user" and text:
            latest_user = text
        clean.append({"role": role, "content": safe_content})
    if not latest_user:
        raise ValueError("a user message is required")
    return clean, latest_user


class RateLimiter:
    def __init__(self) -> None:
        self.hits: defaultdict[str, deque[float]] = defaultdict(deque)
        self.lock = threading.Lock()

    def allow(self, key: str) -> bool:
        now = time.monotonic()
        with self.lock:
            bucket = self.hits[key]
            while bucket and now - bucket[0] > RATE_WINDOW_SECONDS:
                bucket.popleft()
            if len(bucket) >= RATE_LIMIT:
                return False
            bucket.append(now)
            return True


class AtlasHandler(BaseHTTPRequestHandler):
    server_version = "BellHillAtlas/1.0"
    limiter = RateLimiter()
    slots = threading.BoundedSemaphore(4)

    def _headers(self, status: int, content_type: str, length: int, cache: str = "no-store") -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(length))
        self.send_header("Cache-Control", cache)
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "strict-origin-when-cross-origin")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Content-Security-Policy", "default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'")
        self.end_headers()

    def _json(self, status: int, value: object) -> None:
        data = json.dumps(value, ensure_ascii=False).encode("utf-8")
        self._headers(status, "application/json; charset=utf-8", len(data))
        self.wfile.write(data)

    def _client_key(self) -> str:
        if os.environ.get("REPL_ID"):
            forwarded = self.headers.get("X-Forwarded-For", "").split(",", 1)[0].strip()
            if forwarded:
                return forwarded[:80]
        return self.client_address[0]

    def do_POST(self) -> None:  # noqa: N802
        if urlsplit(self.path).path != "/api/chat":
            self._json(HTTPStatus.NOT_FOUND, {"error": "not found"})
            return
        if not self.limiter.allow(self._client_key()):
            self._json(HTTPStatus.TOO_MANY_REQUESTS, {"error": "rate limit exceeded; try again shortly"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        if length <= 0 or length > MAX_BODY or "application/json" not in self.headers.get("Content-Type", ""):
            self._json(HTTPStatus.BAD_REQUEST, {"error": "a bounded application/json body is required"})
            return
        try:
            body = json.loads(self.rfile.read(length))
            messages, latest_user = sanitize_messages(body.get("messages") if isinstance(body, dict) else None)
        except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as exc:
            self._json(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
            return
        context, sources = retrieve(latest_user, pathlib.Path(getattr(self.server, "search_index", SEARCH_INDEX)))
        upstream_messages = [{"role": "system", "content": f"{SYSTEM_PROMPT}\n\nRETRIEVED CONTEXT\n{context}"}, *messages]
        if not self.slots.acquire(blocking=False):
            self._json(HTTPStatus.SERVICE_UNAVAILABLE, {"error": "the agent is busy; try again shortly"})
            return
        try:
            response = self._call_hermes(upstream_messages)
        finally:
            self.slots.release()
        if isinstance(response, tuple):
            self._json(response[0], {"error": response[1]})
            return
        self._json(HTTPStatus.OK, {"message": response, "sources": sources, "model": MODEL})

    def _call_hermes(self, messages: list[dict[str, object]]) -> str | tuple[int, str]:
        base = getattr(self.server, "hermes_url", "http://127.0.0.1:8642").rstrip("/")
        key = getattr(self.server, "hermes_key", "")
        payload = json.dumps({"model": "hermes-agent", "messages": messages, "stream": False}).encode("utf-8")
        request = urllib.request.Request(
            f"{base}/v1/chat/completions", data=payload, method="POST",
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
        )
        try:
            with urllib.request.urlopen(request, timeout=90) as upstream:
                value = json.loads(upstream.read())
            content = value["choices"][0]["message"]["content"]
            if not isinstance(content, str):
                raise ValueError("invalid content")
            return content
        except urllib.error.HTTPError as exc:
            return HTTPStatus.BAD_GATEWAY, f"Hermes rejected the request ({exc.code})."
        except (urllib.error.URLError, TimeoutError):
            return HTTPStatus.SERVICE_UNAVAILABLE, "Hermes is unavailable. Please try again shortly."
        except (json.JSONDecodeError, KeyError, IndexError, TypeError, ValueError):
            return HTTPStatus.BAD_GATEWAY, "Hermes returned an invalid response."

    def do_GET(self) -> None:  # noqa: N802
        path = urlsplit(self.path).path
        if path == "/healthz":
            self._json(HTTPStatus.OK, {"status": "ok", "model": MODEL, "site": SITE.joinpath("index.html").is_file()})
            return
        if path.startswith("/api/") or path.startswith("/v1/"):
            self._json(HTTPStatus.NOT_FOUND, {"error": "not found"})
            return
        self._serve_static(path, head=False)

    def do_HEAD(self) -> None:  # noqa: N802
        self._serve_static(urlsplit(self.path).path, head=True)

    def _serve_static(self, request_path: str, head: bool) -> None:
        relative = unquote(request_path).lstrip("/") or "index.html"
        candidate = (SITE / relative).resolve()
        try:
            candidate.relative_to(SITE.resolve())
        except ValueError:
            self._json(HTTPStatus.NOT_FOUND, {"error": "not found"})
            return
        if candidate.is_dir():
            candidate = candidate / "index.html"
        if not candidate.is_file():
            self._json(HTTPStatus.NOT_FOUND, {"error": "not found"})
            return
        data = candidate.read_bytes()
        kind = mimetypes.guess_type(candidate.name)[0] or "application/octet-stream"
        cache = "public, max-age=31536000, immutable" if "/assets/" in candidate.as_posix() else "public, max-age=300"
        self._headers(HTTPStatus.OK, kind, len(data), cache)
        if not head:
            self.wfile.write(data)

    def log_message(self, fmt: str, *args: object) -> None:
        sys.stderr.write(f"{self.address_string()} - {fmt % args}\n")


def build_site() -> None:
    site_url = os.environ.get("PUBLIC_SITE_URL", "").strip()
    if not site_url:
        replit_domain = os.environ.get("REPLIT_DOMAINS", "").split(",", 1)[0].strip()
        if replit_domain:
            site_url = f"https://{replit_domain}/"
        else:
            development_domain = os.environ.get("REPLIT_DEV_DOMAIN", "").strip()
            site_url = f"https://{development_domain}/" if development_domain else "https://example.invalid/"
    if not site_url.endswith("/"):
        site_url += "/"
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_site.py"), "--site-url", site_url], cwd=ROOT, check=True)


def start_hermes() -> tuple[subprocess.Popen[bytes], str, str]:
    if not os.environ.get("OPENROUTER_API_KEY"):
        raise RuntimeError("OPENROUTER_API_KEY is required to start Hermes")
    executable = shutil.which("hermes")
    if not executable:
        raise RuntimeError("Hermes is not installed; install requirements-replit.txt")
    home = pathlib.Path(os.environ.get("BELLHILL_HERMES_HOME") or str(ROOT / ".hermes-runtime")).resolve()
    home.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERMES_CONFIG, home / "config.yaml")
    key = os.environ.get("API_SERVER_KEY") or secrets.token_urlsafe(32)
    port = os.environ.get("HERMES_PORT", "8642")
    environment = os.environ.copy()
    environment.update({
        "HERMES_HOME": str(home), "OPENROUTER_MODEL": MODEL,
        "API_SERVER_ENABLED": "true", "API_SERVER_HOST": "127.0.0.1",
        "API_SERVER_PORT": port, "API_SERVER_KEY": key,
        "API_SERVER_MODEL_NAME": "hermes-agent",
    })
    process = subprocess.Popen([executable, "gateway"], cwd=ROOT, env=environment)
    base = f"http://127.0.0.1:{port}"
    deadline = time.monotonic() + 45
    while time.monotonic() < deadline:
        if process.poll() is not None:
            raise RuntimeError(f"Hermes stopped during startup with code {process.returncode}")
        try:
            with urllib.request.urlopen(f"{base}/health", timeout=1):
                return process, base, key
        except (urllib.error.URLError, TimeoutError):
            time.sleep(0.5)
    process.terminate()
    raise RuntimeError("Hermes did not become healthy within 45 seconds")


def main() -> int:
    try:
        from dotenv import load_dotenv

        load_dotenv(ROOT / ".env", override=False)
    except ImportError:
        pass
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build", action="store_true", help="rebuild _site before serving")
    parser.add_argument("--start-hermes", action="store_true", help="start the private Hermes gateway")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "3000")))
    parser.add_argument("--hermes-url", default=os.environ.get("HERMES_URL", "http://127.0.0.1:8642"))
    args = parser.parse_args()
    if args.build or not SITE.joinpath("index.html").is_file():
        build_site()
    process: subprocess.Popen[bytes] | None = None
    hermes_url = args.hermes_url
    hermes_key = os.environ.get("API_SERVER_KEY", "")
    try:
        if args.start_hermes:
            process, hermes_url, hermes_key = start_hermes()
        server = ThreadingHTTPServer((args.host, args.port), AtlasHandler)
        server.hermes_url = hermes_url  # type: ignore[attr-defined]
        server.hermes_key = hermes_key  # type: ignore[attr-defined]
        server.search_index = SEARCH_INDEX  # type: ignore[attr-defined]
        print(f"BellHill Atlas listening on http://{args.host}:{args.port} with {MODEL}")
        server.serve_forever()
    except KeyboardInterrupt:
        return 0
    finally:
        if process and process.poll() is None:
            process.terminate()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
