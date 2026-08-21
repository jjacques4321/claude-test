#!/usr/bin/env python3
"""Add one or more standalone ad images (e.g. pasted directly in chat, not
inside a PDF) to the persistent swipe-file library.

Unlike add_to_swipe_file.py, there's no PDF and no heading to
auto-detect — each image already IS a complete ad, so the framework label
for each one must be supplied explicitly by whoever's calling this
(Claude, having looked at the image and judged which framework it best
fits — an existing one, or a new one if it doesn't match anything seen so
far).

Usage:
    python3 add_images_to_swipe_file.py <source_label> <framework1> <image_path1> [<framework2> <image_path2> ...]

Example:
    python3 add_images_to_swipe_file.py chat-batch-1 \\
        "Feature Callouts" ad1.png \\
        "BOLD CLAIM" ad2.png

Writes/updates:
    <skill_dir>/swipe-file/images/<source_id>/*.<ext>
    <skill_dir>/swipe-file/manifest.json

Prints the aggregated framework summary across the ENTIRE library after
adding.
"""
import sys
import os
import shutil
from datetime import datetime, timezone

from pdf_extract_lib import safe_name
from swipe_file_lib import (
    SWIPE_DIR, load_manifest, save_manifest, make_source_id,
    print_library_summary,
)


def main():
    if len(sys.argv) < 4 or len(sys.argv) % 2 != 0:
        print(
            "Usage: add_images_to_swipe_file.py <source_label> "
            "<framework1> <image_path1> [<framework2> <image_path2> ...]",
            file=sys.stderr,
        )
        sys.exit(1)

    source_label = sys.argv[1]
    rest = sys.argv[2:]
    pairs = list(zip(rest[0::2], rest[1::2]))  # (framework, image_path)

    manifest = load_manifest()
    existing_ids = {s["id"] for s in manifest["sources"]}
    source_id = make_source_id(source_label, existing_ids)

    source_images_dir = os.path.join(SWIPE_DIR, "images", source_id)
    os.makedirs(source_images_dir, exist_ok=True)

    source_manifest_images = []
    for counter, (framework, image_path) in enumerate(pairs, start=1):
        if not os.path.exists(image_path):
            print(f"WARNING: {image_path} not found, skipping", file=sys.stderr)
            continue
        ext = os.path.splitext(image_path)[1].lstrip(".").lower() or "png"
        filename = f"{counter:03d}_{safe_name(framework)}.{ext}"
        shutil.copyfile(image_path, os.path.join(source_images_dir, filename))
        source_manifest_images.append({
            "file": f"images/{source_id}/{filename}",
            "heading": framework,
        })

    if not source_manifest_images:
        print("ERROR: no images were added", file=sys.stderr)
        sys.exit(1)

    manifest["sources"].append({
        "id": source_id,
        "source_type": "images",
        "pdf_name": None,
        "added": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "heading_font": None,
        "page_count": None,
        "images": source_manifest_images,
    })
    save_manifest(manifest)

    print(f"Added source '{source_id}': {len(source_manifest_images)} "
          f"manually-labeled image(s).")
    print_library_summary(manifest)


if __name__ == "__main__":
    main()
