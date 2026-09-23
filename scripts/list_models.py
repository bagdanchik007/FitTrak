"""List registered SQLAlchemy model table names."""

from app.infrastructure.database.models import *  # noqa: F401, F403
from app.infrastructure.database.base import Base


def main() -> None:
    tables = sorted(Base.metadata.tables.keys())
    print(f"{len(tables)} tables:")
    for name in tables:
        print(f"  - {name}")


if __name__ == "__main__":
    main()
