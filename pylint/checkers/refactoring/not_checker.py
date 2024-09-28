import astroid
from astroid import nodes
from pylint import checkers
from pylint.checkers import utils

class NotChecker(checkers.BaseChecker):
    """Checks for too many not in comparison expressions.

    - "not not" should trigger a warning
    - "not" followed by a comparison should trigger a warning
    """
    msgs = {'C0117': ('Consider changing "%s" to "%s"', 'unnecessary-negation', 'Used when a boolean expression contains an unneeded negation, e.g. when two negation operators cancel each other out.', {'old_names': [('C0113', 'unneeded-not')]})}
    name = 'refactoring'
    reverse_op = {'<': '>=', '<=': '>', '>': '<=', '>=': '<', '==': '!=', '!=': '==', 'in': 'not in', 'is': 'is not'}
    skipped_nodes = (nodes.Set,)
    skipped_classnames = [f'builtins.{qname}' for qname in ('set', 'frozenset')]