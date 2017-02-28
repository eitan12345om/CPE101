from sys import argv

def groups_of_3(a_list):
   return [a_list[i:i+3] for i in range(0, len(a_list), 3)]

def main():

   try:
      inFile = open(argv[1], 'r')
   except:
      print 'Usage: python puzzle.py <filename>'
      exit()

   outFile = open('hidden.ppm', 'w')
   
   pixels = []

   for i in range(3):
      outFile.write(inFile.readline())

   for line in inFile:
      pixels.extend(line.split())
      pixels = groups_of_3(pixels)

      for el in pixels:
         if len(el) == 3:
            for i in range(3):
               outFile.write(str(int(el[0]) * 10) + ' ')
            outFile.write('\n')
            if pixels[-1] == el:
               pixels = []
         else:
            pixels = pixels[-1]

   outFile.close()
   inFile.close()

if __name__ == '__main__':
   main()
