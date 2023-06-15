from pyspark.sql import DataFrame
from kedro.framework.project import settings
from pyspark.ml.feature import VectorAssembler

def fea_vec(fea_prep: DataFrame, params: dict) -> DataFrame:
    """Return dataframe. Synthesize columns.

    Args:
        fea_prep: A Spark DataFrame. 
        params: Columns to be used for learning.

    Returns:
        A PySpark DataFrame.
    """

    #学習に使用するカラムをまとめる 
    assembler = VectorAssembler(
        inputCols=params["vec_in"],
        outputCol='features'
    )

    fea_prep = assembler.transform(fea_prep)
    
    return fea_prep