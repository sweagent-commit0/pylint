from __future__ import annotations
import tokenize
from collections import defaultdict
from typing import TYPE_CHECKING, Literal
from pylint import exceptions, interfaces
from pylint.constants import MSG_STATE_CONFIDENCE, MSG_STATE_SCOPE_CONFIG, MSG_STATE_SCOPE_MODULE, MSG_TYPES, MSG_TYPES_LONG
from pylint.interfaces import HIGH
from pylint.message import MessageDefinition
from pylint.typing import ManagedMessage
from pylint.utils.pragma_parser import OPTION_PO, InvalidPragmaError, UnRecognizedOptionError, parse_pragma
if TYPE_CHECKING:
    from pylint.lint.pylinter import PyLinter

class _MessageStateHandler:
    """Class that handles message disabling & enabling and processing of inline
    pragma's.
    """

    def __init__(self, linter: PyLinter) -> None:
        self.linter = linter
        self._msgs_state: dict[str, bool] = {}
        self._options_methods = {'enable': self.enable, 'disable': self.disable, 'disable-next': self.disable_next}
        self._bw_options_methods = {'disable-msg': self._options_methods['disable'], 'enable-msg': self._options_methods['enable']}
        self._pragma_lineno: dict[str, int] = {}
        self._stashed_messages: defaultdict[tuple[str, str], list[tuple[str | None, str]]] = defaultdict(list)
        'Some messages in the options (for --enable and --disable) are encountered\n        too early to warn about them.\n\n        i.e. before all option providers have been fully parsed. Thus, this dict stores\n        option_value and msg_id needed to (later) emit the messages keyed on module names.\n        '

    def _set_one_msg_status(self, scope: str, msg: MessageDefinition, line: int | None, enable: bool) -> None:
        """Set the status of an individual message."""
        pass

    def _get_messages_to_set(self, msgid: str, enable: bool, ignore_unknown: bool=False) -> list[MessageDefinition]:
        """Do some tests and find the actual messages of which the status should be set."""
        pass

    def _set_msg_status(self, msgid: str, enable: bool, scope: str='package', line: int | None=None, ignore_unknown: bool=False) -> None:
        """Do some tests and then iterate over message definitions to set state."""
        pass

    def _register_by_id_managed_msg(self, msgid_or_symbol: str, line: int | None, is_disabled: bool=True) -> None:
        """If the msgid is a numeric one, then register it to inform the user
        it could furnish instead a symbolic msgid.
        """
        pass

    def disable(self, msgid: str, scope: str='package', line: int | None=None, ignore_unknown: bool=False) -> None:
        """Disable a message for a scope."""
        pass

    def disable_next(self, msgid: str, _: str='package', line: int | None=None, ignore_unknown: bool=False) -> None:
        """Disable a message for the next line."""
        pass

    def enable(self, msgid: str, scope: str='package', line: int | None=None, ignore_unknown: bool=False) -> None:
        """Enable a message for a scope."""
        pass

    def disable_noerror_messages(self) -> None:
        """Disable message categories other than `error` and `fatal`."""
        pass

    def _get_message_state_scope(self, msgid: str, line: int | None=None, confidence: interfaces.Confidence | None=None) -> Literal[0, 1, 2] | None:
        """Returns the scope at which a message was enabled/disabled."""
        pass

    def _is_one_message_enabled(self, msgid: str, line: int | None) -> bool:
        """Checks state of a single message for the current file.

        This function can't be cached as it depends on self.file_state which can
        change.
        """
        pass

    def is_message_enabled(self, msg_descr: str, line: int | None=None, confidence: interfaces.Confidence | None=None) -> bool:
        """Is this message enabled for the current file ?

        Optionally, is it enabled for this line and confidence level ?

        The current file is implicit and mandatory. As a result this function
        can't be cached right now as the line is the line of the currently
        analysed file (self.file_state), if it changes, then the result for
        the same msg_descr/line might need to change.

        :param msg_descr: Either the msgid or the symbol for a MessageDefinition
        :param line: The line of the currently analysed file
        :param confidence: The confidence of the message
        """
        pass

    def process_tokens(self, tokens: list[tokenize.TokenInfo]) -> None:
        """Process tokens from the current module to search for module/block level
        options.

        See func_block_disable_msg.py test case for expected behaviour.
        """
        pass