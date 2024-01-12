import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


ddl_classroom = """CREATE TABLE IF NOT EXISTS classroom
	(building		varchar(15),
	 room_number	varchar(7),
	 capacity		numeric(4,0),
	 primary key (building, room_number)
	);"""

ddl_department = """CREATE TABLE IF NOT EXISTS department
	(dept_name		varchar(20), 
	 building		varchar(15), 
	 budget		    numeric(12,2) check (budget > 0),
	 primary key (dept_name)
	);"""

ddl_course = """CREATE TABLE IF NOT EXISTS course
	(course_id		varchar(8), 
	 title			varchar(50), 
	 dept_name		varchar(20),
	 credits		numeric(2,0) check (credits > 0),
	 primary key (course_id),
	 foreign key (dept_name) references department (dept_name) on delete set null
	);"""

ddl_instructor = """CREATE TABLE IF NOT EXISTS instructor
	(instructor_id	varchar(5), 
	 name			varchar(20) not null, 
	 dept_name		varchar(20), 
	 salary			numeric(8,2) check (salary > 29000),
	 primary key (instructor_id),
	 foreign key (dept_name) references department (dept_name) on delete set null
	);"""

ddl_section = """CREATE TABLE IF NOT EXISTS section
	(course_id		varchar(8),
	 instructor_id	varchar(5),
	 sec_id			varchar(8),
	 semester		varchar(6) check (semester in ('Fall', 'Winter', 'Spring', 'Summer')), 
	 year			numeric(4,0) check (year > 1701 and year < 2100), 
	 building		varchar(15),
	 room_number	varchar(7),
	 time_slot_id	varchar(4),
	 primary key (course_id, sec_id, semester, year),
	 foreign key (course_id) references course (course_id) on delete cascade,
  	 foreign key (instructor_id) references instructor (instructor_id) on delete set null
	 foreign key (building, room_number) references classroom (building, room_number) on delete set null
	);"""

ddl_student = """CREATE TABLE IF NOT EXISTS student
	(student_id		varchar(5), 
	 name			varchar(20) not null, 
	 dept_name		varchar(20), 
	 tot_cred		numeric(3,0) check (tot_cred >= 0),
	 primary key (student_id),
	 foreign key (dept_name) references department (dept_name) on delete set null
	);"""

ddl_takes = """CREATE TABLE IF NOT EXISTS takes
	(student_id		varchar(5), 
	 course_id		varchar(8),
	 sec_id			varchar(8), 
	 semester		varchar(6),
	 year			numeric(4,0),
	 grade		    varchar(2),
	 primary key (student_id, course_id, sec_id, semester, year),
	 foreign key (course_id, sec_id, semester, year) references section (course_id, sec_id, semester, year) on delete cascade,
	 foreign key (student_id) references student (student_id) on delete cascade
	);"""

ddl_time_slot = """CREATE TABLE IF NOT EXISTS time_slot
	(time_slot_id	varchar(4),
	 day			varchar(1),
	 start_hr		numeric(2) check (start_hr >= 0 and start_hr < 24),
	 start_min		numeric(2) check (start_min >= 0 and start_min < 60),
	 end_hr			numeric(2) check (end_hr >= 0 and end_hr < 24),
	 end_min		numeric(2) check (end_min >= 0 and end_min < 60),
	 primary key (time_slot_id, day, start_hr, start_min)
	);"""
 
ddl_user = """CREATE TABLE IF NOT EXISTS users
	(id					INTEGER PRIMARY KEY AUTOINCREMENT,
	 email				TEXT UNIQUE NOT NULL,
	 hashed_password	TEXT NOT NULL,
	 is_active			BOOLEAN NOT NULL DEFAULT 1,
	 is_superuser		BOOLEAN NOT NULL DEFAULT 0
	);"""


database = r"./dev.db"

# create a database connection
conn = create_connection(database)

# create tables
if conn is not None:
    # create table
    create_table(conn, ddl_classroom)
    create_table(conn, ddl_department)
    create_table(conn, ddl_course)
    create_table(conn, ddl_instructor)
    create_table(conn, ddl_section)
    create_table(conn, ddl_student)
    create_table(conn, ddl_takes)
    create_table(conn, ddl_time_slot)
    create_table(conn, ddl_user)
else:
    print("Error! cannot create the database connection.")

conn.close()
