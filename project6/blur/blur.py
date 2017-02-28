from sys import argv

def groups_of_3(a_list):
   return [a_list[i:i+3] for i in range(0, len(a_list), 3)]

def find_square2(a_col, a_row, matrix, reach, width):
   top_left_col = max(a_col - reach, 0)
   top_left_row = max(a_row - reach, 0)
   top_right_col = min(a_col + reach, width)
   bot_left_row = min(a_row + reach, len(matrix))
   
   avg = [0, 0, 0]
   num_pixels = 0

   for part_row in matrix[top_left_row:bot_left_row + 1]:
      for pixel in part_row[top_left_col:top_right_col + 1]:
         num_pixels += 1
         avg[0] += int(pixel[0])     
         avg[1] += int(pixel[1])     
         avg[2] += int(pixel[2])

   avg[0] = int(avg[0] / num_pixels)
   avg[1] = int(avg[1] / num_pixels)
   avg[2] = int(avg[2] / num_pixels)
   return avg

def main():

   if len(argv) > 3 or len(argv) == 1:
      print 'Usage: python blur.py <filename> [<reach>]'
      exit()
   
   reach = 4
   if len(argv) == 3:
      reach = int(argv[2])

   try:
      inFile = open(argv[1], 'r')
   except:
      print 'Unable to open %s' % argv[1]
      exit()

   outFile = open('blurred.ppm', 'w')
 

   outFile.write(inFile.readline())
   temp = inFile.readline()
   outFile.write(temp)
   width = int(temp.split()[0])
   outFile.write(inFile.readline())

   pixels = []
   matrix = [[]]
   row = 0

   for line in inFile:
      pixels.extend(line.split())
      pixels = groups_of_3(pixels)

      for el in pixels:
         if len(el) == 3:
            matrix[row].append(el)
            
            if len(matrix[row]) == width:
               row += 1
               matrix.append([])

            if pixels[-1] == el:
               pixels = []
         else:
            pixels = pixels[-1] 

   matrix = matrix[:-1]
   inFile.close()

   a_row = a_col = 0
   new_pixels = []

   for row in matrix:
      for col in row:
         new_pixels.append(find_square2(a_col, a_row, matrix, reach, width))
   
         a_col += 1
      a_col = 0
      a_row += 1         
   
   for new_pixel in new_pixels:
      outFile.write('%d %d %d\n' % (new_pixel[0], new_pixel[1], new_pixel[2]))

   outFile.close()

if __name__ == '__main__':
   main()
