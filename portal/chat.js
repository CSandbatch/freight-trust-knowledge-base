(() => {
  const root = document.querySelector("[data-agent-chat]");
  if (!root) return;

  const form = root.querySelector("[data-chat-form]");
  const input = root.querySelector("[data-chat-input]");
  const imageInput = root.querySelector("[data-chat-image]");
  const attachment = root.querySelector("[data-chat-attachment]");
  const transcript = root.querySelector("[data-chat-transcript]");
  const status = root.querySelector("[data-chat-status]");
  const send = root.querySelector("[data-chat-send]");
  const endpoint = document.body.dataset.chatEndpoint || "/api/chat";
  const history = [];
  let imageData = null;
  let controller = null;
  let authenticated = false;

  function showLogin() {
    root.classList.add("is-locked");
    let gate = root.querySelector("[data-demo-login]");
    if (!gate) {
      gate = document.createElement("form");
      gate.className = "demo-login";
      gate.dataset.demoLogin = "";
      gate.innerHTML = `
        <span class="demo-login-kicker">Private agent demo</span>
        <h2>Unlock the full research agent</h2>
        <p>Enter the shared demo access code to enable Obsidian skills, linked-note research, and agent tools.</p>
        <input type="text" name="username" value="demo" autocomplete="username" class="sr-only" tabindex="-1" aria-hidden="true">
        <label for="demo-access-code">Demo access code</label>
        <input id="demo-access-code" name="accessCode" type="password" autocomplete="current-password" required>
        <button type="submit">Unlock agent</button>
        <p class="demo-login-status" data-demo-login-status aria-live="polite"></p>`;
      root.append(gate);
      gate.addEventListener("submit", async (event) => {
        event.preventDefault();
        const message = gate.querySelector("[data-demo-login-status]");
        const button = gate.querySelector("button");
        button.disabled = true;
        message.textContent = "Checking access…";
        try {
          const response = await fetch("/api/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ accessCode: new FormData(gate).get("accessCode") }),
          });
          const payload = await response.json().catch(() => ({}));
          if (!response.ok) throw new Error(payload.error || "Login failed");
          authenticated = true;
          root.classList.remove("is-locked");
          gate.remove();
          status.textContent = "Full agent enabled: Obsidian vault, research skills, citations, and tools are available.";
          input.focus();
        } catch (error) {
          message.textContent = error.message;
        } finally {
          button.disabled = false;
        }
      });
    }
  }

  fetch("/api/session")
    .then((response) => response.json())
    .then((session) => {
      authenticated = Boolean(session.authenticated);
      if (!authenticated) showLogin();
      else status.textContent = "Full agent enabled: Obsidian vault, research skills, citations, and tools are available.";
    })
    .catch(showLogin);

  function append(role, text, sources = []) {
    const message = document.createElement("article");
    message.className = `chat-message is-${role}`;
    const label = document.createElement("span");
    label.textContent = role === "user" ? "You" : "Knowledge Agent";
    const copy = document.createElement("p");
    copy.textContent = text;
    message.append(label, copy);
    if (sources.length) {
      const list = document.createElement("ul");
      list.className = "chat-sources";
      sources.slice(0, 5).forEach((source) => {
        const item = document.createElement("li");
        const link = document.createElement("a");
        link.textContent = source.title || "Knowledge-base source";
        link.href = source.url || "#";
        item.append(link);
        list.append(item);
      });
      message.append(list);
    }
    transcript.append(message);
    transcript.scrollTop = transcript.scrollHeight;
  }

  imageInput.addEventListener("change", () => {
    const file = imageInput.files && imageInput.files[0];
    imageData = null;
    attachment.textContent = "";
    if (!file) return;
    if (!["image/png", "image/jpeg", "image/webp"].includes(file.type) || file.size > 1_000_000) {
      status.textContent = "Use a PNG, JPEG, or WebP image smaller than 1 MB.";
      imageInput.value = "";
      return;
    }
    const reader = new FileReader();
    reader.onload = () => {
      imageData = String(reader.result);
      attachment.textContent = file.name;
      status.textContent = "Image ready. Add a question and send.";
    };
    reader.readAsDataURL(file);
  });

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (!authenticated) {
      showLogin();
      return;
    }
    const text = input.value.trim();
    if (!text || controller) return;
    const content = imageData
      ? [{ type: "text", text }, { type: "image_url", image_url: { url: imageData } }]
      : text;
    history.push({ role: "user", content });
    append("user", text + (imageData ? " [image attached]" : ""));
    input.value = "";
    imageInput.value = "";
    imageData = null;
    attachment.textContent = "";
    controller = new AbortController();
    send.disabled = true;
    status.textContent = "Retrieving relevant notes and asking Hermes…";
    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: history.slice(-20) }),
        signal: controller.signal,
      });
      const payload = await response.json().catch(() => ({}));
      if (response.status === 401) {
        authenticated = false;
        showLogin();
      }
      if (!response.ok) throw new Error(payload.error || `Request failed (${response.status})`);
      const answer = typeof payload.message === "string" ? payload.message : "The agent returned no answer.";
      history.push({ role: "assistant", content: answer });
      append("assistant", answer, Array.isArray(payload.sources) ? payload.sources : []);
      status.textContent = `Answered with ${payload.model || "the configured model"}. Verify consequential claims in the linked notes.`;
    } catch (error) {
      history.pop();
      append("assistant", `I couldn't complete that request. ${error.message}`);
      status.textContent = "The chat service may be unavailable on static-only hosting. Manual browsing remains available.";
    } finally {
      controller = null;
      send.disabled = false;
      input.focus();
    }
  });

  input.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      form.requestSubmit();
    }
  });
})();
