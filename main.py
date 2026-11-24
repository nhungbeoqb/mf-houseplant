#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun bounty entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Pure stdlib, deterministic: the same fixed
text on every run.
"""

import os

ENTRY = (
    "Out of office. The monstera has claimed the window, "
    "unionised the succulents, and will only reply in photosynthesis."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
