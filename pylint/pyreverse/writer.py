"""Utilities for creating diagrams."""
from __future__ import annotations
import argparse
import itertools
import os
from collections import defaultdict
from collections.abc import Iterable
from astroid import modutils, nodes
from pylint.pyreverse.diagrams import ClassDiagram, ClassEntity, DiagramEntity, PackageDiagram, PackageEntity
from pylint.pyreverse.printer import EdgeType, NodeProperties, NodeType, Printer
from pylint.pyreverse.printer_factory import get_printer_for_filetype
from pylint.pyreverse.utils import is_exception

class DiagramWriter:
    """Base class for writing project diagrams."""

    def __init__(self, config: argparse.Namespace) -> None:
        self.config = config
        self.printer_class = get_printer_for_filetype(self.config.output_format)
        self.printer: Printer
        self.file_name = ''
        self.depth = self.config.max_color_depth
        self.available_colors = itertools.cycle(self.config.color_palette)
        self.used_colors: dict[str, str] = {}

    def write(self, diadefs: Iterable[ClassDiagram | PackageDiagram]) -> None:
        """Write files for <project> according to <diadefs>."""
        pass

    def write_packages(self, diagram: PackageDiagram) -> None:
        """Write a package diagram."""
        pass

    def write_classes(self, diagram: ClassDiagram) -> None:
        """Write a class diagram."""
        pass

    def set_printer(self, file_name: str, basename: str) -> None:
        """Set printer."""
        pass

    def get_package_properties(self, obj: PackageEntity) -> NodeProperties:
        """Get label and shape for packages."""
        pass

    def get_class_properties(self, obj: ClassEntity) -> NodeProperties:
        """Get label and shape for classes."""
        pass

    def get_shape_color(self, obj: DiagramEntity) -> str:
        """Get shape color."""
        pass

    def save(self) -> None:
        """Write to disk."""
        pass