from __future__ import annotations
import functools
from collections import defaultdict
from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, Any
import dill
from pylint import reporters
from pylint.lint.utils import _augment_sys_path
from pylint.message import Message
from pylint.typing import FileItem
from pylint.utils import LinterStats, merge_stats
try:
    import multiprocessing
except ImportError:
    multiprocessing = None
try:
    from concurrent.futures import ProcessPoolExecutor
except ImportError:
    ProcessPoolExecutor = None
if TYPE_CHECKING:
    from pylint.lint import PyLinter
_worker_linter: PyLinter | None = None

def _worker_initialize(linter: bytes, extra_packages_paths: Sequence[str] | None=None) -> None:
    """Function called to initialize a worker for a Process within a concurrent Pool.

    :param linter: A linter-class (PyLinter) instance pickled with dill
    :param extra_packages_paths: Extra entries to be added to `sys.path`
    """
    pass

def _merge_mapreduce_data(linter: PyLinter, all_mapreduce_data: defaultdict[int, list[defaultdict[str, list[Any]]]]) -> None:
    """Merges map/reduce data across workers, invoking relevant APIs on checkers."""
    pass

def check_parallel(linter: PyLinter, jobs: int, files: Iterable[FileItem], extra_packages_paths: Sequence[str] | None=None) -> None:
    """Use the given linter to lint the files with given amount of workers (jobs).

    This splits the work filestream-by-filestream. If you need to do work across
    multiple files, as in the similarity-checker, then implement the map/reduce functionality.
    """
    pass