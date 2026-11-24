"""Make the AI Judge Laugh - make.fun bounty entry (program/v1).

Writes a single funny line (122 characters) to /output/entry.txt and
also prints it byte-exact to stdout, with no trailing newline.
"""

import os
import sys

ENTRY = "I told the AI judge my best joke - it laughed, then sentenced me to life without parole for assaulting its sense of humor."
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main() -> None:
    # The gate reads /output/entry.txt: 1-200 UTF-8 characters, no extra
    # whitespace, so write the line exactly as-is, with no trailing newline.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
