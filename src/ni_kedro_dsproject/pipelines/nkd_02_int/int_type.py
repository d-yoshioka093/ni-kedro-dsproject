from pyspark.sql import DataFrame
#from kedro.config import ConfigLoader
#from kedro.framework.project import settings

from pyspark.ml.feature import StringIndexer

def int_type(int_prep: DataFrame, params: dict) -> DataFrame:
    """Return dataframe. Define data type.

    Args:
        int_prep: A Spark DataFrame. A little processed raw data.

    Returns:
        A PySpark DataFrame.  Data with type definition.
    """

    #性別(Sex)と乗船港(Embarked)の型を数値に変換
    for k, v in params["type_var"].items():

        Indexer = StringIndexer(inputCol=k, outputCol=v)
        Indexer = Indexer.fit(int_prep)

        int_prep = Indexer.transform(int_prep)
        int_prep = int_prep.drop(k)


    return int_prep