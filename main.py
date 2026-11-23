#!/usr/bin/env python3
"""Write a one-line roast of an everyday gadget to /output/entry.txt."""

import os

ROAST = (
    "My AirPods case sits at 100% all day — it's the buds inside, "
    "the parts I actually listen with, that take turns dying "
    "20 minutes apart mid-call."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ROAST)


if __name__ == "__main__":
    main()
