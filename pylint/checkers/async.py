"""Checker for anything related to the async protocol (PEP 492)."""
from __future__ import annotations
import sys
from typing import TYPE_CHECKING
import astroid
from astroid import nodes, util
from pylint import checkers
from pylint.checkers import utils as checker_utils
from pylint.checkers.utils import decorated_with
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class AsyncChecker(checkers.BaseChecker):
    name = 'async'
    msgs = {'E1700': ('Yield inside async function', 'yield-inside-async-function', 'Used when an `yield` or `yield from` statement is found inside an async function.', {'minversion': (3, 5)}), 'E1701': ("Async context manager '%s' doesn't implement __aenter__ and __aexit__.", 'not-async-context-manager', 'Used when an async context manager is used with an object that does not implement the async context management protocol.', {'minversion': (3, 5)})}