import pytest
import pydoclint.spell_checker as sc


@pytest.fixture
def spellcheck():
    docstring = """Speell check a sentence and log spelling problems

        :param line: line to spelll cheeeckk.
        :param line_no: Linerxd numberr of giveen line in docstring."""
    docstring = (0, docstring)
    return sc.SpellChecker(docstring, "file_path")


def test_spell_check(spellcheck):
    spellcheck.spell_check()
