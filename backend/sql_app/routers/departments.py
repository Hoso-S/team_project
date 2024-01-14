from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel, PositiveFloat
from sqlalchemy.orm import Session

from ..dependencies import SessionDep
from .. import database


## Create the FastAPI instance
router = APIRouter(prefix="/departments", tags=["departments"])


## Schema for Department
class department(BaseModel):
    dept_name: str
    building: str
    budget: PositiveFloat

    class Config:
        from_attributes = True


class department_update(BaseModel):
    budget: PositiveFloat

    class Config:
        from_attributes = True


## helper functions
def insert_department(db: Session, department: department):
    db_department = database.department(**department.model_dump())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


def get_department(db: Session, dept_name: str):
    return (
        db.query(database.department)
        .filter(database.department.dept_name == dept_name)
        .first()
    )


def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.department).offset(skip).limit(limit).all()


def del_department(db: Session, dept_name: str):
    db.query(database.department).filter(
        database.department.dept_name == dept_name
    ).delete()
    db.commit()
    return


## Endpoint to Department
@router.get("/{dept_name}", response_model=department)
async def read_department(db: SessionDep, dept_name: str):
    db_department = get_department(db, dept_name=dept_name)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department


@router.get("/", response_model=list[department])
async def read_departments(db: SessionDep, skip: int = 0, limit: int = 100):
    departments = get_departments(db, skip=skip, limit=limit)
    return departments


@router.post("/", response_model=department)
async def create_department(db: SessionDep, department: department):
    db_department = get_department(db, dept_name=department.dept_name)
    if db_department:
        raise HTTPException(status_code=400, detail="Department already registered")
    return insert_department(db=db, department=department)


@router.delete("/{dept_name}")
async def delete_department(db: SessionDep, dept_name: str):
    db_department = get_department(db, dept_name=dept_name)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return del_department(db=db, dept_name=dept_name)
