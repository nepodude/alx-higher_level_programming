#!/usr/bin/python3
"""initialize a function"""
import json


def load_from_json_file(filename):
    """write an object into a filename"""
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
