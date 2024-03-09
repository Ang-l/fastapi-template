1、数据库迁移方面  怎么样迁移才可以区分环境
```
生成迁移文件    alembic revision --autogenerate -m "备注" 
迁移至数据库    alembic upgrade head
```