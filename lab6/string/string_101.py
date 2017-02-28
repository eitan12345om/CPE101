from char import char_rot_13

def str_rot_13(string):
   new_list = [char_rot_13(elem) for elem in string]
   return ''.join(new_list)


def str_translate_101(string, old, new):
   new_string = ''
   for char in string:
      if char != old:
         new_string += char
      else:
         new_string += new
   return new_string        
