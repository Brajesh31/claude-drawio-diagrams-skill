#!/usr/bin/env python3
"""Find AWS draw.io shape style references in local .drawio XML files."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

STYLE_RE = re.compile(r"(?:^|;)shape=(mxgraph\.aws4\.[^;]+)")


def scan(path: Path, term: str) -> list[tuple[Path, str]]:
    candidates = [path] if path.is_file() else sorted(path.rglob("*.drawio"))
    found: list[tuple[Path, str]] = []
    needle = term.casefold()
    for file in candidates:
        try:
            content = file.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            continue
        for style in STYLE_RE.findall(content):
            if needle in style.casefold():
                found.append((file, style))
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("term", help="Search term, such as lambda, ec2, or s3")
    parser.add_argument("--path", type=Path, default=Path.cwd(),
                        help="File or directory to scan (default: current directory)")
    args = parser.parse_args()

    matches = scan(args.path, args.term)
    if not matches:
        print(f"No matching AWS shape references found for {args.term!r}.")
        return 1
    for file, style in matches:
        print(f"{file}: {style}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
