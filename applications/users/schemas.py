"""
This file contains some basic classes.
each of which has been separated separately for display purposes and can be adjusted accordingly.
"""


from pydantic import BaseModel
from typing import Optional


class ResponseBaseModel(BaseModel):     ######  返回的基础类
    code: Optional[int] = 10200
    msg: Optional[str] = "success"


class UserModel(BaseModel):             #### 用户的基础类
    username: str


class LoginModel(UserModel):            #### 登录验证数据类
    password: str

class RegisterModel(UserModel):
    password: str


class LoginResponse(ResponseBaseModel):     ###### 登录返回类
    token: Optional[str] = ""


class RegisterResponse(ResponseBaseModel):
    pass