"""Various helper functions to create the docs of a linter object."""
from __future__ import annotations
import sys
from typing import TYPE_CHECKING, Any, TextIO
from pylint.constants import MAIN_CHECKER_NAME
from pylint.utils.utils import get_rst_section, get_rst_title
if TYPE_CHECKING:
    from pylint.lint.pylinter import PyLinter

def _get_checkers_infos(linter: PyLinter) -> dict[str, dict[str, Any]]:
    """Get info from a checker and handle KeyError."""
    pass

def _get_global_options_documentation(linter: PyLinter) -> str:
    """Get documentation for the main checker."""
    pass

def _get_checkers_documentation(linter: PyLinter, show_options: bool=True) -> str:
    """Get documentation for individual checkers."""
    pass

def print_full_documentation(linter: PyLinter, stream: TextIO=sys.stdout, show_options: bool=True) -> None:
    """Output a full documentation in ReST format."""
    pass