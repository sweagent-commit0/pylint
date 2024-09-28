"""Checker for features used that are not supported by all python versions
indicated by the py-version setting.
"""
from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import only_required_for_messages, safe_infer, uninferable_final_decorators
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class UnsupportedVersionChecker(BaseChecker):
    """Checker for features that are not supported by all python versions
    indicated by the py-version setting.
    """
    name = 'unsupported_version'
    msgs = {'W2601': ('F-strings are not supported by all versions included in the py-version setting', 'using-f-string-in-unsupported-version', 'Used when the py-version set by the user is lower than 3.6 and pylint encounters an f-string.'), 'W2602': ('typing.final is not supported by all versions included in the py-version setting', 'using-final-decorator-in-unsupported-version', 'Used when the py-version set by the user is lower than 3.8 and pylint encounters a ``typing.final`` decorator.')}

    def open(self) -> None:
        """Initialize visit variables and statistics."""
        pass

    @only_required_for_messages('using-f-string-in-unsupported-version')
    def visit_joinedstr(self, node: nodes.JoinedStr) -> None:
        """Check f-strings."""
        pass

    @only_required_for_messages('using-final-decorator-in-unsupported-version')
    def visit_decorators(self, node: nodes.Decorators) -> None:
        """Check decorators."""
        pass

    def _check_typing_final(self, node: nodes.Decorators) -> None:
        """Add a message when the `typing.final` decorator is used and the
        py-version is lower than 3.8.
        """
        pass