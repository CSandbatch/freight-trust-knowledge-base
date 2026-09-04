# Replit runtime

The full Freight Trust Knowledge Base runs through the **Start application** workflow.
It installs the repository-pinned Hermes checkout, builds the public Knowledge Atlas,
starts Hermes privately on loopback, and serves the browser interface on port 5000.

Required Secret:

- `OPENROUTER_API_KEY` — dedicated OpenRouter API key used by Hermes.

To run manually:

```sh
PORT=5000 python scripts/install_hermes.py
PORT=5000 python scripts/replit_server.py --build --start-hermes
```

The public health check is `/healthz`. The browser-facing server keeps the provider
credential private and exposes only the Atlas and its narrow chat gateway.