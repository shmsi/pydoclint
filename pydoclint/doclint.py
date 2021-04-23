"""CLI entry point of pydoclint.
"""
from os.path import isdir
from pydoclint.parse_python import ParsePython
from pydoclint.spell_checker import SpellChecker
import pydoclint.utils as util
import argparse


def start_docs_verfiy(path):
    pyfiles = []
    if isdir(path):
        pyfiles = util.get_all_py_files(path, [])
    else:
        pyfiles.append(path)
    parse_pys = [(x, ParsePython(util.read_file(x))) for x in pyfiles]
    for file_path, pp in parse_pys:
        for doc in pp.get_lineno_with_docstrings():
            SpellChecker(doc, file_path=file_path).spell_check()


def main():
    parser = argparse.ArgumentParser(
        prog="pydoclint", description="Python docstring verifier"
    )
    parser.add_argument(
        "path",
        help="Directory or file name. If Directory is provided \
            pydoclint will recursively go throw all python files.",
    )
    args = parser.parse_args()
    start_docs_verfiy(args.path)


main()