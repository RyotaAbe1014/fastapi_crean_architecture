from pydantic import BaseModel
from typing import Optional


class UserRequestSchema(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class UserResponseSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True
