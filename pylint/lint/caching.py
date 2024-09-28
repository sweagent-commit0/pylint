from __future__ import annotations
import pickle
import sys
import warnings
from pathlib import Path
from pylint.constants import PYLINT_HOME
from pylint.utils import LinterStats
PYLINT_HOME_AS_PATH = Path(PYLINT_HOME)