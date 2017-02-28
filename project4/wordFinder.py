from funcs import find_word

def main():

   letters = raw_input().strip()
   words = raw_input().split()

   puzzle = [letters[x:x+10] for x in range(0, len(letters), 10)]
   a_dict = {}

   for word in words:
      position = find_word(puzzle, word)
      if position != -1:
         if position[2] == 0:
            position[2] = 'DOWN'
         elif position[2] == 1:
            position[2] = 'FORWARD' 
         elif position[2] == 2:
            position[2] = 'UP' 
         else:
            position[2] = 'BACKWARD'
      a_dict[word] = position
   
   print 'Puzzle:\n'
   
   for row in puzzle:
      print row

   print ''

   for word in words:
      if a_dict.get(word) == -1:
         print '%s: word not found' % word
      else:
         print '%s: (%s) row: %d column: %d' % (word, a_dict.get(word)[2], a_dict.get(word)[0], a_dict.get(word)[1])

if __name__ == '__main__':
   main()
