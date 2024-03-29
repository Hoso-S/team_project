from fastapi import FastAPI, APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from typing import List
from secrets import token_urlsafe
from pydantic import BaseModel, AnyHttpUrl
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi_csrf_protect import CsrfProtect
from fastapi_csrf_protect.exceptions import CsrfProtectError

from .security import oauth2_scheme, CsrfSettings
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
BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:5173"]

# Set all CORS enabled origins
if BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

## Session Middleware
app.add_middleware(SessionMiddleware, secret_key=token_urlsafe(32))

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(classrooms.router, dependencies=[Depends(oauth2_scheme)])
api_router.include_router(courses.router, dependencies=[Depends(oauth2_scheme)])
api_router.include_router(departments.router, dependencies=[Depends(oauth2_scheme)])
api_router.include_router(instructors.router, dependencies=[Depends(oauth2_scheme)])
api_router.include_router(sections.router, dependencies=[Depends(oauth2_scheme)])
api_router.include_router(students.router, dependencies=[Depends(oauth2_scheme)])
api_router.include_router(time_slots.router, dependencies=[Depends(oauth2_scheme)])
api_router.include_router(takes.router, dependencies=[Depends(oauth2_scheme)])
app.include_router(api_router)


## CSRF Protect
class Csrf(BaseModel):
    csrf_token: str


@CsrfProtect.load_config
def get_csrf_config():
    return CsrfSettings()


@app.exception_handler(CsrfProtectError)
def csrf_protect_error_handler(_: Request, exc: CsrfProtectError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.error_message},
    )


@app.middleware("http")
async def some_middleware(request: Request, call_next):
    response = await call_next(request)
    session = request.cookies.get("session")
    if session:
        response.set_cookie(
            key="session", value=request.cookies.get("session"), httponly=True
        )
    return response


## Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Hello CollaborativeDevelopment!!!",
    }


@app.get("/csrftoken", response_model=Csrf)
async def get_csrf_token(csrf_protect: CsrfProtect = Depends()):
    csrf_token, _ = csrf_protect.generate_csrf_tokens()
    return {"csrf_token": csrf_token}


@app.get("/session_set")
async def session_set(request: Request):
    request.session["my_var"] = "1234"
    return "ok"


@app.get("/session_info")
async def session_info(request: Request):
    my_var = request.session.get("my_var", None)
    return my_var
