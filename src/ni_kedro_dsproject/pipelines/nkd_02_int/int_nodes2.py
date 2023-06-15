from pyspark.sql import DataFrame
from kedro.config import ConfigLoader
from kedro.framework.project import settings

from pyspark.ml.feature import StringIndexer

def int_node_type(mid_result: DataFrame) -> DataFrame:
    """Return dataframe. Define data type.

    Args:
        mid_result: A Spark DataFrame. A little processed raw data.

    Returns:
        A PySpark DataFrame.  Data with type definition.
    """

    #性別(Sex)と乗船港(Embarked)の型を数値に変換
    SexIndexer = StringIndexer(inputCol='Sex', outputCol='IndexSex')
    SexIndexer = SexIndexer.fit(mid_result)

    mid_result = SexIndexer.transform(mid_result)
    mid_result = mid_result.drop('Sex')

    EmbarkedIndexer = StringIndexer(inputCol='Embarked', outputCol='IndexEmbarked')
    EmbarkedIndexer = EmbarkedIndexer.fit(mid_result)

    mid_result = EmbarkedIndexer.transform(mid_result)
    mid_result = mid_result.drop('Embarked')


    return mid_result