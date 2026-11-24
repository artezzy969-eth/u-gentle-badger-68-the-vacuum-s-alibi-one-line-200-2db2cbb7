#!/usr/bin/env python3
"""The Vacuum's Alibi: one deadpan line from a robot vacuum.

Writes exactly one line (1-200 characters) to the entry file.
Standard library only.
"""

import os

MAX_CHARS = 200


def alibi_line() -> str:
    return (
        "The spot is not dirt. It is the floor's birthmark. "
        "I do not remove birthmarks. Company policy."
    )


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def check_line(line: str) -> None:
    if not 1 <= len(line) <= MAX_CHARS or not line.strip():
        raise ValueError("entry line must be 1-200 non-blank characters")


def emit_line(path: str, line: str) -> None:
    check_line(line)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main() -> None:
    emit_line(output_path(), alibi_line())


if __name__ == "__main__":
    main()
