"""Check for use of while loops."""
from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import only_required_for_messages
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class WhileChecker(BaseChecker):
    name = 'while_used'
    msgs = {'W0149': ('Used `while` loop', 'while-used', 'Unbounded `while` loops can often be rewritten as bounded `for` loops. Exceptions can be made for cases such as event loops, listeners, etc.')}