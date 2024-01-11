from fastapi import FastAPI, APIRouter

from .dependencies import get_db
from .database import Base, engine
from .routers import (
    users,
    login,
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
    description="AIIT Collaborative Development Project"
)


api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(classrooms.router)
api_router.include_router(courses.router)
api_router.include_router(departments.router)
api_router.include_router(instructors.router)
api_router.include_router(sections.router)
api_router.include_router(students.router)
api_router.include_router(time_slots.router)
api_router.include_router(takes.router)
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {
        "message": "Hello CollaborativeDevelopment!!!",
    }
