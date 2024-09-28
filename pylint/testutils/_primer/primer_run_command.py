from __future__ import annotations
import json
import sys
import warnings
from io import StringIO
from git.repo import Repo
from pylint.lint import Run
from pylint.message import Message
from pylint.reporters.json_reporter import JSONReporter, OldJsonExport
from pylint.testutils._primer.package_to_lint import PackageToLint
from pylint.testutils._primer.primer_command import PackageData, PackageMessages, PrimerCommand
GITHUB_CRASH_TEMPLATE_LOCATION = '/home/runner/.cache'
CRASH_TEMPLATE_INTRO = 'There is a pre-filled template'

class RunCommand(PrimerCommand):

    @staticmethod
    def _filter_fatal_errors(messages: list[OldJsonExport]) -> list[Message]:
        """Separate fatal errors so we can report them independently."""
        pass