"""Count registered routes."""

from app.main import app


def main() -> None:
    routes = [r for r in app.routes if getattr(r, "methods", None)]
    print(f"Registered routes: {len(routes)}")
    for r in sorted(routes, key=lambda x: getattr(x, "path", "")):
        methods = ",".join(sorted(r.methods - {"HEAD", "OPTIONS"}))
        if methods:
            print(f"  {methods:15} {r.path}")


if __name__ == "__main__":
    main()
