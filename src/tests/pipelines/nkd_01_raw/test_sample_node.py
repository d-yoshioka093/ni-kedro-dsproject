import pytest
from pyspark.sql import SparkSession
from pyspark.sql import Row
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ni_kedro_dsproject.pipelines.nkd_01_raw.nodes import sample_node

@pytest.fixture(scope="module")
def spark_session():
    spark = SparkSession.builder \
        .appName("sample_node_test") \
        .getOrCreate()
    return spark

def test_sample_node(spark_session):
    # テスト用のデータを作成
    data = [Row(value=1), Row(value=2), Row(value=3)]
    input_df = spark_session.createDataFrame(data)

    # パラメータの設定
    params = {'example_test_data_ratio': 0.2, 'example_num_trees': 10, 'params': 'hello param'}

    # ノードの実行
    output_df = sample_node(input_df, params)

    # テストのアサーション
    assert input_df.count() == output_df.count()
    assert input_df.columns == output_df.columns
