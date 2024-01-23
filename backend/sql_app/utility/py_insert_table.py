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

# コースセクションデータを挿入
for section in data['course']:
    cursor.execute('''
        INSERT INTO section (course_id, instructor_id, sec_id, semester, year, building, room_number, time_slot_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        section['course_id'], section['instructor_id'], section['sec_id'], section['semester'],
        section['year'], section['building'], section['room_number'],
        section['time_slot_id']
    ))

# 変更を保存
conn.commit()

# データベース接続を閉じる
conn.close()
