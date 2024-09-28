"""Check for if / assign blocks that can be rewritten with if-expressions."""
from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class ConsiderTernaryExpressionChecker(BaseChecker):
    name = 'consider_ternary_expression'
    msgs = {'W0160': ('Consider rewriting as a ternary expression', 'consider-ternary-expression', 'Multiple assign statements spread across if/else blocks can be rewritten with a single assignment and ternary expression')}