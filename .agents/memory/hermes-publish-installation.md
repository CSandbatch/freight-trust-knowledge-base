---
name: Hermes publish installation
description: Replit publish-layer constraint for the pinned editable Hermes runtime.
---

Keep Hermes installation idempotent: when the exact pinned package version and launcher
already exist, reuse them rather than reinstalling the editable package during every
publish build.

**Why:** Reinstalling rewrites the generated Hermes launcher in `.pythonlibs` while
Replit creates the Python/Repl archive layers. The layer packer can race that mutation
and fail after an otherwise successful build with an archive size/write error.

**How to apply:** Continue validating the pinned source checkout on each build, but only
run the editable package installation in a clean environment or when the pinned package
version is absent. Verify repeated installer runs do not change the launcher timestamp.