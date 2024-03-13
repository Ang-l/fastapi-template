# 简介

```
基于fastapi搭建的快速模板
```

# 项目结构
```
project_name/
│
├── alembic/
│   ├── versions/
│   ├── README
│   ├── env.py
│   └── script.py.mako
│
├── application/
│
├── db/
│   ├── __init__.py
│   ├── BaseMixin.py
│   ├── base.py
│   └──base_class.py
│
├── setting/
│   ├── __init__.py
│   └── dev.py
│
├── main.py
├── __init__.py
├── requirements.txt
├── alembic.ini
├── startapp.py
└── README.md
```

# 内容

## 环境搭建

```
python环境：python3 
运行环境：liunx
1、pip install -r requirements.txt 
2、cd fastapi-template/settings && ln -s dev.py settings.py && cd ..
3、uvicorn main:app --reload

访问：http://127.0.0.1:8000/docs
```



## 创建应用

```shell
两种方式
1、./startapp.sh appname  # 已舍弃，不进行维护
2、python startapp.py appname
```


## 数据库方面

### 数据库设置

```
1、调整 settings/dev.py 中配置项
2、生成迁移文件    alembic revision --autogenerate -m "备注" 
3、迁移至数据库    alembic upgrade head
```
