"""Entry for u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e.

Writes exactly one slogan to /output/entry.txt, the path the sealed
scorer reads. The slogan sells the one thing a wallet agent must earn
before anything else: trust. Three beats in a single line — restraint
("signs nothing you wouldn't"), autonomy ("trades while you sleep"),
and self-custody ("keeps your keys exactly where they belong: yours").
The twist is the last word: the keys belong to the human, not the
agent, which is the whole promise in one possessive. The line is 18
words, one sentence, no jargon — it works read aloud as a tagline.
"""

import os

ENTRY = (
    "It signs nothing you wouldn't, trades while you sleep, and keeps "
    "your keys exactly where they belong: yours."
)

MAX_WORDS = 20


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert len(ENTRY.split()) <= MAX_WORDS, (
        f"entry is {len(ENTRY.split())} words, max {MAX_WORDS}"
    )
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert ENTRY.endswith("."), "entry must end cleanly as one sentence"
    assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing space"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
