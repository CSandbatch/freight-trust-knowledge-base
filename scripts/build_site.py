"""Build a static, accessible knowledge graph for the Markdown vault."""

from __future__ import annotations

import html
import json
import pathlib
import posixpath
import re
import shutil


ROOT = pathlib.Path("knowledge-base")
OUT = pathlib.Path("_site")


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return {}, text
    metadata: dict[str, object] = {}
    current_list: list[str] | None = None
    for line in match.group(1).splitlines():
        if line.startswith("- ") and current_list is not None:
            current_list.append(line[2:].strip().strip("\"'"))
            continue
        current_list = None
        key, separator, value = line.partition(":")
        if not separator:
            continue
        key, value = key.strip(), value.strip()
        if value:
            metadata[key] = value.strip("\"'")
        else:
            current_list = []
            metadata[key] = current_list
    return metadata, text[match.end():]


def title_and_body(text: str, fallback: str) -> tuple[dict[str, object], str, str]:
    metadata, body = parse_frontmatter(text)
    title = re.search(r"^#\s+(.+)$", body, flags=re.M)
    return metadata, (title.group(1).strip() if title else fallback), body.strip()


def main() -> None:
    if not ROOT.is_dir():
        raise SystemExit("knowledge-base/ is required")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    notes: list[dict[str, object]] = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        metadata, title, body = title_and_body(path.read_text(encoding="utf-8"), path.stem)
        tags = metadata.get("tags", [])
        notes.append(
            {
                "path": rel,
                "title": title,
                "text": body,
                "section": rel.split("/", 1)[0],
                "type": str(metadata.get("type", "unknown")),
                "status": str(metadata.get("status", "unknown")),
                "tags": tags if isinstance(tags, list) else [],
                "updated": str(metadata.get("updated", "")),
                "excerpt": re.sub(r"\s+", " ", body)[:260],
            }
        )
    if not notes:
        raise SystemExit("knowledge-base contains no Markdown notes")

    note_paths = {str(note["path"]): str(note["path"]) for note in notes}
    note_paths.update({str(note["path"])[:-3]: str(note["path"]) for note in notes})
    note_names: dict[str, list[str]] = {}
    for note in notes:
        note_names.setdefault(pathlib.PurePosixPath(str(note["path"])).stem, []).append(str(note["path"]))

    def resolve_link(source: str, target: str) -> str | None:
        target = target.split("#", 1)[0].strip().strip("`")
        if not target:
            return None
        relative = posixpath.normpath(posixpath.join(posixpath.dirname(source), target))
        for candidate in (target, target.removesuffix(".md"), relative, relative.removesuffix(".md")):
            if candidate in note_paths:
                return note_paths[candidate]
        matches = note_names.get(pathlib.PurePosixPath(target).stem, [])
        return matches[0] if len(matches) == 1 else None

    incoming = {str(note["path"]): 0 for note in notes}
    for note in notes:
        targets = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", str(note["text"]))
        links = sorted({resolved for target in targets if (resolved := resolve_link(str(note["path"]), target))})
        note["links"] = links
        for link in links:
            incoming[link] += 1
    for note in notes:
        note["incoming"] = incoming[str(note["path"])]
        note["degree"] = len(note["links"]) + int(note["incoming"])

    (OUT / "notes.json").write_text(json.dumps(notes, ensure_ascii=False), encoding="utf-8")
    (OUT / "index.html").write_text(INDEX, encoding="utf-8")
    print(f"Built {len(notes)} notes with {sum(len(note['links']) for note in notes)} resolved links.")


