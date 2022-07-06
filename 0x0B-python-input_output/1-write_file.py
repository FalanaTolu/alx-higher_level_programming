#!/usr/bin/python3
"""Module for 1-write_file."""


def write_file(filename="", text=""):
    """Writes text in filename."""

    with open(filename, 'w') as f:
        return f.write(text)
