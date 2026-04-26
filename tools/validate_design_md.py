#!/usr/bin/env python3
"""Validate the structure of the project design.md file."""

from __future__ import annotations

import re
import sys
from pathlib import Path


SECTION_ORDER = [
    "Overview",
    "Colors",
    "Typography",
    "Layout",
    "Elevation & Depth",
    "Shapes",
    "Components",
    "Do's and Don'ts",
]


def _extract_headings(markdown_body: str) -> list[str]:
    """Return level-two Markdown headings without their marker."""
    return re.findall(r"^##\s+(.+?)\s*$", markdown_body, flags=re.MULTILINE)


def validate_design_md(path: Path) -> list[str]:
    """Return validation errors for a design.md file."""
    errors: list[str] = []
    markdown_body = path.read_text(encoding="utf-8")

    if not markdown_body.startswith("---\n") or "\n---\n" not in markdown_body[4:]:
        errors.append("Missing YAML front matter fences")

    section_positions = {
        section_name: index for index, section_name in enumerate(SECTION_ORDER)
    }
    highest_section_index = -1
    highest_section_name = ""

    for heading in _extract_headings(markdown_body):
        if heading not in section_positions:
            continue

        section_index = section_positions[heading]
        if section_index < highest_section_index:
            errors.append(
                f"Section order violation: {heading} appears after {highest_section_name}"
            )
            continue

        highest_section_index = section_index
        highest_section_name = heading

    return errors


def main() -> int:
    """Validate ./design.md and print a command-line status."""
    path = Path("design.md")

    if not path.exists():
        print("FAIL: design.md not found")
        return 1

    errors = validate_design_md(path)
    if errors:
        print("FAIL: design.md validation failed")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: design.md validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
