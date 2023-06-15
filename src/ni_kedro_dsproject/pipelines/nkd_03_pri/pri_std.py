from pyspark.sql import DataFrame
# from kedro.config import ConfigLoader
# from kedro.framework.project import settings
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler

def pri_std(int_result: DataFrame, params: dict) -> DataFrame:
    """Return dataframe. Standardize.

    Args:
        int_result: A Spark DataFrame. 
        params: Numeric variables to be standardized.

    Returns:
        A PySpark DataFrame. Standardized data.
    """
    # 外部パラメーターから受け取ったカラムをまとめ、'num_cols'列を作成 
    
    assembler = VectorAssembler(inputCols = params['std_input'],outputCol="num_cols")

    int_result = assembler.transform(int_result)
    #return assembler.transform(int_result)

    # 標準化
    #sc = StandardScaler(inputCol='Pclass', outputCol='Age_scaled')
    sc = StandardScaler(inputCol='num_cols', outputCol='num_cols_scaled')
    sc_model = sc.fit(int_result)
    int_result = sc_model.transform(int_result)
    
    return int_result