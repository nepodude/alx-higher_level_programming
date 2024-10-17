#!/usr/bin/python3

""" A function which prints a square matrix using '#' """


def print_square(size):

    """
    Prints a rectangular grid of '#' characters whose
    height and width are both equal to size.

    Args:
        size: a numeric quantity which is suposed to be
        an integer otherwise an error will be raised.

    Raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        TypeError: size must be an integer

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
