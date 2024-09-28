"""Looks for try/except statements with too much code in the try clause."""
from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint import checkers
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class BroadTryClauseChecker(checkers.BaseChecker):
    """Checks for try clauses with too many lines.

    According to PEP 8, ``try`` clauses shall contain the absolute minimum
    amount of code. This checker enforces a maximum number of statements within
    ``try`` clauses.
    """
    name = 'broad_try_clause'
    msgs = {'W0717': ('%s', 'too-many-try-statements', 'Try clause contains too many statements.')}
    options = (('max-try-statements', {'default': 1, 'type': 'int', 'metavar': '<int>', 'help': 'Maximum number of statements allowed in a try clause'}),)