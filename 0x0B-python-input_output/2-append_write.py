#!/usr/bin/python3
"""Module for 2-append_write."""


def append_write(filename="", text=""):
    """Appends text to filename."""

    with open(filename, 'a') as f:
        return f.write(text)
