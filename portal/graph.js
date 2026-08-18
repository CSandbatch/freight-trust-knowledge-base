/* Static, deterministic vault graph with traceable navigation. */
(() => {
  const app = document.querySelector("[data-graph]");
  if (!app) return;

  const body = document.body;
  const root = new URL(body.dataset.root || "index.html", window.location.href);
  const urlFor = (route) => new URL(route, root).href;
  const escapeHtml = (value) => String(value ?? "").replace(/[&<>"']/g, (character) => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[character]));
  const canvas = app.querySelector("[data-graph-canvas]");
  const inspector = app.querySelector("[data-graph-inspector]");
  const tree = app.querySelector("[data-graph-list]");
  const count = app.querySelector("[data-graph-count]");
  const legend = app.querySelector("[data-graph-legend]");
  const trailElement = app.querySelector("[data-graph-trail]");
  const mode = app.querySelector("[data-graph-mode]");
  const search = app.querySelector("[data-graph-search]");
  const depth = app.querySelector("[data-graph-depth]");
  const edgesToggle = app.querySelector("[data-graph-edges]");
  const filters = [...app.querySelectorAll("[data-graph-filter]")];
  const colors = {source:"#4f77c8",method:"#2f8f83",moc:"#7967b0",agent:"#b85c4b",experiment:"#b68125",dataset:"#5d815f",brief:"#4f77c8",draft:"#b68125",evidence:"#2f8f83",policy:"#7967b0",archive:"#777777"};
  const ns = "http://www.w3.org/2000/svg";

  let focus = null;
  let trail = [];
  let viewport = {x: 0, y: 0, width: 1000, height: 700};
  let drag = null;

  const setViewBox = () => canvas.setAttribute("viewBox", `${viewport.x} ${viewport.y} ${viewport.width} ${viewport.height}`);
  const params = () => new URLSearchParams(location.search);
  const writeParams = () => {
    const next = params();
    const state = Object.fromEntries(filters.map((filter) => [filter.dataset.graphFilter, filter.value]));
    Object.entries({...state, mode: mode.value, depth: depth.value, focus: focus || ""}).forEach(([key, value]) => value ? next.set(key, value) : next.delete(key));
    history.replaceState(null, "", `${location.pathname}${next.toString() ? `?${next}` : ""}`);
  };
  const zoom = (factor, centerX = viewport.x + viewport.width / 2, centerY = viewport.y + viewport.height / 2) => {
    const nextWidth = Math.max(160, Math.min(1800, viewport.width * factor));
    const nextHeight = nextWidth * 0.7;
    const ratioX = (centerX - viewport.x) / viewport.width;
    const ratioY = (centerY - viewport.y) / viewport.height;
    viewport = {x: centerX - nextWidth * ratioX, y: centerY - nextHeight * ratioY, width: nextWidth, height: nextHeight};
    setViewBox();
  };

  fetch(app.dataset.graphUrl).then((response) => {
    if (!response.ok) throw new Error("Graph data is unavailable");
    return response.json();
  }).then((graph) => {
    const nodes = graph.nodes || [];
    const edges = graph.edges || [];
    const byId = new Map(nodes.map((node) => [node.id, node]));
    const incoming = new Map(nodes.map((node) => [node.id, []]));
    const outgoing = new Map(nodes.map((node) => [node.id, []]));
    nodes.forEach((node) => { node._atlasX = Number(node.x); node._atlasY = Number(node.y); });
    edges.forEach((edge) => {
      if (byId.has(edge.source) && byId.has(edge.target)) {
        outgoing.get(edge.source).push(edge);
        incoming.get(edge.target).push(edge);
      }
    });

    const populate = (element, values) => {
      element.insertAdjacentHTML("beforeend", [...new Set(values)].filter(Boolean).sort().map((value) => `<option value="${escapeHtml(value)}">${escapeHtml(value)}</option>`).join(""));
    };
    populate(filters.find((item) => item.dataset.graphFilter === "collection"), nodes.map((node) => node.section));
    populate(filters.find((item) => item.dataset.graphFilter === "type"), nodes.map((node) => node.type));
    populate(filters.find((item) => item.dataset.graphFilter === "status"), nodes.map((node) => node.status));

    const initial = params();
    mode.value = initial.get("mode") || "global";
    depth.value = initial.get("depth") || "1";
    filters.forEach((filter) => { filter.value = initial.get(filter.dataset.graphFilter) || ""; });
    focus = initial.get("focus") && byId.has(initial.get("focus")) ? initial.get("focus") : null;
    if (focus) trail = [focus];

    const neighborhood = (start, hops) => {
      if (!start || !byId.has(start)) return {distances: new Map(), paths: []};
      const distances = new Map([[start, 0]]);
      const paths = [];
      const queue = [start];
      while (queue.length) {
        const current = queue.shift();
        const currentDepth = distances.get(current) || 0;
        if (currentDepth >= hops) continue;
        const adjacent = [...outgoing.get(current), ...incoming.get(current)].slice().sort((a, b) => {
          const aTarget = a.source === current ? a.target : a.source;
          const bTarget = b.source === current ? b.target : b.source;
          return aTarget.localeCompare(bTarget);
        });
        adjacent.forEach((edge) => {
          const target = edge.source === current ? edge.target : edge.source;
          if (distances.has(target)) return;
          distances.set(target, currentDepth + 1);
          paths.push(edge);
          queue.push(target);
        });
      }
      return {distances, paths};
    };

    const localPositions = (members, distances) => {
      const result = new Map();
      if (!focus) return result;
      result.set(focus, {x: 500, y: 350});
      const levels = new Map();
      members.filter((node) => node.id !== focus).forEach((node) => {
        const level = distances.get(node.id) || 1;
        levels.set(level, [...(levels.get(level) || []), node]);
      });
      levels.forEach((levelNodes, level) => {
        const ordered = levelNodes.slice().sort((a, b) => a.source.localeCompare(b.source));
        const radius = level === 1 ? 150 : level === 2 ? 270 : 330;
        ordered.forEach((node, index) => {
          const angle = -Math.PI / 2 + index * (Math.PI * 2 / ordered.length);
          result.set(node.id, {x: 500 + Math.cos(angle) * radius, y: 350 + Math.sin(angle) * radius});
        });
      });
      return result;
    };

    const renderTrail = () => {
      if (!trail.length) {
        trailElement.innerHTML = "<li>Choose a file to begin</li>";
        return;
      }
      trailElement.innerHTML = trail.map((id, index) => `<li><button type="button" data-trail-index="${index}" title="${escapeHtml(id)}">${escapeHtml(byId.get(id)?.label || id)}</button></li>`).join("");
      trailElement.querySelectorAll("button").forEach((button) => button.addEventListener("click", () => {
        const index = Number(button.dataset.trailIndex);
        trail = trail.slice(0, index + 1);
        focus = trail.at(-1) || null;
        mode.value = focus ? "local" : "global";
        render();
      }));
    };

    const relationshipList = (items, direction) => {
      if (!items.length) return '<p class="empty-state">None</p>';
      return `<ul class="inspector-links">${items.slice().sort((a, b) => {
        const aId = direction === "out" ? a.target : a.source;
        const bId = direction === "out" ? b.target : b.source;
        return (byId.get(aId)?.label || aId).localeCompare(byId.get(bId)?.label || bId);
      }).map((edge) => {
        const id = direction === "out" ? edge.target : edge.source;
        const node = byId.get(id);
        return `<li><button type="button" data-related-node="${escapeHtml(id)}">${escapeHtml(node?.label || id)}</button><a href="${escapeHtml(urlFor(node?.url || ""))}" aria-label="Open note">↗</a></li>`;
      }).join("")}</ul>`;
    };

    const renderInspector = () => {
      const selected = focus ? byId.get(focus) : null;
      if (!selected) {
        inspector.innerHTML = '<div class="pane-heading"><h2>Properties</h2></div><p class="empty-state">Select a node to inspect its path, status, outgoing links, and backlinks.</p>';
        return;
      }
      inspector.innerHTML = `<div class="pane-heading"><h2>Properties</h2></div>
        <p class="inspector-path">${escapeHtml(selected.source)}</p>
        <h3>${escapeHtml(selected.label)}</h3>
        <dl class="property-list"><div><dt>Type</dt><dd>${escapeHtml(selected.type)}</dd></div><div><dt>Status</dt><dd>${escapeHtml(selected.status)}</dd></div><div><dt>Links</dt><dd>${outgoing.get(selected.id).length} out / ${incoming.get(selected.id).length} in</dd></div></dl>
        <div class="inspector-actions"><a class="button" href="${escapeHtml(urlFor(selected.url))}">Open note</a><a class="button button-quiet" href="${escapeHtml(urlFor(selected.raw_url))}">Raw file</a></div>
        <section><h4>Outgoing</h4>${relationshipList(outgoing.get(selected.id), "out")}</section>
        <section><h4>Backlinks</h4>${relationshipList(incoming.get(selected.id), "in")}</section>`;
      inspector.querySelectorAll("[data-related-node]").forEach((button) => button.addEventListener("click", () => selectNode(button.dataset.relatedNode, true)));
    };

    const updateTree = (visible) => {
      tree.querySelectorAll("[data-graph-list-item]").forEach((item) => {
        item.hidden = !visible.has(item.dataset.nodeId);
        item.classList.toggle("is-selected", item.dataset.nodeId === focus);
      });
      tree.querySelectorAll("[data-vault-folder]").forEach((folder) => {
        folder.hidden = ![...folder.querySelectorAll("[data-graph-list-item]")].some((item) => !item.hidden);
        if (focus && folder.querySelector(`[data-node-id="${CSS.escape(focus)}"]`)) folder.open = true;
      });
      tree.querySelector(".is-selected")?.scrollIntoView({block: "nearest"});
    };

    const svgElement = (tag, attributes = {}) => {
      const element = document.createElementNS(ns, tag);
      Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, String(value)));
      return element;
    };

    const render = () => {
      const state = Object.fromEntries(filters.map((filter) => [filter.dataset.graphFilter, filter.value]));
      const query = search.value.trim().toLowerCase();
      const local = mode.value === "local" && Boolean(focus);
      const baseVisible = new Set(nodes.filter((node) =>
        (!state.collection || node.section === state.collection) &&
        (!state.type || node.type === state.type) &&
        (!state.status || node.status === state.status) &&
        (local || !query || `${node.label} ${node.source} ${(node.tags || []).join(" ")}`.toLowerCase().includes(query))
      ).map((node) => node.id));
      const localGraph = local ? neighborhood(focus, Number(depth.value)) : null;
      const visible = localGraph ? new Set([...baseVisible].filter((id) => localGraph.distances.has(id))) : baseVisible;
      const visibleNodes = nodes.filter((node) => visible.has(node.id));
      const positions = localGraph ? localPositions(visibleNodes, localGraph.distances) : new Map(visibleNodes.map((node) => [node.id, {x: node._atlasX, y: node._atlasY}]));
      const visibleEdges = edges.filter((edge) => visible.has(edge.source) && visible.has(edge.target));
      const trailPairs = new Set(trail.slice(1).flatMap((id, index) => [`${trail[index]}→${id}`, `${id}→${trail[index]}`]));

      canvas.replaceChildren();
      const defs = svgElement("defs");
      const marker = svgElement("marker", {id: "graph-arrow", viewBox: "0 0 10 10", refX: 9, refY: 5, markerWidth: 5, markerHeight: 5, orient: "auto-start-reverse"});
      marker.append(svgElement("path", {d: "M 0 0 L 10 5 L 0 10 z"}));
      defs.append(marker); canvas.append(defs);

      const edgeLayer = svgElement("g", {class: "edge-layer"});
      visibleEdges.forEach((edge) => {
        const a = positions.get(edge.source); const b = positions.get(edge.target);
        if (!a || !b) return;
        const classes = ["edge"];
        if (focus === edge.source) classes.push("is-outgoing");
        if (focus === edge.target) classes.push("is-incoming");
        if (trailPairs.has(`${edge.source}→${edge.target}`)) classes.push("is-trail");
        if (!edgesToggle.checked && !local && focus !== edge.source && focus !== edge.target && !classes.includes("is-trail")) classes.push("is-context");
        edgeLayer.append(svgElement("line", {x1: a.x, y1: a.y, x2: b.x, y2: b.y, class: classes.join(" "), "marker-end": "url(#graph-arrow)"}));
      });
      canvas.append(edgeLayer);

      const ranked = visibleNodes.slice().sort((a, b) => b.degree - a.degree);
      const labelled = new Set((local ? visibleNodes : ranked.slice(0, 18)).map((node) => node.id));
      visibleNodes.forEach((node) => {
        const point = positions.get(node.id); if (!point) return;
        const selected = node.id === focus;
        const group = svgElement("g", {class: `graph-node${selected ? " is-selected" : ""}`, tabindex: "0", role: "button", "aria-label": `${node.label}; ${node.type}; ${node.degree} relationships`, transform: `translate(${point.x} ${point.y})`});
        const radius = selected ? 9 : Math.max(3.5, Math.min(7, 3.5 + Math.sqrt(node.degree || 0) * 0.42));
        group.append(svgElement("circle", {r: radius, fill: colors[node.type] || "#77808a"}));
        if (selected) group.append(svgElement("circle", {r: radius + 5, class: "selection-ring"}));
        if (selected || labelled.has(node.id)) {
          const label = svgElement("text", {x: radius + 6, y: 4, class: "node-label"});
          label.textContent = node.label.length > 36 ? `${node.label.slice(0, 35)}…` : node.label;
          group.append(label);
        }
        group.addEventListener("click", () => selectNode(node.id, true));
        group.addEventListener("dblclick", () => window.location.assign(urlFor(node.url)));
        group.addEventListener("keydown", (event) => {
          if (event.key === "Enter" || event.key === " ") { event.preventDefault(); selectNode(node.id, true); }
        });
        canvas.append(group);
      });

      app.dataset.local = String(local);
      count.textContent = `${visibleNodes.length} files · ${visibleEdges.length} links`;
      legend.innerHTML = '<span><i class="legend-out"></i>Outgoing</span><span><i class="legend-in"></i>Backlink</span><span><i class="legend-trail"></i>Trail</span>';
      updateTree(visible); renderTrail(); renderInspector(); writeParams();
    };

    function selectNode(id, track = true) {
      if (!byId.has(id)) return;
      focus = id; mode.value = "local";
      if (track && trail.at(-1) !== id) trail.push(id);
      search.value = byId.get(id).label;
      viewport = {x: 0, y: 0, width: 1000, height: 700}; setViewBox(); render();
    }

    tree.querySelectorAll("[data-graph-node]").forEach((button) => button.addEventListener("click", () => selectNode(button.dataset.graphNode, true)));
    filters.forEach((filter) => filter.addEventListener("change", render));
    mode.addEventListener("change", render); depth.addEventListener("change", render); edgesToggle.addEventListener("change", render);
    search.addEventListener("input", () => {
      const value = search.value.trim().toLowerCase();
      const exact = nodes.find((node) => node.label.toLowerCase() === value || node.source.toLowerCase() === value);
      if (exact) selectNode(exact.id, true); else render();
    });

    app.querySelector("[data-graph-back]").addEventListener("click", () => {
      if (trail.length > 1) trail.pop();
      focus = trail.at(-1) || null; mode.value = focus ? "local" : "global"; search.value = focus ? byId.get(focus).label : ""; render();
    });
    app.querySelector("[data-graph-reset]").addEventListener("click", () => {
      focus = null; trail = []; search.value = ""; mode.value = "global"; depth.value = "1"; edgesToggle.checked = false;
      filters.forEach((filter) => { filter.value = ""; });
      viewport = {x: 0, y: 0, width: 1000, height: 700}; setViewBox(); render();
    });
    app.querySelector("[data-graph-zoom-in]").addEventListener("click", () => zoom(0.8));
    app.querySelector("[data-graph-zoom-out]").addEventListener("click", () => zoom(1.25));
    app.querySelector("[data-graph-fit]").addEventListener("click", () => { viewport = {x: 0, y: 0, width: 1000, height: 700}; setViewBox(); });

    canvas.addEventListener("wheel", (event) => {
      event.preventDefault();
      const point = canvas.createSVGPoint(); point.x = event.clientX; point.y = event.clientY;
      const localPoint = point.matrixTransform(canvas.getScreenCTM().inverse());
      zoom(event.deltaY > 0 ? 1.12 : 0.88, localPoint.x, localPoint.y);
    }, {passive: false});
    canvas.addEventListener("pointerdown", (event) => {
      if (event.target.closest?.(".graph-node")) return;
      drag = {x: event.clientX, y: event.clientY, view: {...viewport}};
      canvas.setPointerCapture(event.pointerId); canvas.classList.add("is-panning");
    });
    canvas.addEventListener("pointermove", (event) => {
      if (!drag) return;
      viewport.x = drag.view.x - (event.clientX - drag.x) * viewport.width / canvas.clientWidth;
      viewport.y = drag.view.y - (event.clientY - drag.y) * viewport.height / canvas.clientHeight;
      setViewBox();
    });
    const endDrag = () => { drag = null; canvas.classList.remove("is-panning"); };
    canvas.addEventListener("pointerup", endDrag); canvas.addEventListener("pointercancel", endDrag);

    setViewBox(); render();
  }).catch((error) => {
    count.textContent = error.message || "Could not load graph";
    inspector.innerHTML = '<div class="pane-heading"><h2>Properties</h2></div><p class="empty-state">Graph data could not be loaded. Use Explore to browse files.</p>';
  });
})();
