#!/usr/bin/python3


"""Start the function"""


def inherits_from(obj, a_class):
    """Start checking for instance of obj and type"""
    return isinstance(obj, a_class) and (type(obj) is not a_class)
