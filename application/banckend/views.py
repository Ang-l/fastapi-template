from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def index():
    return {"code": 10200}