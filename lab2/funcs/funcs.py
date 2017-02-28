import math

def f(x):
   return 7 * x**2 + 2 * x

def g(x, y):
   return (x**2 + y**2) / (3.0*x)

def hypotenuse(length1, length2):
   return math.sqrt(length1**2 + length2**2)

def is_positive(num):
   return num > 0
