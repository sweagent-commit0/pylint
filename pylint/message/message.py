from __future__ import annotations
from dataclasses import asdict, dataclass
from pylint.constants import MSG_TYPES
from pylint.interfaces import UNDEFINED, Confidence
from pylint.typing import MessageLocationTuple

@dataclass(unsafe_hash=True)
class Message:
    """This class represent a message to be issued by the reporters."""
    msg_id: str
    symbol: str
    msg: str
    C: str
    category: str
    confidence: Confidence
    abspath: str
    path: str
    module: str
    obj: str
    line: int
    column: int
    end_line: int | None
    end_column: int | None

    def __init__(self, msg_id: str, symbol: str, location: MessageLocationTuple, msg: str, confidence: Confidence | None) -> None:
        self.msg_id = msg_id
        self.symbol = symbol
        self.msg = msg
        self.C = msg_id[0]
        self.category = MSG_TYPES[msg_id[0]]
        self.confidence = confidence or UNDEFINED
        self.abspath = location.abspath
        self.path = location.path
        self.module = location.module
        self.obj = location.obj
        self.line = location.line
        self.column = location.column
        self.end_line = location.end_line
        self.end_column = location.end_column

    def format(self, template: str) -> str:
        """Format the message according to the given template.

        The template format is the one of the format method :
        cf. https://docs.python.org/2/library/string.html#formatstrings
        """
        pass