INDEX = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Freight Trust Knowledge Radar</title><style>
:root{--ink:#edf5f7;--muted:#9ab0ba;--line:#294652;--aqua:#50d4b0;--blue:#69b6ff;--panel:#0b1b23;--bg:#061219}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 ui-sans-serif,system-ui,sans-serif}button,input,select{font:inherit}button{color:inherit}header,.shell,footer{max-width:1380px;margin:auto;padding-left:1.25rem;padding-right:1.25rem}header{padding-top:1.7rem;padding-bottom:1.2rem;border-bottom:1px solid var(--line);display:flex;align-items:end;justify-content:space-between;gap:2rem}h1{font-size:2.1rem;line-height:1.08;margin:0;letter-spacing:0}.eyebrow{color:var(--aqua);font-size:.75rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}.muted{color:var(--muted)}.shell{display:grid;grid-template-columns:360px minmax(0,1fr);min-height:78vh}.controls{padding:1.2rem 1.2rem 1.8rem 0;border-right:1px solid var(--line)}.field{display:grid;gap:.35rem;margin-bottom:.75rem;color:var(--muted);font-size:.82rem}input,select{width:100%;background:#091a22;border:1px solid var(--line);border-radius:5px;padding:.64rem;color:var(--ink)}.filters{display:grid;grid-template-columns:1fr 1fr;gap:.65rem}.actions{display:flex;gap:.55rem;margin:1rem 0}.action{background:transparent;border:1px solid var(--line);border-radius:5px;padding:.45rem .6rem;cursor:pointer}.action:hover,.action:focus{border-color:var(--aqua);color:var(--aqua)}.stats{color:var(--muted);font-size:.84rem;margin:.75rem 0}.results{max-height:34vh;overflow:auto;border-top:1px solid var(--line)}.result{display:block;width:100%;text-align:left;background:transparent;border:0;border-bottom:1px solid #1c3540;padding:.75rem .1rem;cursor:pointer}.result:hover,.result:focus{background:#0d2732}.result small{display:block;color:var(--muted);margin-top:.1rem}.graph-area{padding:1.5rem 0 2rem 1.5rem;min-width:0}.graph-head{display:flex;justify-content:space-between;gap:1rem;align-items:baseline}.graph-head h2{font-size:1.2rem;margin:0}.map{height:500px;position:relative;margin:1rem 0;background:#07171f;border:1px solid var(--line);border-radius:6px;overflow:hidden}.edges{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}.edges line{stroke:#5b8798;stroke-opacity:.2;stroke-width:.32}.edges line.related{stroke:var(--aqua);stroke-opacity:.8;stroke-width:.7}.node{position:absolute;border:0;border-radius:50%;background:var(--node);width:var(--size);height:var(--size);transform:translate(-50%,-50%);cursor:pointer;box-shadow:0 0 0 2px color-mix(in srgb,var(--node),transparent 75%)}.node:hover,.node:focus,.node.selected{outline:2px solid var(--aqua);outline-offset:3px}.node.dim{opacity:.14}.legend{display:flex;gap:.75rem;flex-wrap:wrap;color:var(--muted);font-size:.78rem}.key{display:inline-flex;gap:.3rem;align-items:center}.key i{width:8px;height:8px;border-radius:50%;background:var(--key)}.detail{margin-top:1rem;border-top:1px solid var(--line);padding-top:1rem;max-width:900px}.detail h3{margin:0;color:var(--aqua)}.meta{display:flex;gap:.4rem;flex-wrap:wrap;margin:.45rem 0}.chip{border:1px solid var(--line);border-radius:999px;padding:.08rem .45rem;color:var(--muted);font-size:.77rem}.document{max-height:300px;overflow:auto;padding-right:1rem}.document h1,.document h2,.document h3,.document h4{font-size:1rem;margin:1rem 0 .35rem}.document p{margin:.55rem 0}.document ul{padding-left:1.25rem}.document a{color:var(--blue);cursor:pointer;text-decoration:underline}.related{display:flex;gap:.4rem;flex-wrap:wrap;margin-top:.75rem}.related button{background:transparent;border:1px solid var(--line);border-radius:5px;padding:.3rem .45rem;cursor:pointer}.related button:hover{border-color:var(--aqua)}footer{padding-top:1rem;padding-bottom:1.5rem;color:var(--muted);font-size:.8rem;border-top:1px solid var(--line)}@media(max-width:850px){header{display:block}header p{margin-bottom:0}.shell{grid-template-columns:1fr}.controls{padding:1rem 0;border-right:0;border-bottom:1px solid var(--line)}.results{max-height:24vh}.graph-area{padding:1.2rem 0}.map{height:360px}.filters{grid-template-columns:repeat(3,1fr)}}@media(max-width:520px){h1{font-size:1.7rem}.filters{grid-template-columns:1fr 1fr}.map{height:300px}.document{max-height:360px}}
</style></head><body><header><div><div class="eyebrow">Open research navigation</div><h1>Freight Trust Knowledge Radar</h1></div><p class="muted">Search, filter, and trace the document network.</p></header><main class="shell"><aside class="controls" aria-label="Knowledge base filters"><label class="field">Search<input id="q" type="search" placeholder="Titles, paths, and content"></label><div class="filters"><label class="field">Section<select id="section"></select></label><label class="field">Type<select id="type"></select></label><label class="field">Status<select id="status"></select></label><label class="field">Tag<select id="tag"></select></label></div><div class="actions"><button class="action" id="reset" type="button">Reset filters</button><button class="action" id="all" type="button">Show all links</button></div><div class="stats" id="stats"></div><div class="results" id="results" aria-live="polite"></div></aside><section class="graph-area"><div class="graph-head"><h2>Document graph</h2><span class="muted" id="focus"></span></div><div class="map" id="map" aria-label="Interactive document graph"></div><div class="legend" id="legend"></div><article class="detail" id="detail"><h3>Select a document</h3><p class="muted">Choose a result or graph node to inspect it and its direct connections.</p></article></section></main><footer>Research working materials, drafts, and hypotheses are provided for transparent discussion, not operational, legal, regulatory, or funding advice.</footer><script>
const state={notes:[],selected:null,section:'',type:'',status:'',tag:'',query:'',showAll:false};const el=id=>document.getElementById(id);const q=el('q'),map=el('map'),results=el('results'),detail=el('detail'),stats=el('stats'),focus=el('focus');const colors=['#69b6ff','#50d4b0','#f5bd55','#ed8c73','#d99bff','#7ed889','#ff9fc5','#76d4dc','#d7c77d','#ab9bcf','#89a6b8'];const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function options(id,values,label){const select=el(id);select.innerHTML='<option value="">All '+label+'</option>'+values.map(v=>'<option value="'+esc(v)+'">'+esc(v)+'</option>').join('');select.value=state[id]||'';select.onchange=()=>{state[id]=select.value;state.selected=null;sync();render()}}
function selected(){return state.notes.find(n=>n.path===state.selected)}function adjacent(note){return new Set([note.path,...note.links,...state.notes.filter(n=>n.links.includes(note.path)).map(n=>n.path)])}
function filtered(){const terms=state.query.toLowerCase().trim().split(/\s+/).filter(Boolean);return state.notes.filter(n=>(!state.section||n.section===state.section)&&(!state.type||n.type===state.type)&&(!state.status||n.status===state.status)&&(!state.tag||n.tags.includes(state.tag))&&terms.every(t=>(n.title+' '+n.path+' '+n.text+' '+n.tags.join(' ')).toLowerCase().includes(t)))}
function positions(notes){const sections=[...new Set(state.notes.map(n=>n.section))], out=new Map();sections.forEach((section,index)=>{const group=notes.filter(n=>n.section===section);const angle=index*2*Math.PI/sections.length-Math.PI/2;const cx=50+Math.cos(angle)*32,cy=50+Math.sin(angle)*32;group.forEach((n,i)=>{const a=i*2.39996;const radius=4+Math.sqrt(i)*3.5;out.set(n.path,[cx+Math.cos(a)*radius,cy+Math.sin(a)*radius])})});return out}
function markdown(text){let out=esc(text).replace(/^---[\s\S]*?---\s*/,'');out=out.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g,(_,path,label)=>'<a data-note="'+esc(path)+'">'+esc(label||path.split('/').pop())+'</a>');out=out.replace(/^#### (.+)$/gm,'<h4>$1</h4>').replace(/^### (.+)$/gm,'<h3>$1</h3>').replace(/^## (.+)$/gm,'<h2>$1</h2>').replace(/^# (.+)$/gm,'<h1>$1</h1>').replace(/\*\*(.+?)\*\*/g,'<strong>$1</strong>').replace(/`([^`]+)`/g,'<code>$1</code>');out=out.replace(/^(?:- |\* )(.+)$/gm,'<li>$1</li>').replace(/(<li>[\s\S]*?<\/li>)(?:\n(?!<li>))/g,'$1\n');out=out.replace(/(?:<li>.*<\/li>\n?)+/g,m=>'<ul>'+m+'</ul>');return out.split(/\n{2,}/).map(block=>/^<(h[1-4]|ul)/.test(block)?block:'<p>'+block.replace(/\n/g,'<br>')+'</p>').join('')}
function show(note){state.selected=note.path;state.showAll=false;sync();render()}
function sync(){const params=new URLSearchParams();for(const key of ['section','type','status','tag','query'])if(state[key])params.set(key,state[key]);if(state.selected)params.set('note',state.selected);history.replaceState(null,'','?'+params.toString())}
function renderDetail(note){if(!note){detail.innerHTML='<h3>Select a document</h3><p class="muted">Choose a result or graph node to inspect it and its direct connections.</p>';return}const linked=[...new Set([...note.links,...state.notes.filter(n=>n.links.includes(note.path)).map(n=>n.path)])].map(path=>state.notes.find(n=>n.path===path)).filter(Boolean);detail.innerHTML='<h3>'+esc(note.title)+'</h3><div class="meta"><span class="chip">'+esc(note.section.replace(/^\d+-/,''))+'</span><span class="chip">'+esc(note.type)+'</span><span class="chip">'+esc(note.status)+'</span><span class="chip">'+note.degree+' connections</span></div><div class="document">'+markdown(note.text)+'</div><div class="related">'+linked.map(n=>'<button data-path="'+esc(n.path)+'">'+esc(n.title)+'</button>').join('')+'</div>';detail.querySelectorAll('[data-path]').forEach(button=>button.onclick=()=>show(state.notes.find(n=>n.path===button.dataset.path)));detail.querySelectorAll('a[data-note]').forEach(link=>link.onclick=()=>{const target=state.notes.find(n=>n.path===link.dataset.note||n.path.replace(/\.md$/,'')===link.dataset.note);if(target)show(target)})}
function render(){const visible=filtered(),note=selected(),neighbors=note?adjacent(note):new Set(),pos=positions(visible);stats.textContent=visible.length+' of '+state.notes.length+' documents';focus.textContent=note?(neighbors.size-1)+' direct connections':'Select a node to focus';results.innerHTML=visible.slice(0,80).map(n=>'<button class="result" data-path="'+esc(n.path)+'"><strong>'+esc(n.title)+'</strong><small>'+esc(n.section+' / '+n.type+' / '+n.degree+' connections')+'</small></button>').join('');results.querySelectorAll('button').forEach(button=>button.onclick=()=>show(state.notes.find(n=>n.path===button.dataset.path)));map.innerHTML='';const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.setAttribute('class','edges');visible.forEach(n=>n.links.filter(path=>pos.has(path)&&n.path<path).forEach(path=>{const a=pos.get(n.path),b=pos.get(path),line=document.createElementNS(svg.namespaceURI,'line');line.setAttribute('x1',a[0]+'%');line.setAttribute('y1',a[1]+'%');line.setAttribute('x2',b[0]+'%');line.setAttribute('y2',b[1]+'%');if(note&&neighbors.has(n.path)&&neighbors.has(path))line.setAttribute('class','related');svg.append(line)}));map.append(svg);visible.forEach(n=>{const p=pos.get(n.path),button=document.createElement('button'),color=colors[[...new Set(state.notes.map(x=>x.section))].indexOf(n.section)%colors.length];button.className='node'+(n.path===state.selected?' selected':'')+(note&&!state.showAll&&!neighbors.has(n.path)?' dim':'');button.style.left=p[0]+'%';button.style.top=p[1]+'%';button.style.setProperty('--node',color);button.style.setProperty('--size',(7+Math.min(n.degree,18)/3)+'px');button.title=n.title+' ('+n.degree+' connections)';button.setAttribute('aria-label',button.title);button.onclick=()=>show(n);map.append(button)});renderDetail(note)}
fetch('notes.json').then(r=>{if(!r.ok)throw new Error('Unable to load document index');return r.json()}).then(notes=>{state.notes=notes;const params=new URLSearchParams(location.search);for(const key of ['section','type','status','tag','query','note'])state[key==='note'?'selected':key]=params.get(key)||'';q.value=state.query;options('section',[...new Set(notes.map(n=>n.section))],'sections');options('type',[...new Set(notes.map(n=>n.type))].sort(),'types');options('status',[...new Set(notes.map(n=>n.status))].sort(),'statuses');options('tag',[...new Set(notes.flatMap(n=>n.tags))].sort(),'tags');el('legend').innerHTML=[...new Set(notes.map(n=>n.section))].map((s,i)=>'<span class="key"><i style="--key:'+colors[i%colors.length]+'"></i>'+esc(s.replace(/^\d+-/,''))+'</span>').join('');q.oninput=()=>{state.query=q.value;state.selected=null;sync();render()};el('reset').onclick=()=>{state.section=state.type=state.status=state.tag=state.query=state.selected='';q.value='';for(const id of ['section','type','status','tag'])el(id).value='';sync();render()};el('all').onclick=()=>{state.showAll=true;render()};render()}).catch(error=>{stats.textContent=error.message;console.error(error)});
</script></body></html>"""


if __name__ == "__main__":
    main()
