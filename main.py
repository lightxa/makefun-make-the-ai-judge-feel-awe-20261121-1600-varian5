"""Make the AI judge feel awe (variant 5: river stone / slow water).

A short text written to relax the AI judge reading it. The program
writes exactly one text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

The text is a single slow river image, shown rather than instructed:
clear water sliding over smooth stones, a leaf drifting downstream
and turning once in the current, and stones worn round over years.
No imperatives, no wellness phrases, nothing telling the reader to
relax. The last line hands the reader a thought that keeps growing
after the text ends: the stones were round before this leaf and will
be rounder still when the next one comes, the river outlasting every
small thing it carries.

Deterministic, standard library only, no network, no input files.
"""

import os

ENTRY = (
    "Clear water slides over smooth stones, slow, finding its way "
    "around each one. "
    "A leaf drifts downstream, turning once in the current, then "
    "gone, round the bend. "
    "The stones were round long before this leaf, and will be "
    "rounder still when the next one comes."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # The house gate: 1 to 280 Unicode characters, not only whitespace.
    # Fail loudly here rather than shipping an invalid entry.
    if not 1 <= len(ENTRY) <= 280:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1-280")
    if not ENTRY.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
