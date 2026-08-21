#!/usr/bin/env python3
"""Extract every image from a PDF and label it with the nearest section
heading above it (the heading names the ad framework: "US VS THEM",
"BOLD CLAIM", etc).

The heading font is auto-detected: it's whichever font shows up on the
most distinct pages inside short text spans (headings are short; body
copy is not).

Usage:
    python3 extract_pdf_sections.py <pdf_path> <output_dir>

Writes:
    <output_dir>/images/*.png|jpg   - every extracted image
    <output_dir>/manifest.json      - {file, page, heading, bbox, ...} per image

Also prints a framework summary (heading -> image count) to stdout so the
caller can show it to the user when asking how many of each to produce.
"""
import sys
import os
import json

import fitz  # PyMuPDF


def is_short_span(text, max_chars=40, max_words=6):
    t = text.strip()
    if not t:
        return False
    return len(t) <= max_chars and len(t.split()) <= max_words


def detect_heading_font(doc):
    """Font that appears on the most distinct pages in short text spans."""
    font_pages = {}
    for page_index in range(len(doc)):
        page = doc[page_index]
        d = page.get_text("dict")
        for block in d.get("blocks", []):
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    font = span.get("font", "")
                    text = span.get("text", "")
                    if not font or not is_short_span(text):
                        continue
                    font_pages.setdefault(font, set()).add(page_index)
    if not font_pages:
        return None
    return max(font_pages.items(), key=lambda kv: len(kv[1]))[0]


def collect_headings(doc, heading_font):
    """(page_index, y0, text) for every heading, in reading order."""
    headings = []
    for page_index in range(len(doc)):
        page = doc[page_index]
        d = page.get_text("dict")
        for block in d.get("blocks", []):
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                line_text = []
                line_y0 = None
                for span in line.get("spans", []):
                    if span.get("font") == heading_font:
                        line_text.append(span.get("text", ""))
                        if line_y0 is None:
                            line_y0 = span["bbox"][1]
                if line_text:
                    text = "".join(line_text).strip()
                    if text and is_short_span(text):
                        headings.append([page_index, line_y0, text])

    # Merge wrapped heading lines that sit close together on the same page.
    merged = []
    for h in headings:
        if merged and merged[-1][0] == h[0] and abs(h[1] - merged[-1][1]) < 20:
            merged[-1][2] = merged[-1][2] + " " + h[2]
        else:
            merged.append(h)
    return [tuple(m) for m in merged]


def nearest_heading(headings, page_index, y0):
    """Latest heading at or before (page_index, y0) in reading order."""
    best = None
    for h_page, h_y0, h_text in headings:
        if h_page < page_index or (h_page == page_index and h_y0 <= y0):
            best = h_text
        elif h_page > page_index:
            break
    return best


def safe_name(text, limit=60):
    cleaned = "".join(c if c.isalnum() or c in " _-" else "" for c in text)
    cleaned = cleaned.strip().replace(" ", "_")
    return cleaned[:limit] or "UNLABELED"


def main():
    if len(sys.argv) != 3:
        print("Usage: extract_pdf_sections.py <pdf_path> <output_dir>", file=sys.stderr)
        sys.exit(1)

    pdf_path, out_dir = sys.argv[1], sys.argv[2]
    images_dir = os.path.join(out_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    doc = fitz.open(pdf_path)
    heading_font = detect_heading_font(doc)
    if heading_font is None:
        print("WARNING: could not detect a heading font; all images will be "
              "labeled UNLABELED", file=sys.stderr)
    headings = collect_headings(doc, heading_font) if heading_font else []

    manifest = []
    counter = 0

    for page_index in range(len(doc)):
        page = doc[page_index]
        for info in page.get_image_info(xrefs=True):
            xref = info.get("xref", 0)
            bbox = info.get("bbox")
            if not xref or not bbox:
                continue
            heading = nearest_heading(headings, page_index, bbox[1]) or "UNLABELED"
            try:
                base = doc.extract_image(xref)
            except Exception as e:
                print(f"WARNING: failed to extract xref {xref} on page "
                      f"{page_index + 1}: {e}", file=sys.stderr)
                continue

            ext = base.get("ext", "png")
            counter += 1
            filename = f"{counter:03d}_{safe_name(heading)}_p{page_index + 1}.{ext}"
            with open(os.path.join(images_dir, filename), "wb") as f:
                f.write(base["image"])

            manifest.append({
                "file": filename,
                "page": page_index + 1,
                "heading": heading,
                "xref": xref,
                "bbox": bbox,
                "width": base.get("width"),
                "height": base.get("height"),
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

    print(f"Extracted {len(manifest)} images from {len(doc)} pages.")
    print(f"Detected heading font: {heading_font}")
    print("Frameworks detected:")
    for name, count in sorted(frameworks.items(), key=lambda kv: -kv[1]):
        print(f"  - {name}: {count} image(s)")
    print(f"Manifest written to {manifest_path}")


if __name__ == "__main__":
    main()
