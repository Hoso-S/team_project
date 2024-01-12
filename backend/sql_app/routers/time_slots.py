from fastapi import APIRouter
from fastapi import HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..dependencies import get_db
from .. import database


## Create the FastAPI instance
router = APIRouter(prefix="/time_slots", tags=["time_slots"])


## Schema for time_slots
class time_slot(BaseModel):
    time_slot_id: str
    day: str
    start_hr: int
    start_min: int
    end_hr: int
    end_min: int

    class Config:
        from_attributes = True


class time_slot_update(BaseModel):
    day: str
    start_hr: int
    start_min: int
    end_hr: int
    end_min: int

    class Config:
        from_attributes = True


## helper functions
def insert_time_slot(db: Session, time_slot: time_slot):
    db_time_slot = database.time_slot(**time_slot.model_dump())
    db.add(db_time_slot)
    db.commit()
    db.refresh(db_time_slot)
    return db_time_slot


def get_time_slot(db: Session, time_slot_id: str):
    return (
        db.query(database.time_slot)
        .filter(database.time_slot.time_slot_id == time_slot_id)
        .first()
    )


def get_time_slots(db: Session, skip: int = 0, limit: int = 100):
    return db.query(database.time_slot).offset(skip).limit(limit).all()


def del_time_slot(db: Session, time_slot_id: str):
    db.query(database.time_slot).filter(
        database.time_slot.time_slot_id == time_slot_id
    ).delete()
    db.commit()
    return


## Endpoint to Classroom
@router.get("/{time_slot_id}", response_model=time_slot)
async def read_time_slot(time_slot_id: str, db: Session = Depends(get_db)):
    db_time_slot = get_time_slot(db, time_slot_id=time_slot_id)
    if db_time_slot is None:
        raise HTTPException(status_code=404, detail="Time_slot not found")
    return db_time_slot


@router.get("/", response_model=list[time_slot])
async def read_time_slots(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    time_slots = get_time_slots(db, skip=skip, limit=limit)
    return time_slots


@router.post("/", response_model=time_slot)
async def create_time_slot(time_slot: time_slot, db: Session = Depends(get_db)):
    db_time_slot = get_time_slot(db, time_slot_id=time_slot.time_slot_id)
    if db_time_slot:
        raise HTTPException(status_code=400, detail="Time_slot already registered")
    return insert_time_slot(db=db, time_slot=time_slot)


@router.delete("/{time_slot_id}")
async def delete_time_slot(time_slot_id: str, db: Session = Depends(get_db)):
    db_time_slot = get_time_slot(db, time_slot_id=time_slot_id)
    if db_time_slot is None:
        raise HTTPException(status_code=404, detail="Time_slot not found")
    return del_time_slot(db=db, time_slot_id=time_slot_id)
