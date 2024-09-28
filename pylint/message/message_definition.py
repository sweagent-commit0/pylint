from __future__ import annotations
import sys
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.constants import _SCOPE_EXEMPT, MSG_TYPES, WarningScope
from pylint.exceptions import InvalidMessageError
from pylint.utils import normalize_text
if TYPE_CHECKING:
    from pylint.checkers import BaseChecker

class MessageDefinition:

    def __init__(self, checker: BaseChecker, msgid: str, msg: str, description: str, symbol: str, scope: str, minversion: tuple[int, int] | None=None, maxversion: tuple[int, int] | None=None, old_names: list[tuple[str, str]] | None=None, shared: bool=False, default_enabled: bool=True) -> None:
        self.checker_name = checker.name
        self.check_msgid(msgid)
        self.msgid = msgid
        self.symbol = symbol
        self.msg = msg
        self.description = description
        self.scope = scope
        self.minversion = minversion
        self.maxversion = maxversion
        self.shared = shared
        self.default_enabled = default_enabled
        self.old_names: list[tuple[str, str]] = []
        if old_names:
            for old_msgid, old_symbol in old_names:
                self.check_msgid(old_msgid)
                self.old_names.append((old_msgid, old_symbol))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, MessageDefinition) and self.msgid == other.msgid and (self.symbol == other.symbol)

    def __repr__(self) -> str:
        return f'MessageDefinition:{self.symbol} ({self.msgid})'

    def __str__(self) -> str:
        return f'{self!r}:\n{self.msg} {self.description}'

    def may_be_emitted(self, py_version: tuple[int, ...] | sys._version_info) -> bool:
        """May the message be emitted using the configured py_version?"""
        pass

    def format_help(self, checkerref: bool=False) -> str:
        """Return the help string for the given message id."""
        pass

    def check_message_definition(self, line: int | None, node: nodes.NodeNG | None) -> None:
        """Check MessageDefinition for possible errors."""
        pass