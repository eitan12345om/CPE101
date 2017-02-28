import unittest
from char import *

class TestChar(unittest.TestCase):
   def test_lower1(self):
      self.assertEqual(is_lower_101('t'), True)
   def test_lower2(self):
      self.assertEqual(is_lower_101('A'), False)
   def test_lower3(self):
      self.assertEqual(is_lower_101('G'), False)
   def test_lower4(self):
      self.assertEqual(is_lower_101('a'), True)

   def test_rot1(self):
      self.assertEqual(char_rot_13('a'), 'n')
   def test_rot2(self):
      self.assertEqual(char_rot_13('z'), 'm')
   def test_rot3(self):
      self.assertEqual(char_rot_13('B'), 'O')
   def test_rot4(self):
      self.assertEqual(char_rot_13('P'), 'C')

if __name__ == '__main__':
   unittest.main()

