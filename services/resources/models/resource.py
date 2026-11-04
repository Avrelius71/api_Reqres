from typing import List
from pydantic import BaseModel


class ResourceData(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class Support(BaseModel):
    url: str
    text: str


class SingleResourceResponse(BaseModel):
    data: ResourceData
    support: Support


class ResourcesListResponse(BaseModel):
    data: List[ResourceData]
    page: int
    per_page: int
    total_pages: int
    total: int
