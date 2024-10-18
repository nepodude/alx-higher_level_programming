#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """A class that defines a rectangle with width and height"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets a new value for the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets a new value for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of rectangle"""
        return (self.width) * (self.height)

    def perimeter(self):
        """Calculates the perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """returning the string representation of rectangle"""
        if self.height == 0 or self.width == 0:
            return ''

        rows = ['#' * self.width for _ in range(self.height)]

        return '\n'.join(rows)

    def __repr__(self):
        """returns a string representation of the rectangle
        which is used for creating a new rectangle with eval."""
        return f"Rectangle({self.width}, {self.height})"
