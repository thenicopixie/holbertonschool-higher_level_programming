#!/usr/bin/python3
"""Creates a class that defines a student"""


class Student:
    """Base class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialization of attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a class instance"""
        new_dict = {}
        try:
            for i in attrs:
                if self.__dict__.get(i) is not None:
                    new_dict.update({i: self.__dict__.get(i)})
            return new_dict
        except:
            return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for key in json:
            self.__dict__.update({key: json.get(key)})
