"""Count lines of Python under app/."""

from pathlib import Path


def main() -> None:
    root = Path("app")
    total = 0
    files = 0
    for path in root.rglob("*.py"):
        lines = path.read_text(encoding="utf-8").count("\n") + 1
        total += lines
        files += 1
    print(f"{files} Python files, {total} lines under app/")


if __name__ == "__main__":
    main()
