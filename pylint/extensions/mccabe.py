"""Module to add McCabe checker class for pylint."""
from __future__ import annotations
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, TypeVar, Union
from astroid import nodes
from mccabe import PathGraph as Mccabe_PathGraph
from mccabe import PathGraphingAstVisitor as Mccabe_PathGraphingAstVisitor
from pylint import checkers
from pylint.checkers.utils import only_required_for_messages
from pylint.interfaces import HIGH
if TYPE_CHECKING:
    from pylint.lint import PyLinter
_StatementNodes = Union[nodes.Assert, nodes.Assign, nodes.AugAssign, nodes.Delete, nodes.Raise, nodes.Yield, nodes.Import, nodes.Call, nodes.Subscript, nodes.Pass, nodes.Continue, nodes.Break, nodes.Global, nodes.Return, nodes.Expr, nodes.Await]
_SubGraphNodes = Union[nodes.If, nodes.Try, nodes.For, nodes.While]
_AppendableNodeT = TypeVar('_AppendableNodeT', bound=Union[_StatementNodes, nodes.While, nodes.FunctionDef])

class PathGraph(Mccabe_PathGraph):

    def __init__(self, node: _SubGraphNodes | nodes.FunctionDef):
        super().__init__(name='', entity='', lineno=1)
        self.root = node

class PathGraphingAstVisitor(Mccabe_PathGraphingAstVisitor):

    def __init__(self) -> None:
        super().__init__()
        self._bottom_counter = 0
        self.graph: PathGraph | None = None
    visitAsyncFunctionDef = visitFunctionDef
    visitAssert = visitAssign = visitAugAssign = visitDelete = visitRaise = visitYield = visitImport = visitCall = visitSubscript = visitPass = visitContinue = visitBreak = visitGlobal = visitReturn = visitExpr = visitAwait = visitSimpleStatement
    visitAsyncWith = visitWith

    def _subgraph(self, node: _SubGraphNodes, name: str, extra_blocks: Sequence[nodes.ExceptHandler]=()) -> None:
        """Create the subgraphs representing any `if` and `for` statements."""
        pass

    def _subgraph_parse(self, node: _SubGraphNodes, pathnode: _SubGraphNodes, extra_blocks: Sequence[nodes.ExceptHandler]) -> None:
        """Parse the body and any `else` block of `if` and `for` statements."""
        pass

class McCabeMethodChecker(checkers.BaseChecker):
    """Checks McCabe complexity cyclomatic threshold in methods and functions
    to validate a too complex code.
    """
    name = 'design'
    msgs = {'R1260': ('%s is too complex. The McCabe rating is %d', 'too-complex', 'Used when a method or function is too complex based on McCabe Complexity Cyclomatic')}
    options = (('max-complexity', {'default': 10, 'type': 'int', 'metavar': '<int>', 'help': 'McCabe complexity cyclomatic threshold'}),)

    @only_required_for_messages('too-complex')
    def visit_module(self, node: nodes.Module) -> None:
        """Visit an astroid.Module node to check too complex rating and
        add message if is greater than max_complexity stored from options.
        """
        pass