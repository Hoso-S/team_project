## 環境

Ubuntu
Python3.11

## 初回実行

### データベース

python3 sql_app/utility/py_create_table.py
　 dev.db が出力される
　 sqlite3 dev.db
　　.schema コマンドでテーブル定義が確認できれば OK

## Sample データの登録

python3 sql_app/utility/py_insert_table.py
　 dev.db に sampleData.json の内容が一括で登録される。
　 sqlite3 dev.db
　　.schema コマンドで確認。

## バックエンド立ち上げ方

- backend で実行
  worker-start.sh を実行する
  　 INFO: Application startup complete.　と表示されていれば OK
  ブラウザで http://0.0.0.0:8080　にアクセスする
