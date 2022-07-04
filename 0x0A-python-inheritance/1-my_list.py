#!/usr/bin/python3
"""Module for 1-my_list."""


class MyList(list):
    """Creates a Class MyList that inherits from list."""

    def print_sorted(self):
        """Prints the list, in ascending sort."""

        print(sorted(self))
