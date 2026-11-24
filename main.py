#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for developers to
$MAKEFUN_OUTPUT_DIR/entry.txt (falls back to /output/entry.txt
when the variable is unset). Standard library only.

The work is split into small functions so each step — holding the
line, validating it, resolving the output directory, and writing
the file — can be checked on its own.
"""

import os
import sys

MAX_CHARS = 120

FORTUNE = "You will deploy on Friday and nothing will break, because the universe already approved your pull request."


def get_fortune():
    """Return the fortune line, stripped of surrounding whitespace."""
    return FORTUNE.strip()


def validate_line(line):
    """Check the line against the competition's guards.

    The entry must be exactly one line, non-empty, and no longer
    than MAX_CHARS characters. Anything else fails loudly instead
    of writing a bad entry.
    """
    if not line:
        raise SystemExit("fortune must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit("fortune exceeds 120 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("fortune must be a single line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in line):
        raise SystemExit("fortune must not contain control characters")
    return line


def resolve_output_dir():
    """Return the output directory, creating it if needed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def write_entry(out_dir, line):
    """Write the line plus a trailing newline to entry.txt.

    Reads the file back afterwards and refuses to report success
    unless the written bytes match the line exactly.
    """
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line + "\n":
        raise SystemExit("entry.txt does not match the fortune line")
    return out_path


def main():
    line = validate_line(get_fortune())
    out_dir = resolve_output_dir()
    write_entry(out_dir, line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
