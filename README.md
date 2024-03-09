# 简介

```
基于fastapi搭建的快速模板
```

# 内容

## 环境搭建

```
python环境：python3 
运行环境：liunx
1、pip install -r requirements.txt 
2、cd fastapi-template/setting && ln -s dev.py settings.py && cd ..
3、uvicorn main:app --reload

访问：http://127.0.0.1:8000/docs
```



## 创建应用（目前仅支持liunx）

```shell
1、./startapp appname
```



## 数据库方面

### 数据库设置

```
1、调整 setting/dev.py 中配置项
2、生成迁移文件    alembic revision --autogenerate -m "备注" 
3、迁移至数据库    alembic upgrade head
```