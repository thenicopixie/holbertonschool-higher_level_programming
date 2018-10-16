#!/usr/bin/python3
""" Module for BaseClass that raises and excaption
with a message"""


class BaseGeometry:
    """Base class to raise an exception"""

    def area(self):
        """Method used to raise an exception"""
        raise Exception("area() is not implenented")
