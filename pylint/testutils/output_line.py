from __future__ import annotations
from collections.abc import Sequence
from typing import Any, NamedTuple, TypeVar
from astroid import nodes
from pylint.interfaces import UNDEFINED, Confidence
from pylint.message.message import Message
_T = TypeVar('_T')

class MessageTest(NamedTuple):
    msg_id: str
    line: int | None = None
    node: nodes.NodeNG | None = None
    args: Any | None = None
    confidence: Confidence | None = UNDEFINED
    col_offset: int | None = None
    end_line: int | None = None
    end_col_offset: int | None = None
    "Used to test messages produced by pylint.\n\n    Class name cannot start with Test as pytest doesn't allow constructors in test classes.\n    "

class OutputLine(NamedTuple):
    symbol: str
    lineno: int
    column: int
    end_lineno: int | None
    end_column: int | None
    object: str
    msg: str
    confidence: str

    @classmethod
    def from_msg(cls, msg: Message, check_endline: bool=True) -> OutputLine:
        """Create an OutputLine from a Pylint Message."""
        pass

    @staticmethod
    def _get_column(column: str | int) -> int:
        """Handle column numbers."""
        pass

    @staticmethod
    def _get_py38_none_value(value: _T, check_endline: bool) -> _T | None:
        """Used to make end_line and end_column None as indicated by our version
        compared to `min_pyver_end_position`.
        """
        pass

    @classmethod
    def from_csv(cls, row: Sequence[str] | str, check_endline: bool=True) -> OutputLine:
        """Create an OutputLine from a comma separated list (the functional tests
        expected output .txt files).
        """
        pass

    def to_csv(self) -> tuple[str, str, str, str, str, str, str, str]:
        """Convert an OutputLine to a tuple of string to be written by a
        csv-writer.
        """
        pass

    @staticmethod
    def _value_to_optional_int(value: str | None) -> int | None:
        """Checks if a (stringified) value should be None or a Python integer."""
        pass