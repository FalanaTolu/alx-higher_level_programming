#!/usr/bin/python3
"""Module for 4-from_json_string."""


import json


def from_json_string(my_str):
    """Return the object represented my my_str."""

    return json.loads(my_str)
