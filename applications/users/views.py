import datetime, logging
from functools import wraps
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt

from db.database import get_db
from applications.users.models import Users
from applications.users.schemas import LoginModel, LoginResponse, RegisterResponse, RegisterModel
from applications.users.token import (
    authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, oauth2_scheme,
    SECRET_KEY, ALGORITHM
)


router = APIRouter()

log =  logging.getLogger("user_logger")


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me/")
async def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        print("-----token----", token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        print("-----payload----", payload)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # user = get_user(db, username)
    user = {"username": "111"}
    if user is None:
        raise credentials_exception
    return user


# 修改的 get_user 函数
def get_user(request: Request):
    user = {"username": "johndoe", "role": "admin"}
    # 将 user 信息存储到 request.state
    request.state.user = user
    return user


# 装饰器，用于访问 user 信息
def log_user_activity(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request = kwargs.get('request')
        if request and hasattr(request.state, 'user'):
            user_inf = request.state.user
            print(f"User {user_inf['username']} with role {user_inf['role']} is making a request")
        return await func(*args, **kwargs)
    return wrapper



@router.get("/me", )
@log_user_activity
async def me(request: Request, user_inf = Depends(get_user), db: Session = Depends(get_db)):
    return {"code": 10200, "user": request.state.user}


@router.post("/login", response_model=LoginResponse)
def login(login_user: LoginModel, db: Session = Depends(get_db)):
    user = db.query(Users).filter_by(username=login_user.username, password=login_user.password).first()

    if not user:    #### 用户不存在的情况
        log.warning("错误请求用户不存在")
        ###### 返回业务错误码   推荐、因为一些公司都有一些自己的业务错误码
        return {"code": 10401, "msg": "The username or password you entered is incorrect."}

        ##### 直接返回浏览器的异常  不推荐、因为会直接浏览器抛出401异常
        # raise HTTPException(status_code=401, detail="The username or password you entered is incorrect.")
    
    ########### 用户存在生成token、 exp字段为过期时间单位为秒示例为1天过期
    payload = {
        'user_id': user.id, 
        'username': user.username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 24)
    }

    token = encryption(payload)

    return {"token": token}     ######## 设置过期时间


@router.post("/register", response_model=RegisterResponse)
def register(reg_user: RegisterModel, db: Session = Depends(get_db)):
    try:
        db_user = Users(**reg_user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return {}

    except Exception as e:
        db.rollback()       ########### 回滚事务

        return {"code": 10500, "msg": str(e)}