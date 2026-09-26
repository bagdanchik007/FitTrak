"""List top-level packages under app/."""

from pathlib import Path


def main() -> None:
    app = Path("app")
    for child in sorted(app.iterdir()):
        if child.is_dir() and not child.name.startswith("_") and child.name != "__pycache__":
            print(child.name)


if __name__ == "__main__":
    main()
