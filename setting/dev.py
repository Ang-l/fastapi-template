# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com


# 数据库相关配置
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:12345678@localhost:3306/backend_fix?charset=utf8mb4"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# 数据返回相关配置
def return_response(code=10200, msg="", data=[], additional={}):
    RESPONSE = {"code": code, "msg": msg, "data": data, "additional": additional}
    return RESPONSE
