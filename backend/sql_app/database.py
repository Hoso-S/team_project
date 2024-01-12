from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table

SQLALCHEMY_DATABASE_URL = "sqlite:///./dev.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.bind = engine


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


class student(Base):
    __tablename__ = "student"
    __table__ = Table("student", Base.metadata, autoload_with=engine)


class takes(Base):
    __tablename__ = "takes"
    __table__ = Table("takes", Base.metadata, autoload_with=engine)


class time_slot(Base):
    __tablename__ = "time_slot"
    __table__ = Table("time_slot", Base.metadata, autoload_with=engine)


class users(Base):
    __tablename__ = "users"
    __table__ = Table("users", Base.metadata, autoload_with=engine)