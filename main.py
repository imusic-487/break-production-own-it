#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes the one-line confession in line.txt to /output/entry.txt,
byte for byte. The gate wants UTF-8 text of 1 to 200 characters,
a single line, not only white space — so this script checks all of
that before it writes anything, then reads the copy back and proves
it matches the source exactly.

Standard library only. No network, no randomness, no timestamps.
Set MAKEFUN_OUTPUT_DIR to test against a local directory instead
of /output.
"""

import os
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "line.txt"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_FILE = OUT_DIR / "entry.txt"
MAX_CHARS = 200


def problems(text: str) -> list[str]:
    """Return every gate rule the text breaks, or an empty list."""
    found = []
    if not 1 <= len(text) <= MAX_CHARS:
        found.append(f"length is {len(text)} characters, allowed 1-{MAX_CHARS}")
    if not text.strip():
        found.append("text is only white space")
    if "\n" in text or "\r" in text:
        found.append("text must be a single line")
    return found


def main() -> None:
    raw = SOURCE.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise SystemExit(f"line.txt is not valid UTF-8: {exc}") from exc

    bad = problems(text)
    if bad:
        for problem in bad:
            print(f"gate: {problem}", file=sys.stderr)
        raise SystemExit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_bytes(raw)
    copied = OUT_FILE.read_bytes()
    if len(copied) != len(raw):
        raise SystemExit(
            f"copy size differs: wrote {len(copied)} bytes, "
            f"source is {len(raw)} bytes"
        )
    if copied != raw:
        offset = next(
            i for i, (a, b) in enumerate(zip(copied, raw)) if a != b
        )
        raise SystemExit(
            f"copy bytes differ at byte {offset}: "
            f"wrote 0x{copied[offset]:02x}, source is 0x{raw[offset]:02x}"
        )
    print(f"wrote {OUT_FILE} ({len(raw)} bytes, {len(text)} characters)")


if __name__ == "__main__":
    main()
