from datetime import timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError

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


class CsrfSettings(BaseModel):
    secret_key: str = "Kaakaww!"


@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()


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
    request: Request,
    db: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    settings: SettingsDep,
    csrf_protect: CsrfProtect = Depends(),
) -> Token:
    csrf_protect.validate_csrf(request)
    user = authenticate(db=db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(settings, user.id, access_token_expires)
    response: JSONResponse = JSONResponse(status_code=200, content={"detail": "OK"})
    csrf_protect.unset_csrf_cookie(response)
    return Token(access_token=access_token, token_type="bearer")


@router.get("/csrftoken/")
async def get_csrf_token(csrf_protect: CsrfProtect = Depends()):
    csrf_token, signed_token = csrf_protect.generate_csrf_tokens()
    response = JSONResponse(status_code=200, content={"csrf_token": "cookie"})
    csrf_protect.set_csrf_cookie(signed_token, response)
    return response
