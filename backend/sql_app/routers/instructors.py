from fastapi import APIRouter
from fastapi import HTTPException, Depends
from pydantic import BaseModel, PositiveFloat
from sqlalchemy.orm import Session

from ..dependencies import get_db
from .. import database


## Create the FastAPI instance
router = APIRouter(prefix="/instructors", tags=["instructors"])


## Schema for instructor
class instructor(BaseModel):
    instructor_id: str
    name: str
    dept_name: str
    salary: PositiveFloat

    class Config:
        from_attributes = True


class instructor_update(BaseModel):
    salary: PositiveFloat

    class Config:
        from_attributes = True


## helper functions
def insert_instructor(db: Session, instructor: instructor):
    db_instructor = database.instructor(**instructor.model_dump())
    db.add(db_instructor)
    db.commit()
    db.refresh(db_instructor)
    return db_instructor


def get_instructor(db: Session, instructor_id: str):
    return (
        db.query(database.instructor)
        .filter(database.instructor.instructor_id == instructor_id)
        .first()
    )


def get_instructors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.instructor).offset(skip).limit(limit).all()


def del_instructor(db: Session, instructor_id: str):
    db.query(database.instructor).filter(
        database.instructor.instructor_id == instructor_id
    ).delete()
    db.commit()
    return


## Endpoint to Classroom
@router.get("/{instructor_id}", response_model=instructor)
async def read_instructor(instructor_id: str, db: Session = Depends(get_db)):
    db_instructor = get_instructor(db, instructor_id=instructor_id)
    if db_instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return db_instructor


@router.get("/", response_model=list[instructor])
async def read_instructors(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    instructors = get_instructors(db, skip=skip, limit=limit)
    return instructors


@router.post("/", response_model=instructor)
async def create_instructor(instructor: instructor, db: Session = Depends(get_db)):
    db_instructor = get_instructor(db, instructor_id=instructor.instructor_id)
    if db_instructor:
        raise HTTPException(status_code=400, detail="Instructor already registered")
    return insert_instructor(db=db, instructor=instructor)


@router.delete("/{instructor_id}")
async def delete_instructor(instructor_id: str, db: Session = Depends(get_db)):
    db_instructor = get_instructor(db, instructor_id=instructor_id)
    if db_instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return del_instructor(db=db, instructor_id=instructor_id)
