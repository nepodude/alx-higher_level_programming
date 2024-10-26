#!/usr/bin/python3
"""A function to perform cool stuffs"""


def append_after(filename="", search_string="", new_string=""):
    """open a file and append stuffs in it"""
    with open(filename, "w", encoding="utf-8") as file:
        for line in file:
            if search_string in line:
                line += search_string
