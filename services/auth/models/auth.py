from typing import List
from pydantic import BaseModel


class RegisterRequest(BaseModel):
    email: str
    password: str


class RegisterResponse(BaseModel):
    id: int
    token: str


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    token: str


class ErrorResponse(BaseModel):
    error: str