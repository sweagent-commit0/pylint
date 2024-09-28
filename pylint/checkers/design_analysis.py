"""Check for signs of poor design."""
from __future__ import annotations
import re
from collections import defaultdict
from collections.abc import Iterator
from typing import TYPE_CHECKING
import astroid
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import is_enum, only_required_for_messages
from pylint.typing import MessageDefinitionTuple
if TYPE_CHECKING:
    from pylint.lint import PyLinter
MSGS: dict[str, MessageDefinitionTuple] = {'R0901': ('Too many ancestors (%s/%s)', 'too-many-ancestors', 'Used when class has too many parent classes, try to reduce this to get a simpler (and so easier to use) class.'), 'R0902': ('Too many instance attributes (%s/%s)', 'too-many-instance-attributes', 'Used when class has too many instance attributes, try to reduce this to get a simpler (and so easier to use) class.'), 'R0903': ('Too few public methods (%s/%s)', 'too-few-public-methods', "Used when class has too few public methods, so be sure it's really worth it."), 'R0904': ('Too many public methods (%s/%s)', 'too-many-public-methods', 'Used when class has too many public methods, try to reduce this to get a simpler (and so easier to use) class.'), 'R0911': ('Too many return statements (%s/%s)', 'too-many-return-statements', 'Used when a function or method has too many return statement, making it hard to follow.'), 'R0912': ('Too many branches (%s/%s)', 'too-many-branches', 'Used when a function or method has too many branches, making it hard to follow.'), 'R0913': ('Too many arguments (%s/%s)', 'too-many-arguments', 'Used when a function or method takes too many arguments.'), 'R0914': ('Too many local variables (%s/%s)', 'too-many-locals', 'Used when a function or method has too many local variables.'), 'R0915': ('Too many statements (%s/%s)', 'too-many-statements', 'Used when a function or method has too many statements. You should then split it in smaller functions / methods.'), 'R0916': ('Too many boolean expressions in if statement (%s/%s)', 'too-many-boolean-expressions', 'Used when an if statement contains too many boolean expressions.'), 'R0917': ('Too many positional arguments in a function call.', 'too-many-positional', 'Will be implemented in https://github.com/pylint-dev/pylint/issues/9099,msgid/symbol pair reserved for compatibility with ruff, see https://github.com/astral-sh/ruff/issues/8946.')}
SPECIAL_OBJ = re.compile('^_{2}[a-z]+_{2}$')
DATACLASSES_DECORATORS = frozenset({'dataclass', 'attrs'})
DATACLASS_IMPORT = 'dataclasses'
ATTRS_DECORATORS = frozenset({'define', 'frozen'})
ATTRS_IMPORT = 'attrs'
TYPING_NAMEDTUPLE = 'typing.NamedTuple'
TYPING_TYPEDDICT = 'typing.TypedDict'
TYPING_EXTENSIONS_TYPEDDICT = 'typing_extensions.TypedDict'
STDLIB_CLASSES_IGNORE_ANCESTOR = frozenset(('builtins.object', 'builtins.tuple', 'builtins.dict', 'builtins.list', 'builtins.set', 'bulitins.frozenset', 'collections.ChainMap', 'collections.Counter', 'collections.OrderedDict', 'collections.UserDict', 'collections.UserList', 'collections.UserString', 'collections.defaultdict', 'collections.deque', 'collections.namedtuple', '_collections_abc.Awaitable', '_collections_abc.Coroutine', '_collections_abc.AsyncIterable', '_collections_abc.AsyncIterator', '_collections_abc.AsyncGenerator', '_collections_abc.Hashable', '_collections_abc.Iterable', '_collections_abc.Iterator', '_collections_abc.Generator', '_collections_abc.Reversible', '_collections_abc.Sized', '_collections_abc.Container', '_collections_abc.Collection', '_collections_abc.Set', '_collections_abc.MutableSet', '_collections_abc.Mapping', '_collections_abc.MutableMapping', '_collections_abc.MappingView', '_collections_abc.KeysView', '_collections_abc.ItemsView', '_collections_abc.ValuesView', '_collections_abc.Sequence', '_collections_abc.MutableSequence', '_collections_abc.ByteString', 'typing.Tuple', 'typing.List', 'typing.Dict', 'typing.Set', 'typing.FrozenSet', 'typing.Deque', 'typing.DefaultDict', 'typing.OrderedDict', 'typing.Counter', 'typing.ChainMap', 'typing.Awaitable', 'typing.Coroutine', 'typing.AsyncIterable', 'typing.AsyncIterator', 'typing.AsyncGenerator', 'typing.Iterable', 'typing.Iterator', 'typing.Generator', 'typing.Reversible', 'typing.Container', 'typing.Collection', 'typing.AbstractSet', 'typing.MutableSet', 'typing.Mapping', 'typing.MutableMapping', 'typing.Sequence', 'typing.MutableSequence', 'typing.ByteString', 'typing.MappingView', 'typing.KeysView', 'typing.ItemsView', 'typing.ValuesView', 'typing.ContextManager', 'typing.AsyncContextManager', 'typing.Hashable', 'typing.Sized', TYPING_NAMEDTUPLE, TYPING_TYPEDDICT, TYPING_EXTENSIONS_TYPEDDICT))

def _is_exempt_from_public_methods(node: astroid.ClassDef) -> bool:
    """Check if a class is exempt from too-few-public-methods."""
    pass

