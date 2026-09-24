"""Smoke-import main application modules."""

import importlib
import sys

MODULES = [
    "app.main",
    "app.core.config",
    "app.core.feature_flags",
    "app.domain.streak.services",
    "app.domain.summary.services",
]


def main() -> int:
    failed = []
    for name in MODULES:
        try:
            importlib.import_module(name)
            print(f"OK  {name}")
        except Exception as exc:  # noqa: BLE001
            print(f"FAIL {name}: {exc}")
            failed.append(name)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
