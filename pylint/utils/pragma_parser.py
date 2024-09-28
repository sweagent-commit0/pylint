from __future__ import annotations
import re
from collections.abc import Generator
from typing import NamedTuple
OPTION_RGX = '\n    (?:^\\s*\\#.*|\\s*|               # Comment line, or whitespaces,\n       \\s*\\#.*(?=\\#.*?\\bpylint:))  # or a beginning of an inline comment\n                                   # followed by "pylint:" pragma\n    (\\#                            # Beginning of comment\n    .*?                            # Anything (as little as possible)\n    \\bpylint:                      # pylint word and column\n    \\s*                            # Any number of whitespaces\n    ([^;#\\n]+))                    # Anything except semicolon or hash or\n                                   # newline (it is the second matched group)\n                                   # and end of the first matched group\n    [;#]{0,1}                      # From 0 to 1 repetition of semicolon or hash\n'
OPTION_PO = re.compile(OPTION_RGX, re.VERBOSE)

class PragmaRepresenter(NamedTuple):
    action: str
    messages: list[str]
ATOMIC_KEYWORDS = frozenset(('disable-all', 'skip-file'))
MESSAGE_KEYWORDS = frozenset(('disable-next', 'disable-msg', 'enable-msg', 'disable', 'enable'))
ALL_KEYWORDS = '|'.join(sorted(ATOMIC_KEYWORDS | MESSAGE_KEYWORDS, key=len, reverse=True))
TOKEN_SPECIFICATION = [('KEYWORD', f'\\b({ALL_KEYWORDS:s})\\b'), ('MESSAGE_STRING', '[0-9A-Za-z\\-\\_]{2,}'), ('ASSIGN', '='), ('MESSAGE_NUMBER', '[CREIWF]{1}\\d*')]
TOK_REGEX = '|'.join((f'(?P<{token_name:s}>{token_rgx:s})' for token_name, token_rgx in TOKEN_SPECIFICATION))

class PragmaParserError(Exception):
    """A class for exceptions thrown by pragma_parser module."""

    def __init__(self, message: str, token: str) -> None:
        """:args message: explain the reason why the exception has been thrown
        :args token: token concerned by the exception.
        """
        self.message = message
        self.token = token
        super().__init__(self.message)

class UnRecognizedOptionError(PragmaParserError):
    """Thrown in case the of a valid but unrecognized option."""

class InvalidPragmaError(PragmaParserError):
    """Thrown in case the pragma is invalid."""