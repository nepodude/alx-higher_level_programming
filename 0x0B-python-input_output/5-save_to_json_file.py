#!/usr/bin/python3
"""initialize a function"""
import json


def save_to_json_file(my_obj, filename):
    """write an object into a filename"""
    with open(filename, "w", encoding='utf-8') as file:
        json.dumps(my_obj, file)
