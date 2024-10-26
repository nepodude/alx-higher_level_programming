#!/usr/bin/python3
"""pascal triangle is great"""


def fact(n):
    """pascal triangle is great"""
    if n == 0:
        return 1
    keeper = 1
    for i in range(1, n):
        keeper *= i
    keeper *= n
    return keeper


def combinatorial(i, j):
    """pascal triangle is great"""
    return int(fact(j) / (fact(j - i) * fact(i)))


def pascal_triangle(n):
    """pascal triangle is great"""
    if n <= 0:
        return []
    i = 0
    mylist = []
    for i in range(n):
        helper = []
        for j in range(i + 1):
            helper.append(combinatorial(j, i))
        mylist.append(helper)
    return mylist
