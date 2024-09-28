from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import is_none, node_type, only_required_for_messages
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class MultipleTypesChecker(BaseChecker):
    """Checks for variable type redefinition (NoneType excepted).

    At a function, method, class or module scope

    This rule could be improved:

    - Currently, if an attribute is set to different types in 2 methods of a
      same class, it won't be detected (see functional test)
    - One could improve the support for inference on assignment with tuples,
      ifexpr, etc. Also, it would be great to have support for inference on
      str.split()
    """
    name = 'multiple_types'
    msgs = {'R0204': ('Redefinition of %s type from %s to %s', 'redefined-variable-type', 'Used when the type of a variable changes inside a method or a function.')}
    visit_functiondef = visit_asyncfunctiondef = visit_classdef
    leave_functiondef = leave_asyncfunctiondef = leave_module = leave_classdef