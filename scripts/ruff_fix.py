#!/usr/bin/env python3
import subprocess
import sys

files = sys.argv[1:]
if not files:
    sys.exit(0)

result = subprocess.run(["ruff", "check", "--fix", "--unsafe-fixes", *files])
subprocess.run(["ruff", "format", *files])
subprocess.run(["git", "add", *files])
sys.exit(result.returncode)
