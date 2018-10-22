"""Unittest for Rectangle class"""
"""
Import unittest
Import Rectangle class
Import io
Import sys
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys

class TestRectangle(unittest.TestCase):
    """Test for rectangle class"""
    """Part 1: test class instance
    Test 1.0
    """
    def test_case1_0(self):
        """Test class instance"""
        r = Rectangle(1, 2)
        self.assertIsInstance(r, Rectangle)

    """
    Part 2: test instance attrubte values
    Test 2.0
    """
    def test_case2_0(self):
        """Test positive attributes"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEquals(r.width, 1)
        self.assertEquals(r.height, 2)
        self.assertEquals(r.x, 3)
        self.assertEquals(r.y, 4)
        self.assertEquals(r.id, 5)
    """
    Test 2.1
    """
    def test_case2_1(self):
        """Test value errors for attributes"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, -2, 3, 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3, 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(0, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0, 3, 4, 5)
    """
    Test 2.2
    """
    def test_case2_2(self):
        """Test type errors for attributes"""
        with self.assertRaises(TypeError):
            r = Rectangle("value", 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, "value", 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "value", 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "value", 5)
        with self.assertRaises(TypeError):
            r = Rectangle([1, 2], 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, {'value':2}, 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, (3, 4), 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, None, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(3.35, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, float("NaN"), 3, 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, float("inf"), 4, 5)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, {}, 5)
    """
    Test 2.3
    """
    def test_case2_3(self):
        """Test for area method in Rectangle class"""
        r = Rectangle(1, 2, 3, 4, 5)
        print(r.area())
        self.assertEqual(r.area(), 2)
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)
    """
    Test 2.4
    """
    def test_case2_4(self):
        """Test for display method in Rectangle class"""
        r = Rectangle(5, 3)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#####\n" * 3)
        r.display()
        self.assertEqual(output.getvalue(), "#####\n" * 3)
        r = Rectangle(2, 3, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        string = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output.getvalue(), string)
    """
    Test 2.5
    """
    def test_case2_5(self):
        """Test for string method in Rectangle class"""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        output = io.StringIO()
        sys.stdout = output
        print(r.__str__())
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (5) 3/4 - 1/2\n")
    """
    Test 2.6
    """
    def test_case2_6(self):
        """Test for update method in Rectangle class"""
        Base._Base__nb_objects = 0
        r = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/10")

        output = io.StringIO()
        sys.stdout = output
        print(r.__str__())
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")

        r.update(89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 10/10")

        r.update(89, 2)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 2/10")

        r.update(89, 2, 3)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 2/3")

        r.update(89, 2, 3, 4)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/10 - 2/3")

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        r.update(89, 2, 3, 4, 5)
        output = io.StringIO()
        sys.stdout = output
        print(r.__str__())
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "[Rectangle] (89) 4/5 - 2/3\n")

        r = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r.update(height=1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 1/3 - 4/2")

    """
    Test 2.7
    """
    def test_case2_7(self):
        """Test for to_dictionary method in Rectangle class"""
        Base._Base__nb_objects = 0
        r = Rectangle (10, 2, 3, 9)
        d = r.to_dictionary()
        self.assertEqual(type(d), dict)
        r2 = Rectangle(1, 1)
        r2.update(**d)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 3/9 - 10/2")
        r = Rectangle(3, 2, 1, 5)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)
        with self.assertRaises(TypeError):
            r.to_dictionary("hi")
        with self.assertRaises(TypeError):
            r.to_dictionary(None)
if __name__ == "__main__":
    unittest.main()
