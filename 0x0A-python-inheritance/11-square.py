#!/usr/bin/python3
"""initiates empty class"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """initiate the size"""
    def __init__(self, size):
        """initialize and validate size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A description of the rectangle
            in the format: [Rectangle] <width>/<height>
        """
        return (f"[{str(self.__class__.__name__)}] "
                f"{self.__size}/{self.__size}")

    def __repr__(self):
        """Return a formal string representation of the rectangle.

        Returns:
            str: A description of the rectangle in the same format as __str__.
        """
        return self.__str__()
