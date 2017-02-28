import unittest
import filter

class TestCases(unittest.TestCase):
   def test_positive(self):
      self.assertEqual(filter.are_positive([1,3,-4,-5,6]), [1,3,6])   
   def test_positive2(self):
      self.assertEqual(filter.are_positive([0,-1,-3,-4,-5,-6]), [])   
      
   def test_greater(self):
      self.assertEqual(filter.are_greater_than_n([1,3,-4,-5,6], 2), [3,6])   
   def test_greater2(self):
      self.assertEqual(filter.are_greater_than_n([1,3,-4,-5,6], -2), [1,3,6])   

   def test_divisible(self):
      self.assertEqual(filter.are_divisible_by_n([1,3,-4,-5,6], -2), [-4,6])   
   def test_divisible2(self):
      self.assertEqual(filter.are_divisible_by_n([1,3,-4,-5,6], 1), [1,3,-4,-5,6])   

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

