from __future__ import annotations
import sys
import warnings
from glob import glob
from itertools import chain
from pathlib import Path
from typing import TYPE_CHECKING
from pylint import reporters
from pylint.config.config_file_parser import _ConfigurationFileParser
from pylint.config.exceptions import ArgumentPreprocessingError, _UnrecognizedOptionError
from pylint.utils import utils
if TYPE_CHECKING:
    from pylint.lint import PyLinter

def _config_initialization(linter: PyLinter, args_list: list[str], reporter: reporters.BaseReporter | reporters.MultiReporter | None=None, config_file: None | str | Path=None, verbose_mode: bool=False) -> list[str]:
    """Parse all available options, read config files and command line arguments and
    set options accordingly.
    """
    pass

def _order_all_first(config_args: list[str], *, joined: bool) -> list[str]:
    """Reorder config_args such that --enable=all or --disable=all comes first.

    Raise if both are given.

    If joined is True, expect args in the form '--enable=all,for-any-all'.
    If joined is False, expect args in the form '--enable', 'all,for-any-all'.
    """
    pass