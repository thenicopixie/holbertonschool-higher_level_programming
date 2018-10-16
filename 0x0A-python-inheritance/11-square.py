#!/usr/bin/python3
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

    def area(self):
        """Method to get area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Print area of rectangle"""
        c_name = self.__class__.__name__
        return("[{}] {}/{}".format(c_name, self.__width, self.__height))


class Square(Rectangle):
    """Class that inherites from Rectangle.
    Initializes size"""
    def __init__(self, size):
        """Initialize size"""
        super().__init__(size, size)
