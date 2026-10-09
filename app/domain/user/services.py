"""User domain pure helpers."""


def display_name(full_name: str | None, email: str) -> str:
    if full_name and full_name.strip():
        return full_name.strip()
    return email.split("@")[0]
