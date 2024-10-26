#!/usr/bin/python3
"""A function to read and print file"""


def read_file(filename=""):
    """initialize a function"""
    with open(filename, encoding='UTF8') as my_file:
        print(my_file.read(), end='')
