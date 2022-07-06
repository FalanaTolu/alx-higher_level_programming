#!/usr/bin/python3
"""Module for 11-student."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation
        of a Student instance.
        Args:
            - attrs: list of attributes
        Returns: the dict representation of the instance.
        """

        my_dict = dict()
        if attrs and all(isinstance(a, str) for a in attrs):
            for a in attrs:
                if a in self.__dict__:
                    my_dict.update({a: self.__dict__[a]})
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        Args:
            - json: dictionnary of attributes
        """

        for a in json:
            self.__dict__.update({a: json[a]})
