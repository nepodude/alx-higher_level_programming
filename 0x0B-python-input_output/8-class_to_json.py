#!/usr/bin/python3
"""Initialize a function to return simple dict in json"""


def class_to_json(obj):
    """start the function"""
    return obj.__dict__
