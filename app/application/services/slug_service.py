from app.domain.text.slugify import slugify

def slug_for(title: str | None) -> dict:
    return {"slug": slugify(title), "source": title}
