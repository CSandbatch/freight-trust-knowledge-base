---
name: Private agent boundary
description: Security boundary and intended capability posture for the Hermes demo agent.
---

The tool-enabled Hermes agent must remain behind the browser-facing signed demo session;
never expose its loopback API or `/api/chat` anonymously. The public Atlas may stay
browsable.

**Why:** The Hermes API-server profile includes broad file, terminal, network, memory, and
skill capabilities. Anonymous access would create a remote-command and secret-exfiltration
risk. The shared-code gate is an explicit demo tradeoff, not suitable user authentication
for a long-lived production service.

**How to apply:** Keep login and session secrets in the proxy process only, preserve the
loopback Hermes binding, require authentication before proxying chat, and replace the
shared demo code with account-based authentication before ongoing public use.