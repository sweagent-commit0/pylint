"""Everything related to the 'pylint-config -h' command and subcommands."""
from __future__ import annotations
import argparse
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pylint.lint.pylinter import PyLinter

def get_subparser_help(linter: PyLinter, command: str) -> str:
    """Get the help message for one of the subcommands."""
    pass

def get_help(parser: argparse.ArgumentParser) -> str:
    """Get the help message for the main 'pylint-config' command.

    Taken from argparse.ArgumentParser.format_help.
    """
    pass