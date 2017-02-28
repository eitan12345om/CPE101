import solverFuncs
import time

def main():
   vals = []
   puzzle = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
   solved = False
   checks = backtracks = 0
   row = col = 0   

   num_cages = int(raw_input("Number of cages: "))
   
   for cage in range(num_cages):
      temp = raw_input("Cage number %d: " % cage).split()
      vals.append([int(i) for i in temp])

    
   while not solved:
      # Need to make so that numbers don't go more than 5
      if puzzle[row][col] < 5:
         puzzle[row][col] += 1
      else:
         backtracks += 1
         puzzle[row][col] = 0
         col -= 1
         if col == -1:
            row -= 1
            col = 4 
         continue        
 
      checks += 1
      if solverFuncs.check_everything(vals, puzzle):
         col += 1
         if col == 5:
            row += 1
            col = 0
      elif puzzle[row][col] == 5:
         backtracks += 1
         puzzle[row][col] = 0
         col -= 1
         if col == -1:
            row -= 1
            col = 4 
       
      if row == 5:
         solved = True
        
 
   print '\n---Solution---\n'
   for row in puzzle:
      for col in row:
         print col,
         if row[-1] == col:
            print ''

   print '\nchecks: %d backtracks: %d' % (checks, backtracks)         

if __name__ == '__main__':
   main()
