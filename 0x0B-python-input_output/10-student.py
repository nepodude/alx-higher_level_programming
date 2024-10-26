#!/usr/bin/python3
"""Define a student"""


class Student:
    """initialize the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """retrives a dictioanary representation of a Student
    instance."""
    def to_json(self, attrs=None):
        if type(attrs) is list and type(element) is str for element in attrs:
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dir__
