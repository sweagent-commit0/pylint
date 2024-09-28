"""Check for imports on private external modules and names."""
from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker, utils
from pylint.interfaces import HIGH
if TYPE_CHECKING:
    from pylint.lint.pylinter import PyLinter

class PrivateImportChecker(BaseChecker):
    name = 'import-private-name'
    msgs = {'C2701': ('Imported private %s (%s)', 'import-private-name', 'Used when a private module or object prefixed with _ is imported. PEP8 guidance on Naming Conventions states that public attributes with leading underscores should be considered private.')}

    def __init__(self, linter: PyLinter) -> None:
        BaseChecker.__init__(self, linter)
        self.all_used_type_annotations: dict[str, bool] = {}
        self.populated_annotations = False

    def _get_private_imports(self, names: list[str]) -> list[str]:
        """Returns the private names from input names by a simple string check."""
        pass

    @staticmethod
    def _name_is_private(name: str) -> bool:
        """Returns true if the name exists, starts with `_`, and if len(name) > 4
        it is not a dunder, i.e. it does not begin and end with two underscores.
        """
        pass

    def _get_type_annotation_names(self, node: nodes.Import | nodes.ImportFrom, names: list[str]) -> list[str]:
        """Removes from names any names that are used as type annotations with no other
        illegal usages.
        """
        pass

    def _populate_type_annotations(self, node: nodes.LocalsDictNodeNG, all_used_type_annotations: dict[str, bool]) -> None:
        """Adds to `all_used_type_annotations` all names ever used as a type annotation
        in the node's (nested) scopes and whether they are only used as annotation.
        """
        pass

    def _populate_type_annotations_function(self, node: nodes.FunctionDef, all_used_type_annotations: dict[str, bool]) -> None:
        """Adds all names used as type annotation in the arguments and return type of
        the function node into the dict `all_used_type_annotations`.
        """
        pass

    def _populate_type_annotations_annotation(self, node: nodes.Attribute | nodes.Subscript | nodes.Name | None, all_used_type_annotations: dict[str, bool]) -> str | None:
        """Handles the possibility of an annotation either being a Name, i.e. just type,
        or a Subscript e.g. `Optional[type]` or an Attribute, e.g. `pylint.lint.linter`.
        """
        pass

    @staticmethod
    def _assignments_call_private_name(assignments: list[nodes.AnnAssign | nodes.Assign], private_name: str) -> bool:
        """Returns True if no assignments involve accessing `private_name`."""
        pass

    @staticmethod
    def same_root_dir(node: nodes.Import | nodes.ImportFrom, import_mod_name: str) -> bool:
        """Does the node's file's path contain the base name of `import_mod_name`?"""
        pass