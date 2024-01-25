from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..dependencies import SessionDep
from .. import database


## Create the FastAPI instance
router = APIRouter(prefix="/takes", tags=["takes"])


## Schema for takes
class takes(BaseModel):
    student_id: str
    course_id: str
    sec_id: str
    semester: str
    year: int
    grade: str

    class Config:
        from_attributes = True


class takes_update(BaseModel):
    grade: str

    class Config:
        from_attributes = True


## helper functions
def insert_takes(db: Session, takes: takes):
    db_takes = database.takes(**takes.model_dump())
    db.add(db_takes)
    db.commit()
    db.refresh(db_takes)
    return db_takes


def get_takes(
    db: Session, student_id: str, course_id: str, sec_id: str, semester: str, year: int
):
    return (
        db.query(database.takes)
        .filter(database.takes.student_id == student_id)
        .filter(database.takes.course_id == course_id)
        .filter(database.takes.sec_id == sec_id)
        .filter(database.takes.semester == semester)
        .filter(database.takes.year == year)
        .first()
    )


def get_all_takes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.takes).offset(skip).limit(limit).all()


def del_takes(
    db: Session, student_id: str, course_id: str, sec_id: str, semester: str, year: int
):
    db.query(database.takes).filter(database.takes.student_id == student_id).filter(
        database.takes.course_id == course_id
    ).filter(database.takes.sec_id == sec_id).filter(
        database.takes.semester == semester
    ).filter(
        database.takes.year == year
    ).delete()
    db.commit()
    return


## Endpoint to takes
@router.get(
    "/{student_id}/{course_id}/{sec_id}/{semester}/{year}",
    response_model=takes,
)
async def read_takes(
    db: SessionDep,
    student_id: str,
    course_id: str,
    sec_id: str,
    semester: str,
    year: int,
):
    db_takes = get_takes(
        db,
        student_id=student_id,
        course_id=course_id,
        sec_id=sec_id,
        semester=semester,
        year=year,
    )
    if db_takes is None:
        raise HTTPException(status_code=404, detail="Takes not found")
    return db_takes


@router.get("/", response_model=list[takes])
async def read_takes(db: SessionDep, skip: int = 0, limit: int = 100):
    takes = get_all_takes(db, skip=skip, limit=limit)
    return takes


@router.post("/", response_model=takes)
async def create_takes(db: SessionDep, takes: takes):
    db_takes = get_takes(
        db,
        ID=takes.student_id,
        course_id=takes.course_id,
        sec_id=takes.sec_id,
        semester=takes.semester,
        year=takes.year,
    )
    if db_takes:
        raise HTTPException(status_code=400, detail="Takes already registered")
    return insert_takes(db=db, takes=takes)


@router.delete("/{student_id}/{course_id}/{sec_id}/{semester}/{year}")
async def delete_takes(
    db: SessionDep,
    student_id: str,
    course_id: str,
    sec_id: str,
    semester: str,
    year: int,
):
    db_takes = get_takes(
        db,
        student_id=student_id,
        course_id=course_id,
        sec_id=sec_id,
        semester=semester,
        year=year,
    )
    if db_takes is None:
        raise HTTPException(status_code=404, detail="Takes not found")
    return del_takes(
        db=db,
        student_id=student_id,
        course_id=course_id,
        sec_id=sec_id,
        semester=semester,
        year=year,
    )
