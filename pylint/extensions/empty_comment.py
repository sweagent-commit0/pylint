from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseRawFileChecker
if TYPE_CHECKING:
    from pylint.lint import PyLinter

def is_line_commented(line: bytes) -> bool:
    """Checks if a `# symbol that is not part of a string was found in line."""
    pass

def comment_part_of_string(line: bytes, comment_idx: int) -> bool:
    """Checks if the symbol at comment_idx is part of a string."""
    pass

class CommentChecker(BaseRawFileChecker):
    name = 'empty-comment'
    msgs = {'R2044': ('Line with empty comment', 'empty-comment', 'Used when a # symbol appears on a line not followed by an actual comment')}
    options = ()