#!/usr/bin/env python3
"""Soundline: QR codes for flyers, one per placement.

  python3 tools/qr.py                      -> the standard set below
  python3 tools/qr.py orthodontist-smith   -> one more, for one more wall

Each code points at soundlineschool.com/build/?s=<tag>. The site remembers the
tag for the visit and writes it onto the survey, the call request and the
pixel, so the Sources tab can say which wall produced which family. Needs
`pip install segno` once. Output: print/qr/<tag>.svg, picked up by the flyers
with print/flyer-kids.html?tag=<tag>.
"""
import sys, pathlib
try:
    import segno
except ImportError:
    sys.exit("pip install segno")

STANDARD = ["flyer", "library", "dickens", "orthodontist", "pediatrician", "studio",
            "scouts", "church", "bookstore", "coffee", "lirr", "window", "pta", "homeschool"]
out = pathlib.Path(__file__).resolve().parent.parent / "print" / "qr"
out.mkdir(parents=True, exist_ok=True)
for tag in (sys.argv[1:] or STANDARD):
    tag = tag.strip().lower()
    q = segno.make("https://soundlineschool.com/build/?s=" + tag, error="m")
    q.save(out / f"{tag}.svg", kind="svg", dark="#12222B", light=None, border=0, scale=10, unit=None, svgclass=None, lineclass=None)
    print("wrote", out / f"{tag}.svg")
