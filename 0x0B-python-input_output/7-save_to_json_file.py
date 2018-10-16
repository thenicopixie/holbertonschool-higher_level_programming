#!/usr/bin/python3
"""Creates a function that writes an object to a test file
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a test file using a JSON representation
    Args:
        my_obj - object to write
        filename - file to write to
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
