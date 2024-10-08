#!/usr/bin/python3
"""Module for adding two integers."""
def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int or float): The first integer to add.
        b (int or float, optional): The second integer to add. Defaults to 98.

    Returns:
        int: The sum of 'a' and 'b' as an integer.
    
    Raises:
        TypeError: if 'a' is not an integer or a float.
        TypeError: if 'b' is not an integer or a float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
