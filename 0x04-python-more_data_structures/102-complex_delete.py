#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete =
    [key for key, my_value in a_dictionary.items() if my_value == value]
    for key in to_delete:
        del a_dictionary[key]
    return a_dictionary
