#!/usr/bin/env bash
set -euo pipefail

# fetch_product_photo.sh — best-effort download of the primary product
# photo from a product page.
#
# Usage:
#   fetch_product_photo.sh <product_url> <output_path>
#
# Strategy:
#   1. Shopify stores expose product data at <url>.json - try that first
#      and grab the first image src.
#   2. Fall back to the page's og:image meta tag.
#
# This is a best-effort helper, not a guarantee. If it fails (non-Shopify
# store with no og:image, JS-rendered gallery, etc), fetch the page
# yourself, find the real product image URL, and download it with curl —
# the pipeline requires an actual downloaded photo, not a guess.

URL="$1"
OUTPUT="$2"

mkdir -p "$(dirname "$OUTPUT")"

IMG_URL=""

JSON_URL="${URL%/}.json"
JSON_BODY="$(curl -sSL --max-time 20 -A "Mozilla/5.0" "$JSON_URL" 2>/dev/null || true)"
if echo "$JSON_BODY" | grep -q '"images"'; then
    IMG_URL="$(echo "$JSON_BODY" | perl -0777 -ne \
        'print $1 if /"images"\s*:\s*\[\s*\{[^}]*?"src"\s*:\s*"([^"]+)"/s')"
fi

if [[ -z "$IMG_URL" ]]; then
    PAGE_BODY="$(curl -sSL --max-time 20 -A "Mozilla/5.0" "$URL" 2>/dev/null || true)"
    IMG_URL="$(echo "$PAGE_BODY" | perl -ne \
        'print "$1\n" and exit if /<meta[^>]+property=["'"'"']og:image["'"'"'][^>]+content=["'"'"']([^"'"'"']+)["'"'"']/i')"
fi

if [[ -z "$IMG_URL" ]]; then
    echo "ERROR: could not auto-detect a product image URL for $URL" >&2
    echo "Fetch the page yourself, find the real product photo URL, and" >&2
    echo "download it with curl to: $OUTPUT" >&2
    exit 1
fi

if [[ "$IMG_URL" == //* ]]; then
    IMG_URL="https:$IMG_URL"
fi

curl -sSL --max-time 30 -A "Mozilla/5.0" -o "$OUTPUT" "$IMG_URL"
echo "Saved product photo: $OUTPUT"
echo "Source: $IMG_URL"
