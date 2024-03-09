# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com

from typing import List,Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    is_active: bool
    mobile: str
    email: str

class UserBase(BaseModel):
    mobile: str
    username: str

class UserCreate(UserBase):
    password: str
