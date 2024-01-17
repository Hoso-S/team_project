from fastapi import APIRouter, Depends, Request
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi_csrf_protect import CsrfProtect

from ..dependencies import SessionDep
from ..security import get_password_hash
from .. import database


## Create the FastAPI instance
router = APIRouter(prefix="/users", tags=["users"])


## Schema for User
class UserBase(BaseModel):
    email: str
    is_active: bool
    is_superuser: bool

class UserUpdateEmail(BaseModel):  # メールアドレス変更のためのモデル
    new_email: str

class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int


## helper functions
def get_user(db: Session, user_id: int):
    return db.query(database.users).filter(database.users.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(database.users).filter(database.users.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.users).offset(skip).limit(limit).all()


def insert_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = database.users(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_email(db: Session, user_id: int, new_email: str):
    db_user = get_user(db, user_id=user_id)
    if db_user:
        db_user.email = new_email
        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        return None

## Endpoint to section
@router.post("/", response_model=UserOut)
def create_user(
    db: SessionDep,
    user: UserCreate,
    request: Request,
    csrf_protect: CsrfProtect = Depends(),
):
    csrf_protect.validate_csrf(request)
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return insert_user(db=db, user=user)


@router.get("/", response_model=list[UserOut])
def read_users(db: SessionDep, skip: int = 0, limit: int = 100):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=UserOut)
def read_user(db: SessionDep, user_id: int):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/{user_id}/update_email", response_model=UserOut)  # 追加: メールアドレスの更新エンドポイント
def update_email_endpoint(
    user_id: int,
    user_update_email: UserUpdateEmail,
    db: SessionDep,
    request: Request,
    csrf_protect: CsrfProtect = Depends(),
):
    csrf_protect.validate_csrf(request)
    db_user = get_user(db, user_id=user_id)
    if db_user:
        return update_email(db=db, user_id=user_id, new_email=user_update_email.new_email)
    else:
        raise HTTPException(status_code=404, detail="User not found")

