# Hirotan_Solver

面倒なHirotanを自動で解いてくれるアプリケーション

## インストール方法

.envファイルを作成し、LOG_IN_IDに学生番号、PASSWORDにログイン用のパスワードを代入する。

```sh:.env
LOG_IN_ID="BXXXXXX"
PASSWORD="XXXXXXXXXXX"
```

仮想環境を作成し、ライブラリをインストールする

```sh
# 仮想環境の作成
python -m venv .venv

# 仮想環境をActivate
# linux(mac OS)
source .venv/bin/activate
# Windows
.venv\scripts\activate.bat

# ライブラリのインストール
pip install -r requirements.txt
```

復習モードは解けるのを確認しているが、予習モードは確認していない
