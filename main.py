#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

A one-line out-of-office note, written by the houseplants themselves:
the monstera has claimed the window, the succulents have unionised,
and replies come only in photosynthesis.
"""

import os

OUT_PATH = "/output/entry.txt"

# The note, built from a template with named slots so each clause can be
# tweaked independently without touching the others.
TEMPLATE = "{greeting} {claim} {reply}"

PARTS = {
    "greeting": "Out of office.",
    "claim": "The monstera has claimed the window, unionised the succulents,",
    "reply": "and will only reply in photosynthesis.",
}


def build_note() -> str:
    """Fill the template slots to form the single-line out-of-office note."""
    return TEMPLATE.format(**PARTS)


def main() -> None:
    note = build_note()
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        # No trailing newline: the entry is exactly the 116-character note.
        handle.write(note)


if __name__ == "__main__":
    main()
