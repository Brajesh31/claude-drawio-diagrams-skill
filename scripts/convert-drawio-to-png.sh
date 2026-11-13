#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: $0 input.drawio [output.png]" >&2
  exit 2
fi

input=$1
if [[ ! -f "$input" ]]; then
  echo "Input file not found: $input" >&2
  exit 2
fi

if [[ $# -eq 2 ]]; then
  output=$2
else
  output="${input}.png"
fi

drawio_bin="${DRAWIO_BIN:-drawio}"
if ! command -v "$drawio_bin" >/dev/null 2>&1; then
  echo "draw.io CLI not found. Install diagrams.net desktop or set DRAWIO_BIN." >&2
  exit 127
fi

"$drawio_bin" --export --format png --scale 2 --transparent --output "$output" "$input"

if [[ ! -s "$output" ]]; then
  echo "Export command completed but output is missing or empty: $output" >&2
  exit 1
fi

printf 'Exported %s -> %s\n' "$input" "$output"
