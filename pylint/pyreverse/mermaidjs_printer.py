"""Class to generate files in mermaidjs format."""
from __future__ import annotations
from pylint.pyreverse.printer import EdgeType, NodeProperties, NodeType, Printer
from pylint.pyreverse.utils import get_annotation_label

class MermaidJSPrinter(Printer):
    """Printer for MermaidJS diagrams."""
    DEFAULT_COLOR = 'black'
    NODES: dict[NodeType, str] = {NodeType.CLASS: 'class', NodeType.PACKAGE: 'class'}
    ARROWS: dict[EdgeType, str] = {EdgeType.INHERITS: '--|>', EdgeType.ASSOCIATION: '--*', EdgeType.AGGREGATION: '--o', EdgeType.USES: '-->', EdgeType.TYPE_DEPENDENCY: '..>'}

    def _open_graph(self) -> None:
        """Emit the header lines."""
        pass

    def emit_node(self, name: str, type_: NodeType, properties: NodeProperties | None=None) -> None:
        """Create a new node.

        Nodes can be classes, packages, participants etc.
        """
        pass

    def emit_edge(self, from_node: str, to_node: str, type_: EdgeType, label: str | None=None) -> None:
        """Create an edge from one node to another to display relationships."""
        pass

    def _close_graph(self) -> None:
        """Emit the lines needed to properly close the graph."""
        pass

class HTMLMermaidJSPrinter(MermaidJSPrinter):
    """Printer for MermaidJS diagrams wrapped in a html boilerplate."""
    HTML_OPEN_BOILERPLATE = '<html>\n  <body>\n    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>\n      <div class="mermaid">\n    '
    HTML_CLOSE_BOILERPLATE = '\n       </div>\n  </body>\n</html>\n'
    GRAPH_INDENT_LEVEL = 4