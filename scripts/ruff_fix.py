#!/usr/bin/env python3
import subprocess
import sys

files = sys.argv[1:]
if not files:
    sys.exit(0)

subprocess.run(
    ["ruff", "check", "--fix", "--unsafe-fixes", *files], capture_output=True
)
subprocess.run(["ruff", "format", *files], capture_output=True)

result = subprocess.run(["ruff", "check", *files])

if result.returncode != 0:
    print("\n[!] The above errors require manual fixes.")
else:
    print("[+] All issues fixed.")

subprocess.run(["git", "add", *files])
sys.exit(result.returncode)
