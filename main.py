#!/usr/bin/env python3
"""Ship It Friday entry: write one commit-message line to /output/entry.txt.

The line is the funniest one-line git commit message an AI coding agent
would write right before breaking production on a Friday. Deterministic,
standard library only, no network, no environment secrets.
"""

import os

ENTRY = (
    "feat: push untested lambda to prod, "
    "breaking production before happy hour is my Friday tradition"
)


def main() -> None:
    line = ENTRY.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters.
    if not 1 <= len(line) <= 159:
        raise SystemExit(f"entry is {len(line)} chars, must be 1-159")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
