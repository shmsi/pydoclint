import re
import typing
import spellchecker
import pydoclint.utils as util

WARNING = "- Wrong spelling at [{file_path}:{lineno}]. Did you\
 mean '{corrected_word}' instead of '{word}'."


class SpellChecker:
    def __init__(self, docstring: typing.Tuple[int, str], file_path: str) -> None:
        """Constructor.

        :param docstring: A tuple with starting line number of docstring
                         as first element and docstring as second element.
        """
        self.docstring = docstring
        self.file_path = file_path

    @staticmethod
    def __has_correct_spelling(word: str) -> str:
        spell_checker = spellchecker.SpellChecker()
        corrected_word = spell_checker.correction(word)
        if corrected_word != word:
            return False, corrected_word
        else:
            return True, word

    @staticmethod
    def __spell_check_sentence(line: str, line_no: int, file_path):
        """Spell check a sentence and log spelling problems

        :param line: line to spellcheck.
        :param line_no: Line number of given line in docstring.
        """
        for word in line.split(" "):
            word = word.strip()
            if not word or not util.is_alpha(word):
                continue
            verdict, correct_word = SpellChecker.__has_correct_spelling(word)
            if not verdict:
                print(
                    WARNING.format(
                        file_path=util.color(util.style.GREEN, file_path),
                        lineno=util.color(util.style.MAGENTA, str(line_no)),
                        corrected_word=util.color(util.style.GREEN, correct_word),
                        word=util.color(util.style.RED, word),
                    )
                )

    def spell_check(self):
        initial_line_no, docstr = self.docstring
        docstr_lines = docstr.split("\n")
        for i, line in enumerate(docstr_lines):
            lineno = i + initial_line_no
            self.__spell_check_sentence(line, lineno, self.file_path)
