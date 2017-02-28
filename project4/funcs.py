#For wordFinder.py

"""
DOWN = 0
FORWARD = 1
UP = 2
BACKWARD = 3
"""

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

words = ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'COMPILE', 'VIM', 'TEST']

def check_row(row, word, direction=1):
   index = [row.find(word), direction]

   if index[0] == -1:
      if row[::-1].find(word) == -1:
         index = [-1, direction + 2]
      else:
         index = [9 - row[::-1].find(word), direction + 2]

   return index #[col_in_row, direction] 


def check_col(col, word, direction=0):
   return check_row(col, word, direction) #[row_in_col, direction]      


def check_rows(puzzle, word):
   for i in range(len(puzzle)):   
      row = puzzle[i]
      check1 = check_row(row, word)
      if check1[0] != -1:
         return [i] + check1
   return -1

   
def check_cols(puzzle, word):
   for i in range(len(puzzle)):   
      col = []
      for row in puzzle:
         col.append(row[i])
      col = ''.join(col)
      check1 = check_col(col, word)
      if check1[0] != -1:
         return [check1[0]] + [i] + [check1[1]]
   return -1  

def find_word(puzzle, word):
   rows = check_rows(puzzle, word)
   if rows == -1:
      cols = check_cols(puzzle, word)
      if cols == -1:
         return -1
      return cols
   return rows

