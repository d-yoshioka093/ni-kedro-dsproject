from kedro.pipeline import Pipeline, node
# from .nodes import hello_world
from .int_fillna import *
from .int_type import *

def create_pipeline(**kwargs):
    """Create the project's pipeline.

    Returns:
        A pipeline containing the project's nodes.
    """
    return Pipeline(
        [
            node(
                func=int_fillna,
                inputs=["result", "params:int_params"],
                outputs="int_prep",
                name="int_fillna",
            ),
            node(
                func=int_type,
                inputs=["int_prep", "params:int_params"],
                outputs="int_result",
                name="int_type",
            ),
        ]
    )
