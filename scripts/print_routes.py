"""Print registered API routes (run with app importable)."""

from app.main import app


def main() -> None:
    for route in app.routes:
        methods = getattr(route, "methods", None)
        path = getattr(route, "path", None)
        if methods and path:
            print(f"{','.join(sorted(methods)):10} {path}")


if __name__ == "__main__":
    main()
