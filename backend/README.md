## 環境
Ubuntu
Python3.11

## 初回実行
### データベース
python3  sql_app/utility/py_create_table.py
　dev.dbが出力される
　sqlite3 dev.db
　　.schema コマンドでテーブル定義が確認できればOK
## バックエンド立ち上げ方
- backendで実行
 worker-start.shを実行する
 　INFO:     Application startup complete.　と表示されていればOK
 ブラウザで http://0.0.0.0:8080　にアクセスする