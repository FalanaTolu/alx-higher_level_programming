#!/usr/bin/python3
"""Module 100-append_after."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    after each line containing a specific string."""

    with open(filename, 'r') as f:
        text = f.readlines()

    with open(filename, 'w') as fs:
        str = ""
        for line in text:
            str += line
            if search_string in line:
                str += new_string
        fs.write(str)
