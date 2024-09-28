from __future__ import annotations
from pylint.pyreverse.dot_printer import DotPrinter
from pylint.pyreverse.mermaidjs_printer import HTMLMermaidJSPrinter, MermaidJSPrinter
from pylint.pyreverse.plantuml_printer import PlantUmlPrinter
from pylint.pyreverse.printer import Printer
filetype_to_printer: dict[str, type[Printer]] = {'plantuml': PlantUmlPrinter, 'puml': PlantUmlPrinter, 'mmd': MermaidJSPrinter, 'html': HTMLMermaidJSPrinter, 'dot': DotPrinter}