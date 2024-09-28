"""This is the remnant of the python3 checker.

It was removed because the transition from python 2 to python3 is
behind us, but some checks are still useful in python3 after all.
See https://github.com/pylint-dev/pylint/issues/5025
"""
from astroid import nodes
from pylint import checkers, interfaces
from pylint.checkers import utils
from pylint.lint import PyLinter

class EqWithoutHash(checkers.BaseChecker):
    name = 'eq-without-hash'
    msgs = {'W1641': ('Implementing __eq__ without also implementing __hash__', 'eq-without-hash', 'Used when a class implements __eq__ but not __hash__. Objects get None as their default __hash__ implementation if they also implement __eq__.')}