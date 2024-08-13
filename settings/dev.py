# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com


# 数据库相关配置、使用mysql
DATABASE_HOST = "rm-bp13t56369v8bq2tm7o.mysql.rds.aliyuncs.com"
DATABASE_PORT = "3306"
DATABASE_USER = "root"
DATABASE_PASSWORD = "MdAEpE&K_$3EY%q"

DATABASE_NAME = "fastapi"
DATABASE_LANGUAGE = "utf8mb4"  # 固定参数一般不需要调整

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}?charset={DATABASE_LANGUAGE}"


### redis
REDIS_HOST = "47.99.221.73"
REDIS_PORT = "6379"
REDIS_PASSWORD = "h3qVF0yi"


#################################### celery 相关配置    ##########################################

### 消息队列配置
CELERY_BROKER_INFO = {
    "type": "redis",                ## 数据库类型
    "host": REDIS_HOST,             ## 主机
    "port": REDIS_PORT,             ## 端口
    "password": REDIS_PASSWORD,     ## 密码
    "box": "0"                      ## 数据库编号
}
CELERY_BROKER_URL = f"{CELERY_BROKER_INFO['type']}://:{CELERY_BROKER_INFO['password']}@{CELERY_BROKER_INFO['host']}:{CELERY_BROKER_INFO['port']}/{CELERY_BROKER_INFO['box']}"

### 结果存储 配置
CELERY_BACKEND_INFO = {
    "type": "redis",                ## 数据库类型
    "host": REDIS_HOST,             ## 主机
    "port": REDIS_PORT,             ## 端口
    "password": REDIS_PASSWORD,     ## 密码
    "box": "1"                      ## 数据库编号
}

CELERY_BACKEND_URL = f"{CELERY_BACKEND_INFO['type']}://:{CELERY_BACKEND_INFO['password']}@{CELERY_BACKEND_INFO['host']}:{CELERY_BACKEND_INFO['port']}/{CELERY_BACKEND_INFO['box']}"

CELERY_RESULT_LIFESPAN = 3600   ### 任务存储结果的过期时间、单位秒

#################################### celery 相关配置  end   ##########################################
