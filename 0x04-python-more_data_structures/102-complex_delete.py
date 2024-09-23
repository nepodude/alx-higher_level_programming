#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for my_key, my_value in a_dictionary.items():
        if my_value == value:
            del my_key
