"""Write one funny one-line review of Monday to /output/entry.txt.

Standard library only. No network, no randomness, no clock:
the output is fully deterministic.
"""

import os

LINE = (
    "Monday, one star: my alarm snoozed itself, the bus left without me, "
    "and standup spent forty minutes scheduling a meeting about the next meeting."
)


def validate_entry(text: str) -> None:
    """Check the entry against the bounty gate: 1-200 chars, one line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text.strip() != text or "\n" in text:
        raise ValueError("entry must be a single line with no surrounding whitespace")


def main() -> None:
    validate_entry(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
