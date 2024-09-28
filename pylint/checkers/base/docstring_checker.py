"""Docstring checker from the basic checker."""
from __future__ import annotations
import re
from typing import Literal
import astroid
from astroid import nodes
from pylint import interfaces
from pylint.checkers import utils
from pylint.checkers.base.basic_checker import _BasicChecker
from pylint.checkers.utils import is_overload_stub, is_property_deleter, is_property_setter
NO_REQUIRED_DOC_RGX = re.compile('^_')

class DocStringChecker(_BasicChecker):
    msgs = {'C0112': ('Empty %s docstring', 'empty-docstring', 'Used when a module, function, class or method has an empty docstring (it would be too easy ;).', {'old_names': [('W0132', 'old-empty-docstring')]}), 'C0114': ('Missing module docstring', 'missing-module-docstring', 'Used when a module has no docstring. Empty modules do not require a docstring.', {'old_names': [('C0111', 'missing-docstring')]}), 'C0115': ('Missing class docstring', 'missing-class-docstring', 'Used when a class has no docstring. Even an empty class must have a docstring.', {'old_names': [('C0111', 'missing-docstring')]}), 'C0116': ('Missing function or method docstring', 'missing-function-docstring', 'Used when a function or method has no docstring. Some special methods like __init__ do not require a docstring.', {'old_names': [('C0111', 'missing-docstring')]})}
    options = (('no-docstring-rgx', {'default': NO_REQUIRED_DOC_RGX, 'type': 'regexp', 'metavar': '<regexp>', 'help': 'Regular expression which should only match function or class names that do not require a docstring.'}), ('docstring-min-length', {'default': -1, 'type': 'int', 'metavar': '<int>', 'help': 'Minimum line length for functions/classes that require docstrings, shorter ones are exempt.'}))
    visit_asyncfunctiondef = visit_functiondef

    def _check_docstring(self, node_type: Literal['class', 'function', 'method', 'module'], node: nodes.Module | nodes.ClassDef | nodes.FunctionDef, report_missing: bool=True, confidence: interfaces.Confidence=interfaces.HIGH) -> None:
        """Check if the node has a non-empty docstring."""
        pass