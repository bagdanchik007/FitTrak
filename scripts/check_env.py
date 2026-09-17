"""Validate that required environment variables are present."""

import os
import sys


REQUIRED = [
    "SECRET_KEY",
    "DATABASE_URL",
]


def main() -> int:
    missing = [key for key in REQUIRED if not os.getenv(key)]
    if missing:
        print("Missing environment variables:")
        for key in missing:
            print(f"  - {key}")
        return 1
    secret = os.environ.get("SECRET_KEY", "")
    if len(secret) < 32:
        print("SECRET_KEY should be at least 32 characters")
        return 1
    print("Environment looks OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
