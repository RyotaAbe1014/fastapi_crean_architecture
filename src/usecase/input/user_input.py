from pydantic import BaseModel
from typing import Optional


class UserInputData(BaseModel):
    name: str
    email: str
    password: str