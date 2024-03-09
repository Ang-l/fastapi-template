# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com

from sqlalchemy import Boolean, Column, Integer, String
 
from db.base_class import Base
from db.BaseMixin import BaseMixin
 
 
class User(BaseMixin, Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True, index=True, comment="id")
    username = Column(String(50), comment="名称")
    mobile = Column(String(11), unique=True, index=True, comment="手机号")
    password = Column(String(128), comment="密码")
    is_active = Column(Boolean, default=True, comment="状态")
 