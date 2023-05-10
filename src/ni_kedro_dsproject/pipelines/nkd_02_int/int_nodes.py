from pyspark.sql import DataFrame
from kedro.config import ConfigLoader
from kedro.framework.project import settings

def sample_node2(train: DataFrame, params: dict) -> DataFrame:
    """Return dataframe.

    Args:
        train: A Spark DataFrame.

    Returns:
        A sample PySpark DataFrame.
    """

    print(params)
    print(type(train))
    
    return train