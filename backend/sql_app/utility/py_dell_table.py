import sqlite3

# データベースに接続
conn = sqlite3.connect('../../dev.db')
cursor = conn.cursor()

# studentテーブルからすべてのデータを削除
cursor.execute('DELETE FROM student')
cursor.execute('DELETE FROM instructor')
cursor.execute('DELETE FROM section')

# 変更を保存
conn.commit()

# データベース接続を閉じる
conn.close()
