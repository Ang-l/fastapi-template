from typing import Any
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import as_declarative, declared_attr


class BaseMixin:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)    ##### 时间使用的是utc的时间、可以根据业务调整
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = Column(Boolean, default=False, comment="状态")

@as_declarative()
class Base:
    id: Any
    __name__: str
 
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
