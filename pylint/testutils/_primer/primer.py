from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from pylint.testutils._primer import PackageToLint
from pylint.testutils._primer.primer_command import PrimerCommand
from pylint.testutils._primer.primer_compare_command import CompareCommand
from pylint.testutils._primer.primer_prepare_command import PrepareCommand
from pylint.testutils._primer.primer_run_command import RunCommand

class Primer:
    """Main class to handle priming of packages."""

    def __init__(self, primer_directory: Path, json_path: Path) -> None:
        self.primer_directory = primer_directory
        self._argument_parser = argparse.ArgumentParser(prog='Pylint Primer')
        self._subparsers = self._argument_parser.add_subparsers(dest='command', required=True)
        prepare_parser = self._subparsers.add_parser('prepare')
        prepare_parser.add_argument('--clone', help='Clone all packages.', action='store_true', default=False)
        prepare_parser.add_argument('--check', help='Check consistencies and commits of all packages.', action='store_true', default=False)
        prepare_parser.add_argument('--make-commit-string', help='Get latest commit string.', action='store_true', default=False)
        prepare_parser.add_argument('--read-commit-string', help='Print latest commit string.', action='store_true', default=False)
        run_parser = self._subparsers.add_parser('run')
        run_parser.add_argument('--type', choices=['main', 'pr'], required=True, help='Type of primer run.')
        run_parser.add_argument('--batches', required=False, type=int, help='Number of batches')
        run_parser.add_argument('--batchIdx', required=False, type=int, help='Portion of primer packages to run.')
        compare_parser = self._subparsers.add_parser('compare')
        compare_parser.add_argument('--base-file', required=True, help='Location of output file of the base run.')
        compare_parser.add_argument('--new-file', required=True, help='Location of output file of the new run.')
        compare_parser.add_argument('--commit', required=True, help='Commit hash of the PR commit being checked.')
        compare_parser.add_argument('--batches', required=False, type=int, help='Number of batches (filepaths with the placeholder BATCHIDX will be numbered)')
        self.config = self._argument_parser.parse_args()
        self.packages = self._get_packages_to_lint_from_json(json_path)
        'All packages to prime.'
        if self.config.command == 'prepare':
            command_class: type[PrimerCommand] = PrepareCommand
        elif self.config.command == 'run':
            command_class = RunCommand
        elif self.config.command == 'compare':
            command_class = CompareCommand
        self.command = command_class(self.primer_directory, self.packages, self.config)