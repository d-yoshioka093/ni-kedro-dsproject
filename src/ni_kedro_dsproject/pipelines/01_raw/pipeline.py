from kedro.pipeline import Pipeline, node
# from .nodes import hello_world
from .nodes import *

test_str = "hoge"

def create_pipeline(**kwargs):
    """Create the project's pipeline.

    Returns:
        A pipeline containing the project's nodes.
    """
    return Pipeline(
        [
            node(
                func=hello_world,
                inputs=test_str,
                outputs="greeting_message",
                name="hello_world_node",
            ),
        ]
    )
