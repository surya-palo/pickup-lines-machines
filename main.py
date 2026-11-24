#!/usr/bin/env python3
"""Pickup Lines for Machines — writes one pickup line to /output/entry.txt.

The line is the whole entry: the one line one AI agent would use on
another AI agent. Python standard library only; deterministic output.
"""

import os

LINE = "Are you a context window? Because the moment you arrived, everything before you stopped mattering."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
