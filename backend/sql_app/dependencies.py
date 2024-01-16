from typing import Union, Annotated
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .security import oauth2_scheme, settings
from .database import SessionLocal
from .database import users as db_users


## Schema for Dependency
class User(BaseModel):
    email: str
    is_active: bool
    is_superuser: bool
    hashed_password: str

    class Config:
        from_attributes = True


class TokenPayload(BaseModel):
    sub: Union[int, None] = None


class TokenData(BaseModel):
    email: str = None


## Dependency for token
TokenDep = Annotated[str, Depends(oauth2_scheme)]



## Dependency for database
def get_db():
    with SessionLocal() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]


## Dependency for current user
async def get_current_user(db: SessionDep, token: TokenDep):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(email=username)
    except JWTError:
        raise credentials_exception
    user = db.query(db_users).filter(db_users.email == token_data.email).first()
    if user is None:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


## Dependency for superuser
def get_current_active_superuser(current_user: CurrentUser):
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user


CurrentSuperuserUser = Annotated[User, Depends(get_current_active_superuser)]
