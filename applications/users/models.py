
from sqlalchemy import Column, String

from db.BaseMixin import BaseMixin, Base


class Users(BaseMixin, Base):

    __tablename__ = "users"

    username = Column(String(50), comment="用户名")
    password = Column(String(256), comment="密码")