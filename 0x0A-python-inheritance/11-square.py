#!/usr/bin/python3
"""initiates empty class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """initiate the size"""

    def __init__(self, size):
        """initialize and validate size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
