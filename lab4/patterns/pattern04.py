import driver

def letter(row, col):
   if row in [2,3,4] and col in [3,4,5,6]:
      return 'M'
   else:
      return 'S'

if __name__ == '__main__':
   driver.comparePatterns(letter)
