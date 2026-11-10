#!/usr/bin/env python3
"""Check local Markdown link targets without modifying a research repository.

Usage:
    python3 tools/check_relative_links.py
    python3 tools/check_relative_links.py --root /path/to/repo

Checks referenced *files* in standard inline Markdown links, including optional
#anchors and URL-escaped path components. It does NOT validate heading anchors,
reference-style links, external URLs, image links or transcluded content, and
it can still produce occasional false positives inside literal/code blocks.
This is a lightweight navigation guard, not a complete Markdown parser.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

INLINE_LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+[\"'][^\"']*[\"'])?\s*\)")
EXTERNAL_SCHEMES = {"https", "http", "mailto", "data", "tel"}


def target_path(mdfile: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith("#"):
        return None
    parsed = urlparse(target)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES or parsed.netloc:
        return None
    if parsed.scheme:
        return None  # unknown/external scheme
    path = unquote(parsed.path)
    if not path:
        return None
    return (mdfile.parent / path).resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    root = args.root.resolve()
    missing: list[tuple[str, int, str]] = []
    files = list(root.rglob("*.md"))
    for file in files:
        if ".git" in file.parts:
            continue
        try:
            text = file.read_text(encoding="utf-8")
        except UnicodeError as exc:
            print(f"cannot decode {file}: {exc}", file=sys.stderr)
            return 2
        for match in INLINE_LINK.finditer(text):
            candidate = target_path(file, match.group(1))
            if candidate is not None and not candidate.exists():
                lineno = text.count("\n", 0, match.start()) + 1
                missing.append((str(file.relative_to(root)), lineno, match.group(1)))
    if missing:
        print(f"Found {len(missing)} unresolved relative Markdown link(s) among {len(files)} files:")
        for file, line, dest in missing:
            print(f"  {file}:{line}: {dest}")
        return 1
    print(f"OK: checked {len(files)} Markdown files; no missing inline file targets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
