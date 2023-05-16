from pyspark.sql import DataFrame
from kedro.config import ConfigLoader
from kedro.framework.project import settings

from pyspark.ml.feature import StringIndexer

def int_node_type(result_int: DataFrame) -> DataFrame:
    """Return dataframe. Define data type.

    Args:
        result_int: A Spark DataFrame. Output from int_node_na.

    Returns:
        A PySpark DataFrame.
    """

    #性別(Sex)と乗船港(Embarked)の型を数値に変換
    SexIndexer = StringIndexer(inputCol='Sex', outputCol='IndexSex')
    SexIndexer = SexIndexer.fit(result_int)

    result_int = SexIndexer.transform(result_int)
    result_int = result_int.drop('Sex')

    EmbarkedIndexer = StringIndexer(inputCol='Embarked', outputCol='IndexEmbarked')
    EmbarkedIndexer = EmbarkedIndexer.fit(result_int)

    result_int = EmbarkedIndexer.transform(result_int)
    result_int = result_int.drop('Embarked')


    return result_int