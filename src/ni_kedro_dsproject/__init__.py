# """NI_Kedro_DSProject
# """

# __version__ = "0.1"
# src/ni_kedro_dsproject/__init__.py

import os
import sys

# add project root to PYTHONPATH
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(ROOT_DIR, os.pardir))
sys.path.append(PROJECT_ROOT)

__version__ = "0.1.0"
