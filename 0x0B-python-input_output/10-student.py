#!/usr/bin/python3
"""Define a student"""


class Student:
    """initialize the class"""

    def __init__(self, first_name, last_name, age):
        """define the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return stuffs"""
        if (type(attrs) is list and all(type(ele) is str for ele in attrs)):
            return ({k: getattr(self, k) for k in attrs if hasattr(self, k)})
        else:
            return (self.__dict__)
