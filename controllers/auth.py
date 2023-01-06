from fastapi import APIRouter, status

from schemas import UserRegister, User, UserInDB

# database
from config.database import Session
from models import User as UserModel

# auth
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_password_hash(password):
    return pwd_context.hash(password)

########################

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post(
    path = "/signup",
    response_model = dict,
    status_code = status.HTTP_201_CREATED,
    summary = "Register a User",
)
def signup(user: UserRegister):

    hashed = get_password_hash(user.password)
    userdict = user.dict()
    del userdict['password'] # Remove it because db model is hashed_password

    db = Session()
    new_user = UserModel( 
                    **userdict, 
                    hashed_password = hashed
            )
    db.add(new_user)
    db.commit()

    return {"message": "User created"}

@router.post(
    path = "/login",
    response_model = User,
    status_code = status.HTTP_200_OK,
    summary = "Login a User",
)
def login():
    pass