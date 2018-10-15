#!/usr/bin/python3
"""Module for is same class"""


def is_same_class(obj, a_class):
    """Check for instance of object
    Return: True is object is an instance
    of given class, or False if not
    """
    if type(obj) is a_class:
        return True
    else:
        return False
