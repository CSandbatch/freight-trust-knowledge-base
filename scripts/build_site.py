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
        section = rel.split("/", 1)[0]
        notes.append(
            {
                "path": rel,
                "title": title,
                "text": body,
                "section": section,
                "excerpt": re.sub(r"\s+", " ", body)[:220],
            }
        )
    (OUT / "notes.json").write_text(json.dumps(notes, ensure_ascii=False), encoding="utf-8")
    (OUT / "index.html").write_text(INDEX, encoding="utf-8")


INDEX = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Freight Trust · Knowledge Radar</title><style>
:root{color-scheme:dark;--ink:#f3f7fa;--muted:#93a9b6;--line:#25404d;--aqua:#63e6c2;--blue:#6cb6ff;--panel:#0e202a;--bg:#06131a}*{box-sizing:border-box}body{margin:0;background:radial-gradient(circle at 75% 0,#123547 0,var(--bg) 42rem);color:var(--ink);font:15px/1.5 ui-sans-serif,system-ui,sans-serif}header{max-width:1280px;margin:auto;padding:2rem 1.25rem 1.2rem;display:flex;gap:2rem;justify-content:space-between;align-items:end;border-bottom:1px solid var(--line)}h1{font-size:clamp(1.7rem,4vw,3rem);margin:0;letter-spacing:-.06em}.eyebrow{color:var(--aqua);text-transform:uppercase;letter-spacing:.14em;font-size:.72rem;font-weight:700}.muted{color:var(--muted)}.count{font-variant-numeric:tabular-nums;color:var(--aqua)}main{max-width:1280px;margin:auto;display:grid;grid-template-columns:minmax(280px,390px) 1fr;min-height:75vh}.library{padding:1.2rem;border-right:1px solid var(--line)}input{width:100%;background:#081a23;border:1px solid var(--line);padding:.82rem;color:var(--ink);border-radius:.45rem;font:inherit}.filters{display:flex;gap:.4rem;flex-wrap:wrap;margin:1rem 0}.filter{background:transparent;border:1px solid var(--line);border-radius:99px;padding:.3rem .65rem;color:var(--muted);cursor:pointer}.filter.active,.filter:hover{border-color:var(--aqua);color:var(--aqua)}.results{max-height:57vh;overflow:auto}.result{display:block;width:100%;text-align:left;background:none;border:0;border-bottom:1px solid #1a303b;padding:.85rem .15rem;color:var(--ink);cursor:pointer}.result:hover,.result:focus{background:#102a36}.result small{display:block;color:var(--muted);margin-top:.15rem}.radar{padding:clamp(1.2rem,3vw,2.5rem);position:relative;overflow:hidden}.radar-top{display:flex;justify-content:space-between;gap:1rem;align-items:baseline}.radar h2{margin:0;font-size:1.25rem}.map{height:360px;position:relative;margin:1.3rem 0;background:radial-gradient(circle at center,transparent 0 19%,#15344055 19.2% 19.7%,transparent 20% 38%,#15344055 38.2% 38.7%,transparent 39% 58%,#15344055 58.2% 58.7%,transparent 59%);border:1px solid var(--line);border-radius:1rem}.map:after{content:'';position:absolute;inset:50% auto auto 50%;width:10px;height:10px;background:var(--aqua);border-radius:50%;box-shadow:0 0 25px 8px #63e6c277;transform:translate(-50%,-50%)}.dot{position:absolute;width:9px;height:9px;border:0;border-radius:50%;background:var(--blue);cursor:pointer;transform:translate(-50%,-50%);box-shadow:0 0 0 3px #6cb6ff22}.dot:hover,.dot.selected{background:var(--aqua);box-shadow:0 0 14px 5px #63e6c288}.legend{display:flex;gap:1rem;flex-wrap:wrap;color:var(--muted);font-size:.8rem}.legend i{display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--blue);margin-right:.35rem}article{border:1px solid var(--line);background:#081a23cc;border-radius:1rem;padding:1.35rem;white-space:pre-wrap;overflow-wrap:anywhere;min-height:190px}article h3{margin:0 0 .25rem;color:var(--aqua)}code{color:var(--blue)}.disclaimer{max-width:1280px;margin:auto;padding:1rem 1.25rem 2rem;color:var(--muted);font-size:.82rem}@media(max-width:760px){header{display:block}header p{margin-bottom:0}main{grid-template-columns:1fr}.library{border-right:0;border-bottom:1px solid var(--line)}.results{max-height:23vh}.map{height:260px}}
</style></head><body><header><div><div class="eyebrow">Open research navigation</div><h1>Freight Trust<br>Knowledge Radar</h1></div><p class="muted">Explore the programme as a living constellation. Each point is a document; each orbit is a body of work.</p></header><main><section class="library"><input id="q" autofocus placeholder="Search the vault — titles, paths, claims"><div class="filters" id="filters"></div><div class="results" id="results"></div></section><section class="radar"><div class="radar-top"><h2>Document constellation</h2><span class="count" id="count"></span></div><div class="map" id="map" aria-label="Interactive document map"></div><div class="legend"><span><i></i>document</span><span>Click a point to open its source note</span></div><article id="note"><h3>Start exploring</h3><span class="muted">Search the library or select a point in the constellation. This is a read-only public research browser; canonical updates happen through GitHub pull requests.</span></article></section></main><footer class="disclaimer">Research working materials, drafts, and hypotheses are provided for transparent discussion—not as operational, legal, regulatory, or funding advice.</footer><script>
let notes=[],section='all',selected;const q=document.querySelector('#q'),r=document.querySelector('#results'),map=document.querySelector('#map'),note=document.querySelector('#note'),filters=document.querySelector('#filters'),count=document.querySelector('#count');const esc=s=>s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
function show(x){selected=x.path;location.hash=encodeURIComponent(x.path);note.innerHTML='<h3>'+esc(x.title)+'</h3><code>'+esc(x.path)+'</code><p class="muted">'+esc(x.excerpt)+(x.text.length>x.excerpt.length?'…':'')+'</p><details><summary>Read source note</summary><div>'+esc(x.text)+'</div></details>';render()}
function matches(x){let terms=q.value.toLowerCase().trim().split(/\s+/).filter(Boolean),hay=(x.title+' '+x.path+' '+x.text).toLowerCase();return(section==='all'||x.section===section)&&terms.every(t=>hay.includes(t))}
function render(){let found=notes.filter(matches);count.textContent=found.length+' documents';r.innerHTML='';found.slice(0,45).forEach(x=>{let b=document.createElement('button');b.className='result';b.innerHTML=esc(x.title)+'<small>'+esc(x.section+' · '+x.path)+'</small>';b.onclick=()=>show(x);r.append(b)});map.innerHTML='';found.forEach((x,i)=>{let ring=.18+(i%17)/24,angle=(i*137.508+notes.findIndex(n=>n.path===x.path)*11)*Math.PI/180,b=document.createElement('button');b.className='dot'+(selected===x.path?' selected':'');b.style.left=(50+Math.cos(angle)*ring*92)+'%';b.style.top=(50+Math.sin(angle)*ring*92)+'%';b.title=x.title;b.setAttribute('aria-label',x.title);b.onclick=()=>show(x);map.append(b)})}
function setFilters(){let sections=['all',...new Set(notes.map(x=>x.section))];filters.innerHTML='';sections.forEach(s=>{let b=document.createElement('button');b.className='filter'+(s===section?' active':'');b.textContent=s==='all'?'All systems':s.replace(/^\d+-/,'');b.onclick=()=>{section=s;setFilters();render()};filters.append(b)})}fetch('notes.json').then(x=>x.json()).then(x=>{notes=x;let path=decodeURIComponent(location.hash.slice(1));selected=notes.find(x=>x.path===path)?.path;setFilters();render();if(selected)show(notes.find(x=>x.path===selected))});q.addEventListener('input',render);
</script></body></html>"""


if __name__ == "__main__":
    main()
