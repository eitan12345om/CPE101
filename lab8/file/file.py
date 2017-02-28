f = open('in.txt', 'r')

file_line = 0
for line in f:
   print 'Line %d (%d chars): %s' % (file_line, len(line.strip()), line.strip())
   file_line += 1

f.close()
