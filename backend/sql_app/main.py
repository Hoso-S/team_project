from fastapi import FastAPI, APIRouter, Depends
from typing import List
from pydantic import AnyHttpUrl
from starlette.middleware.cors import CORSMiddleware

from .security import oauth2_scheme
# from .dependencies import get_db
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
    description="AIIT Collaborative Development Project",
)

# BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
# e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
# "http://localhost:8080"
BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost"]

# Set all CORS enabled origins
if BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
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
async def root(token: str = Depends(oauth2_scheme)):
    return {
        "message": "Hello CollaborativeDevelopment!!!",
    }
