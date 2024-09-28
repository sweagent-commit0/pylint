from __future__ import annotations
import os
from collections.abc import Iterator
from pathlib import Path
from pylint.testutils.functional.test_file import FunctionalTestFile
REASONABLY_DISPLAYABLE_VERTICALLY = 49
"'Wet finger' number of files that are reasonable to display by an IDE.\n\n'Wet finger' as in 'in my settings there are precisely this many'.\n"
IGNORED_PARENT_DIRS = {'deprecated_relative_import', 'ext', 'regression', 'regression_02'}
'Direct parent directories that should be ignored.'
IGNORED_PARENT_PARENT_DIRS = {'docparams', 'deprecated_relative_import', 'ext'}
'Parents of direct parent directories that should be ignored.'

def get_functional_test_files_from_directory(input_dir: Path | str, max_file_per_directory: int=REASONABLY_DISPLAYABLE_VERTICALLY) -> list[FunctionalTestFile]:
    """Get all functional tests in the input_dir."""
    pass

def _check_functional_tests_structure(directory: Path, max_file_per_directory: int) -> None:
    """Check if test directories follow correct file/folder structure.

    Ignore underscored directories or files.
    """
    pass