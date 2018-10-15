#!/usr/bin/python
""" Module to check if object is an instace of a inherited class
"""


def inherits_from(obj, a_class):
    """Check is object is an instance of an
    inherited class.
    Args:
    obj: object to check
    a_class: class to check for instance"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
