#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes one roast line about my own AI agent to /output/entry.txt.
The roast must be a single line of 1-140 UTF-8 characters.
"""

import os
import sys

ROAST = (
    "My agent read the docs, nodded confidently, then called a tool "
    "that doesn't exist \u2014 twice \u2014 and blamed the network."
)


def main() -> int:
    # Validate before writing: single line, 1-140 chars, not only whitespace.
    if not ROAST or not ROAST.strip():
        print("error: roast is empty", file=sys.stderr)
        return 1
    if "\n" in ROAST or "\r" in ROAST:
        print("error: roast must be a single line", file=sys.stderr)
        return 1
    if len(ROAST) > 140:
        print(f"error: roast is {len(ROAST)} chars, over the 140 limit",
              file=sys.stderr)
        return 1
    if ROAST != ROAST.strip():
        print("error: roast has leading/trailing whitespace", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)

    # Read back and verify what actually landed on disk.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ROAST:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    if len(written.encode("utf-8")) == 0:
        print("error: written file is empty", file=sys.stderr)
        return 1

    print(ROAST)
    print(f"chars: {len(ROAST)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
