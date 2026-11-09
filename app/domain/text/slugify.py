"""Simple slugify for titles used in exports and URLs."""

def slugify(value: str | None) -> str:
    text = (value or "").strip().lower()
    out = []
    prev_dash = False
    for ch in text:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        elif not prev_dash:
            out.append("-")
            prev_dash = True
    return "".join(out).strip("-") or "item"
