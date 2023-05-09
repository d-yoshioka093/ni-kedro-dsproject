from pyspark.sql import DataFrame

import logging.config
from kedro.config import ConfigLoader
from kedro.framework.project import settings

def sample_node(train: DataFrame, params: dict) -> DataFrame:
    """Return dataframe.

    Args:
        train: A Spark DataFrame.

    Returns:
        A sample PySpark DataFrame.
    """

    # project_path = "C:\notebook\01_study\ni-kedro-dsproject\src"
    # conf_path = str(project_path / settings.CONF_SOURCE)
    # conf_loader = ConfigLoader(conf_source=conf_path, env="local")

    # # conf_logging = conf_loader["logging"]
    # # logging.config.dictConfig(conf_logging)  # set logging conf
    # print(conf_loader)

    print(params)
    print(type(train))
    return train