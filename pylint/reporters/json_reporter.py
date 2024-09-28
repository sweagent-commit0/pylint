"""JSON reporter."""
from __future__ import annotations
import json
from typing import TYPE_CHECKING, Optional, TypedDict
from pylint.interfaces import CONFIDENCE_MAP, UNDEFINED
from pylint.message import Message
from pylint.reporters.base_reporter import BaseReporter
from pylint.typing import MessageLocationTuple
if TYPE_CHECKING:
    from pylint.lint.pylinter import PyLinter
    from pylint.reporters.ureports.nodes import Section
OldJsonExport = TypedDict('OldJsonExport', {'type': str, 'module': str, 'obj': str, 'line': int, 'column': int, 'endLine': Optional[int], 'endColumn': Optional[int], 'path': str, 'symbol': str, 'message': str, 'message-id': str})

class JSONReporter(BaseReporter):
    """Report messages and layouts in JSON.

    Consider using JSON2Reporter instead, as it is superior and this reporter
    is no longer maintained.
    """
    name = 'json'
    extension = 'json'

    def display_messages(self, layout: Section | None) -> None:
        """Launch layouts display."""
        pass

    def display_reports(self, layout: Section) -> None:
        """Don't do anything in this reporter."""
        pass

    def _display(self, layout: Section) -> None:
        """Do nothing."""
        pass

class JSONMessage(TypedDict):
    type: str
    message: str
    messageId: str
    symbol: str
    confidence: str
    module: str
    path: str
    absolutePath: str
    line: int
    endLine: int | None
    column: int
    endColumn: int | None
    obj: str

class JSON2Reporter(BaseReporter):
    name = 'json2'
    extension = 'json2'

    def display_reports(self, layout: Section) -> None:
        """Don't do anything in this reporter."""
        pass

    def _display(self, layout: Section) -> None:
        """Do nothing."""
        pass

    def display_messages(self, layout: Section | None) -> None:
        """Launch layouts display."""
        pass

    def serialize_stats(self) -> dict[str, str | int | dict[str, int]]:
        """Serialize the linter stats into something JSON dumpable."""
        pass