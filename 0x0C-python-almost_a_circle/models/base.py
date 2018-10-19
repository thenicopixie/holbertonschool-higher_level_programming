#!/usr/bin/python3
"""Module for base class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
