"""Utils for arguments/options parsing and handling."""
from __future__ import annotations
import re
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Any
from pylint import extensions, utils
from pylint.config.argument import _CallableArgument, _ExtendArgument, _StoreArgument, _StoreNewNamesArgument, _StoreOldNamesArgument, _StoreTrueArgument
from pylint.config.callback_actions import _CallbackAction
from pylint.config.exceptions import ArgumentPreprocessingError
if TYPE_CHECKING:
    from pylint.lint.run import Run

def _convert_option_to_argument(opt: str, optdict: dict[str, Any]) -> _StoreArgument | _StoreTrueArgument | _CallableArgument | _StoreOldNamesArgument | _StoreNewNamesArgument | _ExtendArgument:
    """Convert an optdict to an Argument class instance."""
    pass

def _parse_rich_type_value(value: Any) -> str:
    """Parse rich (toml) types into strings."""
    pass

def _init_hook(run: Run, value: str | None) -> None:
    """Execute arbitrary code from the init_hook.

    This can be used to set the 'sys.path' for example.
    """
    pass

def _set_rcfile(run: Run, value: str | None) -> None:
    """Set the rcfile."""
    pass

def _set_output(run: Run, value: str | None) -> None:
    """Set the output."""
    pass

def _add_plugins(run: Run, value: str | None) -> None:
    """Add plugins to the list of loadable plugins."""
    pass

def _enable_all_extensions(run: Run, value: str | None) -> None:
    """Enable all extensions."""
    pass
PREPROCESSABLE_OPTIONS: dict[str, tuple[bool, Callable[[Run, str | None], None], int]] = {'--init-hook': (True, _init_hook, 8), '--rcfile': (True, _set_rcfile, 4), '--output': (True, _set_output, 0), '--load-plugins': (True, _add_plugins, 5), '--verbose': (False, _set_verbose_mode, 4), '-v': (False, _set_verbose_mode, 2), '--enable-all-extensions': (False, _enable_all_extensions, 9)}

def _preprocess_options(run: Run, args: Sequence[str]) -> list[str]:
    """Pre-process options before full config parsing has started."""
    pass