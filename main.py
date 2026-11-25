#!/usr/bin/env python3
"""The 3AM Fridge Text.

Writes the one line a smart fridge texts its owner at 3am to
/output/entry.txt. Python standard library only; no network access;
deterministic -- the same single line on every run.
"""

import os

ENTRY = (
    "It's 3am. You've opened me four times tonight and taken nothing. "
    "The leftovers have started to think you're just lonely."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def check_gate(text):
    """Mirror the competition gate: UTF-8, 1-140 chars, one line, not blank."""
    text.encode("utf-8")
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    check_gate(ENTRY)
    # Write exactly the message and nothing else: no trailing newline,
    # so the file holds one line of 120 characters, byte for byte.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
