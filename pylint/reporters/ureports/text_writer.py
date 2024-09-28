"""Text formatting drivers for ureports."""
from __future__ import annotations
from typing import TYPE_CHECKING
from pylint.reporters.ureports.base_writer import BaseWriter
if TYPE_CHECKING:
    from pylint.reporters.ureports.nodes import EvaluationSection, Paragraph, Section, Table, Text, Title, VerbatimText
TITLE_UNDERLINES = ['', '=', '-', '`', '.', '~', '^']
BULLETS = ['*', '-']

class TextWriter(BaseWriter):
    """Format layouts as text
    (ReStructured inspiration but not totally handled yet).
    """

    def __init__(self) -> None:
        super().__init__()
        self.list_level = 0

    def visit_section(self, layout: Section) -> None:
        """Display a section as text."""
        pass

    def visit_evaluationsection(self, layout: EvaluationSection) -> None:
        """Display an evaluation section as a text."""
        pass

    def visit_paragraph(self, layout: Paragraph) -> None:
        """Enter a paragraph."""
        pass

    def visit_table(self, layout: Table) -> None:
        """Display a table as text."""
        pass

    def default_table(self, layout: Table, table_content: list[list[str]], cols_width: list[int]) -> None:
        """Format a table."""
        pass

    def visit_verbatimtext(self, layout: VerbatimText) -> None:
        """Display a verbatim layout as text (so difficult ;)."""
        pass

    def visit_text(self, layout: Text) -> None:
        """Add some text."""
        pass