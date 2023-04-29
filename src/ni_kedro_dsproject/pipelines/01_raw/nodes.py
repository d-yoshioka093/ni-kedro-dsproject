from pyspark.sql import DataFrame
from ni_kedro_dsproject.hooks import SparkHooks

def sample_node(train: DataFrame) -> DataFrame:
    """Return dataframe.

    Args:
        train: A Spark DataFrame.

    Returns:
        A sample PySpark DataFrame.
    """
    print(type(train))
    return train
