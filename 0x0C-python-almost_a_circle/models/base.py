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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of
        list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                j_list = []
                for i in list_objs:
                    j_list.append(cls.to_dictionary(i))
                f.write(cls.to_json_string(j_list))
