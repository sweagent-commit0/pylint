from __future__ import annotations
import linecache
from typing import TYPE_CHECKING
from astroid import nodes
from pylint import checkers
from pylint.checkers.utils import only_required_for_messages
from pylint.interfaces import HIGH
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class DocStringStyleChecker(checkers.BaseChecker):
    """Checks format of docstrings based on PEP 0257."""
    name = 'docstyle'
    msgs = {'C0198': ('Bad docstring quotes in %s, expected """, given %s', 'bad-docstring-quotes', 'Used when a docstring does not have triple double quotes.'), 'C0199': ('First line empty in %s docstring', 'docstring-first-line-empty', 'Used when a blank line is found at the beginning of a docstring.')}
    visit_asyncfunctiondef = visit_functiondef