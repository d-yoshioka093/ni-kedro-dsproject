# NI_Kedro_DSProject

## Overview

これは、`Kedro 0.18.7`を使用して生成された、新しいKedroプロジェクトです。
プロジェクトのアーキテクチャーとして、pysparkを使用してtitanicの予測タスクを実行します。

詳細情報、基本的なアーキテクチャーの情報については、[Kedroドキュメント](https://kedro.readthedocs.io)を参照してください。


## Rules and guidelines

テンプレートの効果を最大限に引き出すには：

* `.gitignore` ファイルから定義を削除しない
* [data engineering convention](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)に従い、結果が再現できることを確認
* データをリポジトリにコミットしない
* 認証情報やローカル設定をリポジトリにコミットせず、すべての認証情報とローカル設定を `conf/local/` に保存
* リポジトリの内容を変更する場合はその作業のためのブランチを作成し、変更後に `pull request` を行い、レビューが完了した後にそのブランチをマージすること
(詳細は[GitHub Flow 図解](https://qiita.com/tbpgr/items/4ff76ef35c4ff0ec8314)を確認してください)

## How to install dependencies

仮想環境を作成し、当プロジェクト専用のpython実行環境を追加してください。

```
conda create --name kedro-environment python=3.10
```

必要なライブラリ群をインストールする際には、`./setup.sh`によって、requirements.txtで定義したライブラリ、pre-commitのインストールを実施し、
依存関係を宣言してください。
インストール:
```
./setup.sh
```

ローカル環境で`spark`を実行するため、`spark`と`hadoop`の実行環境をローカルPCに構築する必要があります。構築のイメージは所定のWebページより、それぞれに必要な実行ファイル群をローカルPCに配置し、環境変数を追加してそれらの実行ファイルがWindows上で認識される必要があります。
詳細については、[winutilsのREADME.md](https://github.com/kitfactory/winutils)を参照してください。2.2のVisualC++インストールは不要です。

ライブラリのバージョン:
　spark-3.4.0　hadoop-3.3.5

## How to run your Kedro pipeline

kedroプロジェクト実行:

```
kedro run
```

kedro run 実行時のログ情報については以下を参考にして設定値を定めてください。
conf\base\logging.ymlのlog level
- シンプルな出力に変更したい場合、`conf\base\logging.yml`の`#log level変更`部分を`INFO`に変更してください。
- 詳細なエラー情報を出力したい場合、`conf\base\logging.yml`の`#log level変更`部分を`DEBUG`に変更してください。

## How to test your Kedro project

テスト実行:  

※テストの書き方については、`src/tests/test_run.py` ファイルを参照

```
kedro test
```

coverage thresholdを設定するには、`.coveragerc` ファイルにアクセスします。

## コーディングルール

### 命名規則  
・スネークケース（小文字のみで、単語間をアンダースコアで区切ります。）  
・使用目的を考慮し、わかりやすい名前を付けます。  
・レイヤーごとにプレフィックスを付けます。（例）int_ (その他の例は、[globals.yml](https://github.com/d-yoshioka093/ni-kedro-dsproject/blob/main/conf/base/globals.yml)ファイルを参照してください。)

``` 
ファイルを削除する関数
def int_deleate_file(~):
```
  
### インデント  
・インデントは半角スペース4つです。    
・インデントがない（=トップレベル）ところに書くクラスや関数に関しては2行分の空行を入れます。  
・インデントが1つ入っている領域に追加する関数などは1行ずつ空行を加えます。  

### import  
・基本的にimportは行を分けて書きます。  
・同一モジュール内での複数のimportは1行にまとめます。   
``` 
import numpy as np  
import pandas as pd  
from datetime import datetime, date  
```

### docstring、コメント　　
・docstringはダブルクォーテーション3つで囲みます。    
・わかりやすさのために機能単位にコメントを入れます。   
・docstringは英語、コメントは日本語とします。  

### コーディングスタイル  
・関数呼び出しなどで、長い場合に途中で改行を入れる際には、括弧の開始部分と要素が合うようにします。  
・文字列の引用符はダブルクォーテーションを使います。  
・1行につき、複数の処理を書くのは避けます。  
``` 
dict(
    train_x="example_train_x",
    train_y="example_train_y",       
),
``` 