from typing import List

from fastapi import APIRouter, status

from schemas import User

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
    pass

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