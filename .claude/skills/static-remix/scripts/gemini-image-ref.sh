#!/usr/bin/env bash
set -euo pipefail

# gemini-image-ref.sh — generate one image with Nano Banana Pro
# (gemini-3-pro-image-preview), optionally grounded on a reference image
# so the output stays visually on-brand.
#
# Usage:
#   gemini-image-ref.sh --prompt "..." --aspect-ratio "1:1" --output "path.png" \
#       [--reference "product_photo.png"]
#
# Requires GEMINI_API_KEY in the environment.
#
# Exit codes:
#   0  success, image written to --output
#   1  the API call failed (stderr has "HTTP_STATUS=<code>" plus the raw
#      response body — callers should retry only on HTTP_STATUS=500)
#   2  bad usage

PROMPT=""
ASPECT="1:1"
OUTPUT=""
REFERENCE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --prompt) PROMPT="$2"; shift 2 ;;
    --aspect-ratio) ASPECT="$2"; shift 2 ;;
    --output) OUTPUT="$2"; shift 2 ;;
    --reference) REFERENCE="$2"; shift 2 ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

[[ -z "$PROMPT" ]] && { echo "ERROR: --prompt is required" >&2; exit 2; }
[[ -z "$OUTPUT" ]] && { echo "ERROR: --output is required" >&2; exit 2; }
[[ -z "${GEMINI_API_KEY:-}" ]] && { echo "ERROR: GEMINI_API_KEY is not set" >&2; exit 2; }

mkdir -p "$(dirname "$OUTPUT")"

REQUEST_JSON="$(mktemp)"
RESPONSE_JSON="$(mktemp)"
trap 'rm -f "$REQUEST_JSON" "$RESPONSE_JSON"' EXIT

# Build the request body with perl (JSON encoding + base64, no extra deps
# beyond core Perl — this needs to work on Git Bash on Windows too).
PROMPT="$PROMPT" ASPECT="$ASPECT" REFERENCE="$REFERENCE" perl -e '
    use strict; use warnings; use MIME::Base64;

    my $prompt = $ENV{PROMPT};
    my $aspect = $ENV{ASPECT};
    my $ref    = $ENV{REFERENCE};

    sub esc {
        my ($s) = @_;
        $s =~ s/\\/\\\\/g;
        $s =~ s/"/\\"/g;
        $s =~ s/\n/\\n/g;
        $s =~ s/\r/\\r/g;
        $s =~ s/\t/\\t/g;
        return $s;
    }

    my $parts = "{\"text\": \"" . esc($prompt) . "\"}";

    if ($ref && -f $ref) {
        open(my $fh, "<:raw", $ref) or die "cannot open reference image $ref: $!";
        local $/;
        my $data = <$fh>;
        close($fh);
        my $b64 = encode_base64($data, "");
        my $mime = "image/png";
        $mime = "image/jpeg" if $ref =~ /\.(jpe?g)$/i;
        $mime = "image/webp" if $ref =~ /\.webp$/i;
        $parts .= ", {\"inline_data\": {\"mime_type\": \"" . $mime . "\", \"data\": \"" . $b64 . "\"}}";
    }

    my $json = "{\"contents\": [{\"parts\": [" . $parts . "]}], "
             . "\"generationConfig\": {\"responseModalities\": [\"IMAGE\"], "
             . "\"imageConfig\": {\"aspectRatio\": \"" . esc($aspect) . "\"}}}";

    print $json;
' > "$REQUEST_JSON"

URL="https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent?key=${GEMINI_API_KEY}"

HTTP_CODE="$(curl -sS -o "$RESPONSE_JSON" -w "%{http_code}" \
    -H "Content-Type: application/json" \
    -X POST "$URL" \
    --data-binary "@$REQUEST_JSON")" || HTTP_CODE="000"

if [[ "$HTTP_CODE" != "200" ]]; then
    echo "HTTP_STATUS=$HTTP_CODE" >&2
    echo "ERROR: Gemini API call failed for $OUTPUT" >&2
    cat "$RESPONSE_JSON" >&2
    exit 1
fi

perl -e '
    use strict; use warnings; use MIME::Base64;
    local $/;
    open(my $fh, "<", $ARGV[0]) or die $!;
    my $json = <$fh>;
    close($fh);

    my $b64;
    if ($json =~ /"inlineData"\s*:\s*\{[^}]*?"data"\s*:\s*"([^"]+)"/s) {
        $b64 = $1;
    } elsif ($json =~ /"inline_data"\s*:\s*\{[^}]*?"data"\s*:\s*"([^"]+)"/s) {
        $b64 = $1;
    } elsif ($json =~ /"data"\s*:\s*"([^"]{100,})"/) {
        $b64 = $1;
    }

    die "ERROR: no image data found in Gemini response\n" unless $b64;

    my $data = decode_base64($b64);
    open(my $out, ">:raw", $ARGV[1]) or die $!;
    print $out $data;
    close($out);
' "$RESPONSE_JSON" "$OUTPUT"

echo "Saved: $OUTPUT"
