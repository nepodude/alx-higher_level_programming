#!/usr/bin/python3
"""A function for dividing a matrix by a certain integer"""
def matrix_divided(matrix, div):

    """
    Divides each item of a matrix by div.

    Args:
        matrix (list of lists): A 2D list containing integers or floats.
        div (int or float): The number to divide each element by.

    Raises:
        TypeError: If it contains a non-numeric value or div is not a number or rows are of different sizes.
        ZeroDivisionError: when div is equal to 0.

    Returns:
        the original matrix but each item is divided by 0, and each item is rounded to 2 decial digits.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

        >>> matrix = [[-4, 4], [2.5, 7]]
        >>> matrix_divided(matrix, 2)
        [[-2.0, 2.0], [1.25, 3.5]]

        >>> matrix = [[1, 2], [3, 4, 5]]
        >>> matrix_divided(matrix, 2)
        Traceback (most recent call last):
            ...
        TypeError: Each row of the matrix must have the same size

        >>> matrix = [[1, "a"], [3, 4]]
        >>> matrix_divided(matrix, 2)
        Traceback (most recent call last):
            ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats

        >>> matrix_divided(None, 2)
        Traceback (most recent call last):
            ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats

        >>> matrix_divided([[1, 2], [3, 4]], "a")
        Traceback (most recent call last):
            ...
        TypeError: div must be a number

        >>> matrix_divided([[1, 2], [3, 4]], 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: division by zero
    """
    num_items = 0
    num_rows = 0
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            num_items += 1
        num_rows += 1

    for row in matrix:
        if len(row) != num_items / num_rows:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item/div, 2) for item in row] for row in matrix]
