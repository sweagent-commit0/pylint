from __future__ import annotations
import functools
from collections.abc import Callable
from typing import Any
from pylint.testutils.checker_test_case import CheckerTestCase

def set_config(**kwargs: Any) -> Callable[[Callable[..., None]], Callable[..., None]]:
    """Decorator for setting an option on the linter.

    Passing the args and kwargs back to the test function itself
    allows this decorator to be used on parameterized test cases.
    """
    pass