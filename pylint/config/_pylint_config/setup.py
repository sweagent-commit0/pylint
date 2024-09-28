"""Everything related to the setup of the 'pylint-config' command."""
from __future__ import annotations
import argparse
from collections.abc import Sequence
from typing import Any
from pylint.config._pylint_config.help_message import get_help
from pylint.config.callback_actions import _AccessParserAction

class _HelpAction(_AccessParserAction):

    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: str | Sequence[Any] | None, option_string: str | None='--help') -> None:
        get_help(self.parser)

def _register_generate_config_options(parser: argparse.ArgumentParser) -> None:
    """Registers the necessary arguments on the parser."""
    pass