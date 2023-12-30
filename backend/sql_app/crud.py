from sqlalchemy.orm import Session

from . import models, schemas

## CRUD for classroom
def create_classroom(db: Session, classroom: schemas.classroom):
    db_classroom = models.classroom(**classroom.dict())
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom

def get_classroom(db: Session, building: str, room_number: str):
    return db.query(models.classroom).filter(models.classroom.building == building).filter(models.classroom.room_number == room_number).first()

def get_classrooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.classroom).offset(skip).limit(limit).all()

def delete_classroom(db: Session, building: str, room_number: str):
    db.query(models.classroom).filter(models.classroom.building == building).filter(models.classroom.room_number == room_number).delete()
    db.commit()
    return

## CRUD for department
def create_department(db: Session, department: schemas.department):
    db_department = models.department(**department.dict())
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department

def get_department(db: Session, dept_name: str):    
    return db.query(models.department).filter(models.department.dept_name == dept_name).first()

def get_departments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.department).offset(skip).limit(limit).all()

def delete_department(db: Session, dept_name: str):
    db.query(models.department).filter(models.department.dept_name == dept_name).delete()
    db.commit()
    return

## CRUD for course
def create_course(db: Session, course: schemas.course):
    db_course = models.course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: str):
    return db.query(models.course).filter(models.course.course_id == course_id).first()

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.course).offset(skip).limit(limit).all()

def delete_course(db: Session, course_id: str):
    db.query(models.course).filter(models.course.course_id == course_id).delete()
    db.commit()
    return

## CRUD for instructor
def create_instructor(db: Session, instructor: schemas.instructor):
    db_instructor = models.instructor(**instructor.dict())
    db.add(db_instructor)
    db.commit()
    db.refresh(db_instructor)
    return db_instructor

def get_instructor(db: Session, ID: str):
    return db.query(models.instructor).filter(models.instructor.ID == ID).first()

def get_instructors(db: Session, skip: int = 0, limit: int = 100):  
    return db.query(models.instructor).offset(skip).limit(limit).all()

def delete_instructor(db: Session, ID: str):
    db.query(models.instructor).filter(models.instructor.ID == ID).delete()
    db.commit()
    return  

## CRUD for section
def create_section(db: Session, section: schemas.section):
    db_section = models.section(**section.dict())
    db.add(db_section)
    db.commit()
    db.refresh(db_section)
    return db_section

def get_section(db: Session, course_id: str, sec_id: str, semester: str, year: int):
    return db.query(models.section).filter(models.section.course_id == course_id).filter(models.section.sec_id == sec_id).filter(models.section.semester == semester).filter(models.section.year == year).first()

def get_sections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.section).offset(skip).limit(limit).all()

def delete_section(db: Session, course_id: str, sec_id: str, semester: str, year: int):
    db.query(models.section).filter(models.section.course_id == course_id).filter(models.section.sec_id == sec_id).filter(models.section.semester == semester).filter(models.section.year == year).delete()
    db.commit()
    return

## CRUD for teaches
def create_teaches(db: Session, teaches: schemas.teaches):
    db_teaches = models.teaches(**teaches.dict())
    db.add(db_teaches)
    db.commit()
    db.refresh(db_teaches)
    return db_teaches

def get_teaches(db: Session, ID: str, course_id: str, sec_id: str, semester: str, year: int):
    return db.query(models.teaches).filter(models.teaches.ID == ID).filter(models.teaches.course_id == course_id).filter(models.teaches.sec_id == sec_id).filter(models.teaches.semester == semester).filter(models.teaches.year == year).first()

def get_all_teaches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.teaches).offset(skip).limit(limit).all()

def delete_teaches(db: Session, ID: str, course_id: str, sec_id: str, semester: str, year: int):
    db.query(models.teaches).filter(models.teaches.ID == ID).filter(models.teaches.course_id == course_id).filter(models.teaches.sec_id == sec_id).filter(models.teaches.semester == semester).filter(models.teaches.year == year).delete()
    db.commit()
    return

## CRUD for student
def create_student(db: Session, student: schemas.student):
    db_student = models.student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, ID: str):
    return db.query(models.student).filter(models.student.ID == ID).first()

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.student).offset(skip).limit(limit).all()

def delete_student(db: Session, ID: str):
    db.query(models.student).filter(models.student.ID == ID).delete()
    db.commit()
    return

## CRUD for takes
def create_takes(db: Session, takes: schemas.takes):
    db_takes = models.takes(**takes.dict())
    db.add(db_takes)
    db.commit()
    db.refresh(db_takes)
    return db_takes

def get_takes(db: Session, ID: str, course_id: str, sec_id: str, semester: str, year: int):
    return db.query(models.takes).filter(models.takes.ID == ID).filter(models.takes.course_id == course_id).filter(models.takes.sec_id == sec_id).filter(models.takes.semester == semester).filter(models.takes.year == year).first()

def get_all_takes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.takes).offset(skip).limit(limit).all()

def delete_takes(db: Session, ID: str, course_id: str, sec_id: str, semester: str, year: int):
    db.query(models.takes).filter(models.takes.ID == ID).filter(models.takes.course_id == course_id).filter(models.takes.sec_id == sec_id).filter(models.takes.semester == semester).filter(models.takes.year == year).delete()
    db.commit()
    return

## CRUD for advisor
def create_advisor(db: Session, advisor: schemas.advisor):
    db_advisor = models.advisor(**advisor.dict())
    db.add(db_advisor)
    db.commit()
    db.refresh(db_advisor)
    return db_advisor

def get_advisor(db: Session, s_ID: str):
    return db.query(models.advisor).filter(models.advisor.s_ID == s_ID).first()

def get_advisors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.advisor).offset(skip).limit(limit).all()

def delete_advisor(db: Session, s_ID: str):
    db.query(models.advisor).filter(models.advisor.s_ID == s_ID).delete()
    db.commit()
    return

## CRUD for time_slot
def create_time_slot(db: Session, time_slot: schemas.time_slot):
    db_time_slot = models.time_slot(**time_slot.dict())
    db.add(db_time_slot)
    db.commit()
    db.refresh(db_time_slot)
    return db_time_slot

def get_time_slot(db: Session, time_slot_id: str):
    return db.query(models.time_slot).filter(models.time_slot.time_slot_id == time_slot_id).first()

def get_time_slots(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.time_slot).offset(skip).limit(limit).all()

def delete_time_slot(db: Session, time_slot_id: str):
    db.query(models.time_slot).filter(models.time_slot.time_slot_id == time_slot_id).delete()
    db.commit()
    return

## CRUD for prereq
def create_prereq(db: Session, prereq: schemas.prereq):
    db_prereq = models.prereq(**prereq.dict())
    db.add(db_prereq)
    db.commit()
    db.refresh(db_prereq)
    return db_prereq

def get_prereq(db: Session, course_id: str, prereq_id: str):
    return db.query(models.prereq).filter(models.prereq.course_id == course_id).filter(models.prereq.prereq_id == prereq_id).first()

def get_prereqs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.prereq).offset(skip).limit(limit).all()

def delete_prereq(db: Session, course_id: str, prereq_id: str):
    db.query(models.prereq).filter(models.prereq.course_id == course_id).filter(models.prereq.prereq_id == prereq_id).delete()
    db.commit()
    return
