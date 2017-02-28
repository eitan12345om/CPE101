import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):
   def test_distance1(self):
      self.assertEqual(distance_all([Point(3, 4), Point(1, 0), Point(6, 8)]), [5, 1, 10])
   def test_distance2(self):
      self.assertEqual(distance_all([Point(0, 4), Point(0, 0), Point(-3, 4)]), [4, 0, 5])
   
   def test_quadrant1(self):
      self.assertEqual(are_in_first_quadrant([Point(0, 4), Point(0, 0), Point(-3, 4)]), [])
   def test_quadrant2(self):
      self.assertEqual(are_in_first_quadrant([Point(3, 4), Point(1, 2), Point(-3, -4)]), [(3, 4), (1,2)])
   def test_quadrant3(self):
      self.assertEqual(are_in_first_quadrant([Point(1, 4), Point(1, 1), Point(3, 4)]), [(1, 4), (1, 1), (3, 4)])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

