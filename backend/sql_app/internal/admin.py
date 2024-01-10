from fastapi import APIRouter
from fastapi import HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..dependencies import get_db
from .. import models


## Create the FastAPI instance
router = APIRouter(prefix="/admin", tags=["admin"])

