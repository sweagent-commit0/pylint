"""Check source code is ascii only or has an encoding declaration (PEP 263)."""
from __future__ import annotations
import re
import tokenize
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseRawFileChecker, BaseTokenChecker
from pylint.typing import ManagedMessage
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class ByIdManagedMessagesChecker(BaseRawFileChecker):
    """Checks for messages that are enabled or disabled by id instead of symbol."""
    name = 'miscellaneous'
    msgs = {'I0023': ('%s', 'use-symbolic-message-instead', 'Used when a message is enabled or disabled by id.', {'default_enabled': False})}
    options = ()

    def process_module(self, node: nodes.Module) -> None:
        """Inspect the source file to find messages activated or deactivated by id."""
        pass

class EncodingChecker(BaseTokenChecker, BaseRawFileChecker):
    """BaseChecker for encoding issues.

    Checks for:
    * warning notes in the code like FIXME, XXX
    * encoding issues.
    """
    name = 'miscellaneous'
    msgs = {'W0511': ('%s', 'fixme', 'Used when a warning note as FIXME or XXX is detected.')}
    options = (('notes', {'type': 'csv', 'metavar': '<comma separated values>', 'default': ('FIXME', 'XXX', 'TODO'), 'help': 'List of note tags to take in consideration, separated by a comma.'}), ('notes-rgx', {'type': 'string', 'metavar': '<regexp>', 'help': 'Regular expression of note tags to take in consideration.', 'default': ''}))

    def process_module(self, node: nodes.Module) -> None:
        """Inspect the source file to find encoding problem."""
        pass

    def process_tokens(self, tokens: list[tokenize.TokenInfo]) -> None:
        """Inspect the source to find fixme problems."""
        pass