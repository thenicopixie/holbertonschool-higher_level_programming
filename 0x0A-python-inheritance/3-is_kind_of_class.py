#!/usr/bin/python3
""" Module to check if object is an instance of a class or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Check if object is an intance of given class
    Return: True is object is an instance, or False
    if not an instance."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
