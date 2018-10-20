"""Unittest for base.py"""
"""
Import unittest and Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test for Base class
    Part 1: Test Base class
    Test 1.0
    """
    def test_case1_0(self):
        """Test for base type"""
        b = Base(1)
        self.assertIsInstance(b, Base)
    """
    Part 2: Test for id
    Test 2.0
    """
    def test_case2_0(self):
        """Test base id with integer"""
        b = Base()
        self.assertEqual(b.id, 1)
    """
    Test 2.1
    """
    def test_case2_1(self):
        """Test base id with None"""
        b = Base(None)
        self.assertEqual(b.id, 2)
    """
    Test 2.2
    """
    def test_case2_2(self):
        """Test base id with integer"""
        b = Base(5)
        self.assertEqual(b.id, 5)
    """
    Test 2.3
    """
    def test_case2_3(self):
        """Test base id with string"""
        b = Base("name")
        self.assertEqual(b.id, "name")
    """
    Test 2.4
    """
    def test_case2_4(self):
        """Test base id with float"""
        b = Base(2.25)
        self.assertEqual(b.id, 2.25)
    """
    Test 2.5
    """
    def test_case2_5(self):
        """Test base id with True"""
        b = Base(True)
        self.assertEqual(b.id, True)
    """
    Test 2.6
    """
    def test_case2_6(self):
        """Test base id with False"""
        b = Base(False)
        self.assertEqual(b.id, False)
    """
    Test 2.7
    """
    def test_case2_7(self):
        """Test base id with list"""
        b = Base([1, 2])
        self.assertEqual(b.id, [1, 2])
    """
    Test 2.8
    """
    def test_case2_8(self):
        """Test base id with tuple"""
        b = Base((1, 2))
        self.assertEqual(b.id, (1, 2))
    """
    Test 2.9
    """
    def test_case2_9(self):
        """Test base id with dictionary"""
        b = Base({"name": "Carl"})
        self.assertEqual(b.id, {"name": "Carl"})
    """
    Test 2.10
    """
    def test_case2_10(self):
        """Test Base id with empty list"""
        b = Base([])
        self.assertEqual(b.id, [])
    """
    Test 2.11
    """
    def test_case2_11(self):
        """Test base id with nan"""
        b = Base(float('nan'))
        self.assertNotEqual(b.id, b.id)
    """
    Test 2.12
    """
    def test_case2_12(self):
        """Test base id with empty argument"""
        b = Base()
        self.assertEqual(b.id, 3)
    """
    Test 2.13
    """
    def test_case2_13(self):
        """Test base id with too many arguments"""
        with self.assertRaises(TypeError):
            Base(1, 2)
#    """
 #   Part 3: test to_json_str
  #  """
   # def test_case3_0(self):
    #    """Test base method for None"""
     #   j = Base(1).to_json_str({'x': 2, 'y': 3})
      #  self.assertDictEqual(j, [{"x": 2, "y":3}])

if __name__ == "__main__":
    unittest.main()
