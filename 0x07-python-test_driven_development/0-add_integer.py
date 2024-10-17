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
        ValueError: if 'a' or 'b' is NaN or infinity.
        OverflowError: if 'a' or 'b' is too large to be converted
        to an integer.
    """
    # Check if 'a' is a valid number
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # Check if 'b' is a valid number
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle infinity for 'a'
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    # Handle infinity for 'b'
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")
    # Handles NaN
    if isinstance(a, float) and (a != a):
        raise ValueError("cannot convert float NaN to integer")
    # Handle NaN
    if isinstance(b, float) and (b != b):
        raise ValueError("cannot convert float NaN to integer")

    # Convert to integers
    a = int(a)
    b = int(b)

    # Return the sum
    return a + b
