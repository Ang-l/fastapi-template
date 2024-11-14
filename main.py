# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com

import uuid

from typing import Callable
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from utils.captcha import Captcha
import settings.logs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.middleware("http")
async def custom_middleware(request: Request, call_next: Callable):

    # bug body = await request.body()       
    # Not recommended to use this method. For detailed information, please refer to the link below
    # https://github.com/fastapi/fastapi/discussions/9678
    # If there is a faster solution, please submit a PR. Thank you

    """ 2024-11-14
    The following solutions can be used, 
    although not perfect, 
    to temporarily solve the problem or achieve middleware like operations
    If there is a better solution, you are still welcome to bring it up
    
    # Add all endpoints to and api_router is not an app
    async def log_json(request: Request):
        print(await request.json())
    
    app = FastAPI()
    
    app.include_router(view.router, prefix="/view", dependencies=[Depends(log_json)])
    """

    response = await call_next(request)
    
    return response


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):

    # Customize the response to include a specific business status code
    return JSONResponse(
        status_code=200,  # Change the HTTP status code to 200
        content={
            "code": 10422,
            "msg": "Validation Error",
            "details": exc.errors()
        }
    )

captcha = Captcha()

@app.post("/v1/captcha")
def create_captcha():
    xxx = Captcha()
    resp = xxx.create(uuid.uuid4().hex)

    return resp
