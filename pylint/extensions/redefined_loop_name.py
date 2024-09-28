"""Optional checker to warn when loop variables are overwritten in the loop's body."""
from __future__ import annotations
from astroid import nodes
from pylint import checkers
from pylint.checkers import utils
from pylint.interfaces import HIGH
from pylint.lint import PyLinter

class RedefinedLoopNameChecker(checkers.BaseChecker):
    name = 'redefined-loop-name'
    msgs = {'W2901': ('Redefining %r from loop (line %s)', 'redefined-loop-name', 'Used when a loop variable is overwritten in the loop body.')}

    def __init__(self, linter: PyLinter) -> None:
        super().__init__(linter)
        self._loop_variables: list[tuple[nodes.For, list[str], nodes.LocalsDictNodeNG]] = []