#!/usr/bin/python
"""Module for base class base geometry and subclass rectangle"""


class BaseGeometry:
    """Base class BaseGeometry that raises an exception
    with a message, and validates a value"""
    def area(self):
        """Method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer
        Args:
        name: string
        value: integer to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class that inherites from BaseGeometry.
    Intializes width and height"""
    def __init__(self, width, height):
        """Method to initialize width and height"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
