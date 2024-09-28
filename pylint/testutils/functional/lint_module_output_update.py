from __future__ import annotations
import csv
import os
from pylint.testutils.lint_module_test import LintModuleTest, MessageCounter
from pylint.testutils.output_line import OutputLine

class LintModuleOutputUpdate(LintModuleTest):
    """Class to be used if expected output files should be updated instead of
    checked.
    """

    class TestDialect(csv.excel):
        """Dialect used by the csv writer."""
        delimiter = ':'
        lineterminator = '\n'
    csv.register_dialect('test', TestDialect)

    def _check_output_text(self, _: MessageCounter, expected_output: list[OutputLine], actual_output: list[OutputLine]) -> None:
        """Overwrite or remove the expected output file based on actual output."""
        pass