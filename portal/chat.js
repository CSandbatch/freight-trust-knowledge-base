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
