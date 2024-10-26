#!/usr/bin/python3
"""Generate Pascal's triangle up to n rows without using factorials."""


def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows."""
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]
    for i in range(1, n):
        # Start the row with 1
        row = [1]

        # Calculate the intermediate values based on the previous row
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle
