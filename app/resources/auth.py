import random
import string
from fastapi import APIRouter, status
from schemas.request.auth import UserRegisterRequest, UserLoginRequest
from schemas.response.auth import TokenResponse


router = APIRouter()


def get_random_token():
    length = 10
    token = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    return token


@router.post(
    "/sign-up/",
    status_code=status.HTTP_201_CREATED,
    response_model=TokenResponse,
)
async def register(
    user_data: UserRegisterRequest,
):
    return {"token": get_random_token()}


@router.post(
    "/login/",
    response_model=TokenResponse,
    status_code=status.HTTP_200_OK,
)
async def login(user_data: UserLoginRequest):
    # validate credentials logic here
    # if not user:
    # raise  HTTPException(status_code=403, detail="User not found")
    return {"token": get_random_token()}

