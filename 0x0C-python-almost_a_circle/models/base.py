#!/usr/bin/python3
"""Module for base class Base"""


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """A Class constructor to initialize id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
