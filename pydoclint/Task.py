from abc import ABC, abstractmethod
from __future__ import annotations
import typing
from os.path import isdir
import pydoclint.utils as util
from pydoclint.parse_python import ParsePython
from pydoclint.spell_checker import SpellChecker


class DoclintTask(ABC):
    def __init__(self, input=None) -> None:
        self.input = input

    @abstractmethod
    def action(self, prev_task_output: typing.Any = None) -> typing.Any:
        """Perform some action on the output of previous action

        If output of previous action is None then it means this is the
        first task in the flow.

        :param prev_task_output: Output of previous action
        :type prev_task_output: result after executing the action.
        """

    def __rshift__(self, other_task: DoclintTask) -> typing.Any:
        """Override right shift operator

        :param other_task: Task to use in the right of right shift op.
        :return: output of `other_task` action.
        """
        return other_task.action(self.action(self.input))


class GetPyFiles(DoclintTask):
    """An inital task in the flow."""

    def __init__(self, path) -> None:
        super().__init__(input=None)
        self.path = path

    def action(self, prev_task_output: typing.Any = None) -> typing.List[str]:
        if isdir(self.path):
            return util.get_all_py_files(self.path, [])
        elif self.path.endswith(".py"):
            return [self.path]
        raise ValueError("Invalid file format provided.")


class PythonParser(DoclintTask):
    def __init__(self) -> None:
        super().__init__(input=None)

    def action(self, py_files: typing.Any) -> typing.Any:
        return [(x, ParsePython(util.read_file(x))) for x in py_files]


class ScanSpelling(DoclintTask):
    def __init__(self, input) -> None:
        super().__init__(input=None)

    def action(self, py_parser_objs: typing.Any) -> typing.Any:
        for file_path, pp in py_parser_objs:
            for doc in pp.get_lineno_with_docstrings():
                SpellChecker(doc, file_path=file_path).spell_check()