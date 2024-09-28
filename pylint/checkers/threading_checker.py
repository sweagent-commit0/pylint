from __future__ import annotations
from typing import TYPE_CHECKING
from astroid import nodes
from pylint.checkers import BaseChecker
from pylint.checkers.utils import only_required_for_messages, safe_infer
if TYPE_CHECKING:
    from pylint.lint import PyLinter

class ThreadingChecker(BaseChecker):
    """Checks for threading module.

    - useless with lock - locking used in wrong way that has no effect (with threading.Lock():)
    """
    name = 'threading'
    LOCKS = frozenset(('threading.Lock', 'threading.RLock', 'threading.Condition', 'threading.Semaphore', 'threading.BoundedSemaphore'))
    msgs = {'W2101': ("'%s()' directly created in 'with' has no effect", 'useless-with-lock', 'Used when a new lock instance is created by using with statement which has no effect. Instead, an existing instance should be used to acquire lock.')}