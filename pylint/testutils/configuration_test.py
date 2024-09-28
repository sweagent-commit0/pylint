"""Utility functions for configuration testing."""
from __future__ import annotations
import copy
import json
import logging
import unittest
from pathlib import Path
from typing import Any, Dict
from unittest.mock import Mock
from pylint.lint import Run
ConfigurationValue = Any
PylintConfiguration = Dict[str, ConfigurationValue]

def get_expected_or_default(tested_configuration_file: str | Path, suffix: str, default: str) -> str:
    """Return the expected value from the file if it exists, or the given default."""
    pass
EXPECTED_CONF_APPEND_KEY = 'functional_append'
EXPECTED_CONF_REMOVE_KEY = 'functional_remove'

def get_expected_configuration(configuration_path: str, default_configuration: PylintConfiguration) -> PylintConfiguration:
    """Get the expected parsed configuration of a configuration functional test."""
    pass

def get_related_files(tested_configuration_file: str | Path, suffix_filter: str) -> list[Path]:
    """Return all the file related to a test conf file ending with a suffix."""
    pass

def get_expected_output(configuration_path: str | Path, user_specific_path: Path) -> tuple[int, str]:
    """Get the expected output of a functional test."""
    pass

def run_using_a_configuration_file(configuration_path: Path | str, file_to_lint: str=__file__) -> tuple[Mock, Mock, Run]:
    """Simulate a run with a configuration without really launching the checks."""
    pass