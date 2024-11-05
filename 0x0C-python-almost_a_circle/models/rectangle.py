#!/usr/bin/python3
"""Define a rectangle"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base.
    Manages width, height, x, y, and id attributes.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Parameters:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle (default is 0).
        y (int): The y-coordinate of the rectangle (default is 0).
        id (int): Optional. If provided,
        this value is used as the rectangle's id.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value of width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets value of height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets value of x with validation"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets value of y with validation"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
        Return the string representation of the Rectangle.

        Format: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )
