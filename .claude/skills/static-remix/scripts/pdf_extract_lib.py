"""Shared extraction logic for pulling labeled ad images out of a PDF.

Used by both extract_pdf_sections.py (single-run extraction into a run
folder) and add_to_swipe_file.py (accumulating extractions into the
persistent swipe-file library). Keeping this in one place means both
callers detect headings and label images identically.
"""
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


def extract_images(pdf_path):
    """Extract every image from pdf_path, labeled with its nearest heading.

    Returns (heading_font, page_count, images) where images is a list of
    dicts: {heading, page, bbox, ext, width, height, image (raw bytes)}.
    Callers decide where/how to save the bytes and build their own manifest.
    """
    doc = fitz.open(pdf_path)
    heading_font = detect_heading_font(doc)
    headings = collect_headings(doc, heading_font) if heading_font else []

    images = []
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
                      f"{page_index + 1}: {e}")
                continue

            images.append({
                "heading": heading,
                "page": page_index + 1,
                "bbox": bbox,
                "ext": base.get("ext", "png"),
                "width": base.get("width"),
                "height": base.get("height"),
                "image": base["image"],
            })

    return heading_font, len(doc), images
