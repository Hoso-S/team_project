import json
import sqlite3

# JSONファイルからデータを読み込む
with open('sampleData.json', 'r') as file:
    data = json.load(file)

# データベースに接続
conn = sqlite3.connect('../../dev.db')
cursor = conn.cursor()

# 学生データを挿入
for student in data['student']:
    cursor.execute('''
        INSERT INTO student (student_id, name, dept_name, tot_cred)
        VALUES (?, ?, ?, ?)
    ''', (student['student_id'], student['name'], student['dept_name'], student['tot_cred']))

# 教員データを挿入
for instructor in data['instructor']:
    cursor.execute('''
        INSERT INTO instructor (instructor_id, name, dept_name, salary)
        VALUES (?, ?, ?, ?)
    ''', (instructor['instructor_id'], instructor['name'], instructor['dept_name'], instructor['salary']))

# コースデータを挿入
for section in data['section']:
    cursor.execute('''
        INSERT INTO section (course_id, instructor_id, sec_id, semester, year, building, room_number, time_slot_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        section['course_id'], section['instructor_id'], section['sec_id'], section['semester'],
        section['year'], section['building'], section['room_number'],
        section['time_slot_id']
    ))

# セクションデータを挿入
for course in data['course']:
    cursor.execute('''
        INSERT INTO course (course_id, title, dept_name, credits)
        VALUES (?, ?, ?, ?)
    ''', (
        course['course_id'], course['title'], course['dept_name'], course['credits']
    ))

# takesを挿入 (一意性制約エラーを無視)
for takes in data['takes']:
    cursor.execute('''
        INSERT OR IGNORE INTO takes (student_id, course_id, sec_id, semester, year, grade)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        takes['student_id'], takes['course_id'], takes['sec_id'], takes['semester'], takes['year'], takes['grade']
    ))

# 変更を保存
conn.commit()

# データベース接続を閉じる
conn.close()
