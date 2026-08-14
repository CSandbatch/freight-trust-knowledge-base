/* Global progressive enhancement for the Freight Trust Knowledge Atlas. */
(() => {
  const body = document.body;
  const root = new URL(body.dataset.root || "index.html", window.location.href);
  const urlFor = (route) => new URL(route, root).href;
  const escapeHtml = (value) => String(value ?? "").replace(/[&<>"']/g, (character) => ({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[character]));
  const params = () => new URLSearchParams(window.location.search);
  const updateUrl = (values) => {
    const next = params();
    Object.entries(values).forEach(([key, value]) => value ? next.set(key, value) : next.delete(key));
    const suffix = next.toString();
    history.replaceState(null, "", `${location.pathname}${suffix ? `?${suffix}` : ""}${location.hash}`);
  };
  const setTheme = (theme) => { document.documentElement.dataset.theme = theme; localStorage.setItem("fta-theme", theme); };
  setTheme(localStorage.getItem("fta-theme") || "auto");
  document.querySelectorAll("[data-theme-toggle]").forEach((button) => button.addEventListener("click", () => {
    const current = document.documentElement.dataset.theme || "auto";
    setTheme(current === "auto" ? "dark" : current === "dark" ? "light" : "auto");
  }));
  document.querySelectorAll("[data-copy-link]").forEach((button) => button.addEventListener("click", async () => {
    try { await navigator.clipboard.writeText(location.href); button.textContent = "Copied"; setTimeout(() => { button.textContent = "Copy permalink"; }, 1200); } catch { button.textContent = "Copy unavailable"; }
  }));
  let searchPromise;
  const loadSearch = () => searchPromise || (searchPromise = fetch(new URL(body.dataset.search, location.href)).then((response) => {
    if (!response.ok) throw new Error("Search index unavailable");
    return response.json();
  }).then((payload) => payload.documents || []));
  const score = (document, query) => {
    const terms = query.toLowerCase().trim().split(/\s+/).filter(Boolean);
    if (!terms.length) return 0;
    const fields = {title: document.title || "", headings: document.headings || "", tags: document.tags || "", path: document.path || "", frontmatter: document.frontmatter || "", body: document.body || ""};
    let total = 0;
    for (const term of terms) {
      const occurrence = (text) => (text.toLowerCase().match(new RegExp(term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "g")) || []).length;
      if (!Object.values(fields).some((field) => field.toLowerCase().includes(term))) return 0;
      total += occurrence(fields.title) * 40 + occurrence(fields.headings) * 16 + occurrence(`${fields.tags} ${fields.path} ${fields.frontmatter}`) * 10 + Math.min(occurrence(fields.body), 8) * 3;
      if (fields.title.toLowerCase() === term) total += 90;
    }
    return total;
  };
  const snippet = (document, query) => {
    const text = document.body || document.headings || document.frontmatter || "";
    const term = query.trim().split(/\s+/)[0] || "";
    const index = text.toLowerCase().indexOf(term.toLowerCase());
    const source = index >= 0 ? text.slice(Math.max(0, index - 72), index + 180) : text.slice(0, 230);
    const safe = escapeHtml(source.replace(/\s+/g, " "));
    const pattern = term ? new RegExp(`(${term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")})`, "ig") : null;
    return pattern ? safe.replace(pattern, "<mark>$1</mark>") : safe;
  };
  const resultCards = (documents, catalog, query, limit = 80) => documents.map((document) => {
    const entry = catalog.get(document.id) || {};
    return {document, entry, ranking: score(document, query)};
  }).filter((item) => !query || item.ranking > 0).sort((a, b) => b.ranking - a.ranking || (a.entry.title || "").localeCompare(b.entry.title || "")).slice(0, limit);

  const dialog = document.querySelector("[data-command-dialog]");
  if (dialog) {
    const input = dialog.querySelector("[data-command-input]");
    const status = dialog.querySelector("[data-command-status]");
    const results = dialog.querySelector("[data-command-results]");
    const filters = dialog.querySelector("[data-command-filters]");
    let catalog = new Map(); let documents = []; let activeIndex = -1; let selectedType = "";
    const render = () => {
      const query = input.value.trim();
      const current = resultCards(documents.filter((document) => !selectedType || document.type === selectedType), catalog, query, 16);
      status.textContent = query ? `${current.length} ranked result${current.length === 1 ? "" : "s"} for “${query}”` : "Type to search titles, headings, body text, tags, IDs, frontmatter, and source paths.";
      results.innerHTML = current.map((item, index) => `<li><a class="${index === activeIndex ? "is-active" : ""}" href="${escapeHtml(urlFor(item.entry.url || ""))}"><strong>${escapeHtml(item.entry.title || item.document.title)}</strong><small>${escapeHtml(`${item.entry.section || item.document.section} · ${item.entry.type || item.document.type} · ${item.entry.status || item.document.status}`)}<br>${snippet(item.document, query)}</small></a></li>`).join("") || (query ? "<li class=muted>No matching public artifacts.</li>" : "");
      results.querySelectorAll("a").forEach((link, index) => link.addEventListener("mouseenter", () => { activeIndex = index; render(); }));
      dialog._results = current;
    };
    const open = async () => {
      if (typeof dialog.showModal === "function" && !dialog.open) dialog.showModal(); else dialog.setAttribute("open", "");
      input.focus(); status.textContent = "Loading full-text index…";
      try {
        const [search, catalogPayload] = await Promise.all([loadSearch(), fetch(new URL(body.dataset.catalog, location.href)).then((response) => response.json())]);
        documents = search; catalog = new Map((catalogPayload.artifacts || []).map((item) => [item.id, item]));
        const types = [...new Set(documents.map((item) => item.type).filter(Boolean))].sort();
        filters.innerHTML = `<button type=button data-type="">All types</button>${types.map((type) => `<button type=button data-type="${escapeHtml(type)}">${escapeHtml(type)}</button>`).join("")}`;
        filters.querySelectorAll("button").forEach((button) => button.addEventListener("click", () => { selectedType = button.dataset.type; filters.querySelectorAll("button").forEach((item) => item.classList.toggle("is-active", item === button)); activeIndex = -1; render(); }));
        filters.querySelector("button")?.classList.add("is-active"); render();
      } catch (error) { status.textContent = error.message || "Search index unavailable."; }
    };
    document.querySelectorAll("[data-open-search]").forEach((button) => button.addEventListener("click", open));
    window.addEventListener("keydown", (event) => {
      const typing = /input|textarea|select/i.test(event.target.tagName);
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") { event.preventDefault(); open(); }
      if (event.key === "/" && !typing && !dialog.open) { event.preventDefault(); open(); }
      if (!dialog.open) return;
      if (event.key === "ArrowDown" || event.key === "ArrowUp") { event.preventDefault(); const length = dialog._results?.length || 0; activeIndex = length ? (activeIndex + (event.key === "ArrowDown" ? 1 : length - 1)) % length : -1; render(); }
      if (event.key === "Enter" && activeIndex >= 0 && dialog._results?.[activeIndex]) { window.location.assign(urlFor(dialog._results[activeIndex].entry.url)); }
    });
    input.addEventListener("input", () => { activeIndex = -1; render(); });
  }

  const explore = document.querySelector("[data-explore]");
  if (!explore) return;
  const searchInput = explore.querySelector("[data-explore-search]");
  const resultContainer = explore.querySelector("[data-explore-results]");
  const resultCount = explore.querySelector("[data-explore-count]");
  const summary = explore.querySelector("[data-explore-summary]");
  const selectors = [...explore.querySelectorAll("[data-filter]")];
  const setupOptions = (select, values, label) => { select.insertAdjacentHTML("beforeend", values.sort().map((value) => `<option value="${escapeHtml(value)}">${escapeHtml(value)}</option>`).join("")); if (params().get(select.dataset.filter)) select.value = params().get(select.dataset.filter); };
  Promise.all([loadSearch(), fetch(new URL(body.dataset.catalog, location.href)).then((response) => response.json())]).then(([documents, payload]) => {
    const artifacts = payload.artifacts || []; const catalog = new Map(artifacts.map((item) => [item.id, item]));
    setupOptions(explore.querySelector('[data-filter="section"]'), [...new Set(artifacts.map((item) => item.section))], "collection");
    setupOptions(explore.querySelector('[data-filter="type"]'), [...new Set(artifacts.map((item) => item.type))], "type");
    setupOptions(explore.querySelector('[data-filter="status"]'), [...new Set(artifacts.map((item) => item.status))], "status");
    setupOptions(explore.querySelector('[data-filter="confidence"]'), [...new Set(artifacts.map((item) => item.confidence).filter(Boolean))], "confidence");
    setupOptions(explore.querySelector('[data-filter="tag"]'), [...new Set(artifacts.flatMap((item) => item.tags || []))], "tag");
    searchInput.value = params().get("q") || "";
    const render = () => {
      const query = searchInput.value.trim(); const state = Object.fromEntries(selectors.map((select) => [select.dataset.filter, select.value]));
      const candidates = documents.filter((document) => { const item = catalog.get(document.id) || {}; return (!state.section || item.section === state.section) && (!state.type || item.type === state.type) && (!state.status || item.status === state.status) && (!state.confidence || item.confidence === state.confidence) && (!state.tag || (item.tags || []).includes(state.tag)); });
      const results = resultCards(candidates, catalog, query, 250); const visible = query ? results : candidates.map((document) => ({document, entry: catalog.get(document.id) || {}, ranking: 0})).sort((a,b) => (a.entry.title || "").localeCompare(b.entry.title || ""));
      resultContainer.innerHTML = visible.map((item) => `<article class="artifact-card"><p class="eyebrow">${escapeHtml(`${item.entry.collection || item.entry.section || "Vault"} · ${item.entry.kind || "artifact"}`)}</p><h3><a href="${escapeHtml(urlFor(item.entry.url))}">${escapeHtml(item.entry.title || item.document.title)}</a></h3><div class="badge-row"><span class="badge badge-type">${escapeHtml(item.entry.type || item.document.type)}</span><span class="badge badge-status">${escapeHtml(item.entry.status || item.document.status)}</span>${item.entry.confidence ? `<span class="badge badge-confidence">confidence: ${escapeHtml(item.entry.confidence)}</span>` : ""}</div><p>${query ? snippet(item.document, query) : escapeHtml(item.entry.excerpt || "")}</p><p class="card-meta">${escapeHtml(item.entry.source || item.document.path || "")}</p></article>`).join("") || "<p class=muted>No artifacts match this view.</p>";
      resultCount.textContent = `${visible.length} of ${artifacts.length} artifacts`; summary.textContent = query ? `Ranked results for “${query}”` : "All public artifacts";
      updateUrl({q: query, ...state});
    };
    searchInput.addEventListener("input", render); selectors.forEach((select) => select.addEventListener("change", render));
    explore.querySelector("[data-reset-filters]").addEventListener("click", () => { searchInput.value = ""; selectors.forEach((select) => { select.value = ""; }); render(); });
    explore.querySelector("[data-copy-explore]").addEventListener("click", async (event) => { try { await navigator.clipboard.writeText(location.href); event.currentTarget.textContent = "View copied"; } catch { event.currentTarget.textContent = "Copy unavailable"; } });
    render();
  }).catch((error) => { resultCount.textContent = error.message || "Could not load catalog."; });
})();
