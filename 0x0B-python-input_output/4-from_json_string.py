#!/usr/bin/python3
"""initialize a function"""
import json


def from_json_string(my_str):
    """return python data structure."""
    return json.loads(my_str)
