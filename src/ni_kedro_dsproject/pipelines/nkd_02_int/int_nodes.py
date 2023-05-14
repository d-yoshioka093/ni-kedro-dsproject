from pyspark.sql import DataFrame
from kedro.config import ConfigLoader
from kedro.framework.project import settings

from pyspark.sql import functions as F
from pyspark.ml.feature import StringIndexer

def int_sample_node2(train: DataFrame) -> DataFrame:
    """Return dataframe.データ型を定義した

    Args:
        train: A Spark DataFrame.rawであること

    Returns:
        A PySpark DataFrame.
    """

    #String型の欠損値を適当な文字列で置き換える
    result = result.na.fill('nodata')

    #性別(Sex)と乗船港(Embarked)の型を数値に変換
    SexIndexer = StringIndexer(inputCol='Sex', outputCol='IndexSex')
    SexIndexer = SexIndexer.fit(result)

    result = SexIndexer.transform(result)
    result = result.drop('Sex')

    EmbarkedIndexer = StringIndexer(inputCol='Embarked', outputCol='IndexEmbarked')
    EmbarkedIndexer = EmbarkedIndexer.fit(result)
    result = EmbarkedIndexer.transform(result)
    result = result.drop('Embarked')

    #年齢(Age)の欠損値を平均に置き換える
    stats = result.agg(F.avg('Age').alias('Age'))
    age_avg = stats.first()[0]
    result = result.na.fill({'Age': age_avg})

    #print(params)
    #print(type(train))
    
    return result