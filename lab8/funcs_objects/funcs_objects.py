from math import sqrt

def distance(a, b):
   return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def circles_overlap(a, b):
   d = distance(a.center, b.center)
   return d < a.radius + b.radius
