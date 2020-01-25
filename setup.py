#!/usr/bin/env python

# https://packaging.python.org/distributing/#setup-py

try:
    from setuptools import setup, find_packages
except ImportError as e:
    error_message = "Unable to find setuptools;"
    error_message += (
        " please visit https://pypi.python.org/pypi/setuptools for instructions"
    )
    raise RuntimeError(error_message, e)

import os
import os.path
import sys

####################

NAME = "zipdir"
DESCRIPTION = "Recursively zip up a directory/folder"

with open(os.path.join(os.path.dirname(__file__), "VERSION")) as version_file:
    VERSION = version_file.read().strip()

README_FILENAME = "README.md"

TEAM = "Jim Knoble"
TEAM_EMAIL = "jmknoble@pobox.com"

AUTHOR = TEAM
AUTHOR_EMAIL = TEAM_EMAIL

MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL

URL = "https://github.com/jmknoble/zipdir"

PACKAGE_INCLUDES = ["*"]
PACKAGE_EXCLUDES = [
    "build",
    "dist",
    "docs",
    "examples",
    "tests",
    "tests.*",
    "*.egg-info",
]
PACKAGES = find_packages(include=PACKAGE_INCLUDES, exclude=PACKAGE_EXCLUDES)

PROVIDES = PACKAGES

SCRIPTS = []

PACKAGE_DATA = {"": ["*.config", "*.json", "*.cfg"]}

REQUIREMENTS = []

TEST_SUITE = "tests"
TEST_REQUIREMENTS = []

SETUP_REQUIREMENTS = ["Sphinx"]

KEYWORDS = "zip cli"
CLASSIFIERS = [
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Environment :: Other Environment",
    "Intended Audience :: Developers",
    "Intended Audience :: Information Technology",
    "License :: Other/Proprietary License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: System :: Distributed Computing",
    "Topic :: Utilities",
]

####################

readme_path = os.path.join(os.path.dirname(__file__), README_FILENAME)
if os.path.exists(readme_path):
    with open(readme_path, "r") as readme_file:
        README = readme_file.read()
else:
    README = None

####################


def should_do_replacements():
    """
    Tell whether it is advisable to do version/author/email replacements.
    """
    setup_dir = os.path.dirname(sys.argv[0])
    # Don't do replacements if we're not running setup.py
    # from the project directory
    return setup_dir in [".", ""]


def do_replacements(
    version=VERSION, author=AUTHOR, author_email=AUTHOR_EMAIL, packages=PACKAGES
):
    """
    Treat setup.py as single source of truth for certain module-level values.

    Replace name, author, and email in each package's __init__.py
    with the given values; this allows making setup.py into a
    source of truth for those values.
    """
    if not should_do_replacements():
        return

    replacement_map = {
        "__version__": version,
        "__author__": author,
        "__email__": author_email,
    }
    init_filename = "__init__.py"
    old_suffix = "old"
    new_suffix = "new"
    for package in packages:
        package_path = os.path.join(*package.split("."))
        currentfile = os.path.join(package_path, init_filename)
        newfile = os.path.join(package_path, ".".join([init_filename, new_suffix]))
        oldfile = os.path.join(package_path, ".".join([init_filename, old_suffix]))
        assignment_op = " = "
        if os.path.exists(currentfile):
            should_replace = False
            with open(currentfile, "r") as i, open(newfile, "w") as o:
                for line in i:
                    for (key, value) in replacement_map.items():
                        if line.startswith("".join([key, assignment_op])):
                            replacement = "".join(
                                [key, assignment_op, repr(value), "\n"]
                            )
                            if line != replacement:
                                line = replacement
                                should_replace = True
                            break
                    o.write(line)
            if should_replace:
                os.rename(currentfile, oldfile)
                os.rename(newfile, currentfile)
            else:
                os.remove(newfile)


# Use setup.py as source of truth
do_replacements()

####################

setup(
    # https://packaging.python.org/distributing/#setup-args
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    url=URL,
    packages=PACKAGES,
    scripts=SCRIPTS,
    package_data=PACKAGE_DATA,
    # package_dir={NAME: NAME},
    # entry_points={
    #         'console_scripts': [
    #                 '{name}={name}.cli:main'.format(name=NAME),
    #                 ]
    #         },
    include_package_data=True,
    provides=PROVIDES,
    install_requires=REQUIREMENTS,
    # Install this package as individual files, not a zipped egg
    zip_safe=False,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    test_suite=TEST_SUITE,
    tests_require=TEST_REQUIREMENTS,
    setup_requires=SETUP_REQUIREMENTS,
)
