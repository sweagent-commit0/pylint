"""Generic classes/functions for pyreverse core/extensions."""
from __future__ import annotations
import os
import re
import shutil
import subprocess
import sys
from typing import TYPE_CHECKING, Any, Callable, Optional, Tuple, Union
import astroid
from astroid import nodes
from astroid.typing import InferenceResult
if TYPE_CHECKING:
    from pylint.pyreverse.diagrams import ClassDiagram, PackageDiagram
    _CallbackT = Callable[[nodes.NodeNG], Union[Tuple[ClassDiagram], Tuple[PackageDiagram, ClassDiagram], None]]
    _CallbackTupleT = Tuple[Optional[_CallbackT], Optional[_CallbackT]]
RCFILE = '.pyreverserc'

def get_default_options() -> list[str]:
    """Read config file and return list of options."""
    pass

def insert_default_options() -> None:
    """Insert default options to sys.argv."""
    pass
SPECIAL = re.compile('^__([^\\W_]_*)+__$')
PRIVATE = re.compile('^__(_*[^\\W_])+_?$')
PROTECTED = re.compile('^_\\w*$')

def get_visibility(name: str) -> str:
    """Return the visibility from a name: public, protected, private or special."""
    pass
_SPECIAL = 2
_PROTECTED = 4
_PRIVATE = 8
MODES = {'ALL': 0, 'PUB_ONLY': _SPECIAL + _PROTECTED + _PRIVATE, 'SPECIAL': _SPECIAL, 'OTHER': _PROTECTED + _PRIVATE}
VIS_MOD = {'special': _SPECIAL, 'protected': _PROTECTED, 'private': _PRIVATE, 'public': 0}

class FilterMixIn:
    """Filter nodes according to a mode and nodes' visibility."""

    def __init__(self, mode: str) -> None:
        """Init filter modes."""
        __mode = 0
        for nummod in mode.split('+'):
            try:
                __mode += MODES[nummod]
            except KeyError as ex:
                print(f'Unknown filter mode {ex}', file=sys.stderr)
        self.__mode = __mode

    def show_attr(self, node: nodes.NodeNG | str) -> bool:
        """Return true if the node should be treated."""
        pass

class LocalsVisitor:
    """Visit a project by traversing the locals dictionary.

    * visit_<class name> on entering a node, where class name is the class of
    the node in lower case

    * leave_<class name> on leaving a node, where class name is the class of
    the node in lower case
    """

    def __init__(self) -> None:
        self._cache: dict[type[nodes.NodeNG], _CallbackTupleT] = {}
        self._visited: set[nodes.NodeNG] = set()

    def get_callbacks(self, node: nodes.NodeNG) -> _CallbackTupleT:
        """Get callbacks from handler for the visited node."""
        pass

    def visit(self, node: nodes.NodeNG) -> Any:
        """Launch the visit starting from the given node."""
        pass

def get_annotation(node: nodes.AssignAttr | nodes.AssignName) -> nodes.Name | nodes.Subscript | None:
    """Return the annotation for `node`."""
    pass

def infer_node(node: nodes.AssignAttr | nodes.AssignName) -> set[InferenceResult]:
    """Return a set containing the node annotation if it exists
    otherwise return a set of the inferred types using the NodeNG.infer method.
    """
    pass

def check_graphviz_availability() -> None:
    """Check if the ``dot`` command is available on the machine.

    This is needed if image output is desired and ``dot`` is used to convert
    from *.dot or *.gv into the final output format.
    """
    pass

def check_if_graphviz_supports_format(output_format: str) -> None:
    """Check if the ``dot`` command supports the requested output format.

    This is needed if image output is desired and ``dot`` is used to convert
    from *.gv into the final output format.
    """
    pass