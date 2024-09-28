from __future__ import annotations
from io import StringIO
from os import getcwd, sep
from typing import TYPE_CHECKING
from pylint.message import Message
from pylint.reporters import BaseReporter
if TYPE_CHECKING:
    from pylint.reporters.ureports.nodes import Section

class GenericTestReporter(BaseReporter):
    """Reporter storing plain text messages."""
    out: StringIO

    def __init__(self) -> None:
        self.path_strip_prefix: str = getcwd() + sep
        self.reset()

    def handle_message(self, msg: Message) -> None:
        """Append messages to the list of messages of the reporter."""
        pass

    def finalize(self) -> str:
        """Format and print messages in the context of the path."""
        pass

    def display_reports(self, layout: Section) -> None:
        """Ignore layouts."""
        pass

class MinimalTestReporter(BaseReporter):
    pass

class FunctionalTestReporter(BaseReporter):

    def display_reports(self, layout: Section) -> None:
        """Ignore layouts and don't call self._display()."""
        pass