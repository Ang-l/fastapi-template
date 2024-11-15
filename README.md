# fastapi template

# 简介

```
基于fastapi搭建的快速模板、由于每次创建一个fastapi项目都要构建结果太麻烦所以做了一个快速搭建项目的模板
(该模版完全是依据作者的编码习惯搭建的，如果有更好的结构欢迎您提PR
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
|   |—— __init__.py
|
├── utils   
│   ├── __init__.py
│   └── captcha.py  # ### captcha 生成人机交互的脚本
│
├── db/
│   ├── __init__.py
│   ├── BaseMixin.py
│   ├── base.py
│   └── base_class.py
│
├── setting/
│   ├── __init__.py
|   ├── logs.py     ### log 相关配置
│   └── dev.py
│
├── main.py     ## 出入口文件
├── __init__.py
├── requirements.txt    ### 依赖文件
├── alembic.ini         ### 数据库迁移相关文件
├── startapp.py         ### 创建app脚本
└── README.md           ### 描述文件
```

# 内容

## 环境搭建

```
python环境：python3 
运行环境：liunx、 windows视情况而定
1、pip install -r requirements.txt 
2、cd fastapi-template/settings && ln -s dev.py settings.py && cd ..
3、uvicorn main:app --reload

#### 启动celery 
celery -A celery_app.config worker --loglevel=info

访问：http://127.0.0.1:8000/docs
```

## 加入 captcha
- [captcha 使用说明](https://github.com/Ang-l/captcha)
- 现在大部分应用都需要有人机操作的验证故在模版中加入 captcha

## 创建应用

```shell
两种方式
1、python startapp.py appname （推荐方式）
```


## 数据库方面

### 数据库设置

```
1、调整 settings/dev.py 中配置项
2、生成迁移文件    alembic revision --autogenerate -m "备注" 
3、迁移至数据库    alembic upgrade head
```
