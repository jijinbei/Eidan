# 英断

英断:Eidan

〇iro〇anを自動で解くスクリプト

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
.venv\scripts\activate

# ライブラリのインストール
pip install -r requirements.txt
```

## デモ動画

![demo2](https://github.com/jijinbei/Hirotan_Solver/assets/87472238/3fc67a93-a0a3-4955-a499-5bca828ed344)
