from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.interfaces import HIGH
if TYPE_CHECKING:
    from pylint.lint import PyLinter
COMPARISON_OP = frozenset(('<', '<=', '>', '>=', '!=', '=='))
IDENTITY_OP = frozenset(('is', 'is not'))
MEMBERSHIP_OP = frozenset(('in', 'not in'))

class BadChainedComparisonChecker(BaseChecker):
    """Checks for unintentional usage of chained comparison."""
    name = 'bad-chained-comparison'
    msgs = {'W3601': ('Suspicious %s-part chained comparison using semantically incompatible operators (%s)', 'bad-chained-comparison', 'Used when there is a chained comparison where one expression is part of two comparisons that belong to different semantic groups ("<" does not mean the same thing as "is", chaining them in "0 < x is None" is probably a mistake).')}