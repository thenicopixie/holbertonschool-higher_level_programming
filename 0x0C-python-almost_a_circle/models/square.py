#!/usr/bin/python3
"""Module for class Square that inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize size, x, y, and id"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return message to stdout"""
        id_s = self.id
        s_s = self.width
        x_s = self.x
        y_s = self.y
        return "[Square] ({}) {}/{} - {}".format(id_s, x_s, y_s, s_s)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update attributes"""
        if args != ():
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif kwargs != {}:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        s_dict = {}
        s_dict['id'] = self.id
        s_dict['size'] = self.size
        s_dict['x'] = self.x
        s_dict['y'] = self.y
        return s_dict
