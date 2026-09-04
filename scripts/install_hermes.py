"""Install the pinned NousResearch Hermes checkout for local/Replit runtime use.

Hermes intentionally refuses wheel/sdist builds.  This script follows its supported
editable-install path while retaining an immutable upstream commit and an isolated,
ignored source directory.
"""

from __future__ import annotations

import os
import pathlib
import shutil
import subprocess
import sys
from importlib import metadata


ROOT = pathlib.Path(__file__).resolve().parents[1]
COMMIT = "29112bef099274229cadff79cdff7bf7b99c4b77"  # v2026.8.31 peeled commit
REPOSITORY = "https://github.com/NousResearch/hermes-agent.git"
PACKAGE_VERSION = "0.21.0"


def run(*command: str, cwd: pathlib.Path | None = None) -> None:
    subprocess.run(list(command), cwd=cwd or ROOT, check=True)


def pip_install(*arguments: str) -> None:
    command = [sys.executable, "-m", "pip", "install"]
    if os.environ.get("REPL_ID"):
        command.append("--break-system-packages")
    run(*command, *arguments)


def output(*command: str, cwd: pathlib.Path | None = None) -> str:
    return subprocess.check_output(list(command), cwd=cwd or ROOT, text=True).strip()


def hermes_is_installed() -> bool:
    try:
        return metadata.version("hermes-agent") == PACKAGE_VERSION and bool(shutil.which("hermes"))
    except metadata.PackageNotFoundError:
        return False


def main() -> int:
    if not shutil.which("git"):
        raise RuntimeError("Git is required to install the pinned Hermes checkout")
    home = pathlib.Path(os.environ.get("BELLHILL_HERMES_HOME") or str(ROOT / ".hermes-runtime")).resolve()
    source = pathlib.Path(os.environ.get("HERMES_INSTALL_DIR", str(home / "hermes-agent"))).resolve()
    if source.exists() and not (source / ".git").is_dir():
        if os.environ.get("HERMES_INSTALL_DIR"):
            raise RuntimeError(f"Refusing to replace non-Git path: {source}")
        # Replit deployment contexts can retain ignored generated directories
        # while stripping nested Git metadata. Recreate only our default cache.
        shutil.rmtree(source)
    if not source.exists():
        source.parent.mkdir(parents=True, exist_ok=True)
        run("git", "clone", "-c", "core.longpaths=true", "--filter=blob:none", "--no-checkout", REPOSITORY, str(source))
        run("git", "fetch", "--depth", "1", "origin", COMMIT, cwd=source)
        run("git", "checkout", "--detach", COMMIT, cwd=source)
    elif output("git", "rev-parse", "HEAD", cwd=source) != COMMIT:
        raise RuntimeError(f"Existing Hermes checkout is not the locked commit: {source}")
    pip_install("-r", str(ROOT / "requirements.txt"))
    if hermes_is_installed():
        print(f"Hermes Agent {PACKAGE_VERSION} already installed; reusing pinned runtime")
    else:
        pip_install("-e", str(source))
    print(f"Hermes Agent installed at locked commit {COMMIT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
