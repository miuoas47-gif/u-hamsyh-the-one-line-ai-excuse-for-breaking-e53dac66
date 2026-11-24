#!/usr/bin/env python3
"""One-line AI excuse for breaking production.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Stdlib only, no network, no arguments, deterministic.
"""

import os
import sys

LINE = "In my defence, the production deploy button glowed when I hovered over it, and I have never once resisted a glowing button."


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in line):
        print("error: entry line contains control characters", file=sys.stderr)
        return 1
    if len(line) > 180:
        print(f"error: entry line is {len(line)} chars, over the 180-char limit", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(line)} chars): {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
