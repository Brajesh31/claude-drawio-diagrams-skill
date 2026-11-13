#!/usr/bin/env python3
"""Validate basic draw.io XML structure and cell references using Python's stdlib."""
from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as exc:
        return [f"Cannot parse XML: {exc}"]

    if root.tag not in {"mxfile", "mxGraphModel"}:
        return [f"Unexpected root element <{root.tag}>; expected <mxfile> or <mxGraphModel>."]

    models = [root] if root.tag == "mxGraphModel" else root.findall(".//mxGraphModel")
    if not models:
        return ["No <mxGraphModel> element found."]

    for model_index, model in enumerate(models, start=1):
        cells = model.findall(".//mxCell")
        ids: set[str] = set()
        duplicate_ids: set[str] = set()
        for cell in cells:
            cell_id = cell.get("id")
            if not cell_id:
                errors.append(f"Model {model_index}: mxCell without an id.")
                continue
            if cell_id in ids:
                duplicate_ids.add(cell_id)
            ids.add(cell_id)

        for duplicate in sorted(duplicate_ids):
            errors.append(f"Model {model_index}: duplicate cell id {duplicate!r}.")

        for cell in cells:
            cell_id = cell.get("id", "<missing>")
            parent = cell.get("parent")
            source = cell.get("source")
            target = cell.get("target")
            for relation, value in (("parent", parent), ("source", source), ("target", target)):
                if value and value not in ids:
                    errors.append(
                        f"Model {model_index}: cell {cell_id!r} references missing "
                        f"{relation} id {value!r}."
                    )

        if not any(cell.get("id") == "0" for cell in cells):
            errors.append(f"Model {model_index}: expected root cell id '0' was not found.")
        if not any(cell.get("id") == "1" for cell in cells):
            errors.append(f"Model {model_index}: expected default layer cell id '1' was not found.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path, help="One or more .drawio files")
    args = parser.parse_args()

    failed = False
    for path in args.files:
        issues = validate(path)
        if issues:
            failed = True
            print(f"FAIL {path}")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"OK   {path}: basic XML and cell-reference checks passed")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
