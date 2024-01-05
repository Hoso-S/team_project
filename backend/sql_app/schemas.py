from pydantic import BaseModel, PositiveFloat, PositiveInt
from typing import  Literal


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
           
class department(BaseModel):
    dept_name: str
    building: str
    budget: PositiveFloat
    class Config:
        from_attributes = True    

class department_update(BaseModel):
    budget: PositiveFloat
    class Config:
        from_attributes = True
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
class instructor(BaseModel):
    ID: str
    name: str
    dept_name: str
    salary: PositiveFloat
    class Config:
        from_attributes = True

class instructor_update(BaseModel):   
    salary: PositiveFloat
    class Config:
        from_attributes = True

class section(BaseModel):
    course_id: str
    sec_id: str
    semester: Literal['Fall', 'Winter', 'Spring', 'Summer']
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


class teaches(BaseModel):
    ID: str
    course_id: str
    sec_id: str
    semester: str
    year: int
    class Config:
        from_attributes = True

class teaches_update(BaseModel):
    semester: str
    year: int
    class Config:
        from_attributes = True


class student(BaseModel):
    ID: str
    name: str
    dept_name: str
    tot_cred: PositiveInt
    class Config:
        from_attributes = True

class student_update(BaseModel):
    tot_cred: PositiveInt
    class Config:
        from_attributes = True

class takes(BaseModel):
    ID: str
    course_id: str
    sec_id: str
    semester: str
    year: int
    grade: str
    class Config:
        from_attributes = True

class takes_update(BaseModel):
    grade: str
    class Config:
        from_attributes = True

class advisor(BaseModel):
    s_ID: str
    i_ID: str
    class Config:
        from_attributes = True

class advisor_update(BaseModel):
    i_ID: str
    class Config:
        from_attributes = True

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
        
class prereq(BaseModel):    
    course_id: str
    prereq_id: str
    class Config:
        from_attributes = True

class prereq_update(BaseModel):
    prereq_id: str
    class Config:
        from_attributes = True
        
class UserBase(BaseModel):
    email: str

class User(UserBase):
    id: int
    is_active: bool
    class Config:
        from_attributes = True