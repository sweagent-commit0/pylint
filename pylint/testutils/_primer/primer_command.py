from __future__ import annotations
import abc
import argparse
from pathlib import Path
from typing import Dict, TypedDict
from pylint.reporters.json_reporter import OldJsonExport
from pylint.testutils._primer import PackageToLint

class PackageData(TypedDict):
    commit: str
    messages: list[OldJsonExport]
PackageMessages = Dict[str, PackageData]

class PrimerCommand:
    """Generic primer action with required arguments."""

    def __init__(self, primer_directory: Path, packages: dict[str, PackageToLint], config: argparse.Namespace) -> None:
        self.primer_directory = primer_directory
        self.packages = packages
        self.config = config