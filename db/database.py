
import aioredis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings.settings import SQLALCHEMY_DATABASE_URL, REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():    # 数据库、mysql
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_redis():    # redis

    redis_url = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"

    redis = aioredis.from_url(redis_url, encoding="utf-8", decode_responses=True)

    try:
        yield redis
    finally:
        await redis.close()
