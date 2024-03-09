# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com

from typing import Any
 
from sqlalchemy.ext.declarative import as_declarative, declared_attr
 
 
@as_declarative()
class Base:
    id: Any
    __name__: str
 
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()