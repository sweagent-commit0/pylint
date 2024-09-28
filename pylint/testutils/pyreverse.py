from __future__ import annotations
import argparse
import configparser
import shlex
from pathlib import Path
from typing import NamedTuple, TypedDict
from pylint.pyreverse.main import DEFAULT_COLOR_PALETTE

class PyreverseConfig(argparse.Namespace):
    """Holds the configuration options for Pyreverse.

    The default values correspond to the defaults of the options' parser.
    """

    def __init__(self, mode: str='PUB_ONLY', classes: list[str] | None=None, show_ancestors: int | None=None, all_ancestors: bool | None=None, show_associated: int | None=None, all_associated: bool | None=None, no_standalone: bool=False, show_builtin: bool=False, show_stdlib: bool=False, module_names: bool | None=None, only_classnames: bool=False, output_format: str='dot', colorized: bool=False, max_color_depth: int=2, color_palette: tuple[str, ...]=DEFAULT_COLOR_PALETTE, ignore_list: tuple[str, ...]=tuple(), project: str='', output_directory: str='') -> None:
        super().__init__()
        self.mode = mode
        if classes:
            self.classes = classes
        else:
            self.classes = []
        self.show_ancestors = show_ancestors
        self.all_ancestors = all_ancestors
        self.show_associated = show_associated
        self.all_associated = all_associated
        self.no_standalone = no_standalone
        self.show_builtin = show_builtin
        self.show_stdlib = show_stdlib
        self.module_names = module_names
        self.only_classnames = only_classnames
        self.output_format = output_format
        self.colorized = colorized
        self.max_color_depth = max_color_depth
        self.color_palette = color_palette
        self.ignore_list = ignore_list
        self.project = project
        self.output_directory = output_directory

class TestFileOptions(TypedDict):
    source_roots: list[str]
    output_formats: list[str]
    command_line_args: list[str]

class FunctionalPyreverseTestfile(NamedTuple):
    """Named tuple containing the test file and the expected output."""
    source: Path
    options: TestFileOptions

def get_functional_test_files(root_directory: Path) -> list[FunctionalPyreverseTestfile]:
    """Get all functional test files from the given directory."""
    pass