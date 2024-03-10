# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from setting import settings
 
SQLALCHEMY_DATABASE_URL = settings.SQLALCHEMY_DATABASE_URL
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()