# """Project pipelines."""
from typing import Dict
from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from ni_kedro_dsproject.pipelines.nkd_01_raw.pipeline import create_pipeline as create_pipeline_01_raw
from ni_kedro_dsproject.pipelines.nkd_02_int.pipeline import create_pipeline as create_pipeline_02_int
from ni_kedro_dsproject.pipelines.nkd_03_pri.pipeline import create_pipeline as create_pipeline_03_pri
from ni_kedro_dsproject.pipelines.nkd_04_fea.pipeline import create_pipeline as create_pipeline_04_fea
from ni_kedro_dsproject.pipelines.nkd_05_mdi.pipeline import create_pipeline as create_pipeline_05_mdi
from ni_kedro_dsproject.pipelines.nkd_06_mod.pipeline import create_pipeline as create_pipeline_06_mod

# def register_pipelines() -> Dict[str, Pipeline]:
#     """Register the project's pipelines.

#     Returns:
#         A mapping from pipeline names to ``Pipeline`` objects.
#     """
#     pipelines = find_pipelines()
#     pipelines["__default__"] = sum(pipelines.values())
#     return pipelines

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # Create individual pipelines
    pipeline_01_raw = create_pipeline_01_raw()
    pipeline_02_int = create_pipeline_02_int()
    pipeline_03_pri = create_pipeline_03_pri()
    pipeline_04_fea = create_pipeline_04_fea()
    pipeline_05_mdi = create_pipeline_05_mdi()
    pipeline_06_mod = create_pipeline_06_mod()

    # Combine pipelines in the desired order
    combined_pipeline = pipeline_01_raw + pipeline_02_int + pipeline_03_pri + pipeline_04_fea + pipeline_05_mdi + pipeline_06_mod

    # Return a dict with the combined pipeline
    return {"__default__": combined_pipeline}
