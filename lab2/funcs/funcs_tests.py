import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_f_1(self):
      # Add code here.
      self.assertEqual(funcs.f(1), 9)

   def test_f_2(self):
      # Add code here.
      self.assertEqual(funcs.f(0), 0)

   def test_f_3(self):
      self.assertEqual(funcs.f(2), 32)

   def test_g_1(self):
      self.assertAlmostEqual(funcs.g(1,0), 0.333333333333333)

   def test_g_2(self):
      self.assertAlmostEqual(funcs.g(2.0,2.0), 1.3333333333333)

   def test_g_3(self):
      self.assertEqual(funcs.g(3,3), 2)

   def test_hyp_1(self):
      self.assertEqual(funcs.hypotenuse(3, 4), 5)

   def test_hyp_2(self):
      self.assertAlmostEqual(funcs.hypotenuse(6.0, 8), 10.0)

   def test_hyp_3(self):
      self.assertEqual(funcs.hypotenuse(39, 80), 89)

   def test_pos_1(self):
      self.assertTrue(funcs.is_positive(7))

   def test_pos_2(self):
      self.assertFalse(funcs.is_positive(0))

   def test_pos_3(self):
      self.assertFalse(funcs.is_positive(-23))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

