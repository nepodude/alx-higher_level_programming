#!/usr/bin/python3

"""Defines a class Square with size and position attributes."""

class Square:
    """Represents a square with a given size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with optional size and position.

        Args:
            size (int): The size of the square.
            position (tuple): A tuple of two integers representing the position.
        """
        self.size = size  # Set size using the setter
        self.position = position  # Set position using the setter

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

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

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.size == 0:
            print("")  # Print empty line if size is 0
            return

        # Print the position (spaces)
        print("\n" * self.position[1], end="")  # Print empty lines for vertical position
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
