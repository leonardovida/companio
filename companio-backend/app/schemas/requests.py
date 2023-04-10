from pydantic import BaseModel, EmailStr


class BaseRequest(BaseModel):
    # may define additional fields or config shared across requests
    pass


class RefreshTokenRequest(BaseRequest):
    refresh_token: str


class UserUpdatePasswordRequest(BaseRequest):
    password: str


class UserCreateRequest(BaseRequest):
    email: EmailStr
    password: str


class ListCreateRequest(BaseRequest):
    email: EmailStr
    city: str
    list: str
    phone: str
    service: str


class NoteIn(BaseModel):
    text: str
    completed: bool
