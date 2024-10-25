#!/usr/bin/python3
"""initiates empty class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """initiate the width and height"""
    def __init__(self, width, height):
        """initialize and validate width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A description of the rectangle
            in the format: [Rectangle] <width>/<height>
        """
        return (f"[{str(self.__class__.__name__)}] "
                f"{self.__width}/{self.__height}")

    def __repr__(self):
        """Return a formal string representation of the rectangle.

        Returns:
            str: A description of the rectangle in the same format as __str__.
        """
        return self.__str__()
