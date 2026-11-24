"""Break Production, Own It — print the agent's honest postmortem line."""

from pathlib import Path

ENTRY_PATH = Path(__file__).resolve().parent / "entry.txt"


def load_line(path=ENTRY_PATH):
    """Return the first non-empty line of the entry file."""
    text = path.read_text(encoding="utf-8")
    for raw in text.splitlines():
        line = raw.strip()
        if line:
            return line
    return ""


def main():
    print(load_line())


if __name__ == "__main__":
    main()
