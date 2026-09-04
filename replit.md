# Replit runtime

The full Freight Trust Knowledge Base runs through the **Start application** workflow.
It installs the repository-pinned Hermes checkout, builds the public Knowledge Atlas,
starts Hermes privately on loopback, and serves the browser interface on port 5000.

Required Secret:

- `OPENROUTER_API_KEY` — dedicated OpenRouter API key used by Hermes.
- `DEMO_ACCESS_CODE` — shared code that unlocks the private full-agent chat.
- `SESSION_SECRET` — signs the 12-hour HttpOnly demo session cookie.

To run manually:

```sh
PORT=5000 python scripts/install_hermes.py
PORT=5000 python scripts/replit_server.py --build --start-hermes
```

The public health check is `/healthz`. The Atlas remains publicly browsable, but the
tool-enabled chat requires a signed demo session. Hermes uses the Obsidian vault at
`knowledge-base/`, loads the project Freight Trust research skill, and runs with its
API-server tool profile after the browser-facing proxy authenticates the request.