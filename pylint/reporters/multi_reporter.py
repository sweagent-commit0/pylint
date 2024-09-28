from __future__ import annotations
import os
from collections.abc import Callable
from copy import copy
from typing import TYPE_CHECKING, TextIO
from pylint.message import Message
from pylint.reporters.base_reporter import BaseReporter
from pylint.utils import LinterStats
if TYPE_CHECKING:
    from pylint.lint import PyLinter
    from pylint.reporters.ureports.nodes import Section

class MultiReporter:
    """Reports messages and layouts in plain text."""
    name = '_internal_multi_reporter'
    extension = ''

    def __init__(self, sub_reporters: list[BaseReporter], close_output_files: Callable[[], None], output: TextIO | None=None):
        self._sub_reporters = sub_reporters
        self.close_output_files = close_output_files
        self._path_strip_prefix = os.getcwd() + os.sep
        self._linter: PyLinter | None = None
        self.out = output
        self.messages: list[Message] = []

    @out.setter
    def out(self, output: TextIO | None=None) -> None:
        """MultiReporter doesn't have its own output.

        This method is only provided for API parity with BaseReporter
        and should not be called with non-None values for 'output'.
        """
        pass

    def __del__(self) -> None:
        self.close_output_files()

    def handle_message(self, msg: Message) -> None:
        """Handle a new message triggered on the current file."""
        pass

    def writeln(self, string: str='') -> None:
        """Write a line in the output buffer."""
        pass

    def display_reports(self, layout: Section) -> None:
        """Display results encapsulated in the layout tree."""
        pass

    def display_messages(self, layout: Section | None) -> None:
        """Hook for displaying the messages of the reporter."""
        pass

    def on_set_current_module(self, module: str, filepath: str | None) -> None:
        """Hook called when a module starts to be analysed."""
        pass

    def on_close(self, stats: LinterStats, previous_stats: LinterStats | None) -> None:
        """Hook called when a module finished analyzing."""
        pass