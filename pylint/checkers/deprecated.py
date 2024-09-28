"""Checker mixin for deprecated functionality."""
from __future__ import annotations
from collections.abc import Container, Iterable
from itertools import chain
import astroid
from astroid import nodes
from astroid.bases import Instance
from pylint.checkers import utils
from pylint.checkers.base_checker import BaseChecker
from pylint.checkers.utils import get_import_name, infer_all, safe_infer
from pylint.interfaces import INFERENCE
from pylint.typing import MessageDefinitionTuple
ACCEPTABLE_NODES = (astroid.BoundMethod, astroid.UnboundMethod, nodes.FunctionDef, nodes.ClassDef, astroid.Attribute)

class DeprecatedMixin(BaseChecker):
    """A mixin implementing logic for checking deprecated symbols.

    A class implementing mixin must define "deprecated-method" Message.
    """
    DEPRECATED_ATTRIBUTE_MESSAGE: dict[str, MessageDefinitionTuple] = {'W4906': ('Using deprecated attribute %r', 'deprecated-attribute', 'The attribute is marked as deprecated and will be removed in the future.', {'shared': True})}
    DEPRECATED_MODULE_MESSAGE: dict[str, MessageDefinitionTuple] = {'W4901': ('Deprecated module %r', 'deprecated-module', 'A module marked as deprecated is imported.', {'old_names': [('W0402', 'old-deprecated-module')], 'shared': True})}
    DEPRECATED_METHOD_MESSAGE: dict[str, MessageDefinitionTuple] = {'W4902': ('Using deprecated method %s()', 'deprecated-method', 'The method is marked as deprecated and will be removed in the future.', {'old_names': [('W1505', 'old-deprecated-method')], 'shared': True})}
    DEPRECATED_ARGUMENT_MESSAGE: dict[str, MessageDefinitionTuple] = {'W4903': ('Using deprecated argument %s of method %s()', 'deprecated-argument', 'The argument is marked as deprecated and will be removed in the future.', {'old_names': [('W1511', 'old-deprecated-argument')], 'shared': True})}
    DEPRECATED_CLASS_MESSAGE: dict[str, MessageDefinitionTuple] = {'W4904': ('Using deprecated class %s of module %s', 'deprecated-class', 'The class is marked as deprecated and will be removed in the future.', {'old_names': [('W1512', 'old-deprecated-class')], 'shared': True})}
    DEPRECATED_DECORATOR_MESSAGE: dict[str, MessageDefinitionTuple] = {'W4905': ('Using deprecated decorator %s()', 'deprecated-decorator', 'The decorator is marked as deprecated and will be removed in the future.', {'old_names': [('W1513', 'old-deprecated-decorator')], 'shared': True})}

    @utils.only_required_for_messages('deprecated-attribute')
    def visit_attribute(self, node: astroid.Attribute) -> None:
        """Called when an `astroid.Attribute` node is visited."""
        pass

    @utils.only_required_for_messages('deprecated-method', 'deprecated-argument', 'deprecated-class')
    def visit_call(self, node: nodes.Call) -> None:
        """Called when a :class:`nodes.Call` node is visited."""
        pass

    @utils.only_required_for_messages('deprecated-module', 'deprecated-class')
    def visit_import(self, node: nodes.Import) -> None:
        """Triggered when an import statement is seen."""
        pass

    def deprecated_decorators(self) -> Iterable[str]:
        """Callback returning the deprecated decorators.

        Returns:
            collections.abc.Container of deprecated decorator names.
        """
        pass

    @utils.only_required_for_messages('deprecated-decorator')
    def visit_decorators(self, node: nodes.Decorators) -> None:
        """Triggered when a decorator statement is seen."""
        pass

    @utils.only_required_for_messages('deprecated-module', 'deprecated-class')
    def visit_importfrom(self, node: nodes.ImportFrom) -> None:
        """Triggered when a from statement is seen."""
        pass

    def deprecated_methods(self) -> Container[str]:
        """Callback returning the deprecated methods/functions.

        Returns:
            collections.abc.Container of deprecated function/method names.
        """
        pass

    def deprecated_arguments(self, method: str) -> Iterable[tuple[int | None, str]]:
        """Callback returning the deprecated arguments of method/function.

        Args:
            method (str): name of function/method checked for deprecated arguments

        Returns:
            collections.abc.Iterable in form:
                ((POSITION1, PARAM1), (POSITION2: PARAM2) ...)
            where
                * POSITIONX - position of deprecated argument PARAMX in function definition.
                  If argument is keyword-only, POSITIONX should be None.
                * PARAMX - name of the deprecated argument.
            E.g. suppose function:

            .. code-block:: python
                def bar(arg1, arg2, arg3, arg4, arg5='spam')

            with deprecated arguments `arg2` and `arg4`. `deprecated_arguments` should return:

            .. code-block:: python
                ((1, 'arg2'), (3, 'arg4'))
        """
        pass

    def deprecated_modules(self) -> Iterable[str]:
        """Callback returning the deprecated modules.

        Returns:
            collections.abc.Container of deprecated module names.
        """
        pass

    def deprecated_classes(self, module: str) -> Iterable[str]:
        """Callback returning the deprecated classes of module.

        Args:
            module (str): name of module checked for deprecated classes

        Returns:
            collections.abc.Container of deprecated class names.
        """
        pass

    def deprecated_attributes(self) -> Iterable[str]:
        """Callback returning the deprecated attributes."""
        pass

    def check_deprecated_attribute(self, node: astroid.Attribute) -> None:
        """Checks if the attribute is deprecated."""
        pass

    def check_deprecated_module(self, node: nodes.Import, mod_path: str | None) -> None:
        """Checks if the module is deprecated."""
        pass

    def check_deprecated_method(self, node: nodes.Call, inferred: nodes.NodeNG) -> None:
        """Executes the checker for the given node.

        This method should be called from the checker implementing this mixin.
        """
        pass

    def check_deprecated_class(self, node: nodes.NodeNG, mod_name: str, class_names: Iterable[str]) -> None:
        """Checks if the class is deprecated."""
        pass

    def check_deprecated_class_in_call(self, node: nodes.Call) -> None:
        """Checks if call the deprecated class."""
        pass