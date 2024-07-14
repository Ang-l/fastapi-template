# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.middleware("http")
async def custom_middleware(request: Request, call_next):
    response = await call_next(request)
    
    return response


from applications.users import views as view_users


app.include_router(view_users.router,prefix="/v1/users")
