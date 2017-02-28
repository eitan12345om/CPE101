import driver

def letter(row, col):
   if row in [4,5] and col in [7,8,9]:
      return 'X'
   elif row in range(2,6) and col in range(4,10):
      return 'Z'
   elif row in [4,5,6] and col in range(7,13):
      return 'B'
   else:
      return 'T' 

if __name__ == '__main__':
   driver.comparePatterns(letter)
