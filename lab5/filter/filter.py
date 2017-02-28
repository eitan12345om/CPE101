def are_positive(a):
   return [x for x in a if x > 0]

def are_greater_than_n(a, n):
   new_list = []
   
   for x in a:
      if x > n:
         new_list.append(x)

   return new_list

def are_divisible_by_n(a, n):
   new_list = []
   index = 0

   while index < len(a):
      if a[index] % n == 0:
         new_list.append(a[index])
      index += 1

   return new_list
   
