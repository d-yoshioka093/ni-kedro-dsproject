# """Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline


# def register_pipelines() -> Dict[str, Pipeline]:
#     """Register the project's pipelines.

#     Returns:
#         A mapping from pipeline names to ``Pipeline`` objects.
#     """
#     pipelines = find_pipelines()
#     pipelines["__default__"] = sum(pipelines.values())
#     return pipelines

from ni_kedro_dsproject.pipelines.nkd_01_raw.pipeline import create_pipeline as create_pipeline_01_raw
from ni_kedro_dsproject.pipelines.nkd_02_int.pipeline import create_pipeline as create_pipeline_02_int

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # Create individual pipelines
    pipeline_01_raw = create_pipeline_01_raw()
    pipeline_02_int = create_pipeline_02_int()

    # Combine pipelines in the desired order
    combined_pipeline = pipeline_01_raw + pipeline_02_int

    # Return a dict with the combined pipeline
    return {"__default__": combined_pipeline}
