#!/usr/bin/python3
"""Module for 8-class_to_json."""


def class_to_json(obj):
    """Creates a dictionary description of object
    with simple data structure.
    """

    return obj.__dict__
