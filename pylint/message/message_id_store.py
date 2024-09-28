from __future__ import annotations
from typing import NoReturn
from pylint.exceptions import DeletedMessageError, InvalidMessageError, MessageBecameExtensionError, UnknownMessageError
from pylint.message._deleted_message_ids import is_deleted_msgid, is_deleted_symbol, is_moved_msgid, is_moved_symbol

class MessageIdStore:
    """The MessageIdStore store MessageId and make sure that there is a 1-1 relation
    between msgid and symbol.
    """

    def __init__(self) -> None:
        self.__msgid_to_symbol: dict[str, str] = {}
        self.__symbol_to_msgid: dict[str, str] = {}
        self.__old_names: dict[str, list[str]] = {}
        self.__active_msgids: dict[str, list[str]] = {}

    def __len__(self) -> int:
        return len(self.__msgid_to_symbol)

    def __repr__(self) -> str:
        result = 'MessageIdStore: [\n'
        for msgid, symbol in self.__msgid_to_symbol.items():
            result += f'  - {msgid} ({symbol})\n'
        result += ']'
        return result

    def add_msgid_and_symbol(self, msgid: str, symbol: str) -> None:
        """Add valid message id.

        There is a little duplication with add_legacy_msgid_and_symbol to avoid a function call,
        this is called a lot at initialization.
        """
        pass

    def add_legacy_msgid_and_symbol(self, msgid: str, symbol: str, new_msgid: str) -> None:
        """Add valid legacy message id.

        There is a little duplication with add_msgid_and_symbol to avoid a function call,
        this is called a lot at initialization.
        """
        pass

    @staticmethod
    def _raise_duplicate_symbol(msgid: str, symbol: str, other_symbol: str) -> NoReturn:
        """Raise an error when a symbol is duplicated."""
        pass

    @staticmethod
    def _raise_duplicate_msgid(symbol: str, msgid: str, other_msgid: str) -> NoReturn:
        """Raise an error when a msgid is duplicated."""
        pass

    def get_active_msgids(self, msgid_or_symbol: str) -> list[str]:
        """Return msgids but the input can be a symbol.

        self.__active_msgids is used to implement a primitive cache for this function.
        """
        pass