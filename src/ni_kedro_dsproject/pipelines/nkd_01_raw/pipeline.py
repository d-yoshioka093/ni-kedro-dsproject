from kedro.pipeline import Pipeline, node
# from .nodes import hello_world
from .nodes import *

def create_pipeline(**kwargs):
    """Create the project's pipeline.

    Returns:
        A pipeline containing the project's nodes.
    """
    return Pipeline(
        [
            node(
                func=sample_node,
                inputs=["train", "parameters"],
                outputs="result@pyspark",
                name="sample_node",
            ),
        ]
    )
