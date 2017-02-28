import unittest
from string_101 import *

class TestString(unittest.TestCase):
   def test_rot1(self):
      self.assertEqual(str_rot_13('abc'), 'nop')
   def test_rot2(self):
      self.assertEqual(str_rot_13('roof'), 'ebbs')
   def test_rot3(self):
      self.assertEqual(str_rot_13('gnat'), 'tang')

   def test_translate1(self):
      self.assertEqual(str_translate_101('banana', 'a', 'o'), 'bonono')
   def test_translate2(self):
      self.assertEqual(str_translate_101('aabbaabb', 'a', 'b'), 'bbbbbbbb')
   def test_translate3(self):
      self.assertEqual(str_translate_101('amanda', 'a', 'the'), 'themthendthe')

if __name__ == '__main__':
   unittest.main()

