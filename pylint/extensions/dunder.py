from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.constants import DUNDER_METHODS, DUNDER_PROPERTIES, EXTRA_DUNDER_METHODS
from pylint.interfaces import HIGH
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class DunderChecker(BaseChecker):
    """Checks related to dunder methods."""
    name = 'dunder'
    msgs = {'W3201': ('Bad or misspelled dunder method name %s.', 'bad-dunder-name', 'Used when a dunder method is misspelled or defined with a name not within the predefined list of dunder names.')}
    options = (('good-dunder-names', {'default': [], 'type': 'csv', 'metavar': '<comma-separated names>', 'help': 'Good dunder names which should always be accepted.'}),)

    def visit_functiondef(self, node: nodes.FunctionDef) -> None:
        """Check if known dunder method is misspelled or dunder name is not one
        of the pre-defined names.
        """
        pass