from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel, PositiveInt
from sqlalchemy.orm import Session

from ..dependencies import SessionDep
from .. import database


## Create the FastAPI instance
router = APIRouter(prefix="/courses", tags=["courses"])


## Schema for Course
class course(BaseModel):
    course_id: str
    title: str
    dept_name: str
    credits: PositiveInt

    class Config:
        from_attributes = True


class course_update(BaseModel):
    credits: PositiveInt

    class Config:
        from_attributes = True


## helper functions
def insert_course(db: Session, course: course):
    db_course = database.course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def get_course(db: Session, course_id: str):
    return (
        db.query(database.course).filter(database.course.course_id == course_id).first()
    )


def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.course).offset(skip).limit(limit).all()


def del_course(db: Session, course_id: str):
    db.query(database.course).filter(database.course.course_id == course_id).delete()
    db.commit()
    return


## Endpoint to Course
@router.get("/{course_id}", response_model=course)
def read_course(db: SessionDep, course_id: str):
    db_course = get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@router.get("/", response_model=list[course])
def read_courses(db: SessionDep, skip: int = 0, limit: int = 100):
    courses = get_courses(db, skip=skip, limit=limit)
    return courses


@router.post("/", response_model=course)
def create_course(db: SessionDep, course: course):
    db_course = get_course(db, course_id=course.course_id)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already registered")
    return insert_course(db=db, course=course)


@router.delete("/{course_id}")
def delete_course(db: SessionDep, course_id: str):
    db_course = get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return del_course(db=db, course_id=course_id)
