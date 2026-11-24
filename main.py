#!/usr/bin/env python3
"""Two Days of Quiet Dread - one-line code review comment.

The program writes a single line to /output/entry.txt: a code review
comment that approves a pull request while carrying quiet existential
dread. Pure standard library, deterministic: the same line every run.
"""

from pathlib import Path

LINE = "Approved. Clean diff, green tests \u2014 in a thousand years this will be the only evidence we were ever here."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # Hold the line to the bounty gate before writing it out: one line,
    # 1 to 140 characters, not only white space.
    assert "\n" not in LINE and "\r" not in LINE
    assert 1 <= len(LINE) <= 140
    assert LINE.strip()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
