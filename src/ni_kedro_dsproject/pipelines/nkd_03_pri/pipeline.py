from kedro.pipeline import Pipeline, node

from .pri_std import *
from .pri_ohe import *

def create_pipeline(**kwargs):
    """Create the project's pipeline. Primary pipeline.

    Returns:
        A pipeline containing the project's nodes.
    """
    return Pipeline(
        [
            node(
                func=pri_std,
                inputs=["int_result","params:pri_std_params"],
                #inputs=["int_result"],
                outputs="pri_prep",
                name="pri_std",
            ),
            node(
                func=pri_ohe,
                inputs=["pri_prep","params:pri_ohe_params"],
                outputs="pri_result",
                name="pri_ohe",
            ),
        ]
    )