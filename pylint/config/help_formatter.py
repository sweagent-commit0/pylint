from __future__ import annotations
import argparse
from pylint.config.callback_actions import _CallbackAction
from pylint.constants import DEFAULT_PYLINT_HOME

class _HelpFormatter(argparse.RawDescriptionHelpFormatter):
    """Formatter for the help message emitted by argparse."""

    def _get_help_string(self, action: argparse.Action) -> str | None:
        """Copied from argparse.ArgumentDefaultsHelpFormatter."""
        pass