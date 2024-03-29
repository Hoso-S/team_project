from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel, PositiveInt
from sqlalchemy.orm import Session

from ..dependencies import SessionDep
from .. import database


## Create the FastAPI instance
router = APIRouter(prefix="/students", tags=["students"])


## Schema for Student
class student(BaseModel):
    student_id: str
    name: str
    dept_name: str
    tot_cred: PositiveInt

    class Config:
        from_attributes = True


class student_update(BaseModel):
    tot_cred: PositiveInt

    class Config:
        from_attributes = True


## helper functions
def insert_student(db: Session, student: student):
    db_student = database.student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_student(db: Session, student_id: str):
    return (
        db.query(database.student)
        .filter(database.student.student_id == student_id)
        .first()
    )


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.student).offset(skip).limit(limit).all()


def del_student(db: Session, student_id: str):
    db.query(database.student).filter(
        database.student.student_id == student_id
    ).delete()
    db.commit()
    return


## Endpoint to Student
@router.get("/{student_id}", response_model=student)
async def read_student(db: SessionDep, student_id: str):
    db_student = get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


@router.get("/", response_model=list[student])
async def read_students(db: SessionDep, skip: int = 0, limit: int = 100):
    students = get_students(db, skip=skip, limit=limit)
    return students


@router.post("/", response_model=student)
async def create_student(db: SessionDep, student: student):
    db_student = get_student(db, student_id=student.student_id)
    if db_student:
        raise HTTPException(status_code=400, detail="Student already registered")
    return insert_student(db=db, student=student)


@router.delete("/{student_id}")
async def delete_student(db: SessionDep, student_id: str):
    db_student = get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return del_student(db=db, student_id=student_id)
