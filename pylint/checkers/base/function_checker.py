"""Function checker for Python code."""
from __future__ import annotations
from itertools import chain
from astroid import nodes
from pylint.checkers import utils
from pylint.checkers.base.basic_checker import _BasicChecker

class FunctionChecker(_BasicChecker):
    """Check if a function definition handles possible side effects."""
    msgs = {'W0135': ('The context used in function %r will not be exited.', 'contextmanager-generator-missing-cleanup', 'Used when a contextmanager is used inside a generator function and the cleanup is not handled.')}

    def _check_contextmanager_generator_missing_cleanup(self, node: nodes.FunctionDef) -> None:
        """Check a FunctionDef to find if it is a generator
        that uses a contextmanager internally.

        If it is, check if the contextmanager is properly cleaned up. Otherwise, add message.

        :param node: FunctionDef node to check
        :type node: nodes.FunctionDef
        """
        pass

    @staticmethod
    def _node_fails_contextmanager_cleanup(node: nodes.FunctionDef, yield_nodes: list[nodes.Yield]) -> bool:
        """Check if a node fails contextmanager cleanup.

        Current checks for a contextmanager:
            - only if the context manager yields a non-constant value
            - only if the context manager lacks a finally, or does not catch GeneratorExit
            - only if some statement follows the yield, some manually cleanup happens

        :param node: Node to check
        :type node: nodes.FunctionDef
        :return: True if fails, False otherwise
        :param yield_nodes: List of Yield nodes in the function body
        :type yield_nodes: list[nodes.Yield]
        :rtype: bool
        """
        pass