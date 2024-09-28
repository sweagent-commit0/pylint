"""Functions that creates the basic options for the Run and PyLinter classes."""
from __future__ import annotations
import re
import sys
from typing import TYPE_CHECKING
from pylint import constants, interfaces
from pylint.config.callback_actions import _DisableAction, _DoNothingAction, _EnableAction, _ErrorsOnlyModeAction, _FullDocumentationAction, _GenerateConfigFileAction, _GenerateRCFileAction, _ListCheckGroupsAction, _ListConfidenceLevelsAction, _ListExtensionsAction, _ListMessagesAction, _ListMessagesEnabledAction, _LongHelpAction, _MessageHelpAction, _OutputFormatAction
from pylint.typing import Options
if TYPE_CHECKING:
    from pylint.lint import PyLinter, Run

def _make_linter_options(linter: PyLinter) -> Options:
    """Return the options used in a PyLinter class."""
    pass

def _make_run_options(self: Run) -> Options:
    """Return the options used in a Run class."""
    pass