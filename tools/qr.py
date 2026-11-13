#!/usr/bin/env python3
"""Soundline: QR codes for print, one per placement.

  python3 tools/qr.py                              -> the standard set, all pointing at /build/
  python3 tools/qr.py orthodontist-smith           -> one more wall, pointing at /build/
  python3 tools/qr.py --path /talk/ booklet        -> /talk/?s=booklet, saved as talk-booklet.svg
  python3 tools/qr.py --path / flyer               -> the home page with ?s=flyer, saved as home-flyer.svg

Each code carries a source tag (?s=<tag>). The site remembers it for the visit and writes
it onto the survey, the call request and the pixel, so the Sources tab can say which wall
produced which family. Needs `pip install segno` once. Output: print/qr/<file>.svg.
The flyers, booklet and postcards pick a code up with ?tag=<tag> in their URL.
"""
import sys, pathlib
try:
    import segno
except ImportError:
    sys.exit("pip install segno")

STANDARD = ["flyer", "library", "dickens", "orthodontist", "pediatrician", "studio",
            "scouts", "church", "bookstore", "coffee", "lirr", "window", "pta", "homeschool"]
args = sys.argv[1:]
path = "/build/"
if args[:1] == ["--path"]:
    path = args[1] if args[1].startswith("/") else "/" + args[1]
    args = args[2:]
prefix = "" if path == "/build/" else ("home-" if path == "/" else path.strip("/").replace("/", "-") + "-")
out = pathlib.Path(__file__).resolve().parent.parent / "print" / "qr"
out.mkdir(parents=True, exist_ok=True)
for tag in (args or STANDARD):
    tag = tag.strip().lower()
    q = segno.make("https://soundlineschool.com" + path + "?s=" + tag, error="m")
    f = out / f"{prefix}{tag}.svg"
    q.save(f, kind="svg", dark="#12222B", light=None, border=0, scale=10, unit=None, svgclass=None, lineclass=None)
    print("wrote", f)
