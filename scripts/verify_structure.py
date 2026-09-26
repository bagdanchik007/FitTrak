"""Verify expected package folders exist."""

from pathlib import Path
import sys

REQUIRED = [
    "app/domain",
    "app/application/services",
    "app/infrastructure/repositories",
    "app/api/v1",
    "tests/unit",
    "tests/integration",
]


def main() -> int:
    missing = [p for p in REQUIRED if not Path(p).exists()]
    if missing:
        print("Missing:")
        for p in missing:
            print(f"  - {p}")
        return 1
    print("Structure OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
