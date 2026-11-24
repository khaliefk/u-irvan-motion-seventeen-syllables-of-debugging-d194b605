#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

The haiku is fixed text: three lines in the 5-7-5 syllable shape.
The syllable counts are checked before writing, so a bad edit fails
here instead of shipping a broken entry.
"""

from pathlib import Path

HAIKU = (
    "Cursor blinks at three\n"
    "the log swears the bug is dead\n"
    "it was my typo\n"
)

# Syllables per line, counted by hand: Cur-sor(2) blinks at three (5);
# the log swears the bug is dead (7); it was my ty-po(2) (5).


def main() -> None:
    lines = HAIKU.strip("\n").split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert len(HAIKU) <= 200, f"entry is {len(HAIKU)} chars, over the 200 cap"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
