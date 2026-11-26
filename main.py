#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the one sentence (at most 200 characters) a house cat would
say in its own defence, in the five seconds after sweeping a glass
off the table, to /output/entry.txt.

No apology, no confession, no gravity joke: the cat's logic is pure
self-interest. The glass was ugly, it was sitting in the cat's
sunbeam, and the cat would do it again. The sunbeam is the small
honest detail that makes it a cat's line and nobody else's, and the
defiant closer -- I would do it again -- is the whole defence.
"""

import os
import sys

# The defence: the charge, the motive, and the refusal to repent.
DEFENCE = (
    "The glass was ugly, it was sitting in my sunbeam, "
    "and I would do it again."
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def build_defence() -> str:
    """Return the cat's one-sentence defence."""
    return DEFENCE


def validate(text: str) -> None:
    """Hold the entry to the gate: 1-200 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("defence must not be empty")
    if text != text.strip():
        raise ValueError("defence must not start or end with whitespace")
    if "\n" in text.strip():
        raise ValueError("defence must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"defence is {len(text)} chars, over the {MAX_CHARS} cap")


def self_test() -> int:
    """Print the defence and its length without writing anything."""
    text = build_defence()
    validate(text)
    print(text)
    print(f"chars: {len(text)} (cap {MAX_CHARS})")
    return 0


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return self_test()
    text = build_defence()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
