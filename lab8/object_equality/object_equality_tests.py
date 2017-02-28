import unittest
from objects import *

class TestCases(unittest.TestCase):
   def test_equality1(self):
      a = Point(2, 1)
      b = Point(2, 1)
      self.assertEqual(a, b)
   def test_equality2(self):
      a = Point(3, 6)
      b = Point(2, 1)
      self.assertNotEqual(a, b)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

