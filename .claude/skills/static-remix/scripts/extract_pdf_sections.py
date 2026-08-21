#!/usr/bin/env python3
"""Extract every image from a PDF and label it with the nearest section
heading above it (the heading names the ad framework: "US VS THEM",
"BOLD CLAIM", etc).

Usage:
    python3 extract_pdf_sections.py <pdf_path> <output_dir>

Writes:
    <output_dir>/images/*.png|jpg   - every extracted image
    <output_dir>/manifest.json      - {file, page, heading, bbox, ...} per image

Also prints a framework summary (heading -> image count) to stdout so the
caller can show it to the user when asking how many of each to produce.

See pdf_extract_lib.py for the extraction logic itself (shared with
add_to_swipe_file.py).
"""
import sys
import os
import json

from pdf_extract_lib import extract_images, safe_name


def main():
    if len(sys.argv) != 3:
        print("Usage: extract_pdf_sections.py <pdf_path> <output_dir>", file=sys.stderr)
        sys.exit(1)

    pdf_path, out_dir = sys.argv[1], sys.argv[2]
    images_dir = os.path.join(out_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    heading_font, page_count, images = extract_images(pdf_path)
    if heading_font is None:
        print("WARNING: could not detect a heading font; all images will be "
              "labeled UNLABELED", file=sys.stderr)

    manifest = []
    for counter, img in enumerate(images, start=1):
        filename = f"{counter:03d}_{safe_name(img['heading'])}_p{img['page']}.{img['ext']}"
        with open(os.path.join(images_dir, filename), "wb") as f:
            f.write(img["image"])

        manifest.append({
            "file": filename,
            "page": img["page"],
            "heading": img["heading"],
            "bbox": img["bbox"],
            "width": img["width"],
            "height": img["height"],
        })

    manifest_path = os.path.join(out_dir, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump({
            "pdf": pdf_path,
            "heading_font": heading_font,
            "images": manifest,
        }, f, indent=2)

    frameworks = {}
    for m in manifest:
        frameworks[m["heading"]] = frameworks.get(m["heading"], 0) + 1

    print(f"Extracted {len(manifest)} images from {page_count} pages.")
    print(f"Detected heading font: {heading_font}")
    print("Frameworks detected:")
    for name, count in sorted(frameworks.items(), key=lambda kv: -kv[1]):
        print(f"  - {name}: {count} image(s)")
    print(f"Manifest written to {manifest_path}")


if __name__ == "__main__":
    main()
