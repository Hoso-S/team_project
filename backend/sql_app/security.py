from datetime import datetime, timedelta
from functools import lru_cache
from typing import Any, Union
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login/access-token")


## Settings
class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )


@lru_cache
def get_settings():
    return Settings()


class CsrfSettings(BaseModel):
    secret_key: str = "asecrettoeverybody"
    cookie_samesite: str = "none"
    cookie_secure: bool = True
    token_location: str = "body"
    token_key: str = "csrf-token"


def create_access_token(
    settings: Settings, subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def verify_csrf(csrf_protect, headers):
    csrf_token = csrf_protect.get_csrf_from_headers(headers)
    csrf_protect.validate_csrf(csrf_token)
    return
