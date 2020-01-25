"""Recursively zip up a directory/folder."""

from __future__ import absolute_import

import sys

import zipdir.cli as cli


def main():
    """Provide a generic main entry point."""
    sys.exit(cli.main(*sys.argv))


if __name__ == "__main__":
    main()
