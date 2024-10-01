#!/usr/bin/python3

"""Defines a class Square with size validation and an area method."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize the square with a given size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter to initialize size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """To print the square down."""
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print()
