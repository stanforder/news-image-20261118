#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261118.

Writes the finished image to /output/entry.png (or $MAKEFUN_OUTPUT_DIR
when set, for local testing). Standard library only, no network, fully
deterministic: it copies the entry.png shipped in this repository, which
was drawn by draw_entry.py from the 18 November 2026 news.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Copy verbatim: same bytes in, same bytes out, every run.
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
