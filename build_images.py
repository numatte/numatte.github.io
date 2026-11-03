"""LPのPDF（numatte-lp.pdf）から写真を取り出し、Web用に軽いJPEGにして assets/ に保存する。

使い方: python build_images.py <numatte-lp.pdf>
"""
import io
import sys
from pathlib import Path

import pymupdf
from PIL import Image

HERE = Path(__file__).parent
OUT = HERE / "assets"

# (ページ, ページ内の画像番号, 保存名, 長辺の最大px)
PICK = [
    (1, 1, "hero-taishi.jpg", 1600),
    (3, 1, "spotlight.jpg", 1100),
    (4, 1, "style-student.jpg", 1100),
    (4, 2, "style-office.jpg", 1100),
    (5, 1, "taishi.jpg", 1200),
    (5, 2, "shumpei.jpg", 1200),
    (6, 7, "cheki-taishi.jpg", 900),
    (6, 4, "cheki-next.jpg", 900),
]


def main():
    doc = pymupdf.open(sys.argv[1])
    OUT.mkdir(exist_ok=True)
    for page_no, idx, name, max_side in PICK:
        xref = doc[page_no - 1].get_images(full=True)[idx - 1][0]
        img = Image.open(io.BytesIO(doc.extract_image(xref)["image"])).convert("RGB")
        img.thumbnail((max_side, max_side), Image.LANCZOS)
        img.save(OUT / name, "JPEG", quality=82, optimize=True, progressive=True)
        print(name, img.size, (OUT / name).stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
