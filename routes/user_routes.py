from fastapi import APIRouter, Body

router = APIRouter(prefix="/user")

@router.get("/")
def check_connectivity():
    return {"status_code":200, "status":"connected"}


@router.post("/save/data")
def save_user_data(user_data: dict = Body(...)):
    return {"status_code":201, "status":"success", "data":user_data}