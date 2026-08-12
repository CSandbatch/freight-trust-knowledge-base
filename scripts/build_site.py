"""Build a static, read-only browser for the Freight Trust Markdown vault."""

from __future__ import annotations

import html
import json
import pathlib
import re
import shutil


ROOT = pathlib.Path("knowledge-base")
OUT = pathlib.Path("_site")


def title_and_body(text: str, fallback: str) -> tuple[str, str]:
    body = re.sub(r"^---\r?\n.*?\r?\n---\r?\n", "", text, count=1, flags=re.S)
    title = re.search(r"^#\s+(.+)$", body, flags=re.M)
    return (title.group(1).strip() if title else fallback, body.strip())


def main() -> None:
    if not ROOT.is_dir():
        raise SystemExit("knowledge-base/ is required")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    notes = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        title, body = title_and_body(path.read_text(encoding="utf-8"), path.stem)
        notes.append({"path": rel, "title": title, "text": body})
    (OUT / "notes.json").write_text(json.dumps(notes, ensure_ascii=False), encoding="utf-8")
    (OUT / "index.html").write_text(INDEX, encoding="utf-8")


INDEX = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Freight Trust Knowledge Base</title><style>
:root{color-scheme:dark;--ink:#e8edf2;--muted:#9cabb8;--line:#263746;--accent:#58c4a3;--panel:#10202b}
*{box-sizing:border-box}body{margin:0;background:#09151d;color:var(--ink);font:16px/1.5 system-ui,sans-serif}
header{padding:2rem max(1.25rem,calc((100vw - 1100px)/2));border-bottom:1px solid var(--line)}h1{margin:0;font-size:clamp(1.7rem,4vw,2.5rem)}p{color:var(--muted)}main{display:grid;grid-template-columns:minmax(260px,360px) 1fr;max-width:1100px;margin:auto;min-height:70vh}aside{padding:1rem;border-right:1px solid var(--line)}input{width:100%;background:var(--panel);border:1px solid var(--line);color:var(--ink);padding:.75rem;border-radius:.35rem}.result{display:block;width:100%;text-align:left;background:none;border:0;border-bottom:1px solid var(--line);padding:.8rem 0;color:var(--ink);cursor:pointer}.result small{display:block;color:var(--muted)}article{padding:1.5rem;white-space:pre-wrap;overflow-wrap:anywhere}code{color:var(--accent)}@media(max-width:720px){main{grid-template-columns:1fr}aside{border-right:0;border-bottom:1px solid var(--line)}}</style></head>
<body><header><h1>Freight Trust Knowledge Base</h1><p>Read-only view of the canonical Markdown vault. Search exact titles, paths, IDs, and document text.</p></header>
<main><aside><input id="q" autofocus placeholder="Search the knowledge base"><div id="results"></div></aside><article id="note"><h2>Start here</h2><p>Select a note to read it. This site is a browser surface only; canonical changes are made through Git pull requests.</p></article></main>
<script>let notes=[];const q=document.querySelector('#q'),r=document.querySelector('#results'),n=document.querySelector('#note');
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}function show(x){n.innerHTML='<h2>'+esc(x.title)+'</h2><p><code>'+esc(x.path)+'</code></p>'+esc(x.text)}
function search(){let terms=q.value.toLowerCase().trim().split(/\s+/).filter(Boolean);let found=notes.map(x=>({x,score:terms.reduce((s,t)=>s+(x.title.toLowerCase().includes(t)?8:0)+(x.path.toLowerCase().includes(t)?5:0)+(x.text.toLowerCase().includes(t)?1:0),0)})).filter(x=>!terms.length||x.score).sort((a,b)=>b.score-a.score).slice(0,30);r.innerHTML='';found.forEach(({x})=>{let b=document.createElement('button');b.className='result';b.innerHTML=esc(x.title)+'<small>'+esc(x.path)+'</small>';b.onclick=()=>show(x);r.append(b)})}
fetch('notes.json').then(x=>x.json()).then(x=>{notes=x;search()});q.addEventListener('input',search);</script></body></html>"""


if __name__ == "__main__":
    main()
