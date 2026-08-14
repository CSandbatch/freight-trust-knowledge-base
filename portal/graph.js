/* Deterministic SVG atlas graph. Positions come from the build, never a browser force loop. */
(() => {
  const app = document.querySelector("[data-graph]");
  if (!app) return;
  const body = document.body;
  const root = new URL(body.dataset.root || "index.html", window.location.href);
  const urlFor = (route) => new URL(route, root).href;
  const escapeHtml = (value) => String(value ?? "").replace(/[&<>"']/g, (character) => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[character]));
  const canvas = app.querySelector("[data-graph-canvas]");
  const inspector = app.querySelector("[data-graph-inspector]");
  const navigatorList = app.querySelector("[data-graph-list]");
  const count = app.querySelector("[data-graph-count]");
  const legend = app.querySelector("[data-graph-legend]");
  const mode = app.querySelector("[data-graph-mode]");
  const search = app.querySelector("[data-graph-search]");
  const depth = app.querySelector("[data-graph-depth]");
  const edgesToggle = app.querySelector("[data-graph-edges]");
  const filters = [...app.querySelectorAll("[data-graph-filter]")];
  const color = {source:"#2778e3",method:"#2faeaa",moc:"#7c5fd6",agent:"#d86555",experiment:"#dc9b25",dataset:"#547c56",brief:"#2778e3",draft:"#dc9b25",evidence:"#2faeaa",policy:"#7c5fd6",archive:"#777"};
  const statusColor = {active:"#0b2a3d",current:"#2faeaa",draft:"#dc9b25",planned:"#2778e3",candidate:"#7c5fd6",stretch:"#7c5fd6","to-build":"#2778e3","partner-dependent":"#d86555",superseded:"#7c5fd6",frozen:"#7c5fd6",required:"#547c56"};
  const getParams = () => new URLSearchParams(location.search);
  const writeParams = (state) => { const next = getParams(); Object.entries(state).forEach(([key,value]) => value ? next.set(key,value) : next.delete(key)); history.replaceState(null,"",`${location.pathname}${next.toString()?`?${next}`:""}`); };
  fetch(app.dataset.graphUrl).then((response) => response.json()).then((graph) => {
    const nodes = graph.nodes || []; const edges = graph.edges || []; const byId = new Map(nodes.map((node) => [node.id,node]));
    nodes.forEach((node) => { node._atlasX = Number(node.x); node._atlasY = Number(node.y); });
    const incoming = new Map(nodes.map((node) => [node.id,[]])); const outgoing = new Map(nodes.map((node) => [node.id,[]]));
    edges.forEach((edge) => { if (byId.has(edge.source) && byId.has(edge.target)) { outgoing.get(edge.source).push(edge); incoming.get(edge.target).push(edge); }});
    const populate = (element, values) => { element.insertAdjacentHTML("beforeend", [...new Set(values)].filter(Boolean).sort().map((value) => `<option value="${escapeHtml(value)}">${escapeHtml(value)}</option>`).join("")); };
    populate(filters.find((item) => item.dataset.graphFilter === "collection"), nodes.map((node) => node.section));
    populate(filters.find((item) => item.dataset.graphFilter === "type"), nodes.map((node) => node.type));
    populate(filters.find((item) => item.dataset.graphFilter === "status"), nodes.map((node) => node.status));
    const initial = getParams(); mode.value = initial.get("mode") || "global"; depth.value = initial.get("depth") || "1"; search.value = "";
    filters.forEach((filter) => { filter.value = initial.get(filter.dataset.graphFilter) || ""; });
    let focus = initial.get("focus") && byId.has(initial.get("focus")) ? initial.get("focus") : null;
    const neighborhood = (start, hops) => {
      if (!start || !byId.has(start)) return {distances:new Map(), paths:[]};
      const distances = new Map([[start,0]]); const paths = []; const queue = [start];
      while (queue.length) {
        const current = queue.shift(); const currentDepth = distances.get(current) || 0;
        if (currentDepth >= hops) continue;
        const adjacent = [...outgoing.get(current), ...incoming.get(current)].slice().sort((a,b) => {
          const aTarget = a.source === current ? a.target : a.source;
          const bTarget = b.source === current ? b.target : b.source;
          return aTarget.localeCompare(bTarget) || a.source.localeCompare(b.source);
        });
        adjacent.forEach((edge) => {
          const target = edge.source === current ? edge.target : edge.source;
          if (distances.has(target)) return;
          distances.set(target, currentDepth + 1); paths.push(edge); queue.push(target);
        });
      }
      return {distances, paths};
    };
    const selectedEdges = (visible) => edges.filter((edge) => visible.has(edge.source) && visible.has(edge.target));
    const localPositions = (visibleNodes, distances) => {
      const positions = new Map();
      if (!focus || !byId.has(focus)) return positions;
      positions.set(focus, {x:500,y:350});
      const levels = new Map();
      visibleNodes.filter((node) => node.id !== focus).forEach((node) => {
        const level = distances.get(node.id) || 1;
        levels.set(level, [...(levels.get(level) || []), node]);
      });
      levels.forEach((members, level) => {
        const ordered = members.slice().sort((a,b) => a.source.localeCompare(b.source));
        const capacity = level === 1 ? 42 : 54;
        const baseRadius = level === 1 ? 112 : level === 2 ? 262 : 322;
        ordered.forEach((node, index) => {
          const layer = Math.floor(index / capacity); const first = layer * capacity;
          const count = Math.min(capacity, ordered.length - first);
          const angle = -Math.PI / 2 + (index - first) * (Math.PI * 2 / count);
          const radius = Math.min(326, baseRadius + layer * (level === 1 ? 36 : 28));
          positions.set(node.id, {x:Math.round((500 + Math.cos(angle) * radius) * 100) / 100,y:Math.round((350 + Math.sin(angle) * radius) * 100) / 100});
        });
      });
      return positions;
    };
    const render = () => {
      nodes.forEach((node) => { node.x = node._atlasX; node.y = node._atlasY; });
      const state = Object.fromEntries(filters.map((filter) => [filter.dataset.graphFilter,filter.value]));
      const query = search.value.trim().toLowerCase(); const local = mode.value === "local" && Boolean(focus);
      let visible = new Set(nodes.filter((node) => (!state.collection || node.section === state.collection) && (!state.type || node.type === state.type) && (!state.status || node.status === state.status) && (!query || `${node.label} ${node.source} ${node.tags.join(" ")}`.toLowerCase().includes(query))).map((node)=>node.id));
      const localGraph = local ? neighborhood(focus, Number(depth.value)) : null;
      if (localGraph) visible = new Set([...visible].filter((id) => localGraph.distances.has(id)));
      const visibleNodes = nodes.filter((node) => visible.has(node.id));
      const inducedEdges = selectedEdges(visible);
      // A local view is a readable traversal, not an induced-subgraph hairball. Every
      // visible node retains its complete relationship list in the inspector and
      // semantic navigator; the SVG shows one deterministic discovery path per node.
      const drawEdges = localGraph ? localGraph.paths.filter((edge) => visible.has(edge.source) && visible.has(edge.target)) : inducedEdges;
      const positions = localGraph ? localPositions(visibleNodes, localGraph.distances) : new Map(visibleNodes.map((node) => [node.id,{x:Number(node.x),y:Number(node.y)}]));
      if (localGraph) visibleNodes.forEach((node) => { const point = positions.get(node.id); if (point) { node.x = point.x; node.y = point.y; } });
      const highlighted = focus ? new Set([focus,...(outgoing.get(focus)||[]).map((edge)=>edge.target),...(incoming.get(focus)||[]).map((edge)=>edge.source)]) : new Set();
      canvas.innerHTML = "";
      canvas.dataset.local = String(Boolean(localGraph));
      const ns = "http://www.w3.org/2000/svg";
      if (!local && !focus) {
        const groups = new Map();
        visibleNodes.forEach((node) => groups.set(node.section, [...(groups.get(node.section) || []), node]));
        groups.forEach((members, section) => {
          const label = document.createElementNS(ns, "text");
          const minX = Math.min(...members.map((node) => positions.get(node.id).x));
          const minY = Math.min(...members.map((node) => positions.get(node.id).y));
          label.setAttribute("x", Math.max(8, minX - 5));
          label.setAttribute("y", Math.max(13, minY - 11));
          label.setAttribute("class", "collection-label");
          label.textContent = section;
          canvas.append(label);
        });
      }
      if (edgesToggle.checked || focus || local) drawEdges.forEach((edge) => { const a=positions.get(edge.source),b=positions.get(edge.target); if (!a || !b) return; const line=document.createElementNS(ns,"line"); line.setAttribute("x1",a.x);line.setAttribute("y1",a.y);line.setAttribute("x2",b.x);line.setAttribute("y2",b.y);line.setAttribute("class",`edge ${focus && (edge.source===focus||edge.target===focus)?"is-highlighted":""}`);canvas.append(line); });
      visibleNodes.forEach((node) => { const circle=document.createElementNS(ns,"circle"); const radius=Math.max(3.8,Math.min(9,3.7+Math.sqrt(node.degree||0))); circle.setAttribute("cx",node.x);circle.setAttribute("cy",node.y);circle.setAttribute("r",radius);circle.setAttribute("fill",color[node.type]||"#6b8794");circle.setAttribute("stroke",statusColor[node.status]||"#f6f3eb");circle.setAttribute("class",`node ${focus===node.id?"is-selected":""} ${focus&&!highlighted.has(node.id)?"is-dim":""}`);circle.setAttribute("tabindex","-1");circle.setAttribute("aria-label",node.label);circle.addEventListener("click",()=>{focus=node.id;mode.value="local";render();});circle.addEventListener("mouseenter",()=>{if(!focus){inspector.innerHTML=`<p class=eyebrow>Hover</p><h2>${escapeHtml(node.label)}</h2><p>${escapeHtml(`${node.type} · ${node.section} · ${node.degree} connections`)}</p>`;}});canvas.append(circle); if (focus===node.id) {const label=document.createElementNS(ns,"text");label.setAttribute("x",Number(node.x)+8);label.setAttribute("y",Number(node.y)-6);label.setAttribute("class","node-label");label.textContent=node.label.slice(0,42);canvas.append(label);} });
      navigatorList.innerHTML = visibleNodes.map((node) => `<li class="${focus===node.id?"is-selected":""}"><a href="${escapeHtml(urlFor(node.url))}" data-graph-node="${escapeHtml(node.id)}">${escapeHtml(node.label)}</a><small>${escapeHtml(`${node.type} · ${node.section} · ${node.degree} links`)}</small></li>`).join("");
      navigatorList.querySelectorAll("[data-graph-node]").forEach((link) => link.addEventListener("click", (event) => { if (event.metaKey || event.ctrlKey) return; event.preventDefault(); focus=link.dataset.graphNode;mode.value="local";render(); }));
      count.textContent = `${visibleNodes.length} nodes · ${drawEdges.length} authored links${focus?" · focus set":""}`;
      const types = [...new Set(visibleNodes.map((node)=>node.type))].sort();
      if (localGraph) count.textContent = `${visibleNodes.length} nodes / ${drawEdges.length} focus-path links shown / ${inducedEdges.length} authored links in neighborhood`;
      legend.innerHTML = types.slice(0,12).map((type)=>`<span><i style="--dot:${color[type]||"#6b8794"}"></i>${escapeHtml(type)}</span>`).join("") + (types.length>12?`<span>+${types.length-12} more types</span>`:"") + `<span>color = type · ring = state · position = ${localGraph ? "relationship distance" : "collection"}</span>`;
      if (focus && byId.has(focus)) { const node=byId.get(focus); const related=(collection)=>collection.map((edge)=>byId.get(edge.source===node.id?edge.target:edge.source)).filter(Boolean); const list=(items)=>items.length?`<ul>${items.slice(0,12).map((item)=>`<li><a href="${escapeHtml(urlFor(item.url))}">${escapeHtml(item.label)}</a></li>`).join("")}</ul>`:"<p>No authored links.</p>"; inspector.innerHTML=`<p class=eyebrow>${escapeHtml(`${node.type} · ${node.section}`)}</p><h2>${escapeHtml(node.label)}</h2><p>${escapeHtml(node.source)}</p><div class=badge-row><span class="badge badge-status">${escapeHtml(node.status)}</span><span class="badge">${node.degree} connections</span></div><div class=inspector-actions><a class="button" href="${escapeHtml(urlFor(node.url))}">Open reader</a><a class="button button-quiet" href="${escapeHtml(urlFor(node.raw_url))}" download>Download raw</a><button class="button button-quiet" type=button data-graph-copy>Copy graph link</button></div><div class=inspector-links><div><p class=eyebrow>Outgoing</p>${list(related(outgoing.get(node.id)||[]))}</div><div><p class=eyebrow>Backlinks</p>${list(related(incoming.get(node.id)||[]))}</div></div>`; inspector.querySelector("[data-graph-copy]")?.addEventListener("click",async(event)=>{const next=new URL(location.href);next.searchParams.set("focus",node.id);next.searchParams.set("mode","local");try{await navigator.clipboard.writeText(next.href);event.currentTarget.textContent="Copied";}catch{event.currentTarget.textContent="Copy unavailable";}}); } else { inspector.innerHTML="<p class=eyebrow>Inspector</p><h2>Select an artifact</h2><p>Click a node or use the navigator below to inspect its authored links and backlinks.</p>"; }
      writeParams({focus:focus||"",mode:mode.value,depth:depth.value,collection:state.collection,type:state.type,status:state.status});
    };
    [mode,search,depth,edgesToggle,...filters].forEach((input)=>input.addEventListener(input.type==="search"?"input":"change",render));
    app.querySelector("[data-graph-reset]").addEventListener("click",()=>{focus=null;mode.value="global";search.value="";depth.value="1";filters.forEach((filter)=>filter.value="");edgesToggle.checked=false;render();});
    render();
  }).catch((error)=>{count.textContent=error.message||"Graph data unavailable.";});
})();
