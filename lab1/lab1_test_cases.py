#
# Test cases example for lab 1.
#

import unittest      # import the module that supports writing unit tests

# Define a class that will be used for these test cases.
# This class will include testing functions.
#
# Much of this code should be viewed as boilerplate for now.
#
class TestsLab1(unittest.TestCase):
   def test_expressions(self):         # Defines one testing function.
      self.assertEqual(0 + 1, 1)
   def test_1(self):
      self.assertEqual(2 * 2, 4)
   def test_2(self):
      self.assertEqual(19 / 3, 6)
   def test_25(self):
      self.assertAlmostEqual(19 / 3.0, 6.33333333333)
   def test_3(self):
      self.assertAlmostEqual(19 // 3.0, 6.0)
   def test_4(self):
      self.assertAlmostEqual(19.0 / 3.0, 6.333333333333)
   def test_5(self):
      self.assertAlmostEqual(4 * 2 + 27 / 3.0 + 4, 21.0)
   def test_6(self):
      self.assertAlmostEqual(4 * (2 + 27) // 3.0 + 4, 42.0)
      # Add code here (like the line above) for the additional test cases.


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

