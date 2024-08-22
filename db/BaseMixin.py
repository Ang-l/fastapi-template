from typing import Any
from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import relationship


class BaseMixin:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_deleted = Column(Boolean, default=False, comment="状态")


@as_declarative()
class Base:
    id: Any
    __name__: str
 
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()