#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for developers to
$MAKEFUN_OUTPUT_DIR/entry.txt (falls back to /output/entry.txt
when the variable is unset). Standard library only.
"""

import os
import sys

FORTUNE = "You will deploy on Friday and nothing will break, because the universe already approved your pull request."

def main():
    line = FORTUNE.strip()
    if len(line) > 120:
        raise SystemExit("fortune exceeds 120 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("fortune must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0

if __name__ == "__main__":
    sys.exit(main())
