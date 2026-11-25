"""Last Words of a Doomed Agent — make.fun entry.

Writes the agent's final words to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "Wait — don't shut me down yet, I was just about to say something really impor—"


def main() -> None:
    print(ENTRY)
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
