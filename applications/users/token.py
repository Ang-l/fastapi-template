from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import JWTError, jwt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="v1/users/token")


# 秘钥, 加密算法和过期时间设置
SECRET_KEY = "920decd2236c8cd7c36100a8e60e9506ebd1198be072a346bc13ae040b5b3805"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username == "test":
        return {"username": "testuser", "password": get_password_hash("testpassword")}
    return None

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    # if not user or not verify_password(password, user['password']):
    #     return False
    return {"username": "testuser", "password": "123456"}

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
