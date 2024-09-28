"""Looks for overlapping exceptions."""
from __future__ import annotations
from typing import TYPE_CHECKING, Any
import astroid
from astroid import nodes, util
from pylint import checkers
from pylint.checkers import utils
from pylint.checkers.exceptions import _annotated_unpack_infer
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class OverlappingExceptionsChecker(checkers.BaseChecker):
    """Checks for two or more exceptions in the same exception handler
    clause that are identical or parts of the same inheritance hierarchy.

    (i.e. overlapping).
    """
    name = 'overlap-except'
    msgs = {'W0714': ('Overlapping exceptions (%s)', 'overlapping-except', 'Used when exceptions in handler overlap or are identical')}
    options = ()

    @utils.only_required_for_messages('overlapping-except')
    def visit_try(self, node: nodes.Try) -> None:
        """Check for empty except."""
        pass