#!/usr/bin/python3
"""Define a student"""


helper = __import__('8-class_to_json').class_to_json
class Student:
    """initialize the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """retrives a dictioanary representation of a Student
    instance."""
    def to_json(self):
        return helper(self)
