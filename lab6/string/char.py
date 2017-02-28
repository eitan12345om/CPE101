def is_lower_101(c):
   return ord('a') <= ord(c) <= ord('z')

def char_rot_13(c):
   if c.isalpha():
      if c.islower():
         if ord(c) + 13 <= 122:
            return chr(ord(c) + 13)
         else:
            return chr(ord(c) - 13)
      else:
         if ord(c) + 13 <= 90:
            return chr(ord(c) + 13)
         else:
            return chr(ord(c) - 13)

   return c
