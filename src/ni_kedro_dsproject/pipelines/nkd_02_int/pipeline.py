from kedro.pipeline import Pipeline, node
# from .nodes import hello_world
from .int_nodes import *

def create_pipeline(**kwargs):
    """Create the project's pipeline.

    Returns:
        A pipeline containing the project's nodes.
    """
    return Pipeline(
        [
            node(
                func=int_sample_node2,
                inputs=["result"],
                outputs="result2@pyspark",
                name="int_sample_node2",
            ),
        ]
    )
