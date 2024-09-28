"""Arguments manager class used to handle command-line arguments and options."""
from __future__ import annotations
import argparse
import re
import sys
import textwrap
import warnings
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, TextIO
import tomlkit
from pylint import utils
from pylint.config.argument import _Argument, _CallableArgument, _ExtendArgument, _StoreArgument, _StoreNewNamesArgument, _StoreOldNamesArgument, _StoreTrueArgument
from pylint.config.exceptions import UnrecognizedArgumentAction, _UnrecognizedOptionError
from pylint.config.help_formatter import _HelpFormatter
from pylint.config.utils import _convert_option_to_argument, _parse_rich_type_value
from pylint.constants import MAIN_CHECKER_NAME
from pylint.typing import DirectoryNamespaceDict, OptionDict
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib
if TYPE_CHECKING:
    from pylint.config.arguments_provider import _ArgumentsProvider

class _ArgumentsManager:
    """Arguments manager class used to handle command-line arguments and options."""

    def __init__(self, prog: str, usage: str | None=None, description: str | None=None) -> None:
        self._config = argparse.Namespace()
        'Namespace for all options.'
        self._base_config = self._config
        'Fall back Namespace object created during initialization.\n\n        This is necessary for the per-directory configuration support. Whenever we\n        fail to match a file with a directory we fall back to the Namespace object\n        created during initialization.\n        '
        self._arg_parser = argparse.ArgumentParser(prog=prog, usage=usage or '%(prog)s [options]', description=description, formatter_class=_HelpFormatter, conflict_handler='resolve')
        'The command line argument parser.'
        self._argument_groups_dict: dict[str, argparse._ArgumentGroup] = {}
        'Dictionary of all the argument groups.'
        self._option_dicts: dict[str, OptionDict] = {}
        'All option dictionaries that have been registered.'
        self._directory_namespaces: DirectoryNamespaceDict = {}
        'Mapping of directories and their respective namespace objects.'

    @property
    def config(self) -> argparse.Namespace:
        """Namespace for all options."""
        pass

    def _register_options_provider(self, provider: _ArgumentsProvider) -> None:
        """Register an options provider and load its defaults."""
        pass

    def _add_arguments_to_parser(self, section: str, section_desc: str | None, argument: _Argument) -> None:
        """Add an argument to the correct argument section/group."""
        pass

    @staticmethod
    def _add_parser_option(section_group: argparse._ArgumentGroup, argument: _Argument) -> None:
        """Add an argument."""
        pass

    def _load_default_argument_values(self) -> None:
        """Loads the default values of all registered options."""
        pass

    def _parse_configuration_file(self, arguments: list[str]) -> None:
        """Parse the arguments found in a configuration file into the namespace."""
        pass

    def _parse_command_line_configuration(self, arguments: Sequence[str] | None=None) -> list[str]:
        """Parse the arguments found on the command line into the namespace."""
        pass

    def _generate_config(self, stream: TextIO | None=None, skipsections: tuple[str, ...]=()) -> None:
        """Write a configuration file according to the current configuration
        into the given stream or stdout.
        """
        pass

    def help(self) -> str:
        """Return the usage string based on the available options."""
        pass

    def _generate_config_file(self, *, minimal: bool=False) -> str:
        """Write a configuration file according to the current configuration into
        stdout.
        """
        pass

    def set_option(self, optname: str, value: Any) -> None:
        """Set an option on the namespace object."""
        pass