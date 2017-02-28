# Functions for solver.py

def check_rows_valid(puzzle):
   for row in puzzle:
      temp = []
      for num in row:
         if num != 0:
            if num not in temp:
               temp.append(num)
            else:
               return False
   return True
     

def check_columns_valid(puzzle):
   for idx in range(5):
      temp = []
      for row in puzzle:
         if row[idx] != 0:
            if row[idx] not in temp:
               temp.append(row[idx])
            else:
               return False
   return True  

   
def check_cages_valid(vals, puzzle): 
   for cage in vals:
      sum_cage = cage[0]
      sum_values = 0
      for position in cage[2:]:
         col = position % 5
         row = position / 5
         value = puzzle[row][col]
         sum_values += value
      if puzzle[row][col] == 0:
         if sum_values >= sum_cage:
            return False
      else:
         if sum_values != sum_cage:
            return False
   return True


def check_everything(vals, puzzle):
   return check_rows_valid(puzzle) and check_columns_valid(puzzle) and check_cages_valid(vals, puzzle)
   
