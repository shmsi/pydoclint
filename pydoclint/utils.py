"""Utils module with helper functions.
"""
import re
import glob
from typing import List, Dict
import yaml


def __matches(patterns: List[str], path) -> bool:
    """Check if string matches any pattern in the list.

    :return: True if pattern is found, False otherwise
    """
    for pattern in patterns:
        if re.match(pattern, path):
            return True
    return False


def get_all_py_files(dir_: str, patterns: List[str]) -> List[str]:
    """Recursively get all .py files in a given directory"""
    return [
        x
        for x in glob.glob(f"{dir_}/**/*.py", recursive=True)
        if not __matches(patterns, x)
    ]


def get_config() -> Dict[str, str]:
    """Read config yaml file

    :return: config
    """
    with open("default_conf.yaml") as file:
        config = yaml.safe_load(file)
    return config


def override_config(overriding_config: Dict[str, str]) -> Dict[str, str]:
    """Override the default config with overriding config.

    :param overriding_config: Overriding config
    :return: updated config.
    """
    default_config = get_config()
    for key, value in overriding_config.items():
        default_config[key] = value
    return default_config


def read_file(path):
    with open(path, "r") as file:
        return file.read()


def is_alpha(word: str) -> bool:
    if bool(re.match("^[a-zA-Z]*$", word)) == True:
        return True
    return False


class style:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


def color(color, text):
    return color + text + style.RESET
