from kedro.pipeline import Pipeline, node
from .mod_tree import *
from .mod_auc import *


def create_pipeline(**kwargs):
    """Create the project's pipeline.  Models pipeline.

    Returns:
        A pipeline containing the project's nodes.
    """
    return Pipeline(
        [
            node(
                func=mod_tree,
                inputs=["df_train", "df_valid"],
                outputs=["prediction_train","prediction_valid"],
                name="mod_tree",
            ),
            node(
                func=mod_auc,
                inputs=["prediction_train", "prediction_valid"],
                outputs=None,#["auc_train","auc_valid"],
                name="mod_auc",
            ),
        ]
    )