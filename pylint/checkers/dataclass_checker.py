"""Dataclass checkers for Python code."""
from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from astroid.brain.brain_dataclasses import DATACLASS_MODULES
from pylint.checkers import BaseChecker, utils
from pylint.interfaces import INFERENCE
if TYPE_CHECKING:
    from pylint.lint import PyLinter

def _is_dataclasses_module(node: nodes.Module) -> bool:
    """Utility function to check if node is from dataclasses_module."""
    pass

def _check_name_or_attrname_eq_to(node: nodes.Name | nodes.Attribute, check_with: str) -> bool:
    """Utility function to check either a Name/Attribute node's name/attrname with a
    given string.
    """
    pass

class DataclassChecker(BaseChecker):
    """Checker that detects invalid or problematic usage in dataclasses.

    Checks for
    * invalid-field-call
    """
    name = 'dataclass'
    msgs = {'E3701': ('Invalid usage of field(), %s', 'invalid-field-call', 'The dataclasses.field() specifier should only be used as the value of an assignment within a dataclass, or within the make_dataclass() function.')}

    def _check_invalid_field_call(self, node: nodes.Call) -> None:
        """Checks for correct usage of the dataclasses.field() specifier in
        dataclasses or within the make_dataclass() function.

        Emits message
        when field() is detected to be used outside a class decorated with
        @dataclass decorator and outside make_dataclass() function, or when it
        is used improperly within a dataclass.
        """
        pass

    def _check_invalid_field_call_within_call(self, node: nodes.Call, scope_node: nodes.Call) -> None:
        """Checks for special case where calling field is valid as an argument of the
        make_dataclass() function.
        """
        pass