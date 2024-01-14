from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Literal
from sqlalchemy.orm import Session

from ..dependencies import SessionDep
from .. import database


## Create the FastAPI instance
router = APIRouter(prefix="/sections", tags=["sections"])


## Schema for section
class section(BaseModel):
    course_id: str
    instructor_id: str
    sec_id: str
    semester: Literal["Fall", "Winter", "Spring", "Summer"]
    year: int
    building: str
    room_number: str
    time_slot_id: str

    class Config:
        from_attributes = True


class section_update(BaseModel):
    building: str
    room_number: str
    time_slot_id: str

    class Config:
        from_attributes = True


## helper functions
def insert_section(db: Session, section: section):
    db_section = database.section(**section.model_dump())
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section


def get_section(
    db: Session,
    course_id: str,
    instructor_id: str,
    sec_id: str,
    semester: str,
    year: int,
):
    return (
        db.query(database.section)
        .filter(database.section.course_id == course_id)
        .filter(database.section.instructor_id == instructor_id)
        .filter(database.section.sec_id == sec_id)
        .filter(database.section.semester == semester)
        .filter(database.section.year == year)
        .first()
    )


def get_sections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.section).offset(skip).limit(limit).all()


def del_section(db: Session, course_id: str, sec_id: str, semester: str, year: int):
    db.query(database.section).filter(database.section.course_id == course_id).filter(
        database.section.sec_id == sec_id
    ).filter(database.section.semester == semester).filter(
        database.section.year == year
    ).delete()
    db.commit()
    return


## Endpoint to section
@router.get(
    "/{course_id}/{instructor_id}/{sec_id}/{semester}/{year}",
    response_model=section,
)
async def read_section(
    db: SessionDep,
    course_id: str,
    instructor_id: str,
    sec_id: str,
    semester: str,
    year: int,
):
    db_section = get_section(
        db,
        course_id=course_id,
        instructor_id=instructor_id,
        sec_id=sec_id,
        semester=semester,
        year=year,
    )
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section


@router.get("/", response_model=list[section])
async def read_sections(db: SessionDep, skip: int = 0, limit: int = 100):
    sections = get_sections(db, skip=skip, limit=limit)
    return sections


@router.post("/", response_model=section)
async def create_section(db: SessionDep, section: section):
    db_section = get_section(
        db,
        course_id=section.course_id,
        instructor_id=section.instructor_id,
        sec_id=section.sec_id,
        semester=section.semester,
        year=section.year,
    )
    if db_section:
        raise HTTPException(status_code=400, detail="Section already registered")
    return insert_section(db=db, section=section)


@router.delete("/{course_id}/{instructor_id}/{sec_id}/{semester}/{year}")
async def delete_section(
    db: SessionDep,
    course_id: str,
    instructor_id: str,
    sec_id: str,
    semester: str,
    year: int,
):
    db_section = get_section(
        db=db,
        course_id=course_id,
        instructor_id=instructor_id,
        sec_id=sec_id,
        semester=semester,
        year=year,
    )
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return del_section(
        db=db,
        course_id=course_id,
        instructor_id=instructor_id,
        sec_id=sec_id,
        semester=semester,
        year=year,
    )
