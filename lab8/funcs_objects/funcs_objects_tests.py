import unittest
from objects import *
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_point1(self):
      a = Point(1, 2)
      self.assertEqual(a.x, 1)
      self.assertEqual(a.y, 2)
   def test_point2(self):
      a = Point(2, 1)
      self.assertEqual(a.x, 2)
      self.assertEqual(a.y, 1)

   def test_circle1(self):
      a = Circle(1, 2, 3)
      self.assertEqual(a.center.x, 1)
      self.assertEqual(a.center.y, 2)
      self.assertEqual(a.radius, 3)
   def test_circle2(self):
      a = Circle(3, 2, 1)
      self.assertEqual(a.center.x, 3)
      self.assertEqual(a.center.y, 2)
      self.assertEqual(a.radius, 1)

   def test_distance1(self):
      a = Point(0, 0)
      b = Point(3, 4)
      self.assertEqual(distance(a, b), 5)
   def test_distance2(self):
      a = Point(-2, 4)
      b = Point(1, 0)
      self.assertEqual(distance(a, b), 5)

   def test_circles_overlap1(self):
      a = Circle(-2, 4, 2)
      b = Circle(1, 0, 3)
      self.assertFalse(circles_overlap(a, b))
   def test_circles_overlap2(self):
      a = Circle(0, 0, 3)
      b = Circle(1, 0, 3)
      self.assertTrue(circles_overlap(a, b))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

