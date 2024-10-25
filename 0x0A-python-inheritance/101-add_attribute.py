#!/usr/bin/python3
"""Defines a function to add a new attribute to an object."""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute is added.
        attr_name (str): The name of the attribute.
        attr_value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
