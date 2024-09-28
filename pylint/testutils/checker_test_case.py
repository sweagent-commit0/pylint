from __future__ import annotations
import contextlib
from collections.abc import Generator, Iterator
from typing import Any
from astroid import nodes
from pylint.constants import IS_PYPY, PY39_PLUS
from pylint.testutils.global_test_linter import linter
from pylint.testutils.output_line import MessageTest
from pylint.testutils.unittest_linter import UnittestLinter
from pylint.utils import ASTWalker

class CheckerTestCase:
    """A base testcase class for unit testing individual checker classes."""
    CHECKER_CLASS: Any
    CONFIG: dict[str, Any] = {}

    @contextlib.contextmanager
    def assertNoMessages(self) -> Iterator[None]:
        """Assert that no messages are added by the given method."""
        pass

    @contextlib.contextmanager
    def assertAddsMessages(self, *messages: MessageTest, ignore_position: bool=False) -> Generator[None, None, None]:
        """Assert that exactly the given method adds the given messages.

        The list of messages must exactly match *all* the messages added by the
        method. Additionally, we check to see whether the args in each message can
        actually be substituted into the message string.

        Using the keyword argument `ignore_position`, all checks for position
        arguments (line, col_offset, ...) will be skipped. This can be used to
        just test messages for the correct node.
        """
        pass

    def walk(self, node: nodes.NodeNG) -> None:
        """Recursive walk on the given node."""
        pass