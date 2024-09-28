"""Checker for deprecated builtins."""
from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import only_required_for_messages
if TYPE_CHECKING:
    from pylint.lint import PyLinter
BAD_FUNCTIONS = ['map', 'filter']
LIST_COMP_MSG = 'Using a list comprehension can be clearer.'
BUILTIN_HINTS = {'map': LIST_COMP_MSG, 'filter': LIST_COMP_MSG}

class BadBuiltinChecker(BaseChecker):
    name = 'deprecated_builtins'
    msgs = {'W0141': ('Used builtin function %s', 'bad-builtin', 'Used when a disallowed builtin function is used (see the bad-function option). Usual disallowed functions are the ones like map, or filter , where Python offers now some cleaner alternative like list comprehension.')}
    options = (('bad-functions', {'default': BAD_FUNCTIONS, 'type': 'csv', 'metavar': '<builtin function names>', 'help': 'List of builtins function names that should not be used, separated by a comma'}),)