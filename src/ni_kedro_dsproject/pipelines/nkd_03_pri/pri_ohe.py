from pyspark.sql import DataFrame
# from kedro.config import ConfigLoader
# from kedro.framework.project import settings
from pyspark.ml.feature import OneHotEncoder, StringIndexer

def pri_ohe(pri_prep: DataFrame, params: dict) -> DataFrame:
    """Return dataframe. Encoding.

    Args:
        pri_prep: A Spark DataFrame. 
        params: Category variables to be encoded.

    Returns:
        A PySpark DataFrame. Encoded data.
    """

    # One-Hotエンコーディング 
    ohe_input = params['ohe_input']
    #ohe_input = [  'SibSp', 'Parch']
    ohe_output = [col + '_encoded' for col in ohe_input]

    #stringIndexer = StringIndexer(inputCol="Pclass", outputCol="Pclass_Index")
    #model = stringIndexer.fit(pri_prep)
    #pri_prep = model.transform(pri_prep)

    ohe = OneHotEncoder(
        inputCols=ohe_input,
        #inputCols='Embarked_indexed',
        outputCols=ohe_output,
        #outputCols='Embarked_indexed_encoded'
        dropLast=True,
       # handleInvalid="error"
    )

    ohe_model = ohe.fit(pri_prep)
    pri_prep = ohe_model.transform(pri_prep)
    #pri_prep = ohe.transform(pri_prep)
    
    return pri_prep