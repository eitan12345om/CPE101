import unittest
from fold import *

class TestCases(unittest.TestCase):
   def test_sum_values1(self):
      self.assertEqual(sum_values(range(10)), 45)
   def test_sum_values2(self):
      self.assertAlmostEqual(sum_values([1.5, 2.5, 3.5, 7.3]), 14.8)
   def test_sum_values3(self):
      self.assertAlmostEqual(sum_values([1.5, 2.5, 1, 3, 6, 2.6]), 16.6)

   def test_index_of_smallest1(self):
      self.assertAlmostEqual(index_of_smallest([1.5, 2.5, 1, 3, 6, 2.6]), 2)
   def test_index_of_smallest2(self):
      self.assertEqual(index_of_smallest(range(10, 0, -1)), 9)
   def test_index_of_smallest3(self):
      self.assertAlmostEqual(index_of_smallest([1.5, 2.5, 3, 6, 2.6]), 0)
   def test_index_of_smallest3(self):
      self.assertAlmostEqual(index_of_smallest([]), -1)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

