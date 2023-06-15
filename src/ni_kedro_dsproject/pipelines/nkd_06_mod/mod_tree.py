from pyspark.sql import DataFrame
from pyspark.ml.classification  import DecisionTreeClassifier

def mod_tree(df_train: DataFrame,df_valid: DataFrame) -> DataFrame:
    """Return dataframe. Model Learning.

    Args:
        df_train: A Spark DataFrame. 
        df_valid: A Spark DataFrame. 
       
    Returns:
        A PySpark DataFrame. 
    """
    #決定木
    dtc = DecisionTreeClassifier(
        featuresCol = "features" ,
        labelCol = "Survived" 
    )
    model = dtc.fit(df_train)
    prediction_train = model.transform(df_train)
    prediction_valid = model.transform(df_valid)

    return prediction_train, prediction_valid