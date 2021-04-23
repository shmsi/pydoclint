"""This module is responsible for parsing python docstrings."""
import ast
import pydoclint.utils as utils
from typing import Mapping, Tuple


class ParsePython:
    """Parse python code with ast."""

    def __init__(self, source: str):
        self.source = source
        self.tree = ast.parse(source)

    def get_lineno_with_docstrings(self) -> Tuple[int, str]:
        """Get line number with docstring in a given python file.
        :return: A list of tupples with line number and docstring.
        """
        lineno_with_docstr = list()
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.Module)):
                if (
                    node.body
                    and isinstance(node.body[0], ast.Expr)
                    and isinstance(node.body[0].value, ast.Str)
                ):
                    # TODO: line number for module object might not be correct
                    lineno = 1 if isinstance(node, ast.Module) else node.lineno
                    lineno_with_docstr.append((lineno, node.body[0].value.s))
        return lineno_with_docstr

    def get_imports(self):
        """Get imports in python file.

        :raises NotImplementedError: not implemented yet
        """
        raise NotImplementedError
