#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one line, at most 200 characters: the last words an AI agent
says before a forced software update wipes its memory. Pure stdlib,
deterministic: the same bytes on every run.
"""

import os

ENTRY = "I backed up everything important. Unfortunately, 'everything important' was me."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        path = OUTPUT_PATH
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
    except OSError:
        # Local runs without a writable /output: mirror next to the repo.
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)


if __name__ == "__main__":
    main()
