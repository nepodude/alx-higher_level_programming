#!/usr/bin/python3

"""A function that says my name."""


def say_my_name(first_name, last_name=""):

    """
    This function prints my first name followed by the last name.
    It raises a TypeError when any of the names isn't a string.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    first_name = first_name.strip()
    last_name = last_name.strip()

    if last_name and first_name:
        print(f"My name is {first_name} {last_name}")
    elif first_name and not last_name:
        print(f"My name is {first_name} ")
    elif not first_name and last_name:
        print(f"My name is {last_name}")
    else:
        print("My name is ")
