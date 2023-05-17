from pyspark.sql import DataFrame
from kedro.config import ConfigLoader
from kedro.framework.project import settings

from pyspark.ml.feature import StringIndexer

def int_node_type(int_result: DataFrame) -> DataFrame:
    """Return dataframe. Define data type.

    Args:
        int_result: A Spark DataFrame. Slightly processed raw data.

    Returns:
        A PySpark DataFrame.  Data with type definition.
    """

    #性別(Sex)と乗船港(Embarked)の型を数値に変換
    SexIndexer = StringIndexer(inputCol='Sex', outputCol='IndexSex')
    SexIndexer = SexIndexer.fit(int_result)

    int_result = SexIndexer.transform(int_result)
    int_result = int_result.drop('Sex')

    EmbarkedIndexer = StringIndexer(inputCol='Embarked', outputCol='IndexEmbarked')
    EmbarkedIndexer = EmbarkedIndexer.fit(int_result)

    int_result = EmbarkedIndexer.transform(int_result)
    int_result = int_result.drop('Embarked')


    return int_result