#!/usr/bin/python3
"""Module for class Square that inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize size, x, y, and id"""
        Rectangle.__init__(self, size, size, x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        """Return message to stdout"""
        id_s = self.id
        s_s = self.width
        x_s = self.x
        y_s = self.y
        return "[Square] ({}) {}/{} - {}".format(id_s, x_s, y_s, s_s)
