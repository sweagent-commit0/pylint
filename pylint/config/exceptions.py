from __future__ import annotations

class UnrecognizedArgumentAction(Exception):
    """Raised if an ArgumentManager instance tries to add an argument for which the
    action is not recognized.
    """

class _UnrecognizedOptionError(Exception):
    """Raised if an ArgumentManager instance tries to parse an option that is
    unknown.
    """

    def __init__(self, options: list[str], *args: object) -> None:
        self.options = options
        super().__init__(*args)

class ArgumentPreprocessingError(Exception):
    """Raised if an error occurs during argument pre-processing."""