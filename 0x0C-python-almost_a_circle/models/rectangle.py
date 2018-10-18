#!/usr/bin/python3
"""Module that creates a class Rectangle which inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Subclass that inherited from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize width, height, x, y, and id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self = super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @property
    def height(self):
        """Getter for width"""
        return self.__height

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print rectangle to stdout"""
        row = " " * self.x + "#" * self.width
        print(('\n' * self.y) + ((row + '\n') * self.height), end="")

    def __str__(self):
        """Method that returns a message"""
        s_id = self.id
        s_x = self.x
        s_y = self.y
        s_w = self.width
        s_h = self.height
        r = "[Rectangle]"
        return "{} ({}) {}/{} - {}/{}".format(r, s_id, s_x, s_y, s_w, s_h)
