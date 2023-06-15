from kedro.pipeline import Pipeline, node
from .fea_vec import *
from .fea_bin import *


def create_pipeline(**kwargs):
    """Create the project's pipeline. Feature pipeline.

    Returns:
        A pipeline containing the project's nodes.
    """
    return Pipeline(
        [
            node(
                func=fea_bin,
                inputs=["pri_result","params:fea_params"],
                outputs="fea_prep",
                name="fea_bin",
            ),
            node(
                func=fea_vec,
                inputs=["fea_prep","params:fea_params"],
                outputs="fea_result",
                name="fea_vec",
            ),
        ]
    )