from pyspark.sql import DataFrame
from kedro.config import ConfigLoader
from kedro.framework.project import settings

from pyspark.sql import functions as F

def int_node_na(result: DataFrame) -> DataFrame:
    """Return dataframe. Fill in missing data.

    Args:
        result: A Spark DataFrame. Raw data.

    Returns:
        A PySpark DataFrame.
    """

    #String型の欠損値を適当な文字列で置き換える
    result = result.na.fill('nodata')

    #年齢(Age)の欠損値を平均に置き換える
    stats = result.agg(F.avg('Age').alias('Age'))
    age_avg = stats.first()[0]

    result = result.na.fill({'Age': age_avg})


    return result