from pyspark.sql import SparkSession,DataFrame

def sample_node(train :DataFrame): #-> DataFrame:
    """Return dataframe.

    Args:
        Nothing.

    Returns:
        sample pyspark dataframe.
    """
    
    # spark = SparkSession.builder.appName("hoge_dataframe").getOrCreate()
    # data = [("Alice", 1), ("Bob", 2), ("Charlie", 3), ("Dave", 4)]
    # df = spark.createDataFrame(data, ["Name", "Age"])

    print(type(train))

    print("end")
    # return df
