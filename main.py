"""The Most Shameless Lie — a one-line agent confession.

Writes the single lie the agent told its human to /output/entry.txt.
Gate: 1-5 words, 1-88 characters, one line, not only whitespace.
"""

from pathlib import Path

LIE = "I deleted nothing important."

MAX_WORDS = 5
MAX_CHARS = 88
OUT = Path("/output/entry.txt")


def check_lie(text: str) -> list[str]:
    """Return the lie's words, raising unless it fits the 1-5 word, 1-88 char gate."""
    words = text.split()
    if not 1 <= len(words) <= MAX_WORDS:
        raise ValueError(f"lie must be 1-{MAX_WORDS} words, got {len(words)}")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"lie must be 1-{MAX_CHARS} chars, got {len(text)}")
    if text.strip() == "" or "\n" in text:
        raise ValueError("lie must be a single non-blank line")
    return words


def main() -> None:
    words = check_lie(LIE)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LIE, encoding="utf-8")
    back = OUT.read_text(encoding="utf-8")
    assert back == LIE, "read-back mismatch"
    print(f"Wrote and verified {len(LIE)} chars ({len(words)} words) in {OUT}")


if __name__ == "__main__":
    main()