def _count_boolean_expressions(bool_op: nodes.BoolOp) -> int:
    """Counts the number of boolean expressions in BoolOp `bool_op` (recursive).

    example: a and (b or c or (d and e)) ==> 5 boolean expressions
    """
    pass

def _get_parents_iter(node: nodes.ClassDef, ignored_parents: frozenset[str]) -> Iterator[nodes.ClassDef]:
    """Get parents of ``node``, excluding ancestors of ``ignored_parents``.

    If we have the following inheritance diagram:

             F
            /
        D  E
         \\/
          B  C
           \\/
            A      # class A(B, C): ...

    And ``ignored_parents`` is ``{"E"}``, then this function will return
    ``{A, B, C, D}`` -- both ``E`` and its ancestors are excluded.
    """
    pass

class MisdesignChecker(BaseChecker):
    """Checker of potential misdesigns.

    Checks for sign of poor/misdesign:
    * number of methods, attributes, local variables...
    * size, complexity of functions, methods
    """
    name = 'design'
    msgs = MSGS
    options = (('max-args', {'default': 5, 'type': 'int', 'metavar': '<int>', 'help': 'Maximum number of arguments for function / method.'}), ('max-locals', {'default': 15, 'type': 'int', 'metavar': '<int>', 'help': 'Maximum number of locals for function / method body.'}), ('max-returns', {'default': 6, 'type': 'int', 'metavar': '<int>', 'help': 'Maximum number of return / yield for function / method body.'}), ('max-branches', {'default': 12, 'type': 'int', 'metavar': '<int>', 'help': 'Maximum number of branch for function / method body.'}), ('max-statements', {'default': 50, 'type': 'int', 'metavar': '<int>', 'help': 'Maximum number of statements in function / method body.'}), ('max-parents', {'default': 7, 'type': 'int', 'metavar': '<num>', 'help': 'Maximum number of parents for a class (see R0901).'}), ('ignored-parents', {'default': (), 'type': 'csv', 'metavar': '<comma separated list of class names>', 'help': 'List of qualified class names to ignore when counting class parents (see R0901)'}), ('max-attributes', {'default': 7, 'type': 'int', 'metavar': '<num>', 'help': 'Maximum number of attributes for a class (see R0902).'}), ('min-public-methods', {'default': 2, 'type': 'int', 'metavar': '<num>', 'help': 'Minimum number of public methods for a class (see R0903).'}), ('max-public-methods', {'default': 20, 'type': 'int', 'metavar': '<num>', 'help': 'Maximum number of public methods for a class (see R0904).'}), ('max-bool-expr', {'default': 5, 'type': 'int', 'metavar': '<num>', 'help': 'Maximum number of boolean expressions in an if statement (see R0916).'}), ('exclude-too-few-public-methods', {'default': [], 'type': 'regexp_csv', 'metavar': '<pattern>[,<pattern>...]', 'help': 'List of regular expressions of class ancestor names to ignore when counting public methods (see R0903)'}))

    def __init__(self, linter: PyLinter) -> None:
        super().__init__(linter)
        self._returns: list[int]
        self._branches: defaultdict[nodes.LocalsDictNodeNG, int]
        self._stmts: list[int]

    def open(self) -> None:
        """Initialize visit variables."""
        pass

    @only_required_for_messages('too-many-ancestors', 'too-many-instance-attributes', 'too-few-public-methods', 'too-many-public-methods')
    def visit_classdef(self, node: nodes.ClassDef) -> None:
        """Check size of inheritance hierarchy and number of instance attributes."""
        pass

    @only_required_for_messages('too-few-public-methods', 'too-many-public-methods')
    def leave_classdef(self, node: nodes.ClassDef) -> None:
        """Check number of public methods."""
        pass

    @only_required_for_messages('too-many-return-statements', 'too-many-branches', 'too-many-arguments', 'too-many-locals', 'too-many-statements', 'keyword-arg-before-vararg')
    def visit_functiondef(self, node: nodes.FunctionDef) -> None:
        """Check function name, docstring, arguments, redefinition,
        variable names, max locals.
        """
        pass
    visit_asyncfunctiondef = visit_functiondef

    @only_required_for_messages('too-many-return-statements', 'too-many-branches', 'too-many-arguments', 'too-many-locals', 'too-many-statements')
    def leave_functiondef(self, node: nodes.FunctionDef) -> None:
        """Most of the work is done here on close:
        checks for max returns, branch, return in __init__.
        """
        pass
    leave_asyncfunctiondef = leave_functiondef

    def visit_return(self, _: nodes.Return) -> None:
        """Count number of returns."""
        pass

    def visit_default(self, node: nodes.NodeNG) -> None:
        """Default visit method -> increments the statements counter if
        necessary.
        """
        pass

    def visit_try(self, node: nodes.Try) -> None:
        """Increments the branches counter."""
        pass

    @only_required_for_messages('too-many-boolean-expressions', 'too-many-branches')
    def visit_if(self, node: nodes.If) -> None:
        """Increments the branches counter and checks boolean expressions."""
        pass

    def _check_boolean_expressions(self, node: nodes.If) -> None:
        """Go through "if" node `node` and count its boolean expressions
        if the 'if' node test is a BoolOp node.
        """
        pass

    def visit_while(self, node: nodes.While) -> None:
        """Increments the branches counter."""
        pass
    visit_for = visit_while

    def _inc_branch(self, node: nodes.NodeNG, branchesnum: int=1) -> None:
        """Increments the branches counter."""
        pass