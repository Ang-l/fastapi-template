import datetime, logging

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from db.database import get_db
from applications.users.models import Users
from applications.users.schemas import LoginModel, LoginResponse, RegisterResponse, RegisterModel
from applications.users.token import encryption, decryption


router = APIRouter()

log =  logging.getLogger("user_logger")


@router.get("/me", )
def me(db: Session = Depends(get_db)):
    pass


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