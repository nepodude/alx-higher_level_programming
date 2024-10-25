#!/usr/bin/python3

"""initiates empty class"""


class BaseGeometry:
    """Define a puclic method called area"""
    def area(self):
        """Raise an exception error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates for the integer"""
        if type(value) is not int or value is None:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
