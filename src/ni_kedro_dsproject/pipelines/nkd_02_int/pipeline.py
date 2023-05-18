from kedro.pipeline import Pipeline, node
# from .nodes import hello_world
from .int_nodes import *
from .int_nodes2 import *

def create_pipeline(**kwargs):
    """Create the project's pipeline.

    Returns:
        A pipeline containing the project's nodes.
    """
    return Pipeline(
        [
            node(
                func=int_node_fillna,
                inputs=["result", "parameters"],
                outputs="mid_result",
                name="int_node_fillna",
            ),
            node(
                func=int_node_type,
                inputs=["mid_result"],
                outputs="result2",
                name="int_node_type",
            ),
        ]
    )
