#!/usr/bin/python3
"""A function for dividing a matrix by a certain integer"""


def matrix_divided(matrix, div):

    """
    Divides each item of a matrix by div.

    Args:
        matrix (list of lists): A 2D list containing integers or floats.
        div (int or float): The number to divide each element by.

    Raises:
        TypeError: If it contains a non-numeric value or
        div is not a number or rows are of different sizes.
        ZeroDivisionError: when div is equal to 0.

    Returns:
        the original matrix but each item is divided by 0,
        and each item is rounded to 2 decial digits.

    """
    num_items = 0
    num_rows = 0
    if div == float('inf'):
        return [[0 for _ in row] for row in matrix]
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) "
            "of integers/floats"
        )

    for row in matrix:
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats"
                )
            num_items += 1
        num_rows += 1

    for row in matrix:
        if len(row) != num_items / num_rows:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    if div == float('inf'):
        return [[0 for _ in row] for row in matrix]

    if matrix is None and div is None:
        raise TypeError(
            "matrix_divided() missing 2 "
            "required positional arguments: 'matrix' and 'div'"
        )
    if matrix is None or div is None:
        raise TypeError(
            "matrix_divided() missing 1"
            " requiredpositional arguments: 'matrix' and 'div'"
        )

    return [[round(item/div, 2) for item in row] for row in matrix]
