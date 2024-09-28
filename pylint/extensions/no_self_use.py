from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import PYMETHODS, decorated_with_property, is_overload_stub, is_protocol_class, overrides_a_method
from pylint.interfaces import INFERENCE
if TYPE_CHECKING:
    from pylint.lint.pylinter import PyLinter

class NoSelfUseChecker(BaseChecker):
    name = 'no_self_use'
    msgs = {'R6301': ('Method could be a function', 'no-self-use', "Used when a method doesn't use its bound instance, and so could be written as a function.", {'old_names': [('R0201', 'old-no-self-use')]})}

    def __init__(self, linter: PyLinter) -> None:
        super().__init__(linter)
        self._first_attrs: list[str | None] = []
        self._meth_could_be_func: bool | None = None

    def visit_name(self, node: nodes.Name) -> None:
        """Check if the name handle an access to a class member
        if so, register it.
        """
        pass
    visit_asyncfunctiondef = visit_functiondef

    def _check_first_arg_for_type(self, node: nodes.FunctionDef) -> None:
        """Check the name of first argument."""
        pass

    def leave_functiondef(self, node: nodes.FunctionDef) -> None:
        """On method node, check if this method couldn't be a function.

        ignore class, static and abstract methods, initializer,
        methods overridden from a parent class.
        """
        pass
    leave_asyncfunctiondef = leave_functiondef