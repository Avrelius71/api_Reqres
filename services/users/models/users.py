from datetime import datetime
from typing import Optional
from typing import List
from pydantic import BaseModel, Field


class Support(BaseModel):
    url: str
    text: str


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class SingleUserResponse(BaseModel):
    data: UserData
    support: Support


class CreateUserRequest(BaseModel):
    name: str
    job: str


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime


class UpdateUserRequest(BaseModel):
    name: Optional[str] = None
    job: Optional[str] = None


class UpdateUserResponse(BaseModel):
    name: Optional[str] = None
    job: Optional[str] = None
    updatedAt: datetime


class UsersListResponse(BaseModel):
    data: List[UserData]
    support: Support
    page: int
    per_page: int
    total: int
    total_pages: int
