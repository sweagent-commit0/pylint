from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import only_required_for_messages
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class ConfusingConsecutiveElifChecker(BaseChecker):
    """Checks if "elif" is used right after an indented block that finishes with "if" or
    "elif" itself.
    """
    name = 'confusing_elif'
    msgs = {'R5601': ('Consecutive elif with differing indentation level, consider creating a function to separate the inner elif', 'confusing-consecutive-elif', 'Used when an elif statement follows right after an indented block which itself ends with if or elif. It may not be obvious if the elif statement was willingly or mistakenly unindented. Extracting the indented if statement into a separate function might avoid confusion and prevent errors.')}