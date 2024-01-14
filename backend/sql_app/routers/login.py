from datetime import timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import users
from ..dependencies import SessionDep, SettingsDep
from ..cookie import CookieTransport
from ..security import (
    create_access_token,
    verify_password,
)


## Create the FastAPI login instance
router = APIRouter(prefix="/login", tags=["login"])

cookie_transport = CookieTransport(cookie_max_age=3600)


## Schema for login
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


## helper functions
def authenticate(db: Session, email: str, password: str):
    user = users.get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


## Endpoint to login
@router.post("/access-token")
def login_access_token(
    db: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    settings: SettingsDep,
) -> Token:
    user = authenticate(db=db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(settings, user.id, access_token_expires)
    return Token(access_token=access_token, token_type="bearer")
