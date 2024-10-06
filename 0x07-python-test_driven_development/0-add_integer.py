#!/usr/bin/python3
"""Module for adding two integers."""
def add_integer(a, b=98):
    """
    Adds two integers and returns the result.

    Args:
        a (int or float): The first integer to add.
        b (int or float, optional): The second integer to add. Defaults to 98.

    Returns:
        int: The sume of 'a' and 'b' as an integer.
    
    Raises:
        TypeError: if 'a' is not an integer or a float.
        TypeError: if 'b' is not an integer or a float.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
        >>> add_integer(4, "School")
        Traceback (most recent call last):
            ...
        TypeError: b must be an integer
        >>> add_integer(None)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
