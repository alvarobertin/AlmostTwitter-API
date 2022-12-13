from fastapi import APIRouter, status

from schemas import User

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post(
    path = "/signup",
    response_model = User,
    status_code = status.HTTP_201_CREATED,
    summary = "Register a User",
)
def signup():
    pass

@router.post(
    path = "/login",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Login a User",
)
def login():
    pass