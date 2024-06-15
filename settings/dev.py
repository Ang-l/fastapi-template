# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com


# 数据库相关配置、使用mysql
DATABASE_HOST = ""
DATABASE_PORT = ""
DATABASE_USER = ""
DATABASE_PASSWORD = ""

DATABASE_NAME = ""
DATABASE_LANGUAGE = "utf8mb4"  # 固定参数一般不需要调整

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}?charset={DATABASE_LANGUAGE}"


### redis
REDIS_HOST = ""
REDIS_PORT = ""
REDIS_PASSWORD = ""
