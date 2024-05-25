from pydantic import BaseModel


class UrlBase(BaseModel):
    pass


class UrlCreateRequest(UrlBase):
    url: str


class UrlCreateResponse(UrlBase):
    short_url: str


class UrlCreate(UrlCreateRequest):
    short_url: str


class Url(UrlBase):
    id: int
    original_url: str
    short_url: str
    hits: int
    is_active: bool

    class Config:
        orm_mode = True
