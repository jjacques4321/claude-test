#!/usr/bin/env python3
"""Add a PDF's extracted, labeled ad images to the persistent swipe-file
library at <skill_dir>/swipe-file/, instead of a one-off run folder.

Unlike extract_pdf_sections.py (which extracts into a single run's
extracted/ folder and is forgotten after that run), this accumulates
across every PDF ever added — so later runs of static-remix can draw
examples from the whole library, not just whatever PDF was attached that
day.

Usage:
    python3 add_to_swipe_file.py <pdf_path> [label]

<label> is an optional short human-readable name for this source (e.g.
"winning-statics-nov"); if omitted, one is derived from the PDF's filename.

Writes/updates:
    <skill_dir>/swipe-file/images/<source_id>/*.png|jpg
    <skill_dir>/swipe-file/manifest.json   (one entry appended per source)

Prints the aggregated framework summary across the ENTIRE library after
adding, so the caller can show the user how the library has grown.
"""
import sys
import os
import re
import json
import shutil
from datetime import datetime, timezone

from pdf_extract_lib import extract_images, safe_name

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SWIPE_DIR = os.path.join(SKILL_DIR, "swipe-file")
MANIFEST_PATH = os.path.join(SWIPE_DIR, "manifest.json")


def load_manifest():
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH) as f:
            return json.load(f)
    return {"sources": []}


def save_manifest(manifest):
    os.makedirs(SWIPE_DIR, exist_ok=True)
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)


def make_source_id(pdf_path, label, existing_ids):
    base = label or os.path.splitext(os.path.basename(pdf_path))[0]
    base = re.sub(r"[^a-zA-Z0-9_-]+", "-", base).strip("-").lower() or "source"
    candidate = base
    n = 2
    while candidate in existing_ids:
        candidate = f"{base}-{n}"
        n += 1
    return candidate


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: add_to_swipe_file.py <pdf_path> [label]", file=sys.stderr)
        sys.exit(1)

    pdf_path = sys.argv[1]
    label = sys.argv[2] if len(sys.argv) == 3 else None

    if not os.path.exists(pdf_path):
        print(f"ERROR: {pdf_path} not found", file=sys.stderr)
        sys.exit(1)

    manifest = load_manifest()
    existing_ids = {s["id"] for s in manifest["sources"]}
    source_id = make_source_id(pdf_path, label, existing_ids)

    heading_font, page_count, images = extract_images(pdf_path)
    if heading_font is None:
        print("WARNING: could not detect a heading font; all images will be "
              "labeled UNLABELED", file=sys.stderr)

    source_images_dir = os.path.join(SWIPE_DIR, "images", source_id)
    os.makedirs(source_images_dir, exist_ok=True)

    source_manifest_images = []
    for counter, img in enumerate(images, start=1):
        filename = f"{counter:03d}_{safe_name(img['heading'])}_p{img['page']}.{img['ext']}"
        with open(os.path.join(source_images_dir, filename), "wb") as f:
            f.write(img["image"])
        source_manifest_images.append({
            "file": f"images/{source_id}/{filename}",
            "page": img["page"],
            "heading": img["heading"],
        })

    manifest["sources"].append({
        "id": source_id,
        "pdf_name": os.path.basename(pdf_path),
        "added": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "heading_font": heading_font,
        "page_count": page_count,
        "images": source_manifest_images,
    })
    save_manifest(manifest)

    print(f"Added source '{source_id}' ({os.path.basename(pdf_path)}): "
          f"{len(source_manifest_images)} images from {page_count} pages.")
    print(f"Detected heading font: {heading_font}")

    # Aggregate framework counts across the whole library.
    totals = {}
    for s in manifest["sources"]:
        for img in s["images"]:
            totals[img["heading"]] = totals.get(img["heading"], 0) + 1

    print(f"\nSwipe file now has {len(manifest['sources'])} source(s), "
          f"{sum(len(s['images']) for s in manifest['sources'])} total images.")
    print("Frameworks in the library:")
    for name, count in sorted(totals.items(), key=lambda kv: -kv[1]):
        print(f"  - {name}: {count} image(s)")


if __name__ == "__main__":
    main()
