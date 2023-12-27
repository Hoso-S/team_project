#!/bin/bash

# FILEPATH: /home/johndoe/team_project/backend/worker-start.sh
# 実行コマンド: bash worker-start.sh

# 仮想環境のフォルダのパス
venv_folder="backend/venv"

# フォルダが存在するかどうかを確認
if [ -d "$venv_folder" ]; then
    # フォルダが存在する場合に実行するコマンド
    echo "Target folder exists. Running the command..."
else
    # フォルダが存在しない場合の処理
    echo "Target folder does not exist."
    echo "Creating python venv and installing requirements"
    sudo apt install python3.11-venv -y
    python3 -m venv venv
    
    # 仮想環境を有効化
    source venv/bin/activate

    # requirements.txtに記載されているパッケージをインストール
    pip install -r requirements.txt
    
    # 仮想環境を無効化
    deactivate
fi

# 仮想環境を有効化
source venv/bin/activate

# uvicornnの起動コマンド
uvicorn sql_app.main:app --reload --host 0.0.0.0 --port 8080

# 仮想環境を無効化
deactivate
