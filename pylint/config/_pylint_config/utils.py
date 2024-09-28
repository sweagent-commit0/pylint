"""Utils for the 'pylint-config' command."""
from __future__ import annotations
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Literal, TypeVar
if sys.version_info >= (3, 10):
    from typing import ParamSpec
else:
    from typing_extensions import ParamSpec
_P = ParamSpec('_P')
_ReturnValueT = TypeVar('_ReturnValueT', bool, str)
SUPPORTED_FORMATS = {'t', 'toml', 'i', 'ini'}
YES_NO_ANSWERS = {'y', 'yes', 'n', 'no'}

class InvalidUserInput(Exception):
    """Raised whenever a user input is invalid."""

    def __init__(self, valid_input: str, input_value: str, *args: object) -> None:
        self.valid = valid_input
        self.input = input_value
        super().__init__(*args)

def should_retry_after_invalid_input(func: Callable[_P, _ReturnValueT]) -> Callable[_P, _ReturnValueT]:
    """Decorator that handles InvalidUserInput exceptions and retries."""
    pass

@should_retry_after_invalid_input
def get_and_validate_format() -> Literal['toml', 'ini']:
    """Make sure that the output format is either .toml or .ini."""
    pass

@should_retry_after_invalid_input
def validate_yes_no(question: str, default: Literal['yes', 'no'] | None) -> bool:
    """Validate that a yes or no answer is correct."""
    pass

def get_minimal_setting() -> bool:
    """Ask the user if they want to use the minimal setting."""
    pass

def get_and_validate_output_file() -> tuple[bool, Path]:
    """Make sure that the output file is correct."""
    pass