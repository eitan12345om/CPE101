import unittest
import logic

class TestCases(unittest.TestCase):
   def test_is_even1(self):
      self.assertTrue(logic.is_even(44))
   def test_is_even2(self):
      self.assertTrue(logic.is_even(44.0))
   def test_is_even3(self):
      self.assertFalse(logic.is_even(9))
   def test_is_even4(self):
      self.assertFalse(logic.is_even(9.0))
   
   def test_in_an_interval1(self):
      self.assertTrue(logic.in_an_interval(2))
   def test_in_an_interval15(self):
      self.assertTrue(logic.in_an_interval(3))
   def test_in_an_interval2(self):
      self.assertFalse(logic.in_an_interval(9))
   def test_in_an_interval3(self):
      self.assertFalse(logic.in_an_interval(47))
   def test_in_an_interval35(self):
      self.assertTrue(logic.in_an_interval(56))
   def test_in_an_interval4(self):
      self.assertFalse(logic.in_an_interval(92))
   def test_in_an_interval5(self):
      self.assertFalse(logic.in_an_interval(12))
   def test_in_an_interval55(self):
      self.assertTrue(logic.in_an_interval(15))
   def test_in_an_interval6(self):
      self.assertTrue(logic.in_an_interval(19))
   def test_in_an_interval7(self):
      self.assertTrue(logic.in_an_interval(101))
   def test_in_an_interval75(self):
      self.assertTrue(logic.in_an_interval(102))
   def test_in_an_interval8(self):
      self.assertTrue(logic.in_an_interval(103))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

