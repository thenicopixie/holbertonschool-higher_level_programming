#!/usr/bin/python3
"""Creates a class that defines a student"""


class Student:
    """Base class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialization of attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a class instance"""
        return self.__dict__
