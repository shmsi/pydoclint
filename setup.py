import setuptools

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="pydoclint",
    version="0.0.1",
    author="Shamsi Abdullayev",
    author_email="shamsi@abdullayev.net",
    description="Verify python docstrings",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shmsi/pydoclint",
    classifiers=[
        "Programming Language :: Python :: 3",
        " License :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        pydoclint=pydoclint.pydoclint:main
    """,
)
