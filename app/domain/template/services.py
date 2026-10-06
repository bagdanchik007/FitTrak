"""Workout template pure helpers."""


def normalize_template_name(name: str) -> str:
    cleaned = " ".join(name.strip().split())
    return cleaned[:120] if cleaned else "Untitled template"
