# Testing functions from funcs.py
import unittest
from funcs import *

puzzle = ['WAQHGTTWEE',
          'CBMIVQQELS',
          'AZXWKWIIIL',
          'LDWLFXPIPV',
          'PONDTMVAMN',
          'OEDSOYQGOB',
          'LGQCKGMMCT',
          'YCSLOACUZM',
          'XVDMGSXCYZ',
          'UUIUNIXFNU']

class TestCases(unittest.TestCase):
   def test_check_row1(self):
      self.assertEqual(check_row(puzzle[9], 'UNIX'), [3, 1])    
   def test_check_row2(self):
      self.assertEqual(check_row(puzzle[1], 'VIM'), [4, 3])    
   def test_check_row3(self):
      self.assertEqual(check_row(puzzle[9], 'VIM'), [-1, 3])    

   def test_check_col1(self):
      self.assertEqual(check_col('WCALPOLYXU', 'CALPOLY'), [1, 0])    
   def test_check_col2(self):
      self.assertEqual(check_col('ELIPMOCZYN', 'COMPILE'), [6, 2])    
   def test_check_col3(self):
      self.assertEqual(check_col('WCALPOLYXU', 'UNIX'), [-1, 2])

   def test_check_rows1(self):
      self.assertEqual(check_rows(puzzle, 'SLO'), [7, 2, 1])    
   def test_check_rows2(self):
      self.assertEqual(check_rows(puzzle, 'VIM'), [1, 4, 3])    
   def test_check_rows3(self):
      self.assertEqual(check_rows(puzzle, 'CALPOLY'), -1)    

   def test_check_cols1(self):
      self.assertEqual(check_cols(puzzle, 'CALPOLY'), [1, 0, 0])    
   def test_check_cols2(self):
      self.assertEqual(check_cols(puzzle, 'COMPILE'), [6, 8, 2])    
   def test_check_cols3(self):
      self.assertEqual(check_cols(puzzle, 'UNIX'), -1)    

   def test_find_word1(self):
      self.assertEqual(find_word(puzzle, 'UNIX'), [9, 3, 1])    
   def test_find_word2(self):
      self.assertEqual(find_word(puzzle, 'CALPOLY'), [1, 0, 0])    
   def test_find_word3(self):
      self.assertEqual(find_word(puzzle, 'COMPILE'), [6, 8, 2])    
   def test_find_word4(self):
      self.assertEqual(find_word(puzzle, 'VIM'), [1, 4, 3])    
   def test_find_word5(self):
      self.assertEqual(find_word(puzzle, 'GCC'), -1)    

if __name__ == '__main__':
   unittest.main()
