#!/usr/bin/python3
"""A function to perform cool stuffs"""


def append_after(filename="", search_string="", new_string=""):
    """open a file and append stuffs in it"""
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
