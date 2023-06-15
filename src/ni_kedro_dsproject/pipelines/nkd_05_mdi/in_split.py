from pyspark.sql import DataFrame

def in_split(fea_result: DataFrame) -> DataFrame:
    """Return dataframe. Splitting data.

    Args:
        fea_result: A Spark DataFrame. 
       
    Returns:
        A PySpark DataFrame. 
    """
    #訓練データと評価データに分割
    df_train, df_valid = fea_result.randomSplit([0.7,0.3], seed=20)

    return df_train, df_valid
    