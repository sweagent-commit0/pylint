from __future__ import annotations
import configparser
import os
import sys
from collections.abc import Iterator
from pathlib import Path
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib
RC_NAMES = (Path('pylintrc'), Path('pylintrc.toml'), Path('.pylintrc'), Path('.pylintrc.toml'))
PYPROJECT_NAME = Path('pyproject.toml')
CONFIG_NAMES = (*RC_NAMES, PYPROJECT_NAME, Path('setup.cfg'))

def _find_pyproject() -> Path:
    """Search for file pyproject.toml in the parent directories recursively.

    It resolves symlinks, so if there is any symlink up in the tree, it does not respect them
    """
    pass

def _yield_default_files() -> Iterator[Path]:
    """Iterate over the default config file names and see if they exist."""
    pass

def _find_project_config() -> Iterator[Path]:
    """Traverse up the directory tree to find a config file.

    Stop if no '__init__' is found and thus we are no longer in a package.
    """
    pass

def _find_config_in_home_or_environment() -> Iterator[Path]:
    """Find a config file in the specified environment var or the home directory."""
    pass

def find_default_config_files() -> Iterator[Path]:
    """Find all possible config files."""
    pass