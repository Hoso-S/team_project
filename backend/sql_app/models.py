from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from .database import Base, engine


class classroom(Base):
    __tablename__ = "classroom"
    __table__ = Table("classroom", Base.metadata, autoload_with=engine)

class department(Base):
    __tablename__ = "department"
    __table__ = Table("department", Base.metadata, autoload_with=engine)
        
class course(Base):
    __tablename__ = "course"
    __table__ = Table("course", Base.metadata, autoload_with=engine)

class instructor(Base):
    __tablename__ = "instructor"
    __table__ = Table("instructor", Base.metadata, autoload_with=engine)

class section(Base):
    __tablename__ = "section"
    __table__ = Table("section", Base.metadata, autoload_with=engine)


class teaches(Base):
    __tablename__ = "teaches"
    __table__ = Table("teaches", Base.metadata, autoload_with=engine)

class student(Base):
    __tablename__ = "student"
    __table__ = Table("student", Base.metadata, autoload_with=engine)

class takes(Base):
    __tablename__ = "takes"
    __table__ = Table("takes", Base.metadata, autoload_with=engine)
    
class advisor(Base):
    __tablename__ = "advisor"
    __table__ = Table("advisor", Base.metadata, autoload_with=engine)

class time_slot(Base):
    __tablename__ = "time_slot"
    __table__ = Table("time_slot", Base.metadata, autoload_with=engine)

class prereq(Base):
    __tablename__ = "prereq"
    __table__ = Table("prereq", Base.metadata, autoload_with=engine)