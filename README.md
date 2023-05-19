# NI_Kedro_DSProject

## Overview

This kedro project for internal study, which was generated using `Kedro 0.18.7`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## Environments

```
conda create --name kedro-environment python=3.10 -y
pip install kedro
```
環境構築は上記コマンドを実行し、python仮想環境とkedroをインストール

```
kedro new --starter=pyspark
git init
```
kedro starterを利用して、プロジェクト構成をインストールする方法（git clone時は不要）

## コーディングルール

### 命名規則  
・スネークケース（小文字のみで、単語間をアンダースコアで区切ります。）  
・使用目的を考慮し、わかりやすい名前を付けます。  
``` 
delete_file 
user_id 
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

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `src/requirements.txt` for `pip` installation and `src/environment.yml` for `conda` installation.

To install them, run:

```
pip install -r src/requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

## Project dependencies

To generate or update the dependency requirements for your project:

```
kedro build-reqs
```

This will `pip-compile` the contents of `src/requirements.txt` into a new file `src/requirements.lock`. You can see the output of the resolution by opening `src/requirements.lock`.

After this, if you'd like to update your project requirements, please update `src/requirements.txt` and re-run `kedro build-reqs`.

[Further information about project dependencies](https://kedro.readthedocs.io/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `catalog`, `context`, `pipelines` and `session`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r src/requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to convert notebook cells to nodes in a Kedro project
You can move notebook code over into a Kedro project structure using a mixture of [cell tagging](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#cell-tags) and Kedro CLI commands.

By adding the `node` tag to a cell and running the command below, the cell's source code will be copied over to a Python file within `src/<package_name>/nodes/`:

```
kedro jupyter convert <filepath_to_my_notebook>
```
> *Note:* The name of the Python file matches the name of the original notebook.

Alternatively, you may want to transform all your notebooks in one go. Run the following command to convert all notebook files found in the project root directory and under any of its sub-folders:

```
kedro jupyter convert --all
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html)
