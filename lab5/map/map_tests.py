import unittest
import map

class TestCases(unittest.TestCase):
   def test_square(self):
      self.assertEqual(map.square_all([1,2,3,4,5]), [1,4,9,16,25])
   def test_square2(self):
      self.assertEqual(map.square_all([-1,-2,-3,-4,-5]), [1,4,9,16,25])
      
   def test_add(self):
      self.assertEqual(map.add_n_all([1,2,3,4,5], 3), [4,5,6,7,8])
   def test_add2(self):
      self.assertEqual(map.add_n_all([1,2,3,4,5], -5), [-4,-3,-2,-1,0])

   def test_even(self):
      self.assertEqual(map.even_or_odd_all([1,2,3,4,5]), [False, True, False, True, False])
   def test_even2(self):
      self.assertEqual(map.even_or_odd_all([1,3,5,2,4]), [False, False, False, True, True])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

