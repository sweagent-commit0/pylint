"""Basic Error checker from the basic checker."""
from __future__ import annotations
import itertools
from collections.abc import Iterator
from typing import Any
import astroid
from astroid import nodes
from astroid.typing import InferenceResult
from pylint.checkers import utils
from pylint.checkers.base.basic_checker import _BasicChecker
from pylint.checkers.utils import infer_all
from pylint.interfaces import HIGH
ABC_METACLASSES = {'_py_abc.ABCMeta', 'abc.ABCMeta'}
REDEFINABLE_METHODS = frozenset(('__module__',))
TYPING_FORWARD_REF_QNAME = 'typing.ForwardRef'

def _get_break_loop_node(break_node: nodes.Break) -> nodes.For | nodes.While | None:
    """Returns the loop node that holds the break node in arguments.

    Args:
        break_node (astroid.Break): the break node of interest.

    Returns:
        astroid.For or astroid.While: the loop node holding the break node.
    """
    pass

def _loop_exits_early(loop: nodes.For | nodes.While) -> bool:
    """Returns true if a loop may end with a break statement.

    Args:
        loop (astroid.For, astroid.While): the loop node inspected.

    Returns:
        bool: True if the loop may end with a break statement, False otherwise.
    """
    pass

def _has_abstract_methods(node: nodes.ClassDef) -> bool:
    """Determine if the given `node` has abstract methods.

    The methods should be made abstract by decorating them
    with `abc` decorators.
    """
    pass

def redefined_by_decorator(node: nodes.FunctionDef) -> bool:
    """Return True if the object is a method redefined via decorator.

    For example:
        @property
        def x(self): return self._x
        @x.setter
        def x(self, value): self._x = value
    """
    pass

class BasicErrorChecker(_BasicChecker):
    msgs = {'E0100': ('__init__ method is a generator', 'init-is-generator', 'Used when the special class method __init__ is turned into a generator by a yield in its body.'), 'E0101': ('Explicit return in __init__', 'return-in-init', 'Used when the special class method __init__ has an explicit return value.'), 'E0102': ('%s already defined line %s', 'function-redefined', 'Used when a function / class / method is redefined.'), 'E0103': ('%r not properly in loop', 'not-in-loop', 'Used when break or continue keywords are used outside a loop.'), 'E0104': ('Return outside function', 'return-outside-function', 'Used when a "return" statement is found outside a function or method.'), 'E0105': ('Yield outside function', 'yield-outside-function', 'Used when a "yield" statement is found outside a function or method.'), 'E0106': ('Return with argument inside generator', 'return-arg-in-generator', 'Used when a "return" statement with an argument is found in a generator function or method (e.g. with some "yield" statements).', {'maxversion': (3, 3)}), 'E0107': ('Use of the non-existent %s operator', 'nonexistent-operator', "Used when you attempt to use the C-style pre-increment or pre-decrement operator -- and ++, which doesn't exist in Python."), 'E0108': ('Duplicate argument name %s in function definition', 'duplicate-argument-name', 'Duplicate argument names in function definitions are syntax errors.'), 'E0110': ('Abstract class %r with abstract methods instantiated', 'abstract-class-instantiated', 'Used when an abstract class with `abc.ABCMeta` as metaclass has abstract methods and is instantiated.'), 'W0120': ('Else clause on loop without a break statement, remove the else and de-indent all the code inside it', 'useless-else-on-loop', 'Loops should only have an else clause if they can exit early with a break statement, otherwise the statements under else should be on the same scope as the loop itself.'), 'E0112': ('More than one starred expression in assignment', 'too-many-star-expressions', 'Emitted when there are more than one starred expressions (`*x`) in an assignment. This is a SyntaxError.'), 'E0113': ('Starred assignment target must be in a list or tuple', 'invalid-star-assignment-target', 'Emitted when a star expression is used as a starred assignment target.'), 'E0114': ('Can use starred expression only in assignment target', 'star-needs-assignment-target', 'Emitted when a star expression is not used in an assignment target.'), 'E0115': ('Name %r is nonlocal and global', 'nonlocal-and-global', 'Emitted when a name is both nonlocal and global.'), 'E0116': ("'continue' not supported inside 'finally' clause", 'continue-in-finally', 'Emitted when the `continue` keyword is found inside a finally clause, which is a SyntaxError.'), 'E0117': ('nonlocal name %s found without binding', 'nonlocal-without-binding', 'Emitted when a nonlocal variable does not have an attached name somewhere in the parent scopes'), 'E0118': ('Name %r is used prior to global declaration', 'used-prior-global-declaration', 'Emitted when a name is used prior a global declaration, which results in an error since Python 3.6.', {'minversion': (3, 6)})}

    @utils.only_required_for_messages('star-needs-assignment-target')
    def visit_starred(self, node: nodes.Starred) -> None:
        """Check that a Starred expression is used in an assignment target."""
        pass
    visit_asyncfunctiondef = visit_functiondef

    def _check_nonlocal_and_global(self, node: nodes.FunctionDef) -> None:
        """Check that a name is both nonlocal and global."""
        pass

    @utils.only_required_for_messages('nonexistent-operator')
    def visit_unaryop(self, node: nodes.UnaryOp) -> None:
        """Check use of the non-existent ++ and -- operators."""
        pass

    @utils.only_required_for_messages('abstract-class-instantiated')
    def visit_call(self, node: nodes.Call) -> None:
        """Check instantiating abstract class with
        abc.ABCMeta as metaclass.
        """
        pass

    def _check_else_on_loop(self, node: nodes.For | nodes.While) -> None:
        """Check that any loop with an else clause has a break statement."""
        pass

    def _check_in_loop(self, node: nodes.Continue | nodes.Break, node_name: str) -> None:
        """Check that a node is inside a for or while loop."""
        pass

    def _check_redefinition(self, redeftype: str, node: nodes.Call | nodes.FunctionDef) -> None:
        """Check for redefinition of a function / method / class name."""
        pass