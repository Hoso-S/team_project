from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/classroom/{building}/{room_number}", response_model=schemas.classroom)
def read_classroom(building: str, room_number: str, db: Session = Depends(get_db)):
    db_classroom = crud.get_classroom(db, building=building, room_number=room_number)
    if db_classroom is None:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return db_classroom

@app.get("/api/classrooms/", response_model=list[schemas.classroom])
def read_classrooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    classrooms = crud.get_classrooms(db, skip=skip, limit=limit)
    return classrooms

@app.post("/api/classroom/", response_model=schemas.classroom)
def create_classroom(classroom: schemas.classroom, db: Session = Depends(get_db)):
    db_classroom = crud.get_classroom(db, building=classroom.building, room_number=classroom.room_number)
    if db_classroom:
        raise HTTPException(status_code=400, detail="Classroom already registered")
    return crud.create_classroom(db=db, classroom=classroom)

@app.delete("/api/classroom/{building}/{room_number}")
def delete_classroom(building: str, room_number: str, db: Session = Depends(get_db)):
    db_classroom = crud.get_classroom(db, building=building, room_number=room_number)
    if db_classroom is None:
        raise HTTPException(status_code=404, detail="Classroom not found")
    return crud.delete_classroom(db=db, building=building, room_number=room_number)

@app.get("/api/department/{dept_name}", response_model=schemas.department)
def read_department(dept_name: str, db: Session = Depends(get_db)):
    db_department = crud.get_department(db, dept_name=dept_name)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return db_department

@app.get("/api/departments/", response_model=list[schemas.department])
def read_departments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    departments = crud.get_departments(db, skip=skip, limit=limit)
    return departments

@app.post("/api/department/", response_model=schemas.department)
def create_department(department: schemas.department, db: Session = Depends(get_db)):
    db_department = crud.get_department(db, dept_name=department.dept_name)
    if db_department:
        raise HTTPException(status_code=400, detail="Department already registered")
    return crud.create_department(db=db, department=department)

@app.delete("/api/department/{dept_name}")
def delete_department(dept_name: str, db: Session = Depends(get_db)):
    db_department = crud.get_department(db, dept_name=dept_name)
    if db_department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return crud.delete_department(db=db, dept_name=dept_name)

