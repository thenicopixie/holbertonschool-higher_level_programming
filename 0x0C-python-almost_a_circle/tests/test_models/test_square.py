"""Unittest for Square class"""

"""
Import unittest
Import Square class
"""
import unittest
from models.square import Square

class Test_Square(unittest.TestCase):
    """Class to test class Square"""

    """
    Part 1: Square
    """

    """
    Test 1.0
    """
    def test_case1_0(self):
        """Test for attributes in Square class"""
        s = Square(5, 6, 7, 8)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 7)
        self.assertEqual(s.id, 8)
    """
    Test 1.1
    """
    def test_case1_1(self):
        """Test case for update method in Square class"""
        s = Square(1, 2, 3, 4)
        s.size = 25
        self.assertEqual(s.size, 25)
        self.assertEqual(s._Rectangle__width, 25)
        self.assertEqual(s._Rectangle__height, 25)
        self.assertEqual(s.x, 2)
        s.update(x=12)
        self.assertEqual(s.x, 12)
        s.update(size=33)
        self.assertEqual(s._Rectangle__width, 33)
        self.assertEqual(s._Rectangle__height, 33)
