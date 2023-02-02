from pydantic import BaseModel
from typing import Optional


class UserRequestSchema(BaseModel):
    name: str
    email: str
    password: str


class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str
