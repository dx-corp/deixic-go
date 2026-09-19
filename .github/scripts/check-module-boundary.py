#!/usr/bin/env python3
"""Reject executable dependencies on the private source module.

Generated protobuf descriptor literals may retain an upstream go_package value;
they are data, not import statements or dependencies.
"""

import json
import os
from pathlib import Path
import subprocess
import sys


PRIVATE_MODULE = "github.com/evalops/platform"


def run(root: Path, *args: str) -> str:
    return subprocess.run(
        args,
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        env={**os.environ, "GOWORK": "off"},
    ).stdout


def is_private(path: str) -> bool:
    return path == PRIVATE_MODULE or path.startswith(f"{PRIVATE_MODULE}/")


def verify(root: Path, expected_module: str) -> None:
    module = json.loads(run(root, "go", "mod", "edit", "-json"))
    if module["Module"]["Path"] != expected_module:
        raise ValueError(f"Unexpected Go module: {module['Module']['Path']}")

    declared = [entry["Path"] for entry in module.get("Require") or []]
    for replacement in module.get("Replace") or []:
        declared.extend(
            (replacement["Old"]["Path"], replacement["New"]["Path"])
        )
    if offending := next((path for path in declared if is_private(path)), None):
        raise ValueError(f"Private module in go.mod: {offending}")

    # go list parses Go imports, including imports whose package cannot resolve.
    # The -e flag preserves those paths for the boundary check instead of
    # attempting a private network fetch before we identify the dependency.
    imports = run(
        root,
        "go", "list", "-e", "-deps", "-f", r'{{join .Imports "\n"}}', "./...",
    )
    if offending := next((path for path in imports.splitlines() if is_private(path)), None):
        raise ValueError(f"Private Go package import: {offending}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Usage: check-module-boundary.py <module-root> <public-module-path>")
    try:
        verify(Path(sys.argv[1]).resolve(), sys.argv[2])
    except (subprocess.CalledProcessError, ValueError) as error:
        raise SystemExit(str(error)) from error
