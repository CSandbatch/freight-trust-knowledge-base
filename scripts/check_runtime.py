#!/usr/bin/env python3
"""Secret-safe readiness check for the local AWS/OpenRouter agent runtime."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tomllib
import urllib.error
import urllib.request


ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIRED_AGENT_FIELDS = {"name", "description", "developer_instructions"}
DISCOURAGED_SECRET_NAMES = {
    "AWS_CONSOLE_PASSWORD",
    "AWS_CONSOLE_SIGNIN_URL",
    "AWS_CONSOLE_USERNAME",
    "AWS_SIGN_IN_PASSWORD",
}


class Report:
    def __init__(self) -> None:
        self.failures = 0
        self.warnings = 0

    def pass_(self, label: str, detail: str) -> None:
        print(f"PASS  {label}: {detail}")

    def warn(self, label: str, detail: str) -> None:
        self.warnings += 1
        print(f"WARN  {label}: {detail}")

    def fail(self, label: str, detail: str) -> None:
        self.failures += 1
        print(f"FAIL  {label}: {detail}")


def parse_env(path: pathlib.Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.is_file():
        return values
    for raw_line in path.read_text(encoding="utf-8-sig").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        name, value = line.split("=", 1)
        name = name.strip()
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        if name:
            values[name] = value
    return values


def load_environment(report: Report) -> dict[str, str]:
    env_path = ROOT / ".env"
    values = parse_env(env_path)
    if not env_path.is_file():
        report.fail("env file", "missing .env; copy .env.example and populate it locally")
        return values
    malformed: list[str] = []
    duplicates: set[str] = set()
    seen: set[str] = set()
    for line_number, raw_line in enumerate(env_path.read_text(encoding="utf-8-sig").splitlines(), 1):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            malformed.append(f"line {line_number} has no equals sign")
            continue
        name = line.split("=", 1)[0].strip()
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
            malformed.append(f"line {line_number} has an invalid variable name")
        if name in seen:
            duplicates.add(name)
        seen.add(name)
    if malformed:
        report.fail("env syntax", "; ".join(malformed))
    elif duplicates:
        report.fail("env syntax", "duplicate variables: " + ", ".join(sorted(duplicates)))
    else:
        report.pass_("env syntax", f"{len(values)} unique assignments are dotenv-compatible")

    ignored = subprocess.run(
        ["git", "check-ignore", "--quiet", ".env"], cwd=ROOT, check=False
    ).returncode == 0
    if ignored:
        report.pass_("env tracking", ".env is ignored by Git")
    else:
        report.fail("env tracking", ".env is not ignored by Git")
    for name, value in values.items():
        if value and name not in os.environ:
            os.environ[name] = value
    discouraged = sorted(name for name in DISCOURAGED_SECRET_NAMES if values.get(name))
    if discouraged:
        report.warn(
            "secret scope",
            "console-login material is present in .env; remove it and use SDK/CLI credentials: "
            + ", ".join(discouraged),
        )
    return values


def check_venv(report: Report) -> None:
    expected = (ROOT / ".venv").resolve()
    active = pathlib.Path(sys.prefix).resolve()
    if active == expected:
        report.pass_("virtual environment", f"using {expected.name} with Python {sys.version.split()[0]}")
    elif expected.joinpath("pyvenv.cfg").is_file():
        report.warn("virtual environment", ".venv exists but this command is not running inside it")
    else:
        report.fail("virtual environment", "missing .venv; run python -m venv .venv")

    required_modules = {"yaml": "PyYAML", "markdown_it": "markdown-it-py"}
    missing = [package for module, package in required_modules.items() if importlib.util.find_spec(module) is None]
    if missing:
        report.fail("Python dependencies", "missing " + ", ".join(missing))
    else:
        report.pass_("Python dependencies", "requirements.txt imports are available")


def check_agents(report: Report) -> None:
    agents_path = ROOT / ".codex" / "agents"
    config_path = ROOT / ".codex" / "config.toml"
    contract_path = ROOT / "AGENTS.md"
    if not contract_path.is_file():
        report.fail("agent contract", "AGENTS.md is missing")
    else:
        report.pass_("agent contract", "root AGENTS.md exists")

    try:
        config = tomllib.loads(config_path.read_text(encoding="utf-8"))
        enabled = config.get("agents", {}).get("enabled") is True
        if not enabled:
            raise ValueError("agents.enabled is not true")
        report.pass_("agent configuration", ".codex/config.toml enables subagents")
    except (OSError, tomllib.TOMLDecodeError, ValueError) as exc:
        report.fail("agent configuration", str(exc))

    names: list[str] = []
    errors: list[str] = []
    for path in sorted(agents_path.glob("*.toml")):
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
            missing = REQUIRED_AGENT_FIELDS - data.keys()
            if missing:
                errors.append(f"{path.name} missing {sorted(missing)}")
            names.append(str(data.get("name", "")))
        except (OSError, tomllib.TOMLDecodeError) as exc:
            errors.append(f"{path.name}: {exc}")
    if not names:
        errors.append("no .codex/agents/*.toml files found")
    if len(names) != len(set(names)):
        errors.append("duplicate agent names")
    if errors:
        report.fail("persona factory", "; ".join(errors))
    else:
        report.pass_("persona factory", f"{len(names)} unique persona definitions parsed")


def check_aws(report: Report, live: bool) -> None:
    region = os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION")
    profile = os.getenv("AWS_PROFILE")
    access_key = os.getenv("AWS_ACCESS_KEY_ID")
    secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    if not region:
        report.fail("AWS configuration", "AWS_REGION or AWS_DEFAULT_REGION is required")
    elif profile or (access_key and secret_key):
        method = "named profile" if profile else "environment credential pair"
        report.pass_("AWS configuration", f"region and {method} are configured")
    else:
        report.warn("AWS configuration", "region exists; expecting an attached IAM role or workload identity")

    if not live:
        return
    if not shutil.which("aws"):
        report.fail("AWS authentication", "AWS CLI is not installed")
        return
    completed = subprocess.run(
        ["aws", "sts", "get-caller-identity", "--output", "json"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    if completed.returncode != 0:
        message = (completed.stderr or completed.stdout).strip().splitlines()
        report.fail("AWS authentication", message[-1] if message else "STS request failed")
        return
    try:
        identity = json.loads(completed.stdout)
        if not identity.get("Account") or not identity.get("Arn"):
            raise ValueError("incomplete STS identity")
    except (json.JSONDecodeError, ValueError) as exc:
        report.fail("AWS authentication", str(exc))
        return
    report.pass_("AWS authentication", "STS GetCallerIdentity succeeded")


def check_openrouter(report: Report, live: bool) -> None:
    key = os.getenv("OPENROUTER_API_KEY", "")
    base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1").rstrip("/")
    model = os.getenv("OPENROUTER_MODEL", "")
    if not key:
        report.fail("OpenRouter configuration", "OPENROUTER_API_KEY is missing")
    if not model:
        report.fail("OpenRouter model", "OPENROUTER_MODEL must contain an explicit model slug")
    if not base_url.startswith("https://"):
        report.fail("OpenRouter base URL", "OPENROUTER_BASE_URL must use HTTPS")
    else:
        report.pass_("OpenRouter base URL", base_url)
    if not live or not key:
        return

    request = urllib.request.Request(
        f"{base_url}/key",
        headers={
            "Authorization": f"Bearer {key}",
            "User-Agent": "freight-trust-runtime-check/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
            if response.status != 200 or not isinstance(payload.get("data"), dict):
                raise ValueError("unexpected key metadata response")
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError) as exc:
        status = getattr(exc, "code", None)
        detail = f"HTTP {status}" if status else type(exc).__name__
        report.fail("OpenRouter authentication", detail)
        return
    report.pass_("OpenRouter authentication", "authenticated key metadata request succeeded")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="also run read-only AWS STS and OpenRouter key probes")
    args = parser.parse_args()

    report = Report()
    load_environment(report)
    check_venv(report)
    check_agents(report)
    check_aws(report, args.live)
    check_openrouter(report, args.live)
    print(f"\nSUMMARY failures={report.failures} warnings={report.warnings}")
    return 1 if report.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
