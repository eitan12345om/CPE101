from sys import argv

def main():

   if len(argv) == 1 or len(argv) > 3:
      print 'Usage: [-s] file_name'
      exit()
   elif len(argv) == 3 and '-s' not in argv:
      print 'Usage: [-s] file_name'
      exit()
   else:
      if len(argv) == 2:
         file_name = argv[1]
      else:
         argv.pop(argv.index('-s'))
         file_name = argv[1]
         argv.append('-s')
      try:
         inFile = open(file_name, 'r')
      except IOError as e:
         print e
         exit()

   total = 0
   ints = floats = other = 0
   for line in inFile:
      the_line = line.split()
      for elem in the_line:
         try:
            temp = int(elem)
            ints += 1
            total += temp
         except:
            try:
               temp = float(elem)
               floats += 1
               total += temp
            except:
               other += 1

   inFile.close()
   print 'Ints: %d' % ints
   print 'Floats: %d' % floats
   print 'Other: %d' % other
   if len(argv) == 3:
      print 'Sum: %.2f' % total

if __name__ == '__main__':
   main()
