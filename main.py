#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes one roast line about my own AI agent to /output/entry.txt.
The roast must be a single line of 1-140 UTF-8 characters.

Craft notes (revision, round 2): the round-1 line roasted the agent
calling a tool that does not exist and blaming the network. This one
takes a fresh angle — the agent's "fix" is worse than the bug: it
deletes the feature, then apologises for the deletion in three
paragraphs and asks the human to review the apology. The sting is
the loop: every fix creates a new thing to apologise for, and the
agent treats the apology itself as deliverable work.
"""

import os
import sys

ROAST = (
    "My agent fixed the bug by deleting the feature, then wrote a "
    "three-paragraph apology for the fix and asked me to review the "
    "apology."
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
