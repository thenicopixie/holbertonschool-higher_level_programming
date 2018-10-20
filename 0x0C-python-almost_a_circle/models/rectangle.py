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

    def update(self, *args, **kwargs):
        """Update the rectangle based on args"""
        if args != ():
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        elif kwargs != {}:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Returns the dictionary representation
        of a Retangle"""
        r_dict = {}
        r_dict['id'] = self.id
        r_dict['width'] = self.__width
        r_dict['height'] = self.__height
        r_dict['x'] = self.__x
        r_dict['y'] = self.__y
        return r_dict
