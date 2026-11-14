#!/usr/bin/env python3
"""news-image-01 v2 entry: write the rendered front page to /output/entry.png.

The image (assets/entry.png) is the finished 1024x1024 render: masthead,
numbered world map, and a 22-story ledger of Friday 13 November 2026.
This program only copies it, byte-for-byte, so the output is deterministic.
Python 3.13, standard library only, no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "assets", "entry.png")
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.png"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(src, out)
    # Fail loudly instead of handing the grader a truncated file.
    if os.path.getsize(out) != os.path.getsize(src):
        raise SystemExit("entry.png copy incomplete: size mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
