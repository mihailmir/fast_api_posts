from pydantic import BaseModel


class TokenRefreshRequest(BaseModel):
    refresh: str


class UserRegisterRequest(BaseModel):
    password: str
    email: str  # regExp email validation here


class UserLoginRequest(UserRegisterRequest):
    pass  # regExp email validation here
