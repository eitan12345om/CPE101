import unittest
import conditional

class TestCases(unittest.TestCase):
   def test_max_101(self):
      self.assertEqual(conditional.max_101(40, 50), 50)
   def test_max_101_2(self):
      self.assertEqual(conditional.max_101(50, 40), 50)
   def test_max_101_3(self):
      self.assertEqual(conditional.max_101(40.999, 50), 50)
 
   def test_max_of_three(self):
      self.assertAlmostEqual(conditional.max_of_three(40.999, 40.80, 42.98), 42.98)
   def test_max_of_three2(self):
      self.assertAlmostEqual(conditional.max_of_three(40.432, 40.433, 40.431), 40.433)
   def test_max_of_three3(self):
      self.assertAlmostEqual(conditional.max_of_three(40.999, 50.0001, 48.992), 50.0001)
   def test_max_of_three4(self):
      self.assertAlmostEqual(conditional.max_of_three(40.4234, 40.2121, 40.1222), 40.4234)

   def test_rental_late_fee(self):
      self.assertEqual(conditional.rental_late_fee(0), 0)
   def test_rental_late_fee2(self):
      self.assertEqual(conditional.rental_late_fee(9), 5)
   def test_rental_late_fee3(self):
      self.assertEqual(conditional.rental_late_fee(15), 7)
   def test_rental_late_fee4(self):
      self.assertEqual(conditional.rental_late_fee(24), 19)
   def test_rental_late_fee5(self):
      self.assertEqual(conditional.rental_late_fee(123), 100)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

