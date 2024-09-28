from __future__ import annotations
import collections
from collections import defaultdict
from typing import cast
from pylint import checkers, exceptions
from pylint.reporters.ureports.nodes import Section, Table
from pylint.typing import MessageTypesFullName
from pylint.utils import LinterStats

def report_total_messages_stats(sect: Section, stats: LinterStats, previous_stats: LinterStats | None) -> None:
    """Make total errors / warnings report."""
    pass

def report_messages_stats(sect: Section, stats: LinterStats, _: LinterStats | None) -> None:
    """Make messages type report."""
    pass

def report_messages_by_module_stats(sect: Section, stats: LinterStats, _: LinterStats | None) -> None:
    """Make errors / warnings by modules report."""
    pass