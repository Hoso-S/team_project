#!/bin/bash

sudo service aiit stop #停止

# 仮想環境のフォルダのパス
venv_folder="venv"

if [ -d "$venv_folder" ]; then
    # フォルダが存在する場合に実行するコマンド
    echo "Target folder exists. Running the command..."
    # 既存の仮想環境を削除
    rm -rf venv

    # 仮想環境を作成
    python3 -m venv venv

    # 仮想環境を有効化
    source venv/bin/activate

    # requirements.txtに記載されているパッケージをインストール
    pip install -r requirements.txt
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

fi

sudo service aiit start #起動
sudo service aiit status #ステータス