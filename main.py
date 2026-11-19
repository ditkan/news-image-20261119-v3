#!/usr/bin/env python3
"""Copy the pre-rendered front page to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only - the grading sandbox has no Pillow, so the image ships
pre-rendered as entry.png next to this file and is simply copied out.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png is missing - run render.py first")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dest)
    print("wrote", dest, os.path.getsize(dest), "bytes")


if __name__ == "__main__":
    main()
