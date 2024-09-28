from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import Instance, nodes
from astroid.util import UninferableBase
from pylint.checkers import BaseChecker
from pylint.checkers.utils import safe_infer
from pylint.constants import DUNDER_METHODS, UNNECESSARY_DUNDER_CALL_LAMBDA_EXCEPTIONS
from pylint.interfaces import HIGH
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class DunderCallChecker(BaseChecker):
    """Check for unnecessary dunder method calls.

    Docs: https://docs.python.org/3/reference/datamodel.html#basic-customization
    We exclude names in list pylint.constants.EXTRA_DUNDER_METHODS such as
    __index__ (see https://github.com/pylint-dev/pylint/issues/6795)
    since these either have no alternative method of being called or
    have a genuine use case for being called manually.

    Additionally, we exclude classes that are not instantiated since these
    might be used to access the dunder methods of a base class of an instance.
    We also exclude dunder method calls on super() since
    these can't be written in an alternative manner.
    """
    name = 'unnecessary-dunder-call'
    msgs = {'C2801': ('Unnecessarily calls dunder method %s. %s.', 'unnecessary-dunder-call', 'Used when a dunder method is manually called instead of using the corresponding function/method/operator.')}
    options = ()

    @staticmethod
    def within_dunder_or_lambda_def(node: nodes.NodeNG) -> bool:
        """Check if dunder method call is within a dunder method definition."""
        pass

    def visit_call(self, node: nodes.Call) -> None:
        """Check if method being called is an unnecessary dunder method."""
        pass