#!/usr/bin/python3
"""Creates a function that returns the dictionary description with simple
data structure for JSON serialization of an object"""


def class_to_json(obj):
    """Return the dict descrption for a JSON serialization of an object"""
    return obj.__dict__
