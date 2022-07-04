#!/usr/bin/python3
"""Module for lookup."""


def lookup(obj):
    """Returns that list of attributes and methods.
    Args:
        obj: object to look up
    Returns:
        list: object list of attributes and methods
    """

    return dir(obj)
