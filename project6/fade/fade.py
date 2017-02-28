from sys import argv
from math import sqrt

def groups_of_3(a_list):
   return [a_list[i:i+3] for i in range(0, len(a_list), 3)]

def find_dist(a_row, a_col, row, col):
   return sqrt((a_row - row)**2 + (a_col - col)**2)

def compute_scale(radius, dist):
   temp = (radius - dist) / radius
   return max(0.2, temp)

def main():

   if len(argv) != 5:
      print 'Usage: python fade.py <image> <row> <column> <radius>'
      exit()
   else:
      row = int(argv[2])
      col = int(argv[3])
      radius = int(argv[4])
      try:
         inFile = open(argv[1], 'r')
      except:
         print 'Unable to open %s' % argv[1]
         exit()

   outFile = open('faded.ppm', 'w')
 
   outFile.write(inFile.readline())
   temp = inFile.readline()
   outFile.write(temp)
   width = int(temp.split()[0])
   outFile.write(inFile.readline())

   a_row = a_col = 1

   pixels = []

   for line in inFile:
      pixels.extend(line.split())
      pixels = groups_of_3(pixels)

      for el in pixels:
         if len(el) == 3:
            dist = find_dist(a_row, a_col, row, col)
            for i in range(3):
               outFile.write(str(int(int(el[i]) * compute_scale(radius, dist))) + ' ')
            outFile.write('\n')
            
            a_col += 1
            if a_col > width:
               a_col = 1
               a_row += 1
            if pixels[-1] == el:
               pixels = []
         else:
            pixels = pixels[-1] 

   outFile.close()
   inFile.close()

if __name__ == '__main__':
   main()
