from pyspark.sql import DataFrame
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from ni_kedro_dsproject.pipelines.util.logger import logging_node

def mod_auc(prediction_train: DataFrame,prediction_valid: DataFrame) :
    """Return dataframe. Model Learning.

    Args:
        prediction_train: A Spark DataFrame. 
        prediction_valid: A Spark DataFrame. 
       
    Returns:
        A PySpark DataFrame. 
    """
    # モデル評価（AUC）
    evaluater = BinaryClassificationEvaluator(
        rawPredictionCol='prediction',
        labelCol='Survived',
        metricName='areaUnderROC'
    )
    auc_train = evaluater.evaluate(prediction_train)
    auc_valid = evaluater.evaluate(prediction_valid)
    
    logging_node(auc_valid)

    #return auc_train, auc_valid