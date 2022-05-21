from uuid import UUID, uuid4
from pydantic import BaseModel, Field, constr
from typing import List, Optional


class UserInfo(BaseModel):
    """
    用户信息
    """
    phone: Optional[constr(max_length=11, min_length=11)]
    usename: Optional[constr(max_length=6)]
    email: Optional[constr(regex=r'^[A-Za-z0-9]+([_\.][A-Za-z0-9]+)*@([A-Za-z0-9\-]+\.)+[A-Za-z]{2,6}$')]
    password: str


class LoginInfo(BaseModel):
    """
    登陆信息
    """
    username: str
    password: str
