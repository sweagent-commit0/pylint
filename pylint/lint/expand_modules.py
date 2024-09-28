from __future__ import annotations
import os
import sys
from collections.abc import Sequence
from pathlib import Path
from re import Pattern
from astroid import modutils
from pylint.typing import ErrorDescriptionDict, ModuleDescriptionDict

def discover_package_path(modulepath: str, source_roots: Sequence[str]) -> str:
    """Discover package path from one its modules and source roots."""
    pass

def _is_in_ignore_list_re(element: str, ignore_list_re: list[Pattern[str]]) -> bool:
    """Determines if the element is matched in a regex ignore-list."""
    pass

def expand_modules(files_or_modules: Sequence[str], source_roots: Sequence[str], ignore_list: list[str], ignore_list_re: list[Pattern[str]], ignore_list_paths_re: list[Pattern[str]]) -> tuple[dict[str, ModuleDescriptionDict], list[ErrorDescriptionDict]]:
    """Take a list of files/modules/packages and return the list of tuple
    (file, module name) which have to be actually checked.
    """
    pass