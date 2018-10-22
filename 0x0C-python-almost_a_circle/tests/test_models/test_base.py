"""Unittest for base.py"""
"""
Import unittest, Base class, and Rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle

class Test_Base(unittest.TestCase):
    """Test for Base class
    Set up and Teardown
    """
    def setUp(self):
        """Setup environment"""
        pass
    def tearDown(self):
        """Tear down environment"""
        pass
    """
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
        """Test base id"""
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base(None)
        self.assertEqual(b.id, 2)
        b = Base()
        self.assertEqual(b.id, 3)
        self.assertNotEqual(b.id, 25)
    """
    Test 2.1
    """
    def test_case2_1(self):
        """Test base id with None"""
        b = Base(None)
        self.assertEqual(b.id, 4)
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
        b = Base(-3.35)
        self.assertEqual(b.id, -3.35)
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
        """Test base id with nan and inf"""
        b = Base(float('inf'))
        self.assertEqual(float('inf'), b.id)
        b = Base(float('NaN'))
        self.assertNotEqual(float('NaN'), b.id)
    """
    Test 2.12
    """
    def test_case2_12(self):
        """Test base id with empty argument"""
        b = Base()
        self.assertEqual(b.id, 5)
    """
    Test 2.13
    """
    def test_case2_13(self):
        """Test base id with too many arguments"""
        with self.assertRaises(TypeError):
            b = Base(1, 2)
    """
    Test 2.14
    """
    def test_case2_14(self):
        """Test for error cases"""
        with self.assertRaises(ValueError):
            b = Base(int("hello"))
        with self.assertRaises(ValueError):
            b = Base(float("lazers"))
        #with self.assertRaises():
         #   self.assert
#    """
 #   Part 3: test to_json_str
  #  """
   # def test_case3_0(self):
    #    """Test base method for None"""
     #   j = Base(1).to_json_str({'x': 2, 'y': 3})
      #  self.assertDictEqual(j, [{"x": 2, "y":3}])
    """
    Part 3: JSON
    Test 3.0
    """
    def test_case3_0(self):
        """Test for to_json_string method in Base class"""
        r = Rectangle(1, 2, 3, 4)
        r_dict = r.to_dictionary()
        j_dict = Base.to_json_string([r_dict])
        print(r_dict)
        self.assertEqual(type(r_dict), dict)
        print(j_dict)
        self.assertEqual(type(j_dict), str)
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')
    """
    Test 3.1
    """
    def test_case3_1(self):
        """Test for save_to_file method in Base class"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertIsInstance(r1, Base)
        try:
            with open("Rectangle.json", "r") as file:
                print(file.read())
        except Exception as e:
            print("{}".format(e))
        Rectangle.save_to_file(None)
        try:
            with open("rectangle.json", "r") as file:
                print(file.read())
        except Exception as e:
            print("{}".format(e))
        try:
            Rectangle.save_to_file()
        except Exception as e:
            print("{}".format(e))
    """
    Test 3.2
    """
    def test_case3_2(self):
        """Test for from_json_string method in Base class"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string([]), [])
        l_in = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        j_in = Rectangle.to_json_string(l_in)
        l_out = Rectangle.from_json_string(j_in)
        self.assertEqual(type(l_in), list)
        self.assertEqual(type(j_in), str)
        self.assertEqual(type(l_out), list)
    """
    Test 3.3
    """
    def test_case3_3(self):
        """Test case for create method in Base class"""
        r1 = Rectangle(3, 5, 1, 1, 1)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/1 - 3/5")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/1 - 3/5")
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        try:
            Rectangle.create("hello")
        except Exception as e:
            print("{}".format(e))
        try:
            Rectanlge.create()
        except Exception as e:
            print("{}".format(e))
        try:
            Rectangle.create("hi")
        except Exception as e:
            print("{}".format(e))
    """
    Test 3.4
    """
#    def test_case3_4(self):
 #       """Test for load_from_file method in Base class"""

if __name__ == "__main__":
    unittest.main()
