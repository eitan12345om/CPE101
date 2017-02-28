def square_all(a):
   return [x*x for x in a]

def add_n_all(a, n):
   new_list = []
   
   for i in a:
      new_list.append(i + n)

   return new_list

def even_or_odd_all(a):
   new_list = []
   index = 0
   
   while index < len(a):
      if a[index] % 2 == 0:
         new_list.append(True)
      else:
         new_list.append(False)
      index += 1

   return new_list 
