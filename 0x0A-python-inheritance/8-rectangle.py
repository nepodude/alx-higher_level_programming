#!/usr/bin/python3

"""initiates empty class"""


class Rectangle(BaseGeometry):
    """initiate the width and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
