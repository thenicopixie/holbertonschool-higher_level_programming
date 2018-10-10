#!/usr/bin/python3
""" LockedClass module"""


class LockedClass:
    """ Base LockedClass class"""

    def __setattr__(self, key, value):
        """
        Set attribute if key is found
        """
        string = "'LockedClass' object has no attribute "
        if key is not "first_name":
            raise AttributeError("{}'{}'".format(string, key))
