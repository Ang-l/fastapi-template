FROM python:3.11.9

COPY ../requirements.txt /requirements.txt

RUN mkdir /fastapi

WORKDIR /fastapi

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /requirements.txt

