"""Check for use of for loops that only check for a condition."""
from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import assigned_bool, only_required_for_messages, returns_bool
from pylint.interfaces import HIGH
if TYPE_CHECKING:
    from pylint.lint.pylinter import PyLinter

class ConsiderUsingAnyOrAllChecker(BaseChecker):
    name = 'consider-using-any-or-all'
    msgs = {'C0501': ('`for` loop could be `%s`', 'consider-using-any-or-all', 'A for loop that checks for a condition and return a bool can be replaced with any or all.')}

    @staticmethod
    def _if_statement_returns_bool(if_children: list[nodes.NodeNG], node_after_loop: nodes.NodeNG) -> bool:
        """Detect for-loop, if-statement, return pattern:

        Ex:
            def any_uneven(items):
                for item in items:
                    if not item % 2 == 0:
                        return True
                return False
        """
        pass

    @staticmethod
    def _assigned_reassigned_returned(node: nodes.For, if_children: list[nodes.NodeNG], node_after_loop: nodes.NodeNG) -> bool:
        """Detect boolean-assign, for-loop, re-assign, return pattern:

        Ex:
            def check_lines(lines, max_chars):
                long_line = False
                for line in lines:
                    if len(line) > max_chars:
                        long_line = True
                    # no elif / else statement
                return long_line
        """
        pass

    @staticmethod
    def _build_suggested_string(node: nodes.For, final_return_bool: bool) -> str:
        """When a nodes.For node can be rewritten as an any/all statement, return a
        suggestion for that statement.

        'final_return_bool' is the boolean literal returned after the for loop if all
        conditions fail.
        """
        pass