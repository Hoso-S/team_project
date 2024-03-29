from datetime import timedelta
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi_csrf_protect import CsrfProtect

from . import users
from ..dependencies import SessionDep
from ..security import settings, create_access_token, verify_password


## Create the FastAPI login instance
router = APIRouter(prefix="/login", tags=["login"])


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
    request: Request,
    csrf_protect: CsrfProtect = Depends(),
) -> Token:
    csrf_protect.validate_csrf(request)
    user = authenticate(db=db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(user.id, access_token_expires)
    response: JSONResponse = JSONResponse(status_code=200, content={"detail": "OK"})
    return Token(access_token=access_token, token_type="bearer")
