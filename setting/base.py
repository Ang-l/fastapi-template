# Author: Ang-l
# github: https://github.com/Ang-l/fastapi-template
# Date: 2024-03-10
# email: lijiang_lja@163.com

# from db.database import SessionLocal

# def get_db():
#     try:
#         db = SessionLocal()
#         yield db
#     finally:
#         db.close()

def return_response(code=10200, msg="", data=[], additional={}):
    RESPONSE = {"code": code, "msg": msg, "data": data, "additional": additional}
    return RESPONSE
