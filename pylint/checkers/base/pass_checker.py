from astroid import nodes
from pylint.checkers import utils
from pylint.checkers.base.basic_checker import _BasicChecker

class PassChecker(_BasicChecker):
    """Check if the pass statement is really necessary."""
    msgs = {'W0107': ('Unnecessary pass statement', 'unnecessary-pass', 'Used when a "pass" statement can be removed without affecting the behaviour of the code.')}