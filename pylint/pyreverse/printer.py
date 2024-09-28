"""Base class defining the interface for a printer."""
from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import NamedTuple
from astroid import nodes
from pylint.pyreverse.utils import get_annotation_label

class NodeType(Enum):
    CLASS = 'class'
    PACKAGE = 'package'

class EdgeType(Enum):
    INHERITS = 'inherits'
    ASSOCIATION = 'association'
    AGGREGATION = 'aggregation'
    USES = 'uses'
    TYPE_DEPENDENCY = 'type_dependency'

class Layout(Enum):
    LEFT_TO_RIGHT = 'LR'
    RIGHT_TO_LEFT = 'RL'
    TOP_TO_BOTTOM = 'TB'
    BOTTOM_TO_TOP = 'BT'

class NodeProperties(NamedTuple):
    label: str
    attrs: list[str] | None = None
    methods: list[nodes.FunctionDef] | None = None
    color: str | None = None
    fontcolor: str | None = None

class Printer(ABC):
    """Base class defining the interface for a printer."""

    def __init__(self, title: str, layout: Layout | None=None, use_automatic_namespace: bool | None=None) -> None:
        self.title: str = title
        self.layout = layout
        self.use_automatic_namespace = use_automatic_namespace
        self.lines: list[str] = []
        self._indent = ''
        self._open_graph()

    def _inc_indent(self) -> None:
        """Increment indentation."""
        pass

    def _dec_indent(self) -> None:
        """Decrement indentation."""
        pass

    @abstractmethod
    def _open_graph(self) -> None:
        """Emit the header lines, i.e. all boilerplate code that defines things like
        layout etc.
        """
        pass

    @abstractmethod
    def emit_node(self, name: str, type_: NodeType, properties: NodeProperties | None=None) -> None:
        """Create a new node.

        Nodes can be classes, packages, participants etc.
        """
        pass

    @abstractmethod
    def emit_edge(self, from_node: str, to_node: str, type_: EdgeType, label: str | None=None) -> None:
        """Create an edge from one node to another to display relationships."""
        pass

    def generate(self, outputfile: str) -> None:
        """Generate and save the final outputfile."""
        pass

    @abstractmethod
    def _close_graph(self) -> None:
        """Emit the lines needed to properly close the graph."""
        pass