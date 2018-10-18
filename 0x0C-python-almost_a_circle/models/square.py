#!/usr/bin/python3
"""Module for class Square that inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize size, x, y, and id"""
        self.__size = size
        self.__x = x
        self.__y = y
        self.id = id
        self = super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return message to stdout"""
        id_s = self.id
        s_s = self.__size
        x_s = self.__x
        y_s = self.__y
        return "[Square] ({}) {}/{} - {}".format(id_s, x_s, y_s, s_s)
