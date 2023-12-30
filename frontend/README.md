# Git Pull後に実施すること
## モジュールのローカルインストール
* frontend直下(package.jsonが配置されているディレクトリ)で以下のコマンドを実行
  * `npm install`
## ローカル起動の確認
* frontend直下(package.jsonが配置されているディレクトリ)で以下のコマンドを実行
  * `npm run dev`
* ターミナルに表示されたLocal:のアドレスにアクセス
  * 例：http://localhost:5173/
  * ページが表示されたらOK
  * `Ctrl + C` でローカル実行は終了できる
### npm installでやっていること
ざっくり：package.jsonに記載されたモジュールをローカルに持ってきてnode_modulesフォルダに格納しています
# 初期構成メモ
* プロジェクト作成
  * `npm create vite@latest frontend -- --template react`
* MUIパッケージのインストール
  * `npm install @mui/material @emotion/react @emotion/styled`
* 状態管理パッケージ(Recoil)のインストール
  * `npm install recoil`
* ルーティング管理パッケージ(React Router)のインストール
  * `npm install react-router-dom`
