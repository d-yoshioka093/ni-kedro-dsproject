from kedro.pipeline import Pipeline, node
from .in_split import *


def create_pipeline(**kwargs):
    """Create the project's pipeline.  Model_input pipeline.

    Returns:
        A pipeline containing the project's nodes.
    """
    return Pipeline(
        [
            node(
                func=in_split,
                inputs=["fea_result"],
                outputs=["df_train", "df_valid"],
                name="in_split",
            ),
        ]
    )