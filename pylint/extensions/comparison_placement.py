"""Checks for yoda comparisons (variable before constant)
See https://en.wikipedia.org/wiki/Yoda_conditions.
"""
from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker, utils
if TYPE_CHECKING:
    from pylint.lint import PyLinter
REVERSED_COMPS = {'<': '>', '<=': '>=', '>': '<', '>=': '<='}
COMPARISON_OPERATORS = frozenset(('==', '!=', '<', '>', '<=', '>='))

class MisplacedComparisonConstantChecker(BaseChecker):
    """Checks the placement of constants in comparisons."""
    name = 'comparison-placement'
    msgs = {'C2201': ('Comparison should be %s', 'misplaced-comparison-constant', 'Used when the constant is placed on the left side of a comparison. It is usually clearer in intent to place it in the right hand side of the comparison.', {'old_names': [('C0122', 'old-misplaced-comparison-constant')]})}
    options = ()