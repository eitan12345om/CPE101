def poly_add2(list1, list2):
   return [list1[0]+list2[0], list1[1]+list2[1], list1[2]+list2[2]] 

def poly_mult2(a, b):
   return [a[0]*b[0], a[1]*b[0] + a[0]*b[1], a[2]*b[0] + a[1]*b[1] + a[0]*b[2], a[2]*b[1] + a[1]*b[2], a[2]*b[2]] 
