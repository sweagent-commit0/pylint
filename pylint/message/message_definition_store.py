from __future__ import annotations
import collections
import functools
import sys
from collections.abc import Sequence, ValuesView
from typing import TYPE_CHECKING
from pylint.exceptions import UnknownMessageError
from pylint.message.message_definition import MessageDefinition
from pylint.message.message_id_store import MessageIdStore
if TYPE_CHECKING:
    from pylint.checkers import BaseChecker

class MessageDefinitionStore:
    """The messages store knows information about every possible message definition but
    has no particular state during analysis.
    """

    def __init__(self, py_version: tuple[int, ...] | sys._version_info=sys.version_info) -> None:
        self.message_id_store: MessageIdStore = MessageIdStore()
        self._messages_definitions: dict[str, MessageDefinition] = {}
        self._msgs_by_category: dict[str, list[str]] = collections.defaultdict(list)
        self.py_version = py_version

    @property
    def messages(self) -> ValuesView[MessageDefinition]:
        """The list of all active messages."""
        pass

    def register_messages_from_checker(self, checker: BaseChecker) -> None:
        """Register all messages definitions from a checker."""
        pass

    def register_message(self, message: MessageDefinition) -> None:
        """Register a MessageDefinition with consistency in mind."""
        pass

    @functools.lru_cache(maxsize=None)
    def get_message_definitions(self, msgid_or_symbol: str) -> list[MessageDefinition]:
        """Returns the Message definition for either a numeric or symbolic id.

        The cache has no limit as its size will likely stay minimal. For each message we store
        about 1000 characters, so even if we would have 1000 messages the cache would only
        take up ~= 1 Mb.
        """
        pass

    def get_msg_display_string(self, msgid_or_symbol: str) -> str:
        """Generates a user-consumable representation of a message."""
        pass

    def help_message(self, msgids_or_symbols: Sequence[str]) -> None:
        """Display help messages for the given message identifiers."""
        pass

    def list_messages(self) -> None:
        """Output full messages list documentation in ReST format."""
        pass

    def find_emittable_messages(self) -> tuple[list[MessageDefinition], list[MessageDefinition]]:
        """Finds all emittable and non-emittable messages."""
        pass