@app.get("/api/course/{course_id}", response_model=schemas.course)
def read_course(course_id: str, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.get("/api/courses/", response_model=list[schemas.course])
def read_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    courses = crud.get_courses(db, skip=skip, limit=limit)
    return courses

@app.post("/api/course/", response_model=schemas.course)
def create_course(course: schemas.course, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course.course_id)
    if db_course:
        raise HTTPException(status_code=400, detail="Course already registered")
    return crud.create_course(db=db, course=course)

@app.delete("/api/course/{course_id}")
def delete_course(course_id: str, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return crud.delete_course(db=db, course_id=course_id)

@app.get("/api/instructor/{ID}", response_model=schemas.instructor)
def read_instructor(ID: str, db: Session = Depends(get_db)):
    db_instructor = crud.get_instructor(db, ID=ID)
    if db_instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return db_instructor

@app.get("/api/instructors/", response_model=list[schemas.instructor])
def read_instructors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    instructors = crud.get_instructors(db, skip=skip, limit=limit)
    return instructors

@app.post("/api/instructor/", response_model=schemas.instructor)
def create_instructor(instructor: schemas.instructor, db: Session = Depends(get_db)):
    db_instructor = crud.get_instructor(db, ID=instructor.ID)
    if db_instructor:
        raise HTTPException(status_code=400, detail="Instructor already registered")
    return crud.create_instructor(db=db, instructor=instructor)

@app.delete("/api/instructor/{ID}")
def delete_instructor(ID: str, db: Session = Depends(get_db)):
    db_instructor = crud.get_instructor(db, ID=ID)
    if db_instructor is None:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return crud.delete_instructor(db=db, ID=ID)

@app.get("/api/section/{course_id}/{sec_id}/{semester}/{year}", response_model=schemas.section)
def read_section(course_id: str, sec_id: str, semester: str, year: int, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, course_id=course_id, sec_id=sec_id, semester=semester, year=year)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return db_section

@app.get("/api/sections/", response_model=list[schemas.section])
def read_sections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sections = crud.get_sections(db, skip=skip, limit=limit)
    return sections

@app.post("/api/section/", response_model=schemas.section)
def create_section(section: schemas.section, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, course_id=section.course_id, sec_id=section.sec_id, semester=section.semester, year=section.year)
    if db_section:
        raise HTTPException(status_code=400, detail="Section already registered")
    return crud.create_section(db=db, section=section)

@app.delete("/api/section/{course_id}/{sec_id}/{semester}/{year}")
def delete_section(course_id: str, sec_id: str, semester: str, year: int, db: Session = Depends(get_db)):
    db_section = crud.get_section(db, course_id=course_id, sec_id=sec_id, semester=semester, year=year)
    if db_section is None:
        raise HTTPException(status_code=404, detail="Section not found")
    return crud.delete_section(db=db, course_id=course_id, sec_id=sec_id, semester=semester, year=year)

@app.get("/api/teaches/{ID}/{course_id}/{sec_id}/{semester}/{year}", response_model=schemas.teaches)
def read_teaches(ID: str, course_id: str, sec_id: str, semester: str, year: int, db: Session = Depends(get_db)):
    db_teaches = crud.get_teaches(db, ID=ID, course_id=course_id, sec_id=sec_id, semester=semester, year=year)
    if db_teaches is None:
        raise HTTPException(status_code=404, detail="Teaches not found")
    return db_teaches

@app.get("/api/teaches/", response_model=list[schemas.teaches])
def read_teaches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teaches = crud.get_teaches(db, skip=skip, limit=limit)
    return teaches

@app.post("/api/teaches/", response_model=schemas.teaches)
def create_teaches(teaches: schemas.teaches, db: Session = Depends(get_db)):
    db_teaches = crud.get_teaches(db, ID=teaches.ID, course_id=teaches.course_id, sec_id=teaches.sec_id, semester=teaches.semester, year=teaches.year)
    if db_teaches:
        raise HTTPException(status_code=400, detail="Teaches already registered")
    return crud.create_teaches(db=db, teaches=teaches)

@app.delete("/api/teaches/{ID}/{course_id}/{sec_id}/{semester}/{year}")
def delete_teaches(ID: str, course_id: str, sec_id: str, semester: str, year: int, db: Session = Depends(get_db)):
    db_teaches = crud.get_teaches(db, ID=ID, course_id=course_id, sec_id=sec_id, semester=semester, year=year)
    if db_teaches is None:
        raise HTTPException(status_code=404, detail="Teaches not found")
    return crud.delete_teaches(db=db, ID=ID, course_id=course_id, sec_id=sec_id, semester=semester, year=year)

@app.get("/api/student/{ID}", response_model=schemas.student)
def read_student(ID: str, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, ID=ID)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.get("/api/students/", response_model=list[schemas.student])
def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students

@app.post("/api/student/", response_model=schemas.student)
def create_student(student: schemas.student, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, ID=student.ID)
    if db_student:
        raise HTTPException(status_code=400, detail="Student already registered")
    return crud.create_student(db=db, student=student)

@app.delete("/api/student/{ID}")
def delete_student(ID: str, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, ID=ID)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return crud.delete_student(db=db, ID=ID)

@app.get("/api/takes/{ID}/{course_id}/{sec_id}/{semester}/{year}", response_model=schemas.takes)
def read_takes(ID: str, course_id: str, sec_id: str, semester: str, year: int, db: Session = Depends(get_db)):
    db_takes = crud.get_takes(db, ID=ID, course_id=course_id, sec_id=sec_id, semester=semester, year=year)
    if db_takes is None:
        raise HTTPException(status_code=404, detail="Takes not found")
    return db_takes

@app.get("/api/takes/", response_model=list[schemas.takes])
def read_takes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    takes = crud.get_takes(db, skip=skip, limit=limit)
    return takes

@app.post("/api/takes/", response_model=schemas.takes)
def create_takes(takes: schemas.takes, db: Session = Depends(get_db)):
    db_takes = crud.get_takes(db, ID=takes.ID, course_id=takes.course_id, sec_id=takes.sec_id, semester=takes.semester, year=takes.year)
    if db_takes:
        raise HTTPException(status_code=400, detail="Takes already registered")
    return crud.create_takes(db=db, takes=takes)

@app.delete("/api/takes/{ID}/{course_id}/{sec_id}/{semester}/{year}")
def delete_takes(ID: str, course_id: str, sec_id: str, semester: str, year: int, db: Session = Depends(get_db)):
    db_takes = crud.get_takes(db, ID=ID, course_id=course_id, sec_id=sec_id, semester=semester, year=year)
    if db_takes is None:
        raise HTTPException(status_code=404, detail="Takes not found")
    return crud.delete_takes(db=db, ID=ID, course_id=course_id, sec_id=sec_id, semester=semester, year=year)

@app.get("/api/advisor/{s_ID}/{i_ID}", response_model=schemas.advisor)
def read_advisor(s_ID: str, i_ID: str, db: Session = Depends(get_db)):
    db_advisor = crud.get_advisor(db, s_ID=s_ID, i_ID=i_ID)
    if db_advisor is None:
        raise HTTPException(status_code=404, detail="Advisor not found")
    return db_advisor

@app.get("/api/advisors/", response_model=list[schemas.advisor])
def read_advisors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    advisors = crud.get_advisors(db, skip=skip, limit=limit)
    return advisors

@app.post("/api/advisor/", response_model=schemas.advisor)
def create_advisor(advisor: schemas.advisor, db: Session = Depends(get_db)):
    db_advisor = crud.get_advisor(db, s_ID=advisor.s_ID, i_ID=advisor.i_ID)
    if db_advisor:
        raise HTTPException(status_code=400, detail="Advisor already registered")
    return crud.create_advisor(db=db, advisor=advisor)

@app.delete("/api/advisor/{s_ID}/{i_ID}")
def delete_advisor(s_ID: str, i_ID: str, db: Session = Depends(get_db)):
    db_advisor = crud.get_advisor(db, s_ID=s_ID, i_ID=i_ID)
    if db_advisor is None:
        raise HTTPException(status_code=404, detail="Advisor not found")
    return crud.delete_advisor(db=db, s_ID=s_ID, i_ID=i_ID)

@app.get("/api/time_slot/{time_slot_id}", response_model=schemas.time_slot)
def read_time_slot(time_slot_id: str, db: Session = Depends(get_db)):
    db_time_slot = crud.get_time_slot(db, time_slot_id=time_slot_id)
    if db_time_slot is None:
        raise HTTPException(status_code=404, detail="Time_slot not found")
    return db_time_slot

@app.get("/api/time_slots/", response_model=list[schemas.time_slot])
def read_time_slots(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    time_slots = crud.get_time_slots(db, skip=skip, limit=limit)
    return time_slots

@app.post("/api/time_slot/", response_model=schemas.time_slot)
def create_time_slot(time_slot: schemas.time_slot, db: Session = Depends(get_db)):
    db_time_slot = crud.get_time_slot(db, time_slot_id=time_slot.time_slot_id)
    if db_time_slot:
        raise HTTPException(status_code=400, detail="Time_slot already registered")
    return crud.create_time_slot(db=db, time_slot=time_slot)

@app.delete("/api/time_slot/{time_slot_id}")
def delete_time_slot(time_slot_id: str, db: Session = Depends(get_db)):
    db_time_slot = crud.get_time_slot(db, time_slot_id=time_slot_id)
    if db_time_slot is None:
        raise HTTPException(status_code=404, detail="Time_slot not found")
    return crud.delete_time_slot(db=db, time_slot_id=time_slot_id)

@app.get("/api/prereq/{course_id}/{prereq_id}", response_model=schemas.prereq)
def read_prereq(course_id: str, prereq_id: str, db: Session = Depends(get_db)):
    db_prereq = crud.get_prereq(db, course_id=course_id, prereq_id=prereq_id)
    if db_prereq is None:
        raise HTTPException(status_code=404, detail="Prereq not found")
    return db_prereq

@app.get("/api/prereqs/", response_model=list[schemas.prereq])
def read_prereqs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prereqs = crud.get_prereqs(db, skip=skip, limit=limit)
    return prereqs

@app.post("/api/prereq/", response_model=schemas.prereq)
def create_prereq(prereq: schemas.prereq, db: Session = Depends(get_db)):
    db_prereq = crud.get_prereq(db, course_id=prereq.course_id, prereq_id=prereq.prereq_id)
    if db_prereq:
        raise HTTPException(status_code=400, detail="Prereq already registered")
    return crud.create_prereq(db=db, prereq=prereq)

@app.delete("/api/prereq/{course_id}/{prereq_id}")
def delete_prereq(course_id: str, prereq_id: str, db: Session = Depends(get_db)):
    db_prereq = crud.get_prereq(db, course_id=course_id, prereq_id=prereq_id)
    if db_prereq is None:
        raise HTTPException(status_code=404, detail="Prereq not found")
    return crud.delete_prereq(db=db, course_id=course_id, prereq_id=prereq_id)


# @app.post("/api/users/", response_model=schemas.User)
# def create_user(user: schemas.User, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/api/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/api/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

