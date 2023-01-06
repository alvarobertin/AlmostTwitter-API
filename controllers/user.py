from typing import List

from fastapi import APIRouter, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from schemas import User, UserInDB

# database
from config.database import Session
from models import User as UserModel


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.get(
    path = "/",
    response_model = List[User],
    status_code = status.HTTP_200_OK,
    summary = "Get all User",
    tags = ["Users"]
)
def get_all_users():
    db = Session()
    result = db.query(UserModel).all()


    return jsonable_encoder(result)


@router.get(
    path = "/{user_id}",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Get a User",
    tags = ["Users"]
)
def get_a_user():
    pass

@router.delete(
    path = "/{user_id}",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Delete a User",
    tags = ["Users"]
)
def delete_a_user():
    pass

@router.put(
    path = "/{user_id}",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Update a User",
    tags = ["Users"]
)
def update_a_user():
    pass