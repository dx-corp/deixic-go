#!/usr/bin/env python3
"""Regression fixtures for executable imports versus inert descriptors."""

from pathlib import Path
import tempfile
import importlib.util


checker = Path(__file__).resolve().parents[1] / "scripts/check-module-boundary.py"
spec = importlib.util.spec_from_file_location("module_boundary", checker)
module_boundary = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module_boundary)

with tempfile.TemporaryDirectory(prefix="deixic-go-boundary-") as directory:
    root = Path(directory)
    public = "example.com/public-module"
    module_file = root / "go.mod"
    source = root / "example.go"
    module_file.write_text(f"module {public}\n\ngo 1.26.0\n")
    source.write_text(
        'package example\nconst descriptor = "github.com/evalops/platform/gen/go/deixic/v1"\n'
    )
    module_boundary.verify(root, public)  # Descriptor text is inert.

    source.write_text(
        'package example\nimport "github.com/evalops/platform/gen/go/deixic/v1"\n'
    )
    try:
        module_boundary.verify(root, public)
    except ValueError as error:
        assert "Private Go package import" in str(error), error
    else:
        raise AssertionError("Private source import was accepted")

    source.write_text("package example\n")
    module_file.write_text(
        f"module {public}\n\ngo 1.26.0\n\nrequire github.com/evalops/platform/gen/go v0.0.0\n"
    )
    try:
        module_boundary.verify(root, public)
    except ValueError as error:
        assert "Private module in go.mod" in str(error), error
    else:
        raise AssertionError("Private source module requirement was accepted")

    module_file.write_text(
        f"module {public}\n\ngo 1.26.0\n\nreplace github.com/evalops/platform/gen/go => ../private\n"
    )
    try:
        module_boundary.verify(root, public)
    except ValueError as error:
        assert "Private module in go.mod" in str(error), error
    else:
        raise AssertionError("Private source module replacement was accepted")

print("Go module boundary fixtures passed")
