"""Shared manifest read/write/summarize logic for the persistent swipe-file
library. Used by add_to_swipe_file.py (PDF sources) and
add_images_to_swipe_file.py (standalone pasted-image sources) so both
append to the same manifest.json consistently.
"""
import os
import re
import json

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


def make_source_id(label, existing_ids):
    base = re.sub(r"[^a-zA-Z0-9_-]+", "-", label).strip("-").lower() or "source"
    candidate = base
    n = 2
    while candidate in existing_ids:
        candidate = f"{base}-{n}"
        n += 1
    return candidate


def framework_totals(manifest):
    totals = {}
    for s in manifest["sources"]:
        for img in s["images"]:
            totals[img["heading"]] = totals.get(img["heading"], 0) + 1
    return totals


def print_library_summary(manifest):
    totals = framework_totals(manifest)
    total_images = sum(len(s["images"]) for s in manifest["sources"])
    print(f"\nSwipe file now has {len(manifest['sources'])} source(s), "
          f"{total_images} total images.")
    print("Frameworks in the library:")
    for name, count in sorted(totals.items(), key=lambda kv: -kv[1]):
        print(f"  - {name}: {count} image(s)")
