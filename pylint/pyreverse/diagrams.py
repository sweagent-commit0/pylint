"""Diagram objects."""
from __future__ import annotations
from collections.abc import Iterable
from typing import Any
import astroid
from astroid import nodes, util
from pylint.checkers.utils import decorated_with_property, in_type_checking_block
from pylint.pyreverse.utils import FilterMixIn

class Figure:
    """Base class for counter handling."""

    def __init__(self) -> None:
        self.fig_id: str = ''

class Relationship(Figure):
    """A relationship from an object in the diagram to another."""

    def __init__(self, from_object: DiagramEntity, to_object: DiagramEntity, relation_type: str, name: str | None=None):
        super().__init__()
        self.from_object = from_object
        self.to_object = to_object
        self.type = relation_type
        self.name = name

class DiagramEntity(Figure):
    """A diagram object, i.e. a label associated to an astroid node."""
    default_shape = ''

    def __init__(self, title: str='No name', node: nodes.NodeNG | None=None) -> None:
        super().__init__()
        self.title = title
        self.node: nodes.NodeNG = node or nodes.NodeNG(lineno=None, col_offset=None, end_lineno=None, end_col_offset=None, parent=None)
        self.shape = self.default_shape

class PackageEntity(DiagramEntity):
    """A diagram object representing a package."""
    default_shape = 'package'

class ClassEntity(DiagramEntity):
    """A diagram object representing a class."""
    default_shape = 'class'

    def __init__(self, title: str, node: nodes.ClassDef) -> None:
        super().__init__(title=title, node=node)
        self.attrs: list[str] = []
        self.methods: list[nodes.FunctionDef] = []

class ClassDiagram(Figure, FilterMixIn):
    """Main class diagram handling."""
    TYPE = 'class'

    def __init__(self, title: str, mode: str) -> None:
        FilterMixIn.__init__(self, mode)
        Figure.__init__(self)
        self.title = title
        self.objects: list[Any] = []
        self.relationships: dict[str, list[Relationship]] = {}
        self._nodes: dict[nodes.NodeNG, DiagramEntity] = {}

    def add_relationship(self, from_object: DiagramEntity, to_object: DiagramEntity, relation_type: str, name: str | None=None) -> None:
        """Create a relationship."""
        pass

    def get_relationship(self, from_object: DiagramEntity, relation_type: str) -> Relationship:
        """Return a relationship or None."""
        pass

    def get_attrs(self, node: nodes.ClassDef) -> list[str]:
        """Return visible attributes, possibly with class name."""
        pass

    def get_methods(self, node: nodes.ClassDef) -> list[nodes.FunctionDef]:
        """Return visible methods."""
        pass

    def add_object(self, title: str, node: nodes.ClassDef) -> None:
        """Create a diagram object."""
        pass

    def class_names(self, nodes_lst: Iterable[nodes.NodeNG]) -> list[str]:
        """Return class names if needed in diagram."""
        pass

    def has_node(self, node: nodes.NodeNG) -> bool:
        """Return true if the given node is included in the diagram."""
        pass

    def object_from_node(self, node: nodes.NodeNG) -> DiagramEntity:
        """Return the diagram object mapped to node."""
        pass

    def classes(self) -> list[ClassEntity]:
        """Return all class nodes in the diagram."""
        pass

    def classe(self, name: str) -> ClassEntity:
        """Return a class by its name, raise KeyError if not found."""
        pass

    def extract_relationships(self) -> None:
        """Extract relationships between nodes in the diagram."""
        pass

class PackageDiagram(ClassDiagram):
    """Package diagram handling."""
    TYPE = 'package'

    def modules(self) -> list[PackageEntity]:
        """Return all module nodes in the diagram."""
        pass

    def module(self, name: str) -> PackageEntity:
        """Return a module by its name, raise KeyError if not found."""
        pass

    def add_object(self, title: str, node: nodes.Module) -> None:
        """Create a diagram object."""
        pass

    def get_module(self, name: str, node: nodes.Module) -> PackageEntity:
        """Return a module by its name, looking also for relative imports;
        raise KeyError if not found.
        """
        pass

    def add_from_depend(self, node: nodes.ImportFrom, from_module: str) -> None:
        """Add dependencies created by from-imports."""
        pass

    def extract_relationships(self) -> None:
        """Extract relationships between nodes in the diagram."""
        pass