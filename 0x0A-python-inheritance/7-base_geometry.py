#!/usr/bin/python3
"""Module for base class base geometry"""


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
