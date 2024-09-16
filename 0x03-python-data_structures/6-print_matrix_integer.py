#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, x in enumerate(row):
            if i < (len(row) - 1):
                print("{:d}".format(x), end=' ')
            else:
                print("{:d}".format(x), end='')
        print()
