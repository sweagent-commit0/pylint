from __future__ import annotations
from typing import TYPE_CHECKING
from pylint.reporters.base_reporter import BaseReporter
if TYPE_CHECKING:
    from pylint.reporters.ureports.nodes import Section

class CollectingReporter(BaseReporter):
    """Collects messages."""
    name = 'collector'

    def __init__(self) -> None:
        super().__init__()
        self.messages = []