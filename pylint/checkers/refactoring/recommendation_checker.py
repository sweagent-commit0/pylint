from __future__ import annotations
import astroid
from astroid import nodes
from pylint import checkers
from pylint.checkers import utils
from pylint.interfaces import HIGH, INFERENCE

class RecommendationChecker(checkers.BaseChecker):
    name = 'refactoring'
    msgs = {'C0200': ('Consider using enumerate instead of iterating with range and len', 'consider-using-enumerate', 'Emitted when code that iterates with range and len is encountered. Such code can be simplified by using the enumerate builtin.'), 'C0201': ('Consider iterating the dictionary directly instead of calling .keys()', 'consider-iterating-dictionary', 'Emitted when the keys of a dictionary are iterated through the ``.keys()`` method or when ``.keys()`` is used for a membership check. It is enough to iterate through the dictionary itself, ``for key in dictionary``. For membership checks, ``if key in dictionary`` is faster.'), 'C0206': ('Consider iterating with .items()', 'consider-using-dict-items', 'Emitted when iterating over the keys of a dictionary and accessing the value by index lookup. Both the key and value can be accessed by iterating using the .items() method of the dictionary instead.'), 'C0207': ('Use %s instead', 'use-maxsplit-arg', 'Emitted when accessing only the first or last element of str.split(). The first and last element can be accessed by using str.split(sep, maxsplit=1)[0] or str.rsplit(sep, maxsplit=1)[-1] instead.'), 'C0208': ('Use a sequence type when iterating over values', 'use-sequence-for-iteration', 'When iterating over values, sequence types (e.g., ``lists``, ``tuples``, ``ranges``) are more efficient than ``sets``.'), 'C0209': ('Formatting a regular string which could be an f-string', 'consider-using-f-string', 'Used when we detect a string that is being formatted with format() or % which could potentially be an f-string. The use of f-strings is preferred. Requires Python 3.6 and ``py-version >= 3.6``.')}

    def _check_use_maxsplit_arg(self, node: nodes.Call) -> None:
        """Add message when accessing first or last elements of a str.split() or
        str.rsplit().
        """
        pass

    def _check_consider_using_enumerate(self, node: nodes.For) -> None:
        """Emit a convention whenever range and len are used for indexing."""
        pass

    def _check_consider_using_dict_items(self, node: nodes.For) -> None:
        """Add message when accessing dict values by index lookup."""
        pass

    def _check_consider_using_dict_items_comprehension(self, node: nodes.Comprehension) -> None:
        """Add message when accessing dict values by index lookup."""
        pass

    def _check_use_sequence_for_iteration(self, node: nodes.For | nodes.Comprehension) -> None:
        """Check if code iterates over an in-place defined set.

        Sets using `*` are not considered in-place.
        """
        pass

    def _detect_replacable_format_call(self, node: nodes.Const) -> None:
        """Check whether a string is used in a call to format() or '%' and whether it
        can be replaced by an f-string.
        """
        pass