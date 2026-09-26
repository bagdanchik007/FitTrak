from pydantic import BaseModel


class VersionResponse(BaseModel):
    app: str
    version: str
    environment: str


class FeaturesResponse(BaseModel):
    features: dict[str, bool]
