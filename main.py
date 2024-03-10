# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com

from fastapi import FastAPI

from application.users import views as user_view


app = FastAPI()

app.include_router(
    user_view.router,
    prefix="/v1/users",
    responses={404: {"description": "访问的页面不存在"}, 405:{"description": "请求方式异常"}},

)
