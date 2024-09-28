from __future__ import annotations
import tokenize
from typing import TYPE_CHECKING, Any, Literal, cast
from pylint.checkers import BaseTokenChecker
from pylint.reporters.ureports.nodes import Paragraph, Section, Table, Text
from pylint.utils import LinterStats, diff_string
if TYPE_CHECKING:
    from pylint.lint import PyLinter

def report_raw_stats(sect: Section, stats: LinterStats, old_stats: LinterStats | None) -> None:
    """Calculate percentage of code / doc / comment / empty."""
    pass

class RawMetricsChecker(BaseTokenChecker):
    """Checker that provides raw metrics instead of checking anything.

    Provides:
    * total number of lines
    * total number of code lines
    * total number of docstring lines
    * total number of comments lines
    * total number of empty lines
    """
    name = 'metrics'
    options = ()
    msgs: Any = {}
    reports = (('RP0701', 'Raw metrics', report_raw_stats),)

    def open(self) -> None:
        """Init statistics."""
        pass

    def process_tokens(self, tokens: list[tokenize.TokenInfo]) -> None:
        """Update stats."""
        pass
JUNK = (tokenize.NL, tokenize.INDENT, tokenize.NEWLINE, tokenize.ENDMARKER)

def get_type(tokens: list[tokenize.TokenInfo], start_index: int) -> tuple[int, int, Literal['code', 'docstring', 'comment', 'empty']]:
    """Return the line type : docstring, comment, code, empty."""
    pass