"""Configuration file parser class."""
from __future__ import annotations
import configparser
import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List, Tuple
from pylint.config.utils import _parse_rich_type_value
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib
if TYPE_CHECKING:
    from pylint.lint import PyLinter
PylintConfigFileData = Tuple[Dict[str, str], List[str]]

class _RawConfParser:
    """Class to parse various formats of configuration files."""

    @staticmethod
    def parse_ini_file(file_path: Path) -> PylintConfigFileData:
        """Parse and handle errors of an ini configuration file.

        Raises ``configparser.Error``.
        """
        pass

    @staticmethod
    def _ini_file_with_sections(file_path: Path) -> bool:
        """Return whether the file uses sections."""
        pass

    @staticmethod
    def parse_toml_file(file_path: Path) -> PylintConfigFileData:
        """Parse and handle errors of a toml configuration file.

        Raises ``tomllib.TOMLDecodeError``.
        """
        pass

    @staticmethod
    def parse_config_file(file_path: Path | None, verbose: bool) -> PylintConfigFileData:
        """Parse a config file and return str-str pairs.

        Raises ``tomllib.TOMLDecodeError``, ``configparser.Error``.
        """
        pass

class _ConfigurationFileParser:
    """Class to parse various formats of configuration files."""

    def __init__(self, verbose: bool, linter: PyLinter) -> None:
        self.verbose_mode = verbose
        self.linter = linter

    def parse_config_file(self, file_path: Path | None) -> PylintConfigFileData:
        """Parse a config file and return str-str pairs."""
        pass