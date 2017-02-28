def sum_values(a_list):
   total = 0
   for elem in a_list:
      total += elem
   
   return total

def index_of_smallest(a_list):
   if len(a_list) == 0:
      return -1
   
   idx_of_smallest = 0
   
   for idx in range(len(a_list)):
      if a_list[idx] < a_list[idx_of_smallest]:
         idx_of_smallest = idx
   
   return idx_of_smallest
