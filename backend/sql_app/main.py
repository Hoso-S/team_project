from fastapi import Depends, FastAPI, Request
from sqlalchemy.orm import Session


from .dependencies import get_db
from .database import Base, engine
from .routers import (
    classrooms,
    courses,
    departments,
    instructors,
    sections,
    students,
    time_slots,
    takes,
)


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Collaborative Development",
    description="AIIT Collaborative Development Project",
    root_path="/api/v1",
    tags=["root"],
)


app.include_router(classrooms.router)
app.include_router(courses.router)
app.include_router(departments.router)
app.include_router(instructors.router)
app.include_router(sections.router)
app.include_router(students.router)
app.include_router(time_slots.router)
app.include_router(takes.router)


@app.get("/app")
async def read_main(request: Request):
    return {
        "message": "Hello CollaborativeDevelopment!!!",
        "root_path": request.scope.get("root_path"),
    }
