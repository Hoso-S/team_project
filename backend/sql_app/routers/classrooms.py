from fastapi import APIRouter
from fastapi import HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..dependencies import get_db
from .. import database


## Create the FastAPI instance
router = APIRouter(prefix="/classrooms", tags=["classrooms"])


## Schema for Classroom
class classroom(BaseModel):
    building: str
    room_number: str
    capacity: int

    class Config:
        from_attributes = True


class classroom_update(BaseModel):
    capacity: int

    class Config:
        from_attributes = True


## helper functions
def insert_classroom(db: Session, classroom: classroom):
    db_classroom = database.classroom(**classroom.model_dump())
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom


def get_classroom(db: Session, building: str, room_number: str):
    return (
        db.query(database.classroom)
        .filter(database.classroom.building == building)
        .filter(database.classroom.room_number == room_number)
        .first()
    )


def get_classrooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.classroom).offset(skip).limit(limit).all()


def del_classroom(db: Session, building: str, room_number: str):
    db.query(database.classroom).filter(database.classroom.building == building).filter(
        database.classroom.room_number == room_number
    ).delete()
    db.commit()
    return


## Endpoint to Classroom
@router.get("/{building}/{room_number}", response_model=classroom)
async def read_classroom(
    building: str, room_number: str, db: Session = Depends(get_db)
):
    db_classroom = get_classroom(db, building=building, room_number=room_number)
    if db_classroom is None:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return db_classroom


@router.get("/", response_model=list[classroom])
async def read_classrooms(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    classrooms = get_classrooms(db, skip=skip, limit=limit)
    return classrooms


@router.post("/", response_model=classroom)
async def create_classroom(classroom: classroom, db: Session = Depends(get_db)):
    db_classroom = get_classroom(
        db, building=classroom.building, room_number=classroom.room_number
    )
    if db_classroom:
        raise HTTPException(status_code=400, detail="Classroom already registered")
    return insert_classroom(db=db, classroom=classroom)


@router.delete("/{building}/{room_number}")
async def delete_classroom(
    building: str, room_number: str, db: Session = Depends(get_db)
):
    db_classroom = get_classroom(db, building=building, room_number=room_number)
    if db_classroom is None:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return del_classroom(db=db, building=building, room_number=room_number)
