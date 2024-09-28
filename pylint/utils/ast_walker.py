from __future__ import annotations
import sys
import traceback
from collections import defaultdict
from collections.abc import Sequence
from typing import TYPE_CHECKING, Callable
from astroid import nodes
if TYPE_CHECKING:
    from pylint.checkers.base_checker import BaseChecker
    from pylint.lint import PyLinter
AstCallback = Callable[[nodes.NodeNG], None]

class ASTWalker:

    def __init__(self, linter: PyLinter) -> None:
        self.nbstatements = 0
        self.visit_events: defaultdict[str, list[AstCallback]] = defaultdict(list)
        self.leave_events: defaultdict[str, list[AstCallback]] = defaultdict(list)
        self.linter = linter
        self.exception_msg = False

    def add_checker(self, checker: BaseChecker) -> None:
        """Walk to the checker's dir and collect visit and leave methods."""
        pass

    def walk(self, astroid: nodes.NodeNG) -> None:
        """Call visit events of astroid checkers for the given node, recurse on
        its children, then leave events.
        """
        pass