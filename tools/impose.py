#!/usr/bin/env python3
"""Impose an 8-page half-letter booklet onto two letter sheets for home duplex printing.

  python3 tools/impose.py print/Soundline-Booklet.pdf print/Soundline-Booklet-Imposed.pdf

Sheet 1 front: pages 8 | 1    Sheet 1 back: 2 | 7
Sheet 2 front: 6 | 3          Sheet 2 back: 4 | 5
Print the result double-sided, landscape, FLIP ON THE SHORT EDGE, fold the stack in half.
Needs `pip install pypdf` once. A print shop does this itself from the sequential PDF.
"""
import sys
from pypdf import PdfReader, PdfWriter, Transformation, PageObject

src, dst = sys.argv[1], sys.argv[2]
r = PdfReader(src)
n = len(r.pages)
if n % 4:
    sys.exit(f"{n} pages: a saddle-stitched booklet needs a multiple of four")
w, h = float(r.pages[0].mediabox.width), float(r.pages[0].mediabox.height)   # 396 x 612 pt
order = []
lo, hi = 1, n
while lo < hi:                       # front: hi|lo, back: lo+1|hi-1
    order.append((hi, lo)); order.append((lo + 1, hi - 1)); lo += 2; hi -= 2
out = PdfWriter()
for left, right in order:
    sheet = PageObject.create_blank_page(width=2 * w, height=h)
    sheet.merge_transformed_page(r.pages[left - 1], Transformation().translate(0, 0))
    sheet.merge_transformed_page(r.pages[right - 1], Transformation().translate(w, 0))
    out.add_page(sheet)
with open(dst, "wb") as f:
    out.write(f)
print("wrote", dst, f"({len(order)} sides from {n} pages)")
