from pydantic import BaseModel


class SearchTorrentsBody(BaseModel):
    query: str


class GetLinkBody(BaseModel):
    link: str