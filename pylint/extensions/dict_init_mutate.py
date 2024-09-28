"""Check for use of dictionary mutation after initialization."""
from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import only_required_for_messages
from pylint.interfaces import HIGH
if TYPE_CHECKING:
    from pylint.lint.pylinter import PyLinter

class DictInitMutateChecker(BaseChecker):
    name = 'dict-init-mutate'
    msgs = {'C3401': ('Declare all known key/values when initializing the dictionary.', 'dict-init-mutate', 'Dictionaries can be initialized with a single statement using dictionary literal syntax.')}

    @only_required_for_messages('dict-init-mutate')
    def visit_assign(self, node: nodes.Assign) -> None:
        """
        Detect dictionary mutation immediately after initialization.

        At this time, detecting nested mutation is not supported.
        """
        pass