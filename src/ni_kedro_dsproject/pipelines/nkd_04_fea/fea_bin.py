from pyspark.sql import DataFrame
from kedro.framework.project import settings
from pyspark.ml.feature import QuantileDiscretizer

def fea_bin(pri_result: DataFrame, params: dict) -> DataFrame:
    """Return dataframe.  Discretization.

    Args:
        pri_result: A Spark DataFrame. 
        params: Variable to be discretized.

    Returns:
        A PySpark DataFrame. Discretized data.
    """

    #運賃をビニング処理
    qds = QuantileDiscretizer(
            numBuckets=10, 
            inputCol=params["bin_var"], 
            outputCol='quantile'
        )
    pri_result=qds.fit(pri_result).transform(pri_result)

    return pri_result